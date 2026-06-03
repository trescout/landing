#!/usr/bin/env python3
"""
TreScout Sözlük · oto-büyüme motoru
===================================
Raporların "Sektörden Terimler" sözlüğündeki YENİ terimleri, sözlüğe "ders gibi"
sayfalarla otomatik ekler. Idempotent: var olan terimi tekrar eklemez.

Akış:
  1) Glossary terimlerini topla · rapor JSON'unun "glossary" alanı (tercih) ya da rapor PDF'i (yedek).
  2) Mevcut sözlükte slug olarak olmayan adayları Gemini'ye ver · Gemini eş-anlamlıları ayıklar
     (ör. "large language models" → zaten "llm" var) + yeni olanlara ders-gibi içerik üretir.
  3) Yeni terimler için sayfa + .md üret, index/manifest/sitemap güncelle.

GEMINI_API_KEY: ortam değişkeni (CI secret) ya da ../trescout-app/.env.local (yerel).
Kullanım: python3 scripts/dict-sync.py [--dry]   (--dry: yazma, sadece ne ekleneceğini göster)
"""
import os, re, sys, json, glob, time, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # landing repo kökü
REPORTS = os.path.join(ROOT, "reports")
DICT = os.path.join(ROOT, "dictionary")
OG = os.path.join(ROOT, "assets", "dictionary")
MANIFEST = os.path.join(OG, "dictionary.json")
SITEMAP = os.path.join(ROOT, "sitemap.xml")
MODEL = "gemini-3.1-flash-lite"
DRY = "--dry" in sys.argv
CAT_TR = {"ai": "Yapay Zekâ", "dev": "Geliştirme", "data": "Veri & Altyapı"}
import datetime
TODAY_ISO = os.environ.get("DICT_DATE") or datetime.date.today().isoformat()
def tr_date(iso):
    ay=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
    y,m,d=iso.split("-"); return f"{int(d)} {ay[int(m)-1]} {y}"
TODAY_TR = tr_date(TODAY_ISO)

def gemini_key():
    k = os.environ.get("GEMINI_API_KEY")
    if k: return k
    envp = os.path.join(os.path.dirname(ROOT), "trescout-app", ".env.local")
    if os.path.exists(envp):
        for l in open(envp):
            if l.strip().startswith("GEMINI_API_KEY="):
                return l.split("=", 1)[1].strip().strip('"').strip("'")
    return None

def esc(s): import html; return html.escape(s or "", quote=True)
def slugify(t):
    t = t.lower().strip()
    for a,b in [("ç","c"),("ğ","g"),("ı","i"),("ş","s"),("ö","o"),("ü","u")]: t=t.replace(a,b)
    t = re.sub(r"[^a-z0-9]+","-",t).strip("-")
    return t

# ---------- 1) glossary toplama ----------
TR = re.compile(r"[çğışöüâÇĞİŞÖÜ]")
def parse_pdf_glossary(pdf):
    try:
        txt = subprocess.run(["pdftotext","-layout",pdf,"-"],capture_output=True,text=True).stdout
    except Exception:
        return []
    if "Sektörden" not in txt: return []
    region = txt.split("Sektörden",1)[1]
    region = region.split("\n",1)[1] if "\n" in region else region
    region = region.replace("\f","\n")
    out=[]; term=None; expl=[]
    def is_term(l):
        l=l.strip()
        if not l or len(l)>46 or l.endswith(".") or l.endswith(":") or TR.search(l): return False
        if "·" in l or "TERİM" in l or "Sözlü" in l or l[:1].isdigit(): return False
        return bool(re.match(r"^[A-Za-z0-9][A-Za-z0-9 ./+\-]*$", l))
    def flush():
        nonlocal term,expl
        if term and expl:
            e=" ".join(expl).strip()
            if TR.search(e): out.append({"term":term,"explanation":e})
        term=None; expl=[]
    for ln in region.split("\n"):
        s=ln.strip()
        if not s: continue
        if "·" in s or "trescout" in s.lower(): break
        if is_term(s): flush(); term=s; expl=[]
        elif term: expl.append(s)
    flush()
    return out

