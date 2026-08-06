#!/usr/bin/env python3
"""
TreScout · İngilizce sözlük sayfalarını Türkçesinden üretir.
============================================================

Neden gerekti: İngilizce sözlük sayfaları `build-en.js` içindeki SABİT kalıpla
üretiliyordu · "Modern software systems leverage <TERİM> to streamline data
flow…" cümlesi 480 sayfanın hepsinde aynıydı. Analoji, SSS ve "ilgili terimler"
de sabitti (her sayfada aynı beş link). Yani sayfa terimi açıklıyormuş gibi
duruyor ama hiçbir şey söylemiyordu · hem okur için değersiz hem de yakın-kopya
sayfa yığını olarak arama tarafında risk.

Yöntem `discover-en.py` ile aynı: Türkçe sayfanın gerçek bölümlerini okur,
ücretsiz uç noktadan çevirir (Gemini kotasından harcamaz), aynı CSS sınıflarıyla
basar. Çeviriler `assets/dictionary/en-cache.json`'da · tekrar çalıştırmak ucuz.

Kullanım:
  python3 scripts/dictionary-en.py [--limit=N] [--slug=rag] [--dry]
"""
import os, re, sys, json, html, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR_DIR = os.path.join(ROOT, "dictionary")
EN_DIR = os.path.join(ROOT, "en", "dictionary")
DICT = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
CACHE = os.path.join(ROOT, "assets", "dictionary", "en-cache.json")
BASE = "https://trescout.com"

DRY = "--dry" in sys.argv
LIMIT = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--limit=")), None)
ONLY = next((a.split("=")[1] for a in sys.argv if a.startswith("--slug=")), None)

_cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
_yeni = 0

BASLIK = {
    "Tanım": "Overview",
    "Nasıl çalışır?": "How it works",
    "Nerede kullanılır?": "Where it is used",
    "Sık karıştırılanlar": "Commonly confused with",
    "Sıkça sorulanlar": "Frequently asked questions",
    "İlgili terimler": "Related terms",
    "İlgili araçlar": "Related tools",
}
KATEGORI = {"ai": "AI", "web": "Web", "devops": "DevOps", "mobil": "Mobile",
            "veri": "Data", "guvenlik": "Security", "genel": "Tech"}


def tr2en(s):
    global _yeni
    s = (s or "").strip()
    if not s:
        return ""
    if s in _cache:
        return _cache[s]
    url = ("https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl=en&dt=t&q="
           + urllib.parse.quote(s))
    out, oldu = s, False
    for deneme in range(3):
        try:
            with urllib.request.urlopen(url, timeout=25) as r:
                d = json.loads(r.read().decode())
            out = "".join(p[0] for p in d[0])
            oldu = True
            break
        except Exception:
            time.sleep(1 + deneme * 2)
    # Başarısız çeviriyi ÖNBELLEĞE YAZMA · yoksa Türkçe metin kalıcı olarak
    # İngilizce sayfaya yapışır, sonraki çalıştırmalar da onu kullanır.
    if oldu:
        _cache[s] = out
        _yeni += 1
    else:
        print(f"  ! çeviri başarısız (önbelleğe yazılmadı): {s[:60]}")
    time.sleep(0.15)
    return out


def blok(pat, t, flags=re.S):
    m = re.search(pat, t, flags)
    return m.group(1) if m else ""


def metin(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h or "")).strip()


def esc(s):
    return html.escape(s or "", quote=True).replace("&#x27;", "&#39;")


