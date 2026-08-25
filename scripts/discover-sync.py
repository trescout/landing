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
import os, re, sys, json, glob, html, time, base64, datetime, urllib.request, urllib.error
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
ACR={"rag","llm","ai","tts","cli","api","ml","ui","ux","sdk","mcp","db","vtuber","osint","slm","agi","nlp","gpu","cpu","io","cv","qa","ide","crm","pdf","html","css","json","yaml","ar","vr","p2p"}
SMALL={"for","and","of","to","the","in","on","a","an","with","ile","ve","by","from"}
def nice_title(repo):
    """Repo adından otomatik düzgün başlık · zaten proper-case'i korur, tireyi boşluğa çevirir, akronimleri büyütür."""
    repo=(repo or "").strip()
    if re.search(r'[A-Z]',repo) and re.search(r'[a-z]',repo): return repo  # MoneyPrinterTurbo, Open-LLM-VTuber → aynen
    if '-' not in repo and '_' not in repo and len(repo)<=3 and repo.isalpha() and repo.islower(): return repo.upper()  # fff → FFF (≤3 akronim; odoo gibi 4-harf isimler title-case kalır)
    out=[]
    for i,w in enumerate(re.split(r'[-_]+',repo)):
        lw=w.lower()
        if lw in ACR: out.append(lw.upper())
        elif i>0 and lw in SMALL: out.append(lw)
        elif w: out.append(w[0].upper()+w[1:])
    return " ".join(out)

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
                # Aynı günün tekrarsız raporu ana raporu alfabetik olarak
                # ezebilir. Her repo için dosya sırasına değil ISO tarihe göre
                # en yeni rapor kazanmalı; eski tarih sabitlenmemeli.
                if u and (u not in seen or date >= str(seen[u].get("_date") or "")):
                    seen[u]={**it,"_date":date}
    return list(seen.values())

def parse_meta(meta):
    lang=""; stars=0
    m=re.search(r'★\s*([\d.]+)',meta or ''); stars=int(m.group(1).replace('.','')) if m else 0
    m2=re.match(r'^\s*([A-Za-z0-9+#. ]+?)\s*·',meta or ''); lang=m2.group(1).strip() if m2 else ""
    mom=re.search(r'(\+[\d.]+\s*bugün)',meta or ''); momentum=mom.group(1) if mom else ""
    return lang,stars,momentum

def make_tagline(summary, fallback):
    """Özetin ilk cümlesi · gerekirse KELİME sınırında kes (mid-word kesme yok)."""
    if not summary: return fallback
    s=re.split(r'(?<=[.!?])\s', summary.strip())[0].strip()
    if len(s)>130: s=s[:127].rsplit(' ',1)[0].rstrip(' ,;:')+"…"
    return s

def infer_tags(summary):
    s=(summary or '').lower()
    tags=[]
    if any(k in s for k in ["yapay zek","model","ajan","llm","yapay zeka"," ai "]): tags.append("Yapay zekâ araçları")
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
def make_card(slug,title,tagline,stars,lang,out,dil="tr"):
    """Marka kapak kartı (1200×630) · metin GÖRSELE gömülü olduğu için dile bağlı.
    2026-08-08'e kadar tek dosya üretiliyordu ve İngilizce/Fransızca sayfalarda
    da Türkçe etiket + Türkçe tanıtım cümlesi + Türkçe sayı biçimi görünüyordu.
    Paylaşımda çıkan OG görseli de buydu."""
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
    ETIKET={"tr":"KEŞİF · GİTHUB","en":"DISCOVER · GITHUB","fr":"DÉCOUVRIR · GITHUB",
            "pt":"DESCOBRIR · GITHUB","es":"DESCUBRIR · GITHUB"}
    BINLIK={"tr":".","en":",","fr":"\u00a0","pt":".","es":"."}
    YEDEK={"tr":"TreScout Keşif","en":"TreScout Discover","fr":"TreScout Découvrir",
           "pt":"TreScout Descobrir","es":"TreScout Descubrir"}
    d.text((PAD,PAD+78),ETIKET.get(dil,ETIKET["tr"]),font=f(20,700),fill=YELLOW)
    tf=f(64,800);tl=wrap(d,title,tf,W-2*PAD,2)
    for i,ln in enumerate(tl):d.text((PAD,PAD+128+i*74),ln,font=tf,fill=WHITE)
    gy=PAD+128+len(tl)*74+8
    for ln in wrap(d,tagline,f(28,400),W-2*PAD,3):d.text((PAD,gy),ln,font=f(28,400),fill=LIGHT);gy+=40
    foot=(f"★ {stars:,}".replace(',',BINLIK.get(dil,'.'))+(f" · {lang}" if lang else "")) if stars else (lang or YEDEK.get(dil,YEDEK["tr"]))
    d.text((PAD,H-PAD-30),foot,font=f(24,500),fill=BLUE)
    img.save(out,"WEBP",quality=86,method=6)
    return True

LOGO='<svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>'
# DİKKAT · buradaki nav/footer eskiyebilir. Kanonik chrome tek yerde:
# scripts/fix-all-headers-and-footers.js · iş akışı üretimden sonra onu çalıştırır.
# Buradaki kalıbı elle güncellerseniz oradakiyle aynı olduğundan emin olun.
NAV='<nav><div class="container nav-inner"><a class="logo-link" href="/" aria-label="TreScout anasayfa">'+LOGO+'<span>TreScout</span></a><div class="nav-actions"><a href="/discover/" class="btn btn-ghost">Keşif</a><a href="/dictionary/" class="btn btn-ghost">Sözlük</a><a href="/reports/" class="btn btn-ghost">Raporlar</a><a href="/compare/rss-vs-ai/" class="btn btn-ghost">Karşılaştır</a><a href="/en/" class="btn btn-ghost" aria-label="İngilizceye geç">EN</a><a href="/fr/" class="btn btn-ghost" aria-label="Fransızcaya geç">FR</a><a href="/pt/" class="btn btn-ghost" aria-label="Portekizceye geç">PT</a><a href="/es/" class="btn btn-ghost" aria-label="İspanyolcaya geç">ES</a><a href="/de/" class="btn btn-ghost" aria-label="Almancaya geç">DE</a></div></div></nav>'
FOOTER='<footer><div class="container"><div class="footer-grid"><div class="footer-brand-block"><div class="footer-logo">'+LOGO+'<span>TreScout</span></div><p class="footer-tagline">TreScout tarar, özetler, gönderir. Siz sadece okursunuz.</p></div><div class="footer-col"><div class="footer-col-title">Ürün</div><ul><li><a href="/#how-it-works">Nasıl Çalışır</a></li><li><a href="/discover/">Keşif</a></li><li><a href="/dictionary/">Sözlük</a></li><li><a href="/reports/">Raporlar</a></li><li><a href="/compare/rss-vs-ai/">Karşılaştır</a></li><li><a href="/#top">Erken Erişim</a></li></ul></div><div class="footer-col"><div class="footer-col-title">İletişim</div><ul><li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li><li><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a></li></ul></div><div class="footer-col"><div class="footer-col-title">Sosyal medya</div><ul><li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X</a></li></ul></div></div><div class="footer-bottom"><span>© 2026 TreScout · Tüm hakları saklıdır.</span></div></div></footer>'
FORM='<form class="cta-form disc-cta-form js-subscribe" data-source="discover" novalidate><div class="form-row"><input class="input" type="email" name="email" placeholder="E-postanızı yazın" autocomplete="email" required><button class="btn btn-primary" type="submit">Erken erişim</button></div><label class="form-consent"><input type="checkbox" name="consent" required><span><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a>\'ni okudum, e-postamın bu amaçla işlenmesini onaylıyorum.</span></label><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field"></form>'
PRE=('<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
     '<link rel="preload" href="/assets/fonts/inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin>\n')
