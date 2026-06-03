#!/usr/bin/env python3
"""
TreScout Keşif · oto-büyüme motoru (LITE)
=========================================
Günlük raporların GitHub bölümündeki YENİ repoları, keşfe "lite" entry olarak ekler.
Lite = başlık + raporun Türkçe özeti + marka kart (kapak) + sözlük çapraz-link + funnel.
(Mevcut 47 küratörlü entry kadar zengin DEĞİL: araştırılmış komut / gerçek ekran görüntüsü / AI-prompt yok.
 Sonra elle zenginleştirilir · catalog'da "lite": true ile işaretlenir.)

Dedup: repo URL ile (slug değil) → "FreeDomain"/"free-domain" gibi yanlış kopya engellenir. Idempotent.
Index grid catalog.json'dan client-side render olduğu için index'i ayrıca üretmeye gerek yok.
Kullanım: python3 scripts/discover-sync.py [--dry]
"""
import os, re, sys, json, glob, html, datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS=os.path.join(ROOT,"reports"); DISC=os.path.join(ROOT,"discover")
OGDIR=os.path.join(ROOT,"assets","discover","og")
CATALOG=os.path.join(ROOT,"assets","discover","catalog.json")
DICTMAN=os.path.join(ROOT,"assets","dictionary","dictionary.json")
SITEMAP=os.path.join(ROOT,"sitemap.xml")
DRY="--dry" in sys.argv
TODAY=os.environ.get("DICT_DATE") or datetime.date.today().isoformat()
def esc(s): return html.escape(s or "",quote=True)
def norm_url(u): return re.sub(r'\.git$','',(u or '').strip().rstrip('/').lower())
def slugify(s): return re.sub(r'[^a-z0-9]+','-',s.split('/')[-1].lower()).strip('-')

# ---- mevcut repo URL'leri (dedup) ----
def existing_urls():
    urls=set()
    for f in glob.glob(DISC+"/*/index.html"):
        t=open(f,encoding="utf-8").read()
        m=re.search(r'"codeRepository":\s*"([^"]+)"',t) or re.search(r'href="(https://github\.com/[^"]+?)"',t)
        if m: urls.add(norm_url(m.group(1)))
    return urls

# ---- rapor GitHub item'ları ----
def report_items():
    seen={}
    for f in sorted(glob.glob(REPORTS+"/*.json")):
        try: d=json.load(open(f,encoding="utf-8"))
        except Exception: continue
        date=d.get("date","")
        for sec in d.get("sections",[]):
            if sec.get("sourceName")!="github": continue
            for it in sec.get("items",[]):
                u=norm_url(it.get("url",""))
                if u and u not in seen: seen[u]={**it,"_date":date}
    return list(seen.values())

def parse_meta(meta):
    lang=""; stars=0
    m=re.search(r'★\s*([\d.]+)',meta or ''); stars=int(m.group(1).replace('.','')) if m else 0
    m2=re.match(r'^\s*([A-Za-z0-9+#. ]+?)\s*·',meta or ''); lang=m2.group(1).strip() if m2 else ""
    mom=re.search(r'(\+[\d.]+\s*bugün)',meta or ''); momentum=mom.group(1) if mom else ""
    return lang,stars,momentum

def infer_tags(summary):
    s=(summary or '').lower()
    tags=[]
    if any(k in s for k in ["yapay zek","model","ajan","llm","yapay zeka"," ai "]): tags.append("AI ajan araçları")
    tags.append("Geliştirici aracı")
    return tags[:2] or ["Geliştirici aracı"]

# ---- sözlük çapraz-link (özet içinde geçen terimler) ----
def dict_matcher():
    man=json.load(open(DICTMAN,encoding="utf-8"))
    EN={t["slug"]:t["en"] for t in man}
    ALIAS={"open-source":["açık kaynak"],"artificial-intelligence":["yapay zekâ","yapay zeka"],"llm":["büyük dil model"],
           "web-scraping":["web kazıma"],"voice-cloning":["ses klonla"],"text-to-speech":["metinden konuşma"]}
    pats=[]
    for t in man:
        ps=[t["en"]]+ALIAS.get(t["slug"],[])
        for p in ps:
            acr=p.isupper() and len(p)<=5
            pats.append((t["slug"],re.compile(r'(?<![\w-])'+re.escape(p)+r'(?![\w-])',0 if acr else re.I)))
    freq={}  # global frekans (özgül önce sıralama için kabaca)
    return EN,pats