def en_chrome():
    """Mevcut İngilizce sözlük sayfasından nav/footer/form al · guard'lar kanonik seti bekliyor."""
    ornek = next(os.path.join(EN_DIR, d, "index.html") for d in sorted(os.listdir(EN_DIR))
                 if os.path.isdir(os.path.join(EN_DIR, d))
                 and os.path.exists(os.path.join(EN_DIR, d, "index.html")))
    t = open(ornek, encoding="utf-8").read()
    nav = re.search(r"<nav>.*?</nav>", t, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", t, re.S).group(0)
    form = re.search(r'<form class="cta-form.*?</form>', t, re.S)
    vercel = "".join(re.findall(r'<script[^>]*src="/_vercel[^>]*></script>', t))
    return nav, footer, (form.group(0) if form else ""), vercel


def bolumler(b):
    """Bölümleri LİSTE olarak döndürür · analoji Türkçedeki gibi ilk bölümün
    hemen ardına girsin diye (tek metin olsaydı sona eklenirdi)."""
    out = []
    for m in re.finditer(r'<section class="disc-sec"><h2>(.*?)</h2>(.*?)</section>', b, re.S):
        h2, govde = metin(m.group(1)), m.group(2)
        yeni = BASLIK.get(h2) or tr2en(h2)
        if 'class="dict-faq"' in govde:
            items = ""
            for q, a in re.findall(r'<p class="dict-faq-q">(.*?)</p><p class="dict-faq-a">(.*?)</p>', govde, re.S):
                items += (f'<div class="dict-faq-item"><p class="dict-faq-q">{esc(tr2en(metin(q)))}</p>'
                          f'<p class="dict-faq-a">{esc(tr2en(metin(a)))}</p></div>')
            if items:
                out.append(f'<section class="disc-sec"><h2>{esc(yeni)}</h2><div class="dict-faq">{items}</div></section>\n')
        elif 'class="dict-related"' in govde:
            cips = ""
            for yol, ad in re.findall(r'<a href="/(dictionary|discover)/([^/]+)/">(.*?)</a>', govde, re.S) and \
                    [(m2.group(1) + "/" + m2.group(2), m2.group(3))
                     for m2 in re.finditer(r'<a href="/(dictionary|discover)/([^/]+)/">(.*?)</a>', govde, re.S)]:
                tur, slug = yol.split("/")
                if os.path.isdir(os.path.join(ROOT, "en", tur, slug)):
                    cips += f'<a href="/en/{tur}/{slug}/">{esc(metin(ad))}</a>'
            if cips:
                out.append(f'<section class="disc-sec"><h2>{esc(yeni)}</h2><div class="dict-related">{cips}</div></section>\n')
        else:
            p = metin(blok(r"<p>(.*?)</p>", govde))
            if p:
                out.append(f'<section class="disc-sec"><h2>{esc(yeni)}</h2><p>{esc(tr2en(p))}</p></section>\n')
    return out


AYLAR_EN = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]


def tarih_en(iso):
    """2026-06-03 → June 3, 2026 (Türkçe sayfadaki 'Son güncelleme' rozetinin karşılığı)."""
    try:
        y, a, g = iso.split("-")
        return f"{AYLAR_EN[int(a)-1]} {int(g)}, {y}"
    except Exception:
        return iso