VERCEL='  <script defer src="/_vercel/insights/script.js"></script>\n  <script defer src="/_vercel/speed-insights/script.js"></script>\n'

# ============ ZENGİN OTO (README'den gerçek komut + Gemini anlatım) ============
MODEL="gemini-3.1-flash-lite"
def gemini_key():
    k=os.environ.get("GEMINI_API_KEY")
    if k: return k
    envp=os.path.join(os.path.dirname(ROOT),"trescout-app",".env.local")
    if os.path.exists(envp):
        for l in open(envp):
            if l.strip().startswith("GEMINI_API_KEY="): return l.split("=",1)[1].strip().strip('"').strip("'")
    return None

# ---- GitHub README + meta (kimliksiz 60/saat · token varsa 5000) ----
def gh_get(url):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"trescout-discover-sync"})
    tok=os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization","Bearer "+tok)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code in (403,429,500,502,503) and attempt<2: time.sleep((attempt+1)*3); continue
            return None
        except Exception:
            if attempt<2: time.sleep((attempt+1)*3); continue
            return None
    return None
def owner_repo(url):
    m=re.search(r'github\.com/([^/]+)/([^/#?]+)',url or '')
    return (m.group(1),re.sub(r'\.git$','',m.group(2))) if m else (None,None)
def fetch_readme(owner,repo):
    d=gh_get(f"https://api.github.com/repos/{owner}/{repo}/readme")
    if not d or "content" not in d: return ""
    try: return base64.b64decode(d["content"]).decode("utf-8","replace")
    except Exception: return ""
def fetch_meta(owner,repo):
    d=gh_get(f"https://api.github.com/repos/{owner}/{repo}") or {}
    lic=((d.get("license") or {}).get("spdx_id") or "")
    hp=(d.get("homepage") or "").strip()
    return {"license":"" if lic in ("","NOASSERTION") else lic,
            "homepage":hp if hp.startswith("http") else ""}

# ---- gerçek komut bloklarını ayıkla (verbatim kaynak) ----
RUN_HINT=re.compile(r'\b(pip|pipx|uv|conda|npm|npx|pnpm|yarn|bun|cargo|go|docker|git clone|brew|apt|apt-get|make|poetry|gem|composer|dotnet|curl|wget|bash|sh|python3?|node|deno)\b')
def clean_cmd(c):
    return "\n".join(re.sub(r'^\s*\$\s+','',l) for l in (c or '').splitlines()).strip()
def install_blocks(md):
    out=[]; seen=set()
    for lang,code in re.findall(r'```([\w+.\-]*)\n(.*?)```',md,re.S):
        code=clean_cmd(code)
        lines=[l for l in code.splitlines() if l.strip() and not l.strip().startswith("#")]
        if not lines or len(lines)>8: continue
        if lang.lower() in ("bash","sh","shell","console","zsh","") and RUN_HINT.search(code) and code not in seen:
            seen.add(code); out.append(code)
    return out[:6]
def _norm(s):
    return re.sub(r'\s+',' ',re.sub(r'(?m)^\s*[\$#]\s+',' ',s or '')).strip()
def verbatim_ok(cmd,hay):
    c=_norm(cmd); return bool(c) and c in hay

# ---- Gemini: README'den zengin içerik (UYDURMA YOK, komut birebir) ----
ENRICH_SYS=("Sen TreScout için Türkçe içerik editörüsün; kod bilmeyene bir GitHub aracını tanıtıyorsun. "
 "Sana README ve ondan AYIKLANMIŞ gerçek komut blokları verilecek (boş da olabilir). "
 "MUTLAK KURALLAR: UYDURMA, sadece README'de geçeni kullan. Komutu SADECE verilen bloklardan BİREBİR al (tek karakter bile değiştirme/ekleme yok); emin değilsen boş bırak. "
 "'siz' dili; em dash (—) YASAK; pazarlama/abartı yok; TreScout bu aracı geliştirmedi, yalnızca tanıtıyor. "
 "OKUR YAZILIMCI OLMAYABİLİR: bir ürün, servis ya da teknoloji adı geçiriyorsan (Zendesk, Docker, Redis, Slack gibi) "
 "yanına 2-4 kelimeyle ne olduğunu ekle ('destek yazılımı Zendesk', 'veriyi saklayan PostgreSQL'). Kısaltmayı ilk "
 "geçtiği yerde aç. Bunu yan cümleyle yap, madde sayısını ve cümle sayısını artırma; metni uzatmak değil anlaşılır kılmak amaç. "
 "İki noktadan (:) sonra cümle geliyorsa BÜYÜK harfle başlat ('Şunu yapar: Belgeyi metne çevirir'). "
 "Yer yoksa adı HİÇ YAZMA: açıklanmamış ürün adı ('Captain ile', 'Dify ve RAGFlow ile uyumlu') okura hiçbir şey söylemez, "
 "onun yerine ne işe yaradığını yaz ('hazır sorulara otomatik yanıt verir'). Bu kural özellikle kısa maddeler için geçerli. "
 'ÇIKTI yalnızca JSON: {'
 '"baslik"(aracın ne yaptığını yakalayan KISA çekici Türkçe başlık, 2-6 kelime, blog başlığı gibi; repo adını tekrarlama, abartı/hype yok, em dash yok, AI yerine "yapay zekâ" (şapkalı/küçük), nokta opsiyonel · ör. "yapay zekâ ajanınıza kalıcı hafıza"),'
 '"kazanimlar"(3 kısa somut madde),'
 '"kurulum"([{"baslik","komut"}] 0-2, komut SADECE verilen bloklardan birebir),'
 '"calistirma"([{"baslik","komut"}] 0-2, ilk kullanım),'
 '"nasil_baslanir"(EĞER gerçek kurulum komutu YOKSA kod bilmeyenin nasıl başlayacağını 1-3 cümle DÜZ METİN anlat: kabuk komutu YAZMA, README\'de geçen indirme/resmî site/doküman yolunu tarif et. Komut varsa boş bırak),'
 '"ai_prompt"(kod bilmeyenin yapay zekâ ajanına yapıştıracağı tek paragraf Türkçe istem; yalnızca gerçek komutlara dayan),'
 '"kimin_icin"(tek cümle)}. Başka metin yok.')
def start_url(md):
    """README'nin kurulum/indirme bölümündeki ilk gerçek URL (linki uydurmadan vermek için).
    README başlığındaki rozet/görselleri (shields.io, .png/.svg ...) atlar · onlar
    'resmî kaynak' değil. Gerçek bir URL bulunmazsa "" döner (kart o satırı basmaz)."""
    BAD=re.compile(r'(?i)\.(?:png|jpe?g|gif|svg|webp|ico)(?:[?#]|$)|shields\.io|/badge/|badgen\.net')
    m=re.search(r'(?is)#{1,4}[^\n]*(?:install|setup|getting started|download|quick ?start|kurulum)[^\n]*\n(.+?)(?=\n#{1,4}\s|\Z)',md)
    region=m.group(1) if m else md[:1500]
    # Markdown link hedefleri önce, sonra çıplak URL'ler · sondaki tırnak/işaret kırpılır
    for g in re.findall(r'\((https?://[^)\s]+)\)|(https?://[^)\s\]>"\']+)',region):
        u=(g[0] or g[1]).rstrip('"\'/.,);]>')
        if u and not BAD.search(u): return u
    return ""