EN_MAP,DPATS=dict_matcher()
def related_terms(summary):
    hits=[]
    for slug,rx in DPATS:
        if slug not in hits and rx.search(summary or ''): hits.append(slug)
    return hits[:5]

# ---- marka kart (font fallback: SF Pro → DejaVu → atla) ----
def make_card(slug,title,tagline,stars,lang,out):
    try:
        from PIL import Image,ImageDraw,ImageFont
    except Exception:
        return False
    FONT=next((p for p in ["/System/Library/Fonts/SFNS.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"] if os.path.exists(p)),None)
    if not FONT: return False
    W,H=1200,630;PAD=76
    NAVY=(27,73,101);YELLOW=(244,211,94);BLUE=(95,168,211);WHITE=(255,255,255);LIGHT=(205,218,229);BG_TOP=(19,44,67);BG_BOT=(9,17,28)
    def f(s,w=400):
        x=ImageFont.truetype(FONT,s)
        try:x.set_variation_by_axes([100,max(17,min(96,s)),400,w])
        except Exception:pass
        return x
    def wrap(d,t,fn,mw,ml):
        ws=t.split();ls=[];c=""
        for w in ws:
            x=(c+" "+w).strip()
            if d.textlength(x,font=fn)<=mw:c=x
            else:
                if c:ls.append(c)
                c=w
                if len(ls)==ml:break
        if c and len(ls)<ml:ls.append(c)
        return ls
    img=Image.new("RGB",(W,H),BG_BOT);d=ImageDraw.Draw(img,"RGBA")
    for yy in range(H):d.line([(0,yy),(W,yy)],fill=tuple(int(BG_TOP[i]+(BG_BOT[i]-BG_TOP[i])*(yy/H)) for i in range(3)))
    for r in (520,400,280,160):d.arc([W-260-r,H-40-r,W-260+r,H-40+r],180,360,fill=(95,168,211,28),width=3)
    k=52/100.0;x=y=PAD
    d.rounded_rectangle([x,y,x+52,y+52],radius=int(22*k),fill=NAVY)
    for r in (30,20,10):
        rr=r*k;cx,cy=x+50*k,y+56*k;d.arc([cx-rr,cy-rr,cx+rr,cy+rr],180,360,fill=BLUE,width=2)
    d.rounded_rectangle([x+20*k,y+56*k,x+80*k,y+67*k],radius=2,fill=YELLOW)
    d.rounded_rectangle([x+44.5*k,y+56*k,x+55.5*k,y+84*k],radius=2,fill=YELLOW)
    d.text((PAD+68,PAD+8),"TreScout",font=f(30,700),fill=WHITE)
    d.text((PAD,PAD+78),"KEŞİF · GİTHUB",font=f(20,700),fill=YELLOW)
    tf=f(64,800);tl=wrap(d,title,tf,W-2*PAD,2)
    for i,ln in enumerate(tl):d.text((PAD,PAD+128+i*74),ln,font=tf,fill=WHITE)
    gy=PAD+128+len(tl)*74+8
    for ln in wrap(d,tagline,f(28,400),W-2*PAD,3):d.text((PAD,gy),ln,font=f(28,400),fill=LIGHT);gy+=40
    foot=(f"★ {stars:,}".replace(',','.')+(f" · {lang}" if lang else "")) if stars else (lang or "TreScout Keşif")
    d.text((PAD,H-PAD-30),foot,font=f(24,500),fill=BLUE)
    img.save(out,"WEBP",quality=86,method=6)
    return True