def collect_glossary():
    seen={}
    for jp in sorted(glob.glob(os.path.join(REPORTS,"*.json"))):
        try: d=json.load(open(jp,encoding="utf-8"))
        except Exception: continue
        g=d.get("glossary") or []
        for e in g:
            t=(e.get("term") or "").strip(); ex=(e.get("explanation") or e.get("definition") or "").strip()
            if t and ex:
                k=t.lower()
                if k not in seen or len(ex)>len(seen[k][1]): seen[k]=(t,ex)
    # JSON'da yoksa PDF yedeği
    if not seen:
        for pp in sorted(glob.glob(os.path.join(REPORTS,"*.pdf"))):
            for e in parse_pdf_glossary(pp):
                k=e["term"].lower()
                if k not in seen or len(e["explanation"])>len(seen[k][1]): seen[k]=(e["term"],e["explanation"])
    return [{"term":t,"explanation":x} for t,x in seen.values()]

# ---------- 2) Gemini dedup + ders-gibi içerik ----------
SYS=("Sen TreScout için Türkçe teknoloji sözlüğü editörüsün; kod bilmeyene DERS ANLATIR gibi yazarsın. "
 "Sana MEVCUT sözlük terimleri (slug · ad) ve raporlardan gelen ADAY terimler (terim · açıklama) verilecek. "
 "Her aday için: MEVCUT bir terimle AYNI kavram mı? AYNIYSA çıktıya KOYMA. YENİYSE ders-gibi içerik üret. "
 "KURALLAR: 'siz' dili; em dash (—) YASAK; UYDURMA (emin değilsen genel-doğru); jargon yığma; marka TreScout. "
 'Her YENİ terim için JSON: {"slug"(ingilizce-kucuk-tireli),"en"(görünen ingilizce ad),"full"(akronim açılımı veya ""),'
 '"cat"("ai"|"dev"|"data"),"kisa"(verilen açıklamayı temel al, tek cümle),"tanim"(2-4 cümle),"analoji"(günlük benzetme 1-2 cümle),'
 '"nasil"(2-4 cümle),"nerede"(2-3 cümle),"karistirilan"(1-2 cümle veya ""),"sss"([{"soru","cevap"}] 2-3 adet),'
 '"related"(mevcut/yeni slug listesinden 3-5)}. ÇIKTI: SADECE YENİ terimlerin JSON dizisi, başka metin yok.')