def _http_retry_delay(error, attempt):
    """Provider'ın Retry-After/retryDelay bilgisini kullan; response body loglama."""
    header = error.headers.get("Retry-After") if error.headers else None
    if header:
        try:
            return min(max(float(header), 1.0), 90.0)
        except ValueError:
            pass
    try:
        body = error.read().decode("utf-8", errors="replace")
        m = re.search(r'"retryDelay"\s*:\s*"([0-9.]+)s"', body)
        if m:
            return min(max(float(m.group(1)), 1.0), 90.0)
    except Exception:
        pass
    return min((attempt + 1) * 4.0, 60.0)


def gemini_enrich(title,summary,readme,blocks,key):
    payload=("ARAÇ: "+title+"\nÖZET: "+(summary or "")+"\n\nREADME:\n"+readme[:8000]+
             "\n\nAYIKLANAN GERÇEK KOMUTLAR (komutu yalnızca bunlardan, birebir seç):\n"+json.dumps(blocks,ensure_ascii=False))
    body={"systemInstruction":{"parts":[{"text":ENRICH_SYS}]},"contents":[{"parts":[{"text":payload}]}],
          "generationConfig":{"temperature":0.4,"responseMimeType":"application/json","maxOutputTokens":2048}}
    # key header'da taşınır · URL query param'ı log/proxy'lerde sızabilir
    url=f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":key},method="POST")
    for attempt in range(4):
        try:
            raw=json.loads(urllib.request.urlopen(req,timeout=120).read().decode())["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(raw)
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503) and attempt<3:
                time.sleep(_http_retry_delay(e, attempt))
                continue
            return None
        except Exception:
            if attempt<3: time.sleep((attempt+1)*4); continue
            return None
    return None

def enrich_entry(url,title,summary,key):
    """Döner: (rich_dict, None) ya da (None, reason). reason: readme_yok | komut_yok"""
    owner,repo=owner_repo(url)
    if not owner: return None,"readme_yok"
    readme=fetch_readme(owner,repo)
    if not readme.strip(): return None,"readme_yok"
    if not key: return None,"komut_yok"
    blocks=install_blocks(readme)
    g=gemini_enrich(title,summary,readme,blocks,key)
    if not isinstance(g,dict): return None,"komut_yok"
    hay=_norm(readme+" "+" ".join(blocks))
    for grp in ("kurulum","calistirma"):  # UYDURMA ENGELİ: README'de birebir geçmeyen komutu at
        g[grp]=[{"baslik":str(x.get("baslik","Komut"))[:40],"komut":clean_cmd(x.get("komut",""))}
                for x in (g.get(grp) or []) if isinstance(x,dict) and verbatim_ok(x.get("komut",""),hay)]
    g["kazanimlar"]=[str(x) for x in (g.get("kazanimlar") or [])][:4]
    g["ai_prompt"]=str(g.get("ai_prompt") or ""); g["kimin_icin"]=str(g.get("kimin_icin") or "")
    g["nasil_baslanir"]=str(g.get("nasil_baslanir") or "").strip()
    meta=fetch_meta(owner,repo); g["license"]=meta.get("license","")
    if not (g["kurulum"] or g["calistirma"]):   # komut yok → komutsuz-zengin (düz-metin başlangıç + GERÇEK link)
        g["start_url"]=meta.get("homepage") or start_url(readme)   # repo sahibinin beyan ettiği resmî site, yoksa README
        if not g["kazanimlar"] and not g["nasil_baslanir"]: return None,"komut_yok"
    return g,None

def cmd_block(it):
    return ('<div class="disc-cmd"><div class="disc-cmd-head"><span>'+esc(it.get("baslik","Komut"))+'</span>'
            '<button type="button" class="disc-copy" aria-label="Komutu kopyala">Kopyala</button></div>'
            '<pre><code>'+esc(it.get("komut",""))+'</code></pre></div>')

def rich_sections(g, cmds=None):
    s=""
    if g.get("kazanimlar"):
        s+='<section class="disc-sec"><h2>Ne kazandırır?</h2><ul class="disc-wins">'+"".join(f"<li>{esc(x)}</li>" for x in g["kazanimlar"])+'</ul></section>\n      '
    if cmds:   # elle araştırılmış + DOĞRULANMIŞ komutlar (README dışı yetkili kaynak: resmî docs / paket yöneticisi / depo)
        for grp,h in (("kurulum","Kurulum"),("calistirma","Çalıştırma")):
            its=cmds.get(grp) or []
            if its: s+=f'<section class="disc-sec"><h2>{h}</h2>'+"".join(cmd_block(it) for it in its)+'</section>\n      '
        if cmds.get("kaynak"): s+=f'<p class="disc-note"><strong>Kaynak:</strong> {esc(cmds["kaynak"])}</p>\n      '
    else:
        for grp,h in (("kurulum","Kurulum"),("calistirma","Çalıştırma")):
            if g.get(grp): s+=f'<section class="disc-sec"><h2>{h}</h2>'+"".join(cmd_block(it) for it in g[grp])+'</section>\n      '
        if not (g.get("kurulum") or g.get("calistirma")) and g.get("nasil_baslanir"):
            link=(f'<ul class="disc-links"><li><a href="{esc(g.get("start_url",""))}" target="_blank" rel="noopener">Resmî kaynak →</a></li></ul>' if g.get("start_url") else '')
            s+=f'<section class="disc-sec"><h2>Nasıl başlanır?</h2><p>{esc(g["nasil_baslanir"])}</p>{link}</section>\n      '
    komut_var=bool(g.get("kurulum") or g.get("calistirma") or (cmds and (cmds.get("kurulum") or cmds.get("calistirma"))))
    if komut_var and g.get("ai_prompt"):  # elle eklenen komutlar da bu bölümü açar (README'den komut çıkmasa bile)
        s+=('<section class="disc-sec"><h2>Kod bilmiyorsanız</h2><div class="disc-ai"><div class="disc-ai-head">'
            '<span>🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın</span>'
            '<button type="button" class="disc-copy" aria-label="İstemi kopyala">Kopyala</button></div>'
            '<p class="disc-ai-text">'+esc(g["ai_prompt"])+'</p></div></section>\n      ')
    facts=""
    if g.get("kimin_icin"): facts+='<div class="disc-fact"><span class="disc-fact-k">Kimin için</span><span class="disc-fact-v">'+esc(g["kimin_icin"])+'</span></div>'
    if g.get("license"): facts+='<div class="disc-fact"><span class="disc-fact-k">Lisans</span><span class="disc-fact-v">'+esc(g["license"])+'</span></div>'
    if facts: s+=f'<div class="disc-facts">{facts}</div>\n      '
    return s

def editorial_sections(editorial):
    """Elle doğrulanmış exemplar içeriği · kaynaklı, kısa ve taranabilir."""
    if not editorial:
        return ""
    s = ""
    if editorial.get("overview"):
        s += '<section class="disc-sec disc-editorial disc-overview"><h2>Bu araç ne yapar?</h2><p>' + esc(editorial["overview"]) + '</p></section>\n      '
    if editorial.get("best_for"):
        s += '<section class="disc-sec disc-editorial disc-best-for"><h2>Kimin için?</h2><p>' + esc(editorial["best_for"]) + '</p></section>\n      '
    if editorial.get("not_for"):
        s += '<section class="disc-sec disc-editorial disc-not-for"><h2>Ne beklememeli?</h2><p>' + esc(editorial["not_for"]) + '</p></section>\n      '
    wins = [str(x).strip() for x in (editorial.get("wins") or []) if str(x).strip()]
    if wins:
        s += '<section class="disc-sec disc-editorial disc-wins-section"><h2>Öne çıkanlar</h2><ul class="disc-wins">' + ''.join('<li>' + esc(x) + '</li>' for x in wins[:4]) + '</ul></section>\n      '
    steps = [str(x).strip() for x in (editorial.get("first_run_steps") or []) if str(x).strip()]
    if steps:
        s += '<section class="disc-sec disc-editorial disc-first-run"><h2>İlk kullanım akışı</h2><ol class="disc-steps">' + ''.join('<li>' + esc(x) + '</li>' for x in steps[:5]) + '</ol></section>\n      '
    if editorial.get("safety_note"):
        s += '<section class="disc-sec disc-editorial disc-safety"><h2>Güvenli başlangıç</h2><div class="disc-note">' + esc(editorial["safety_note"]) + '</div></section>\n      '
    if editorial.get("first_prompt"):
        s += ('<section class="disc-sec disc-editorial disc-first-prompt"><h2>İlk görev istemi</h2>'
              '<div class="disc-ai"><div class="disc-ai-head"><span>İlk adım için hazır istem</span>'
              '<button type="button" class="disc-copy" aria-label="İstemi kopyala">Kopyala</button></div>'
              '<p class="disc-ai-text">' + esc(editorial["first_prompt"]) + '</p></div></section>\n      ')
    return s