def build(term, chrome):
    nav, footer, form, vercel = chrome
    slug = term["slug"]
    tp = os.path.join(TR_DIR, slug, "index.html")
    if not os.path.exists(tp):
        return None
    t = open(tp, encoding="utf-8").read()
    b = t.split("<main", 1)[1].split("</main>")[0]

    baslik = term.get("en") or slug
    full = term.get("full") or ""
    lead = tr2en(metin(blok(r'<p class="disc-lead">(.*?)</p>', b))) or (term.get("kisa_en") or "")
    analoji = metin(blok(r'<div class="dict-analogy">(.*?)</div>', b))
    analoji = analoji.replace("Şöyle düşünün:", "").strip()
    analoji_html = (f'<div class="dict-analogy"><strong>Analogy:</strong> {esc(tr2en(analoji))}</div>\n'
                    if analoji else "")
    kat = KATEGORI.get(term.get("cat", ""), (term.get("cat") or "Tech").title())
    # "Son güncelleme" rozeti · Türkçe sayfada var, İngilizcede yoktu (parite)
    gt = re.search(r'<time class="dict-time" datetime="([^"]+)"', b)
    zaman = (f'<time class="dict-time" datetime="{gt.group(1)}">Last updated: {tarih_en(gt.group(1))}</time>'
             if gt else "")
    canon_en = f"{BASE}/en/dictionary/{slug}/"
    canon_tr = f"{BASE}/dictionary/{slug}/"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "DefinedTerm", "name": baslik,
        "description": lead, "inLanguage": "en", "url": canon_en,
        "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "TreScout Tech Dictionary",
                             "url": f"{BASE}/en/dictionary/"},
    }, ensure_ascii=False, indent=2)

    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>What is {esc(baslik)}? · Dictionary · TreScout</title>\n'
            f'<meta name="description" content="{esc(lead[:155])}">\n'
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'<link rel="canonical" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="tr" href="{canon_tr}">\n'
            f'<link rel="alternate" hreflang="en" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{canon_en}">\n'
            f'<link rel="alternate" type="text/markdown" href="/en/dictionary/{slug}.md">\n'
            f'<meta property="og:title" content="What is {esc(baslik)}?">\n'
            f'<meta property="og:description" content="{esc(lead[:155])}">\n'
            f'<meta property="og:url" content="{canon_en}">\n<meta property="og:type" content="article">\n'
            '<meta property="og:locale" content="en_US">\n'
            f'<meta property="og:image" content="{BASE}/og-image.png">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            f'<script type="application/ld+json">\n{ld}\n</script>\n'
            '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
            '<link rel="stylesheet" href="/assets/site.css">\n'
            '<link rel="stylesheet" href="/assets/discover.css">\n'
            '<link rel="stylesheet" href="/assets/dictionary.css">\n</head>\n')

    govde = ('<body>\n<a class="skip-link" href="#main">Skip to main content</a>\n' + nav +
             '\n<main id="main">\n<article class="disc">\n'
             '<a class="disc-back" href="/en/dictionary/">← Dictionary</a>\n'
             f'<div class="disc-top"><span class="disc-eyebrow">Dictionary · {esc(kat)}</span>{zaman}</div>\n'
             f'<h1 class="disc-title">What is <span class="disc-accent">{esc(baslik)}</span>?</h1>\n'
             + (f'<p class="dict-en">{esc(full)}</p>\n' if full else "")
             + f'<p class="disc-lead">{esc(lead)}</p>\n'
             + (lambda s: (s[0] + analoji_html + "".join(s[1:])) if s else analoji_html)(bolumler(b))
             + '<aside class="disc-cta"><p><strong>New tech terms in your inbox every morning.</strong> '
               'Join TreScout early access for the daily digest.</p>' + form +
             '<a class="btn btn-ghost disc-cta-all" href="/en/dictionary/">All terms →</a></aside>\n'
             '<p class="disc-disclaimer">This explanation was written in plain language for TreScout · '
             'translated from the Turkish original. If something looks wrong or missing, write to '
             '<a href="mailto:hello@trescout.com">hello@trescout.com</a>. '
             f'<a href="{canon_tr}">Read in Turkish →</a></p>\n'
             '</article>\n</main>\n' + footer + '\n<script src="/assets/subscribe.js" defer></script>\n'
             + vercel + '</body>\n</html>\n')
    return head + govde


def main():
    terms = json.load(open(DICT, encoding="utf-8"))
    chrome = en_chrome()
    if ONLY:
        terms = [t for t in terms if t["slug"] == ONLY]
    if LIMIT:
        terms = terms[:LIMIT]
    yazilan = 0
    for i, term in enumerate(terms, 1):
        h = build(term, chrome)
        if not h:
            print(f"  ! {term['slug']}: Türkçe sayfa yok · atlandı")
            continue
        if DRY:
            print(f"  ~ {term['slug']}: {len(h.split())} kelime")
            continue
        d = os.path.join(EN_DIR, term["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)
        yazilan += 1
        if i % 25 == 0:
            json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
            print(f"  · {i}/{len(terms)} sayfa · önbellek {len(_cache)} kayıt")
    if not DRY:
        json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"✅ {yazilan} İngilizce sözlük sayfası · {_yeni} yeni çeviri · önbellek {len(_cache)} kayıt")


main()