LOGO='<svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>'
NAV='<nav><div class="container nav-inner"><a class="logo-link" href="/" aria-label="TreScout anasayfa">'+LOGO+'<span>TreScout</span></a><div class="nav-actions"><a href="/discover/" class="btn btn-ghost">Keşif</a><a href="/dictionary/" class="btn btn-ghost">Sözlük</a><a href="/#top" class="btn btn-primary">Erken erişim</a></div></div></nav>'
FOOTER='<footer><div class="container"><div class="footer-grid"><div class="footer-brand-block"><div class="footer-logo">'+LOGO+'<span>TreScout</span></div><p class="footer-tagline">TreScout tarar, özetler, gönderir. Siz sadece okursunuz.</p></div><div class="footer-col"><div class="footer-col-title">Ürün</div><ul><li><a href="/#how-it-works">Nasıl Çalışır</a></li><li><a href="/discover/">Keşif</a></li><li><a href="/dictionary/">Sözlük</a></li><li><a href="/reports/">Raporlar</a></li></ul></div><div class="footer-col"><div class="footer-col-title">İletişim</div><ul><li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li><li><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a></li></ul></div><div class="footer-col"><div class="footer-col-title">Sosyal medya</div><ul><li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X</a></li></ul></div></div><div class="footer-bottom"><span>© 2026 TreScout · Tüm hakları saklıdır.</span></div></div></footer>'
FORM='<form class="cta-form disc-cta-form js-subscribe" data-source="discover" novalidate><div class="form-row"><input class="input" type="email" name="email" placeholder="E-postanızı yazın" autocomplete="email" required><button class="btn btn-primary" type="submit">Erken erişim</button></div><label class="form-consent"><input type="checkbox" name="consent" required><span><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a>\'ni okudum, e-postamın bu amaçla işlenmesini onaylıyorum.</span></label><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field"></form>'
PRE=('<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
     '<link rel="preload" href="/assets/fonts/inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin>\n')
VERCEL='  <script defer src="/_vercel/insights/script.js"></script>\n  <script defer src="/_vercel/speed-insights/script.js"></script>\n'

def build_page(e):
    slug=e["slug"];title=e["title"];tagline=e["tagline"];summary=e["summary"];url=e["url"]
    lang=e["lang"];stars=e["stars"];momentum=e["momentum"];date=e["date"]
    canon=f"https://trescout.com/discover/{slug}/";ogimg=f"https://trescout.com/assets/discover/og/{slug}.webp"
    ld=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"inLanguage":"tr",
        "description":tagline,"author":{"@type":"Organization","name":"TreScout","url":"https://trescout.com"},
        "publisher":{"@type":"Organization","name":"TreScout"},"image":ogimg,"url":canon,
        "about":{"@type":"SoftwareSourceCode","name":title,"codeRepository":url,**({"programmingLanguage":lang} if lang else {})}},ensure_ascii=False,indent=2)
    metas="".join(f"<li>{esc(x)}</li>" for x in ([f"★ {stars:,}".replace(',','.')] if stars else [])+([lang] if lang else [])+[f"GitHub Trending · {date}"] if x)
    rel=related_terms(summary)
    relsec=""
    if rel:
        chips="".join(f'<a href="/dictionary/{r}/">{esc(EN_MAP.get(r,r))}</a>' for r in rel if r in EN_MAP)
        if chips: relsec=f'<section class="disc-sec"><h2>İlgili sözlük terimleri</h2><div class="disc-related">{chips}</div></section>'
    mom=f'<span class="disc-momentum">🚀 {esc(momentum)}</span>' if momentum else ''
    head=('<!DOCTYPE html>\n<html lang="tr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      f'<title>{esc(title)} · Keşif · TreScout</title>\n<meta name="description" content="{esc(tagline)}">\n'
      '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
      f'<link rel="canonical" href="{canon}">\n<meta property="og:title" content="{esc(title)}">\n<meta property="og:description" content="{esc(tagline)}">\n'
      f'<meta property="og:url" content="{canon}">\n<meta property="og:type" content="article">\n<meta property="og:locale" content="tr_TR">\n'
      f'<meta property="og:image" content="{ogimg}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:site" content="@GetTreScout">\n<meta name="twitter:title" content="{esc(title)}">\n<meta name="twitter:image" content="{ogimg}">\n'
      f'<script type="application/ld+json">\n{ld}\n</script>\n'+PRE+
      '<link rel="stylesheet" href="/assets/site.css">\n<link rel="stylesheet" href="/assets/discover.css">\n</head>\n')
    body=('<body>\n<a class="skip-link" href="#main">Ana içeriğe atla</a>\n'+NAV+'\n<main id="main">\n<article class="disc">\n'
      '<a class="disc-back" href="/discover/">← Keşif</a>\n'
      f'<div class="disc-top"><span class="disc-eyebrow">Keşif · GitHub</span>{mom}</div>\n'
      f'<h1 class="disc-title">{esc(title)}</h1>\n<p class="disc-lead">{esc(summary)}</p>\n'
      f'<ul class="disc-meta">{metas}</ul>\n{relsec}\n'
      f'<section class="disc-sec"><h2>Bağlantılar</h2><ul class="disc-links"><li><a href="{esc(url)}" target="_blank" rel="noopener">GitHub deposu →</a></li></ul></section>\n'
      '<aside class="disc-cta"><p><strong>Bunun gibi araçları her gün TreScout yakalıyor.</strong> GitHub, Hacker News ve HuggingFace taranır, öne çıkanlar Türkçe özetlenir.</p>'
      +FORM+'<a class="btn btn-ghost disc-cta-all" href="/discover/">Tüm keşifler →</a></aside>\n'
      '<p class="disc-disclaimer">TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.</p>\n'
      '</article>\n</main>\n'+FOOTER+'\n<script src="/assets/subscribe.js" defer></script>\n'+VERCEL+'</body>\n</html>\n')
    return head+body