def source_links(e, url):
    """GitHub ve katalogda doğrulanmış resmî kaynaklar."""
    items = []
    if url:
        items.append(f'<li><a href="{esc(url)}" target="_blank" rel="noopener">GitHub deposu →</a></li>')
    for source in (e.get("sources") or []):
        if not isinstance(source, dict) or not source.get("url"):
            continue
        label = source.get("label") or "Resmî kaynak"
        items.append(f'<li><a href="{esc(source["url"])}" target="_blank" rel="noopener">{esc(label)} →</a></li>')
    return '<section class="disc-sec"><h2>Bağlantılar</h2><ul class="disc-links">' + ''.join(items) + '</ul></section>' if items else ""


def build_page(e, rich=None):
    slug=e["slug"];title=e["title"];tagline=e["tagline"];summary=e["summary"];url=e["url"]
    # Detay sayfası H1 · Gemini'nin yazdığı editöryel başlık (varsa); yoksa repo adı.
    # Keşif LİSTESİ (kartlar) repo adını kullanır · burası yalnız tek-tek açılan sayfa.
    headline=(rich.get("baslik") if rich else None) or e.get("headline") or title
    eyebrow_repo=f" · {esc(title)}" if headline.strip().lower()!=title.strip().lower() else ""
    lang=e["lang"];stars=e["stars"];momentum=e["momentum"];date=e["date"]
    canon=f"https://trescout.com/discover/{slug}/";ogimg=f"https://trescout.com/assets/discover/og/{slug}.webp"
    ld=json.dumps({"@context":"https://schema.org","@type":"Article","headline":headline,"inLanguage":"tr",
        "description":summary,"author":{"@type":"Organization","name":"TreScout","url":"https://trescout.com"},
        "publisher":{"@type":"Organization","name":"TreScout"},"image":ogimg,"url":canon,
        "about":{"@type":"SoftwareSourceCode","name":title,"codeRepository":url,**({"programmingLanguage":lang} if lang else {})}},ensure_ascii=False,indent=2)
    metas="".join(f"<li>{esc(x)}</li>" for x in ([f"★ {stars:,}".replace(',','.')] if stars else [])+([lang] if lang else [])+[f"GitHub Trending · {date}"] if x)
    rel=related_terms(summary)
    relsec=""
    if rel:
        chips="".join(f'<a href="/dictionary/{r}/">{esc(EN_MAP.get(r,r))}</a>' for r in rel if r in EN_MAP)
        if chips: relsec=f'<section class="disc-sec"><h2>İlgili sözlük terimleri</h2><div class="disc-related">{chips}</div></section>'
    # ↑ · marka kuralı 🚀'yi yasaklıyor (hype). Aynı bilgiyi tipografik işaretle veriyoruz.
    mom=f'<span class="disc-momentum">↑ {esc(momentum)}</span>' if momentum else ''
    editorial_html=editorial_sections(e.get("editorial"))
    rich_html=rich_sections(rich or {}, e.get("cmds")) if (rich or e.get("cmds")) else ''
    notu=(e.get("trescout_notu") or "").strip()   # elle yazılan editöryel yargı · README özetinden farkımız
    not_html=f'<aside class="disc-note"><p><strong>TreScout notu:</strong> {esc(notu)}</p></aside>\n      ' if notu else ''
    guncelleme_html=update_section(e.get("guncellemeler"))
    sh=e.get("shot"); shot_html=''
    if sh:   # lisansı temiz gerçek ekran görüntüsü (catalog 'shot' alanı · reprocess'te korunur)
        shot_html=(f'<figure class="disc-shot"><img src="{esc(sh["src"])}" width="{sh.get("w","")}" height="{sh.get("h","")}" '
                   f'loading="lazy" decoding="async" alt="{esc(sh.get("alt",""))}"><figcaption>{esc(sh.get("credit",""))}</figcaption></figure>\n      ')
    head=('<!DOCTYPE html>\n<html lang="tr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      f'<title>{esc(title)} · Keşif · TreScout</title>\n<meta name="description" content="{esc(tagline)}">\n'
      '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
      f'<link rel="alternate" type="text/markdown" href="/discover/{slug}.md">\n<link rel="canonical" href="{canon}">\n<meta property="og:title" content="{esc(title)}">\n<meta property="og:description" content="{esc(tagline)}">\n'
      f'<meta property="og:url" content="{canon}">\n<meta property="og:type" content="article">\n<meta property="og:locale" content="tr_TR">\n'
      f'<meta property="og:image" content="{ogimg}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      f'<meta property="og:image:alt" content="{esc(title)}">\n'
      f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:site" content="@GetTreScout">\n<meta name="twitter:title" content="{esc(title)}">\n<meta name="twitter:description" content="{esc(tagline)}">\n<meta name="twitter:image" content="{ogimg}">\n'
      f'<script type="application/ld+json">\n{ld}\n</script>\n'+PRE+
      '<link rel="stylesheet" href="/assets/site.css">\n<link rel="stylesheet" href="/assets/discover.css">\n</head>\n')
    body=('<body>\n<a class="skip-link" href="#main">Ana içeriğe atla</a>\n'+NAV+'\n<main id="main">\n<article class="disc">\n'
      '<a class="disc-back" href="/discover/">← Keşif</a>\n'
      f'<div class="disc-top"><span class="disc-eyebrow">Keşif · GitHub{eyebrow_repo}</span>{mom}</div>\n'
      f'<h1 class="disc-title">{esc(headline)}</h1>\n<p class="disc-lead">{esc(summary)}</p>\n'
      f'<ul class="disc-meta">{metas}</ul>\n      {not_html}{guncelleme_html}{shot_html}{editorial_html}{rich_html}{relsec}\n'
      f'{source_links(e, url)}\n'
      f'<p class="disc-disclaimer">TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun {date} tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.</p>\n'
      '<aside class="disc-cta"><p><strong>Bunun gibi araçları her gün TreScout yakalıyor.</strong> GitHub, Hacker News ve HuggingFace taranır, öne çıkanlar Türkçe özetlenir.</p>'
      +FORM+'<a class="btn btn-ghost disc-cta-all" href="/discover/">Tüm keşifler →</a></aside>\n'
      '</article>\n</main>\n'+FOOTER+'\n'+('<script src="/assets/discover.js" defer></script>\n' if rich else '')+'<script src="/assets/subscribe.js" defer></script>\n'+VERCEL+'</body>\n</html>\n')
    return head+body