def gemini(existing, candidates, key):
    payload=("MEVCUT terimler:\n"+json.dumps([{"slug":s,"ad":n} for s,n in existing],ensure_ascii=False)+
             "\n\nADAY terimler:\n"+json.dumps(candidates,ensure_ascii=False))
    body={"systemInstruction":{"parts":[{"text":SYS}]},"contents":[{"parts":[{"text":payload}]}],
          "generationConfig":{"temperature":0.5,"responseMimeType":"application/json","maxOutputTokens":8192}}
    url=f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}"
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json"},method="POST")
    last=None
    for attempt in range(5):  # geçici 429/500/503/timeout için retry + backoff
        try:
            raw=json.loads(urllib.request.urlopen(req,timeout=150).read().decode())["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(raw)
        except urllib.error.HTTPError as e:
            last=e
            if e.code in (429,500,502,503) and attempt<4: time.sleep((attempt+1)*5); continue
            raise
        except Exception as e:
            last=e
            if attempt<4: time.sleep((attempt+1)*5); continue
            raise
    raise last

# ---------- 3) render ----------
LOGO='<svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>'
NAV='<nav><div class="container nav-inner"><a class="logo-link" href="/" aria-label="TreScout anasayfa">'+LOGO+'<span>TreScout</span></a><div class="nav-actions"><a href="/discover/" class="btn btn-ghost">Keşif</a><a href="/dictionary/" class="btn btn-ghost">Sözlük</a><a href="/#top" class="btn btn-primary">Erken erişim</a></div></div></nav>'
FOOTER='<footer><div class="container"><div class="footer-grid"><div class="footer-brand-block"><div class="footer-logo">'+LOGO+'<span>TreScout</span></div><p class="footer-tagline">TreScout tarar, özetler, gönderir. Siz sadece okursunuz.</p></div><div class="footer-col"><div class="footer-col-title">Ürün</div><ul><li><a href="/#how-it-works">Nasıl Çalışır</a></li><li><a href="/discover/">Keşif</a></li><li><a href="/dictionary/">Sözlük</a></li><li><a href="/reports/">Raporlar</a></li></ul></div><div class="footer-col"><div class="footer-col-title">İletişim</div><ul><li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li><li><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a></li></ul></div><div class="footer-col"><div class="footer-col-title">Sosyal medya</div><ul><li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X</a></li></ul></div></div><div class="footer-bottom"><span>© 2026 TreScout · Tüm hakları saklıdır.</span></div></div></footer>'
FORM='<form class="cta-form disc-cta-form js-subscribe" data-source="dictionary" novalidate><div class="form-row"><input class="input" type="email" name="email" placeholder="E-postanızı yazın" autocomplete="email" required><button class="btn btn-primary" type="submit">Erken erişim</button></div><label class="form-consent"><input type="checkbox" name="consent" required><span><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a>\'ni okudum, e-postamın bu amaçla işlenmesini onaylıyorum.</span></label><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field"></form>'

def render_page(e, en_map):
    slug=e["slug"]; en=e["en"]; full=e.get("full",""); cattr=CAT_TR.get(e["cat"],"")
    kisa=e["kisa"]; tanim=e.get("tanim",""); analoji=e.get("analoji",""); nasil=e.get("nasil","")
    nerede=e.get("nerede",""); kar=e.get("karistirilan",""); sss=e.get("sss",[]); rel=e.get("related",[])
    canon=f"https://trescout.com/dictionary/{slug}/"
    ogfile=f"/assets/dictionary/og/{slug}.webp" if os.path.exists(os.path.join(OG,"og",slug+".webp")) else "/assets/dictionary/og-default.webp"
    ogimg="https://trescout.com"+ogfile
    title=f"{en} nedir?"+(f" · {full}" if full else "")+" · TreScout Sözlük"
    dt=json.dumps({"@context":"https://schema.org","@type":"DefinedTerm","name":en,**({"alternateName":full} if full else {}),"inLanguage":"tr","description":tanim,"inDefinedTermSet":{"@type":"DefinedTermSet","name":"TreScout Teknoloji Sözlüğü","url":"https://trescout.com/dictionary/"},"url":canon},ensure_ascii=False,indent=2)
    faqjson=""
    if sss:
        faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q["soru"],"acceptedAnswer":{"@type":"Answer","text":q["cevap"]}} for q in sss]}
        faqjson='<script type="application/ld+json">\n'+json.dumps(faq,ensure_ascii=False,indent=2)+'\n</script>\n'
    secs=f'<section class="disc-sec"><h2>Tanım</h2><p>{esc(tanim)}</p></section>'
    if analoji: secs+=f'<div class="dict-analogy">{esc(analoji)}</div>'
    if nasil: secs+=f'<section class="disc-sec"><h2>Nasıl çalışır?</h2><p>{esc(nasil)}</p></section>'
    if nerede: secs+=f'<section class="disc-sec"><h2>Nerede kullanılır?</h2><p>{esc(nerede)}</p></section>'
    if kar: secs+=f'<section class="disc-sec"><h2>Sık karıştırılanlar</h2><p>{esc(kar)}</p></section>'
    if sss:
        items="".join(f'<div class="dict-faq-item"><p class="dict-faq-q">{esc(q["soru"])}</p><p class="dict-faq-a">{esc(q["cevap"])}</p></div>' for q in sss)
        secs+=f'<section class="disc-sec"><h2>Sıkça sorulanlar</h2><div class="dict-faq">{items}</div></section>'
    if rel:
        links="".join(f'<a href="/dictionary/{r}/">{esc(en_map.get(r,r))}</a>' for r in rel if r in en_map)
        if links: secs+=f'<section class="disc-sec"><h2>İlgili terimler</h2><div class="dict-related">{links}</div></section>'
    enline=f'<p class="dict-en">{esc(full)}</p>' if full else ''
    head=('<!DOCTYPE html>\n<html lang="tr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      f'<title>{esc(title)}</title>\n<meta name="description" content="{esc(kisa)}">\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
      f'<link rel="canonical" href="{canon}">\n<meta property="og:title" content="{esc(en+" nedir?")}">\n<meta property="og:description" content="{esc(kisa)}">\n'
      f'<meta property="og:url" content="{canon}">\n<meta property="og:type" content="article">\n<meta property="og:locale" content="tr_TR">\n'
      f'<meta property="og:image" content="{ogimg}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:site" content="@GetTreScout">\n<meta name="twitter:title" content="{esc(en+" nedir?")}">\n<meta name="twitter:image" content="{ogimg}">\n'
      f'<script type="application/ld+json">\n{dt}\n</script>\n{faqjson}<link rel="alternate" type="text/markdown" href="/dictionary/{slug}.md">\n'
      '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n      <link rel="preload" href="/assets/fonts/inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin>\n'
      '<link rel="stylesheet" href="/assets/site.css">\n<link rel="stylesheet" href="/assets/discover.css">\n<link rel="stylesheet" href="/assets/dictionary.css">\n</head>\n')
    body=('<body>\n<a class="skip-link" href="#main">Ana içeriğe atla</a>\n'+NAV+'\n<main id="main">\n<article class="disc">\n'
      '<a class="disc-back" href="/dictionary/">← Sözlük</a>\n'
      f'<div class="disc-top"><span class="disc-eyebrow">Sözlük · {esc(cattr)}</span><time class="dict-time" datetime="{TODAY_ISO}">Son güncelleme: {TODAY_TR}</time></div>\n'
      f'<h1 class="disc-title">{esc(en)} <span class="disc-accent">nedir?</span></h1>\n{enline}\n<p class="disc-lead">{esc(kisa)}</p>\n{secs}\n'
      '<aside class="disc-cta"><p><strong>Her sabah Sektörden Terimler e-postanızda.</strong> Teknoloji dünyasında her gün yeni bir terim çıkıyor; geride kalmamak için TreScout\'a katılın.</p>'
      +FORM+'<a class="btn btn-ghost disc-cta-all" href="/dictionary/">Tüm sözlük →</a></aside>\n'
      '<p class="disc-disclaimer">Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa <a href="mailto:hello@trescout.com">hello@trescout.com</a>. TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.</p>\n'
      '</article>\n</main>\n'+FOOTER+'\n<script src="/assets/subscribe.js" defer></script>\n  <script defer src="/_vercel/insights/script.js"></script>\n  <script defer src="/_vercel/speed-insights/script.js"></script>\n</body>\n</html>\n')
    os.makedirs(os.path.join(DICT,slug),exist_ok=True)
    open(os.path.join(DICT,slug,"index.html"),"w",encoding="utf-8").write(head+body)
    md=f"# {en} nedir?\n"+(f"\n> {full}\n" if full else "")+f"\n**Kategori:** {cattr}  \n**Son güncelleme:** {TODAY_ISO}\n\n{kisa}\n\n## Tanım\n{tanim}\n"
    if analoji: md+=f"\n## Bir benzetmeyle\n{analoji}\n"
    if nasil: md+=f"\n## Nasıl çalışır?\n{nasil}\n"
    if nerede: md+=f"\n## Nerede kullanılır?\n{nerede}\n"
    if kar: md+=f"\n## Sık karıştırılanlar\n{kar}\n"
    if sss: md+="\n## Sıkça sorulanlar\n"+"".join(f"\n**{q['soru']}**  \n{q['cevap']}\n" for q in sss)
    if rel: md+="\n## İlgili terimler\n"+"".join(f"- [{en_map.get(r,r)}](/dictionary/{r}/)\n" for r in rel if r in en_map)
    md+=f"\n---\nKaynak: TreScout Teknoloji Sözlüğü · {canon}\nTreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.\n"
    open(os.path.join(DICT,slug+".md"),"w",encoding="utf-8").write(md)