def main():
    ex=existing_urls()
    items=report_items()
    cat=json.load(open(CATALOG,encoding="utf-8"))
    cat_slugs={c["slug"] for c in cat}
    new=[]
    for it in items:
        if norm_url(it.get("url","")) in ex: continue
        title=it.get("title","").split("/")[-1] or it.get("title","")
        slug=slugify(it.get("title",""))
        if not slug or slug in cat_slugs: continue
        lang,stars,momentum=parse_meta(it.get("meta",""))
        summary=it.get("summary","").strip()
        tagline=re.split(r'(?<=[.!?])\s',summary)[0][:120] if summary else title
        new.append({"slug":slug,"title":title,"tagline":tagline,"summary":summary,"url":it.get("url",""),
                    "lang":lang,"stars":stars,"momentum":momentum,"date":it.get("_date",TODAY),
                    "tags":infer_tags(summary)})
    print(f"rapor GitHub repo: {len(items)} · mevcut (URL): {len(ex)} · YENİ lite eklenecek: {len(new)}")
    for n in new: print(f"  + {n['slug']}  ({n['title']})")
    if DRY: print("[--dry] yazılmadı."); return
    if not new: print("eklenecek yeni repo yok · keşif güncel ✅"); return
    os.makedirs(OGDIR,exist_ok=True)
    for n in new:
        os.makedirs(os.path.join(DISC,n["slug"]),exist_ok=True)
        open(os.path.join(DISC,n["slug"],"index.html"),"w",encoding="utf-8").write(build_page(n))
        make_card(n["slug"],n["title"],n["tagline"],n["stars"],n["lang"],os.path.join(OGDIR,n["slug"]+".webp"))
        cat.append({"slug":n["slug"],"title":n["title"],"tagline":n["tagline"],
                    "meta":(f"★ {n['stars']:,}".replace(',','.')+(f" · {n['lang']}" if n['lang'] else "")) if n['stars'] else n['lang'],
                    "image":f"/assets/discover/og/{n['slug']}.webp","source":"GitHub","date":n["date"],
                    "tags":n["tags"],"stars":n["stars"],"lite":True})
    json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    sm=open(SITEMAP,encoding="utf-8").read(); lines=[]
    for n in new:
        u=f"https://trescout.com/discover/{n['slug']}/"
        if u in sm: continue
        lines+=["  <url>",f"    <loc>{u}</loc>",f"    <lastmod>{n['date']}</lastmod>","    <changefreq>monthly</changefreq>","    <priority>0.6</priority>","  </url>"]
    if lines: open(SITEMAP,"w",encoding="utf-8").write(sm.replace("</urlset>","\n".join(lines)+"\n</urlset>"))
    print(f"✅ {len(new)} lite keşif entry eklendi (catalog 'lite':true · sonra elle zenginleştir)")

if __name__=="__main__": main()