AI_IZI=re.compile(r'(yapay zek|makine öğren|derin öğren|sinir ağ|büyük dil model|\bai\b|\bllm\b|\bgpt\b|\bml\b|model|ajan|agent|chatbot|sohbet bot|üretken|çıkarım|inference|transformer|embedding|vektör|neural|prompt|claude|copilot|kopilot|gemini|\bmcp\b)',re.I)
def _ai_iddiasi(s): return bool(re.search(r'yapay zek',s or '',re.I))
def _kaynakta_ai(n):
    blob=" ".join(str(n.get(k) or "") for k in ("title","tagline","summary"))+" "+" ".join(n.get("tags") or [])
    return bool(AI_IZI.search(blob))

def vet_headline(h, n, key):
    """Başlıktaki yapay zekâ iddiası kaynak metinde karşılık bulmalı.

    Model, yazım kuralını konu yönlendirmesi gibi okuyup alakasız araca (web sunucusu,
    derleyici, kütüphane) yapay zekâ iddiası ekleyebiliyor. Kaynakta iz yoksa bir kez
    daha üretiyoruz; yine geliyorsa başlığı kullanmıyoruz (mevcut başlık korunur).
    """
    if not h or not _ai_iddiasi(h) or _kaynakta_ai(n): return h
    if key:
        h2=gemini_headline(n.get("title",""), n.get("tagline",""), key,
                           extra="UYARI: Bu araç yapay zekâ ile ilgili DEĞİL. Başlıkta yapay zekâdan söz etme.")
        if h2 and not _ai_iddiasi(h2): return h2
    print(f"  ⚠ başlık reddedildi · kaynakta yapay zekâ izi yok: {n.get('slug')} → '{h}'")
    return None

def base_entry(n, rich, reason, key=None):
    """catalog kaydı · komutlu-zengin→temiz; komutsuz-zengin→lite:False ama kuyrukta (ekran görüntüsü/cila); README yok→lite+kuyruk."""
    meta=(f"★ {n['stars']:,}".replace(',','.')+(f" · {n['lang']}" if n['lang'] else "")) if n['stars'] else n['lang']
    c={"slug":n["slug"],"title":n["title"],"tagline":n["tagline"],"meta":meta,
       "image":f"/assets/discover/og/{n['slug']}.webp","source":"GitHub","date":n["date"],
       "tags":n["tags"],"stars":n["stars"]}
    if n.get("summary"):
        c["summary"] = n["summary"]
    curated = bool(rich or n.get("editorial") or n.get("cmds"))
    if n.get("headline"):
        c["headline"] = n["headline"]
    if curated:
        c["lite"]=False
        if n.get("headline_locked") and n.get("headline"):  # elle yazılmış başlık · model üzerine yazamaz
            c["headline"]=n["headline"]; c["headline_locked"]=True
        elif rich and rich.get("baslik"):  # detay sayfası editöryel H1
            nb=vet_headline(normalize_headline(rich["baslik"].strip()), n, key)
            eski=n.get("headline")
            if nb: c["headline"]=nb
            elif eski and not _ai_iddiasi(eski): c["headline"]=eski  # reddedildi · mevcut başlık temizse korunur
        if n.get("shot"): c["shot"]=n["shot"]
        if n.get("cmds"): c["cmds"]=n["cmds"]
        if n.get("editorial"): c["editorial"]=n["editorial"]
        if n.get("sources"): c["sources"]=n["sources"]
        if n.get("localized"): c["localized"]=n["localized"]
        if n.get("trescout_notu"): c["trescout_notu"]=n["trescout_notu"]
        for k in ("guncellemeler","last_review","arsivlendi"):
            if n.get(k): c[k]=n[k]
        if not (rich and (rich.get("kurulum") or rich.get("calistirma")) or n.get("cmds") or n.get("editorial")):  # hiç komut/kürasyon yok → kuyrukta
            c["needs_enrichment"]=True; c["enrich_reason"]="komutsuz"
    else:
        c.update({"lite":True,"needs_enrichment":True,"enrich_reason":reason})
    return c

HEADLINE_SYS=("Sen TreScout için Türkçe içerik editörüsün. Verilen GitHub aracı için KISA çekici bir başlık yaz: "
  "2-6 kelime, aracın ne yaptığını yakalasın, blog başlığı gibi. 'siz' dili; repo adını tekrarlama; "
  "abartı/hype yok; em dash (—) YASAK. Yalnızca tanıtımda GEÇEN yeteneği yaz, yetenek uydurma: "
  "araç yapay zekâ ile ilgili değilse başlıkta 'yapay zekâ' GEÇMESİN (web sunucusu, derleyici, kütüphane, "
  "veri deposu gibi araçlara yapay zekâ iddiası eklemek yanlış bilgidir). Yapay zekâdan söz edeceksen "
  "MUTLAKA 'yapay zekâ' (şapkalı â, küçük harf) yaz, 'AI/yapay zeka' yazma. "
  "YAZIM: Cümle düzeni kullan · yalnız ilk harf ve özel adlar büyük ('Kubernetes dağıtımlarını "
  "otomatize edin'), İngilizcedeki gibi Her Kelimeyi Büyük yazma. "
  "ÇIKTI yalnızca JSON: {\"baslik\":\"...\"}. Başka metin yok.")

def _bas_harf_buyut(s):
    """Cümle başı büyük · Türkçe 'i' → 'İ' (str.upper() 'I' verir, yanlış)."""
    if not s or not s[0].isalpha() or s[0].isupper(): return s
    return ('İ' if s[0]=='i' else s[0].upper())+s[1:]

def normalize_headline(s):
    """Marka düzeltmeleri · 'AI' → 'yapay zekâ'; 'Yapay Zeka/Zekayla' → 'yapay zekâ...' (şapkalı, küçük); em dash → ·

    'yapay zekâ' kuralı küçük harf dayattığı için cümle başındaki başlıklar da küçük
    başlıyordu (2026-08-06: 397 başlığın 117'si · 99'u 'yapay zekâ' ile). H1 olarak
    basıldıkları için son adımda ilk harf tekrar büyütülür.
    """
    s=re.sub(r'\bAI\b','yapay zekâ',s)
    s=re.sub(r'(?i)yapay\s+zek[aâ](\w*)', lambda m: 'yapay zekâ'+m.group(1), s)
    return _bas_harf_buyut(s.replace('—','·').strip())

def gemini_headline(title,tagline,key,extra=""):
    """Mevcut girdiler için yalnız başlık üreten küçük çağrı (full enrich'i tekrar etmez)."""
    payload=f"ARAÇ: {title}\nTANIM: {tagline or ''}"+(f"\n{extra}" if extra else "")
    body={"systemInstruction":{"parts":[{"text":HEADLINE_SYS}]},"contents":[{"parts":[{"text":payload}]}],
          "generationConfig":{"temperature":0.5,"responseMimeType":"application/json","maxOutputTokens":64}}
    url=f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":key},method="POST")
    for attempt in range(4):
        try:
            raw=json.loads(urllib.request.urlopen(req,timeout=60).read().decode())["candidates"][0]["content"]["parts"][0]["text"]
            b=normalize_headline((json.loads(raw).get("baslik") or "").strip())
            return b or None
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503) and attempt<3:
                time.sleep(_http_retry_delay(e, attempt))
                continue
            return None
        except Exception:
            if attempt<3: time.sleep((attempt+1)*4); continue
            return None
    return None

def _set_page_headline(c, headline):
    """Detay sayfasının H1'ini + eyebrow'unu cerrahi güncelle · diğer içerik korunur."""
    p=os.path.join(DISC,c["slug"],"index.html")
    if not os.path.exists(p): return
    html=open(p,encoding="utf-8").read()
    html=re.sub(r'<h1 class="disc-title">.*?</h1>', f'<h1 class="disc-title">{esc(headline)}</h1>', html, count=1, flags=re.S)
    if f'GitHub · {esc(c["title"])}' not in html:  # eyebrow'a repo adı ekle (yoksa)
        html=re.sub(r'(<span class="disc-eyebrow">Keşif · GitHub)(</span>)', rf'\1 · {esc(c["title"])}\2', html, count=1)
    open(p,"w",encoding="utf-8").write(html)