def render_index(manifest):
    cards=""
    for e in sorted(manifest,key=lambda x:x["en"].lower()):
        enl=f'<p class="dict-card-en">{esc(e["full"])}</p>' if e.get("full") else ''
        hay=f"{e['en']} {e.get('full','')} {e['kisa']} {e['slug']}"
        cards+=(f'<a class="dict-card" data-cat="{e["cat"]}" data-search="{esc(hay)}" href="/dictionary/{e["slug"]}/">'
                f'<h2 class="dict-card-term">{esc(e["en"])}</h2>{enl}<p class="dict-card-kisa">{esc(e["kisa"])}</p></a>\n')
    chips=('<button type="button" class="dict-chip dict-chip-active" data-cat="">Tümü</button>'
           '<button type="button" class="dict-chip" data-cat="ai">Yapay Zekâ</button>'
           '<button type="button" class="dict-chip" data-cat="dev">Geliştirme</button>'
           '<button type="button" class="dict-chip" data-cat="data">Veri & Altyapı</button>')
    jl=json.dumps({"@context":"https://schema.org","@type":"DefinedTermSet","name":"TreScout Teknoloji Sözlüğü","description":"Yapay zekâ ve yazılım terimlerinin sade Türkçe açıklamaları.","inLanguage":"tr","url":"https://trescout.com/dictionary/","hasDefinedTerm":[{"@type":"DefinedTerm","name":m["en"],"url":f"https://trescout.com/dictionary/{m['slug']}/"} for m in manifest]},ensure_ascii=False,indent=2)
    head=('<!DOCTYPE html>\n<html lang="tr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      '<title>Teknoloji Sözlüğü · Yapay zekâ ve yazılım terimleri · TreScout</title>\n'
      '<meta name="description" content="RAG, fine-tuning, embedding, MCP ve daha fazlası: yapay zekâ ve yazılım terimlerinin sade Türkçe açıklamaları. TreScout her gün yeni terimler ekler.">\n'
      '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n<link rel="canonical" href="https://trescout.com/dictionary/">\n'
      '<meta property="og:title" content="Teknoloji Sözlüğü · TreScout">\n<meta property="og:description" content="Yapay zekâ ve yazılım terimlerinin sade Türkçe açıklamaları.">\n'
      '<meta property="og:url" content="https://trescout.com/dictionary/">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="tr_TR">\n'
      '<meta property="og:image" content="https://trescout.com/assets/dictionary/og-default.webp">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:site" content="@GetTreScout">\n<meta name="twitter:image" content="https://trescout.com/assets/dictionary/og-default.webp">\n'
      f'<script type="application/ld+json">\n{jl}\n</script>\n'
      '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
      '<link rel="stylesheet" href="/assets/site.css">\n<link rel="stylesheet" href="/assets/discover.css">\n<link rel="stylesheet" href="/assets/dictionary.css">\n</head>\n')
    body=('<body>\n<a class="skip-link" href="#main">Ana içeriğe atla</a>\n'+NAV+'\n<main id="main">\n<div class="disc">\n'
      '<div class="dict-index-hero"><span class="disc-eyebrow">Sözlük</span><h1 class="dict-index-title">Teknoloji Sözlüğü</h1>'
      '<p class="dict-index-lead">Yapay zekâ ve yazılımın <strong>yeni terimleri</strong>, sade Türkçe açıklamalarıyla. TreScout her gün trendleri tararken karşılaştığı terimleri buraya ekler.</p></div>\n'
      '<div class="dict-controls"><input type="search" id="dict-search" class="dict-search" placeholder="Terim ara: RAG, embedding, fine-tuning…" aria-label="Terim ara"></div>\n'
      f'<div class="dict-tags" id="dict-tags">{chips}</div>\n<p class="dict-count" id="dict-count">{len(manifest)} terim</p>\n'
      f'<div class="dict-grid" id="dict-grid">\n{cards}</div>\n<p class="dict-empty" id="dict-empty">Eşleşme yok. Aramayı değiştirin.</p>\n'
      '<aside class="disc-cta"><p><strong>Her sabah yeni terimler e-postanızda.</strong> Sektörden Terimler Sözlüğü ve günlük teknoloji raporu için TreScout\'a katılın.</p>'+FORM+'</aside>\n'
      '</div>\n</main>\n'+FOOTER+'\n<script src="/assets/dictionary.js" defer></script>\n<script src="/assets/subscribe.js" defer></script>\n  <script defer src="/_vercel/insights/script.js"></script>\n  <script defer src="/_vercel/speed-insights/script.js"></script>\n</body>\n</html>\n')
    open(os.path.join(DICT,"index.html"),"w",encoding="utf-8").write(head+body)