def audit_headlines(cat, key, limit):
    """Eski başlıkları da vet_headline ölçütünden geçir · karşılıksız yapay zekâ iddiasını temizler.

    vet_headline yalnız üretim anında çalışıyordu · guard'dan önce yazılmış başlıklar
    hiç denetlenmedi (2026-08-06 denetimi: 397 kayıtta 7 karşılıksız iddia · Argo CD,
    Insomnia gibi yapay zekâyla ilgisi olmayan araçlar). Kilitli başlık insan
    doğrulamasıdır · dokunulmaz. Döner: değişen kayıt sayısı.
    """
    supheli=[c for c in cat if c.get("headline") and not c.get("headline_locked")
             and _ai_iddiasi(c["headline"]) and not _kaynakta_ai(c)][:limit]
    if not supheli: print("  · başlık denetimi: karşılıksız yapay zekâ iddiası yok"); return 0
    print(f"  · başlık denetimi: {len(supheli)} karşılıksız iddia")
    if DRY:
        for c in supheli: print(f"    ~ {c['slug']}: {c['headline']}")
        return 0
    n=0
    for c in supheli:
        yeni=gemini_headline(c["title"], c.get("tagline",""), key,
                             extra="UYARI: Bu araç yapay zekâ ile ilgili DEĞİL. Başlıkta yapay zekâdan söz etme.")
        yeni=normalize_headline(yeni) if yeni else None
        if not yeni or _ai_iddiasi(yeni):
            print(f"    ! {c['slug']}: temiz başlık üretilemedi · elle bakın"); continue
        print(f"    ✓ {c['slug']}: {c['headline']} → {yeni}")
        c["headline"]=yeni; _set_page_headline(c, yeni); n+=1
        time.sleep(1)  # rate limit
    return n


def headline_backfill(cat, key, limit):
    """1) Normalize et (Gemini'siz · marka). 2) Eski başlıkları denetle. 3) Başlığı olmayanlara üret."""
    # 1. Mevcut başlıkları normalize et (ör. 'Yapay Zeka' → 'yapay zekâ')
    fixed=0
    for c in cat:
        if c.get("headline"):
            nb=normalize_headline(c["headline"])
            if nb!=c["headline"]:
                c["headline"]=nb; fixed+=1
                if not DRY: _set_page_headline(c, nb)
    if fixed: print(f"  · {fixed} mevcut başlık normalize edildi (marka)")
    # 2. Guard'dan önce yazılmış başlıkları denetle
    denetlenen=audit_headlines(cat, key, limit)
    if denetlenen and not DRY:
        json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    # 3. Başlığı olmayanlara üret
    todo=[c for c in cat if not c.get("headline")][:limit]
    print(f"--headlines · {len(todo)} girdiye başlık üretilecek")
    if DRY:
        for c in todo: print(f"  ~ {c['slug']}")
        print("[--dry] yazılmadı."); return
    n=0
    for c in todo:
        b=vet_headline(gemini_headline(c["title"], c.get("tagline",""), key), c, key)
        if not b: print(f"  ! {c['slug']}: başlık üretilemedi"); continue
        c["headline"]=b; _set_page_headline(c, b)
        n+=1; print(f"  ✓ {c['slug']}: {b}")
        time.sleep(1)  # rate limit
    json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print(f"✅ {n} yeni başlık · {denetlenen} denetimden geçirildi · {fixed} normalize · catalog güncellendi")

def _basligi_denetle(n, rich, key):
    """Zenginleştirmeden gelen başlığı sayfaya yazmadan önce denetle · tek kaynak.

    build_page sayfaya `rich["baslik"]`ı, base_entry kataloğa vet_headline'dan geçmiş
    hâlini yazıyordu · ikisi ayrışıyordu (2026-08-06: trek sayfasında karşılıksız
    yapay zekâ iddiası geri geldi, katalog temizdi). Denetim burada bir kez yapılır,
    iki yol da aynı değeri kullanır (base_entry'nin tekrar denetlemesi zararsız).
    """
    if not rich or not rich.get("baslik"): return
    if n.get("headline_locked") and n.get("headline"):   # insan doğrulaması · model üzerine yazamaz
        rich["baslik"]=n["headline"]; return
    b=vet_headline(normalize_headline(rich["baslik"].strip()), n, key)
    eski=n.get("headline")
    b=b or (eski if eski and not _ai_iddiasi(eski) else None)
    if b: rich["baslik"]=b
    else: rich.pop("baslik",None)   # temiz başlık yok · sayfa repo adına düşsün


def process_one(n, key, editorial=None):
    """Entry'i zenginleştir + sayfa & kart yaz. Elle editorial varsa dış model çağrılmaz."""
    rich,reason=(None,None) if editorial else enrich_entry(n["url"],n["title"],n.get("summary",""),key)
    _basligi_denetle(n, rich, key)
    page_data=dict(n)
    if editorial:
        page_data["editorial"]=editorial
    os.makedirs(os.path.join(DISC,n["slug"]),exist_ok=True)
    open(os.path.join(DISC,n["slug"],"index.html"),"w",encoding="utf-8").write(build_page(page_data,rich))
    card=os.path.join(OGDIR,n["slug"]+".webp")
    if not os.path.exists(card):   # kart başlık/tagline'a bağlı · varsa yeniden üretme (gereksiz binary churn yok)
        make_card(n["slug"],n["title"],n["tagline"],n["stars"],n["lang"],card)
    return rich,reason

def reprocess(cat, by_slug, key, targets, label):
    """Verilen entry'leri yeniden değerlendir · README+komut→zengin, komut yok→komutsuz-zengin, README yok→lite+işaret."""
    rows=[]
    for c in targets:
        f=os.path.join(DISC,c["slug"],"index.html")
        t=open(f,encoding="utf-8").read() if os.path.exists(f) else ""
        m=re.search(r'"codeRepository":\s*"([^"]+)"',t) or re.search(r'href="(https://github\.com/[^"]+?)"',t)
        lang,stars,momentum=parse_meta(c.get("meta",""))
        ls=re.search(r'<p class="disc-lead">(.*?)</p>',t,re.S)
        summary=c.get("summary") or (html.unescape(re.sub(r'<[^>]+>','',ls.group(1))).strip() if ls else c.get("tagline",""))
        rows.append({"slug":c["slug"],"title":c["title"],"tagline":c["tagline"],"summary":summary,"headline":c.get("headline"),
                     "url":m.group(1) if m else "","lang":lang,"stars":c.get("stars",stars),
                     "momentum":momentum,"date":c.get("date",TODAY),"tags":c.get("tags") or infer_tags(summary),
                     "shot":c.get("shot"),"cmds":c.get("cmds"),"editorial":c.get("editorial"),"sources":c.get("sources"),"localized":c.get("localized"),"trescout_notu":c.get("trescout_notu"),
                     "headline_locked":c.get("headline_locked"),
                     "guncellemeler":c.get("guncellemeler"),"last_review":c.get("last_review"),
                     "arsivlendi":c.get("arsivlendi")})
    print(f"{label}: {len(rows)} entry yeniden değerlendirilecek")
    if DRY:
        for n in rows: print(f"  ~ {n['slug']}  ({n['url']})")
        print("[--dry] yazılmadı."); return
    nrich=nlite=0
    for n in rows:
        if not key and not (n.get("editorial") or n.get("cmds") or n.get("trescout_notu") or n.get("shot")):
            print(f"  ! {n['slug']}: model anahtarı yok · mevcut sayfa korunuyor")
            continue
        rich,reason=process_one(n,key,n.get("editorial"))
        by_slug[n["slug"]].clear(); by_slug[n["slug"]].update(base_entry(n,rich,reason,key))
        if rich: nrich+=1; print(f"  ✅ zengin: {n['slug']} · kurulum {len(rich['kurulum'])} · çalıştırma {len(rich['calistirma'])} · prompt {'var' if rich['ai_prompt'] else 'yok'}")
        else: nlite+=1; print(f"  ◦ lite kaldı: {n['slug']} ({reason})")
    json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print(f"✅ {nrich} zengin · {nlite} lite (işaretli → aylık kuyruğa düşer) · catalog güncellendi")

# ============ TAZELEME · sayfa keşif gününde donmasın ============
AYLAR=("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
def tr_date(iso):
    """2026-08-01 → 1 Ağustos 2026"""
    try: y,m,d=[int(x) for x in iso[:10].split("-")]; return f"{d} {AYLAR[m-1]} {y}"
    except Exception: return iso

def gh_json(path):
    """GitHub REST · token varsa kullanılır (Actions'ta var), yoksa anonim sınırla çalışır."""
    req=urllib.request.Request("https://api.github.com"+path,headers={"Accept":"application/vnd.github+json",
        "User-Agent":"trescout-refresh"})
    tok=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization","Bearer "+tok)
    try:
        with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code==404: return None
        raise
    except Exception: return None

def page_repo(slug):
    f=os.path.join(DISC,slug,"index.html")
    if not os.path.exists(f): return None
    t=open(f,encoding="utf-8").read()
    m=re.search(r'"codeRepository":\s*"https://github\.com/([^/"]+)/([^/"]+)"',t)
    return f"{m.group(1)}/{m.group(2)}" if m else None

def returning_slugs():
    """Son iki rapordaki 'yeniden gündemde' kayıtları → slug kümesi."""
    url2slug={}
    for c in json.load(open(CATALOG,encoding="utf-8")):
        r=page_repo(c["slug"])
        if r: url2slug[r.lower()]=c["slug"]
    out=set()
    for f in sorted(glob.glob(REPORTS+"/*.json"))[-2:]:
        try: d=json.load(open(f,encoding="utf-8"))
        except Exception: continue
        for sec in d.get("sections",[]):
            for it in sec.get("items",[]):
                if not it.get("returning"): continue
                m=re.search(r'github\.com/([^/\s]+)/([^/\s#?]+)',it.get("url",""))
                if m:
                    s=url2slug.get(f"{m.group(1)}/{m.group(2)}".lower())
                    if s: out.add(s)
    return out

def update_section(gs):
    """Tarihli güncelleme katmanları · üzerine yazmaz, biriktirir. Yoksa boş döner."""
    if not gs: return ""
    li=[]
    for g in reversed(gs[-4:]):   # en yeni üstte · en fazla 4 katman
        p=[]
        if g.get("onceki_yildiz") and g.get("yildiz"):
            p.append(f"Yıldız {g['onceki_yildiz']:,} → {g['yildiz']:,}".replace(',','.'))
        elif g.get("yildiz"): p.append(f"Yıldız {g['yildiz']:,}".replace(',','.'))
        if g.get("surum"):
            t=f" ({tr_date(g['surum_tarihi'])})" if g.get("surum_tarihi") else ""
            p.append(f"son sürüm {esc(g['surum'])}{t}")
        if g.get("tasindi"): p.append(f"depo taşındı, yeni adresi {esc(g['tasindi'])}")
        if g.get("arsiv"): p.append("depo arşivlendi, geliştirme durdu")
        if p: li.append(f"<li><strong>{tr_date(g['tarih'])}:</strong> "+", ".join(p)+".</li>")
    if not li: return ""
    return '<section class="disc-sec"><h2>Güncelleme</h2><ul class="disc-wins">'+"".join(li)+'</ul></section>\n      '

def _set_page_update(c):
    """Sayfaya 'Güncelleme' bölümünü ve güncel yıldızı cerrahi yaz · diğer içerik korunur."""
    p=os.path.join(DISC,c["slug"],"index.html")
    if not os.path.exists(p): return
    t=open(p,encoding="utf-8").read()
    blok=update_section(c.get("guncellemeler"))
    t=re.sub(r'\s*<section class="disc-sec"><h2>Güncelleme</h2>.*?</section>\n?','\n',t,flags=re.S)
    if blok:
        # Sıra üreticiyle aynı olmalı: TreScout notu varsa onun altına, yoksa meta listesinin altına
        anchor=r'(<aside class="disc-note"><p><strong>TreScout notu:.*?</aside>\n\s*)' if 'TreScout notu:' in t \
               else r'(<ul class="disc-meta">.*?</ul>\n\s*)'
        t=re.sub(anchor,lambda m:m.group(1)+blok,t,count=1,flags=re.S)
    if c.get("stars"):  # meta listesindeki yıldız güncel kalsın
        t=re.sub(r'<li>★ [\d.]+</li>',"<li>★ "+f"{c['stars']:,}".replace(',','.')+"</li>",t,count=1)
    open(p,"w",encoding="utf-8").write(t)

def gh_graphql(repos):
    """50'şer depo tek istekte · REST'te depo başına 2 istek gerekiyordu, ikincil
    hız sınırına takılıp iş akışını düşürüyordu (403). Token yoksa boş döner."""
    tok=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not tok: return {}
    out={}
    for i in range(0,len(repos),50):
        parts=[]
        for j,r in enumerate(repos[i:i+50]):
            o,n=r.split("/",1)
            parts.append(f'r{j}: repository(owner: {json.dumps(o)}, name: {json.dumps(n)}) '
                         '{ nameWithOwner stargazerCount isArchived latestRelease { tagName publishedAt } }')
        body=json.dumps({"query":"query { "+" ".join(parts)+" }"}).encode()
        req=urllib.request.Request("https://api.github.com/graphql",data=body,method="POST",
            headers={"Authorization":"Bearer "+tok,"Content-Type":"application/json","User-Agent":"trescout-refresh"})
        try:
            with urllib.request.urlopen(req,timeout=60) as r: d=json.loads(r.read().decode())
        except Exception as e:
            print(f"  ! GraphQL isteği başarısız ({e}) · tazeleme yarıda kesildi"); break
        for v in (d.get("data") or {}).values():
            if v and v.get("nameWithOwner"): out[v["nameWithOwner"].lower()]=v
        time.sleep(1)   # nazik davran · ikincil sınıra takılma
    return out

def refresh(cat, by_slug, limit):
    """Yeniden gündeme girenler + en uzun süredir bakılmayanlar · üzerine YAZMAZ, tarihli katman ekler."""
    zengin=[c for c in cat if not c.get("lite")]
    donen=returning_slugs()
    def oncelik(c):
        return (0 if c["slug"] in donen else 1, c.get("last_review") or c.get("date") or "")
    aday=sorted(zengin,key=oncelik) if limit<=0 else sorted(zengin,key=oncelik)[:limit]   # limit=0 → hepsi
    print(f"tazeleme · {len(donen)} yeniden gündemde · {len(aday)} kayıt incelenecek")
    repolar={c["slug"]:page_repo(c["slug"]) for c in aday}
    veri=gh_graphql([r for r in repolar.values() if r])
    if not veri:
        print("  ! depo verisi alınamadı (token yok ya da istek reddedildi) · tazeleme atlandı"); return
    n=0
    for c in aday:
        repo=repolar.get(c["slug"])
        if not repo: continue
        d=veri.get(repo.lower())
        if not d: continue   # silinmiş/erişilemeyen depo
        info={"full_name":d.get("nameWithOwner"),"stargazers_count":d.get("stargazerCount"),"archived":d.get("isArchived")}
        r=d.get("latestRelease") or {}
        rel={"tag_name":r.get("tagName"),"published_at":r.get("publishedAt")}
        eski=c.get("stars") or 0; yeni=info.get("stargazers_count") or 0
        son=(c.get("guncellemeler") or [{}])[-1]
        yeni_surum=rel.get("tag_name") and rel.get("tag_name")!=son.get("surum") and rel.get("tag_name")!=c.get("surum")
        # Depo taşınmış/yeniden adlandırılmışsa API farklı full_name döner · sessiz geçmesin
        tasindi=(info.get("full_name") or "").lower()!=repo.lower()
        onemli=(eski and abs(yeni-eski)>=max(1000,eski*0.05)) or yeni_surum or tasindi or (info.get("archived") and not c.get("arsivlendi"))
        c["last_review"]=TODAY
        if onemli:
            g={"tarih":TODAY,"yildiz":yeni,"onceki_yildiz":eski}
            if rel.get("tag_name"): g["surum"]=rel["tag_name"]; g["surum_tarihi"]=(rel.get("published_at") or "")[:10]
            if info.get("archived"): g["arsiv"]=True; c["arsivlendi"]=True
            if tasindi: g["tasindi"]=info["full_name"]
            c.setdefault("guncellemeler",[]).append(g)
            c["stars"]=yeni
            lang=(c.get("meta") or "").split("·")[-1].strip() if "·" in (c.get("meta") or "") else ""
            c["meta"]=("★ "+f"{yeni:,}".replace(',','.')+(f" · {lang}" if lang else "")) if yeni else c.get("meta")
            if not DRY: _set_page_update(c)
            n+=1
            print(f"  ✅ {c['slug']}: ★{eski:,} → ★{yeni:,}".replace(',','.')+(f" · {g.get('surum','')}" if g.get("surum") else ""))
        else:
            print(f"  · {c['slug']}: kayda değer değişiklik yok")
    if not DRY: json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print(f"✅ {n} sayfaya güncelleme katmanı eklendi · {len(aday)} kayıt incelendi")

def main():
    key=gemini_key()
    cat=json.load(open(CATALOG,encoding="utf-8"))
    by_slug={c["slug"]:c for c in cat}
    os.makedirs(OGDIR,exist_ok=True)
    if "--headlines" in sys.argv:   # mevcut girdilere editöryel H1 backfill (liste kartları repo adında kalır)
        if not key and not DRY: print("UYARI: GEMINI_API_KEY yok · başlık üretilemez."); return
        la=next((a for a in sys.argv if a.startswith("--limit=")),None)
        headline_backfill(cat, key, int(la.split("=")[1]) if la else 10**9); return
    dn=next((a for a in sys.argv if a.startswith("--done=")),None)
    if dn:   # kuyruktan çıkar (insan o entry'i en iyiye çekti ya da 'uygun değil' dedi)
        slugs={s.strip() for s in dn.split("=",1)[1].split(",") if s.strip()}
        n=0
        for c in cat:
            if c["slug"] in slugs and c.get("needs_enrichment"):
                c.pop("needs_enrichment",None); c.pop("enrich_reason",None); n+=1
        json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        print(f"✅ {n} entry kuyruktan çıkarıldı: {', '.join(sorted(slugs))}"); return
    if "--refresh" in sys.argv:   # sayfa keşif gününde donmasın · yeniden gündeme girenler + en eski bakılanlar
        la=next((a for a in sys.argv if a.startswith("--limit=")),None)
        refresh(cat, by_slug, int(la.split("=")[1]) if la else 0); return   # varsayılan: hepsi
    if "--reprocess-lite" in sys.argv:
        if not key: print("UYARI: GEMINI_API_KEY yok · zenginleştirme yapılamaz, lite kalır.")
        reprocess(cat, by_slug, key, [c for c in cat if c.get("lite")], "--reprocess-lite"); return
    rpa=next((a for a in sys.argv if a.startswith("--reprocess=")),None)
    if rpa:
        if not key: print("UYARI: GEMINI_API_KEY yok · zenginleştirme yapılamaz.")
        slugs={s.strip() for s in rpa.split("=",1)[1].split(",") if s.strip()}
        reprocess(cat, by_slug, key, [c for c in cat if c["slug"] in slugs], "--reprocess="+",".join(sorted(slugs))); return
    ex=existing_urls(); items=report_items(); cat_slugs=set(by_slug)
    # Mevcut entry'lerde ilk keşif tarihi korunur; son raporda yeniden
    # görüldüğü tarih ayrı tutulur. “En yeni” görünümü ilk keşif tarihini
    # gösterir; son görülme bilgisi ileride ayrı bir freshness filtresinde
    # kullanılabilir ve ilk keşif tarihini geriye çekmez.
    url_to_entry={}
    for c in cat:
        f=os.path.join(DISC,c["slug"],"index.html")
        if not os.path.exists(f): continue
        t=open(f,encoding="utf-8").read()
        m=re.search(r'"codeRepository":\s*"([^"]+)"',t) or re.search(r'href="(https://github\.com/[^"?]+)',t)
        if m: url_to_entry[norm_url(m.group(1))]=c
    seen_existing=0
    for it in items:
        u=norm_url(it.get("url",""))
        c=url_to_entry.get(u)
        if c:
            latest=it.get("_date") or TODAY
            if latest > str(c.get("last_seen") or ""):
                c["last_seen"]=latest
                seen_existing+=1
    new=[]
    for it in items:
        if norm_url(it.get("url","")) in ex: continue
        slug=slugify(it.get("title",""))
        if not slug or slug in cat_slugs: continue
        title=nice_title(it.get("title","").split("/")[-1] or it.get("title",""))
        lang,stars,momentum=parse_meta(it.get("meta",""))
        summary=it.get("summary","").strip()
        new.append({"slug":slug,"title":title,"tagline":make_tagline(summary,title),"summary":summary,
                    "url":it.get("url",""),"lang":lang,"stars":stars,"momentum":momentum,
                    "date":it.get("_date",TODAY),"last_seen":it.get("_date",TODAY),"tags":infer_tags(summary)})
    print(f"rapor GitHub repo: {len(items)} · mevcut (URL): {len(ex)} · yeniden gündemde: {seen_existing} · YENİ: {len(new)}")
    for n in new: print(f"  + {n['slug']}  ({n['title']})")
    if DRY: print("[--dry] yazılmadı."); return
    if not new:
        if seen_existing:
            json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
            print(f"✅ {seen_existing} mevcut keşif kaydının son rapor tarihi güncellendi")
        else:
            print("eklenecek yeni repo yok · keşif güncel ✅")
        return
    nrich=nlite=0
    for n in new:
        rich,reason=process_one(n,key,n.get("editorial"))
        cat.append(base_entry(n,rich,reason,key))
        if rich: nrich+=1; print(f"  ✅ zengin: {n['slug']}")
        else: nlite+=1; print(f"  ◦ lite: {n['slug']} ({reason})")
    json.dump(cat,open(CATALOG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    sm=open(SITEMAP,encoding="utf-8").read(); lines=[]
    for n in new:
        u=f"https://trescout.com/discover/{n['slug']}/"
        if u in sm: continue
        lines+=["  <url>",f"    <loc>{u}</loc>",f"    <lastmod>{n['date']}</lastmod>","    <changefreq>monthly</changefreq>","    <priority>0.6</priority>","  </url>"]
    if lines: open(SITEMAP,"w",encoding="utf-8").write(sm.replace("</urlset>","\n".join(lines)+"\n</urlset>"))
    print(f"✅ {nrich} zengin + {nlite} lite eklendi (lite'lar aylık kuyruğa düşer)")

if __name__=="__main__": main()