def update_sitemap(new_slugs):
    sm=open(SITEMAP,encoding="utf-8").read()
    lines=[]
    for s in new_slugs:
        u=f"https://trescout.com/dictionary/{s}/"
        if u in sm: continue
        lines+=["  <url>",f"    <loc>{u}</loc>",f"    <lastmod>{TODAY_ISO}</lastmod>","    <changefreq>monthly</changefreq>","    <priority>0.6</priority>","  </url>"]
    if lines: open(SITEMAP,"w",encoding="utf-8").write(sm.replace("</urlset>","\n".join(lines)+"\n</urlset>"))

# ---------- main ----------
def main():
    terms=collect_glossary()
    print(f"raporlardan toplanan glossary terimi: {len(terms)}")
    if not terms: print("glossary bulunamadı (rapor JSON'unda 'glossary' yok, PDF de yok)."); return
    manifest=json.load(open(MANIFEST,encoding="utf-8"))
    existing_slugs={m["slug"] for m in manifest}
    candidates=[t for t in terms if slugify(t["term"]) not in existing_slugs]
    print(f"slug eşleşmeyen aday: {len(candidates)} (gerisi zaten var)")
    if not candidates: print("eklenecek yeni terim yok · sözlük güncel ✅"); return
    key=gemini_key()
    if not key: print("HATA: GEMINI_API_KEY yok (ortam değişkeni ya da app/.env.local)."); sys.exit(1)
    existing=[(m["slug"],m["en"]) for m in manifest]
    new=gemini(existing, [{"term":c["term"],"aciklama":c["explanation"]} for c in candidates], key)
    # geçerlilik + slug çakışması filtre
    new=[n for n in new if n.get("slug") and n["slug"] not in existing_slugs and n.get("en") and n.get("kisa") and n.get("tanim")]
    if not new: print("Gemini yeni terim üretmedi (hepsi eş-anlamlı/mevcut) · sözlük güncel ✅"); return
    print(f"eklenecek YENİ terim: {len(new)} → {[n['slug'] for n in new]}")
    if DRY: print("[--dry] yazılmadı."); return
    en_map={m["slug"]:m["en"] for m in manifest}; en_map.update({n["slug"]:n["en"] for n in new})
    for n in new:
        n["related"]=[r for r in (n.get("related") or []) if r in en_map][:5]
        render_page(n, en_map)
    manifest+=[{"slug":n["slug"],"en":n["en"],"full":n.get("full",""),"cat":n["cat"],"kisa":n["kisa"]} for n in new]
    json.dump(manifest,open(MANIFEST,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    render_index(manifest)
    update_sitemap([n["slug"] for n in new])
    print(f"✅ {len(new)} terim eklendi · toplam {len(manifest)} · index/manifest/sitemap güncellendi")
    print("   OG kartı: og-default (per-term kart için yerel: scripts/dict-cards.py)")

if __name__=="__main__": main()
