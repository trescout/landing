#!/usr/bin/env python3
"""
TreScout · {LANG} sözlük sayfasını Türkçesinden üretir.
============================================================

Neden gerekti: {LANG} sözlük sayfası `build-en.js` içindeki SABİT kalıpla
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import dil, tarih_yaz, chrome as chrome_kur, dil_dugmeleri_yaz, dil_hedefleri
from translation_service import translate_text, translate_texts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR_DIR = os.path.join(ROOT, "dictionary")
LANG = next((a.split("=")[1] for a in sys.argv if a.startswith("--lang=")), "en")
D = dil(LANG)
EN_DIR = os.path.join(ROOT, LANG, "dictionary")
DICT = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
CACHE = os.path.join(ROOT, "assets", "dictionary", f"{LANG}-cache.json")
BASE = "https://trescout.com"

DRY = "--dry" in sys.argv
LIMIT = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--limit=")), None)
ONLY = next((a.split("=")[1] for a in sys.argv if a.startswith("--slug=")), None)

_cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
_yeni = 0
_basarisiz = 0
_basarisiz_metni = set()

BASLIK = D["bolumler"]
KATEGORI = {"ai": "AI", "web": "Web", "devops": "DevOps", "mobil": "Mobile",
            "veri": "Data", "guvenlik": "Security", "genel": "Tech"}


def tr2en(s):
    global _yeni, _basarisiz
    s = (s or "").strip()
    if not s:
        return ""
    if s in _cache:
        return _cache[s]
    if s in _basarisiz_metni:
        return None
    out = translate_text(s, LANG)
    if out:
        _cache[s] = out
        _yeni += 1
        time.sleep(0.15)
        return out
    _basarisiz += 1
    _basarisiz_metni.add(s)
    print(f"  ! çeviri başarısız (önbelleğe yazılmadı, sayfa korunacak): {s[:60]}")
    return None



def toplu_isit(metinler):
    """Sayfayı basmadan ÖNCE çevirileri toplu iste · önbelleğe doldur.

    Neden: tr2en her metin için ayrı istek atıyordu. Bir keşif sayfası 20-40
    metin taşıyor, yani 40 istek. Ücretsiz uç nokta bu hacimde kısıtlamaya
    başlıyor ve istekler 25 sn timeout'a düşüyor · Portekizce üretiminde saatte
    13 sayfaya kadar indi (Fransızca'da sayfa başına 13 sn idi).

    Uç nokta çoklu `q` parametresini yok sayıyor ama SATIR BLOĞUNU segment
    segment çeviriyor: metinleri "\n" ile birleştirip tek istekte alıyoruz,
    dönen metni satırlara bölüyoruz. Satır sayısı tutmazsa blok atılır ve
    tr2en tek tek devam eder · yanlış hizalanmış çeviri yazmaktansa yavaş olmak
    yeğdir.
    """
    global _yeni, _basarisiz
    eksik = []
    for s in metinler:
        s = (s or "").strip()
        if s and s not in _cache and "\n" not in s and s not in eksik:
            eksik.append(s)
    if not eksik:
        return
    translated = translate_texts(eksik, LANG)
    for kaynak in eksik:
        cevrilen = translated.get(kaynak)
        if not cevrilen:
            cevrilen = translate_text(kaynak, LANG)
        if cevrilen:
            _cache[kaynak] = cevrilen
            _yeni += 1
        else:
            _basarisiz += 1
            _basarisiz_metni.add(kaynak)
            print(f"  ! batch çeviri başarısız (önbelleğe yazılmadı, sayfa korunacak): {kaynak[:60]}")


def sayfa_metinleri(tr_html):
    """Türkçe sayfadaki çevrilecek metinleri kabaca topla · ısıtma için.

    Kesin liste olmak zorunda değil: fazlası zararsız (önbellekte durur),
    eksiği tr2en'e düşer. Kod blokları dışarıda · onlar çevrilmiyor.
    """
    govde = re.search(r"<main[\s\S]*?</main>", tr_html)
    if not govde:
        return []
    icerik = re.sub(r"<pre[\s\S]*?</pre>|<code[\s\S]*?</code>|<script[\s\S]*?</script>", "", govde.group(0))
    return [html.unescape(m.group(1)).strip()
            for m in re.finditer(r">([^<>]{3,})<", icerik)]

def blok(pat, t, flags=re.S):
    m = re.search(pat, t, flags)
    return m.group(1) if m else ""


def metin(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h or "")).strip()


def esc(s):
    clean = str(s or "").replace("—", "·").replace("🚀", "")
    return html.escape(clean, quote=True).replace("&#x27;", "&#39;")


def make_dict_form(slug=""):
    slug_attr = f' data-content-slug="{esc(slug)}"' if slug else ''
    return (f'<form class="cta-form disc-cta-form js-subscribe" data-source="dictionary-{LANG}" data-page-type="dictionary"{slug_attr} data-cta-placement="dictionary_detail" action="/api/subscribe" method="post">'
            '<div class="form-row">'
            f'<input class="input" type="email" name="email" placeholder="{D["form_yer_tutucu"]}" autocomplete="email" required>'
            f'<button class="btn btn-primary" type="submit">{D["form_dugme"]}</button></div>'
            '<label class="form-consent"><input type="checkbox" name="consent" required>'
            f'<span>{D["form_onay"].format(gizlilik=D["gizlilik_yolu"])}</span></label>'
            '<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">'
            '</form>')


def en_chrome():
    """nav/footer/form · guard'lar kanonik seti bekliyor.

    İngilizce: mevcut sayfadan kopyalanır (kanonik kaynak normalize edici).
    Diğer diller: DAİMA diller.py tablosundan · normalize edici onları atladığı
    için sayfadan kopyalasaydık bir kere bozulan kabuk her gün çoğalırdı.
    """
    ornek = None
    if LANG == "en" and os.path.isdir(EN_DIR):
        ornek = next((os.path.join(EN_DIR, d, "index.html") for d in sorted(os.listdir(EN_DIR))
                      if os.path.isdir(os.path.join(EN_DIR, d))
                      and os.path.exists(os.path.join(EN_DIR, d, "index.html"))), None)
    if not ornek:
        # Yeni dilin ilk üretimi · kopyalanacak sayfa yok, tablodan kuruluyor.
        tr_ornek = next(os.path.join(TR_DIR, d, "index.html") for d in sorted(os.listdir(TR_DIR))
                        if os.path.exists(os.path.join(TR_DIR, d, "index.html")))
        tt = open(tr_ornek, encoding="utf-8").read()
        logo = re.search(r"<svg[^>]*>.*?</svg>", tt, re.S).group(0)
        nav, footer = chrome_kur(D, logo)
        form = make_dict_form()
        vercel = "".join(re.findall(r'<script[^>]*src="/_vercel[^>]*></script>', tt))
        print(f"  · {LANG}: ilk üretim · chrome ve form diller.py tablosundan kuruldu")
        return nav, footer, form, vercel
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
                if os.path.isdir(os.path.join(ROOT, LANG, tur, slug)):
                    cips += f'<a href="{D["onek"]}/{tur}/{slug}/">{esc(metin(ad))}</a>'
            if cips:
                out.append(f'<section class="disc-sec"><h2>{esc(yeni)}</h2><div class="dict-related">{cips}</div></section>\n')
        else:
            p = metin(blok(r"<p>(.*?)</p>", govde))
            if p:
                out.append(f'<section class="disc-sec"><h2>{esc(yeni)}</h2><p>{esc(tr2en(p))}</p></section>\n')
    return out





def tarih_en(iso):
    """ISO tarihi hedef dilin biçiminde."""
    return tarih_yaz(iso, D)


TR_HARF = re.compile(r"[çğıöşüâîÇĞİÖŞÜÂÎ]")


def ingilizce_acilim(full):
    """`full` alanı iki farklı şey tutuyor · İngilizce okurda yalnız biri işe yarar.

    Çoğu terimde kısaltmanın açılımı (RAG → "Retrieval-Augmented Generation"),
    bazılarında ise Türkçe karşılık (Offline → "Çevrimdışı", Web Scraping →
    "Web Kazıma"). İkincisi İngilizce sayfada anlamsız: okur başlığın altında
    tanımadığı bir Türkçe kelime görüyor (2026-08-07 · kullanıcı fark etti).

    Türkçe'ye özgü harf taşıyan parçaları atıyoruz. "AI · Yapay Zekâ" gibi karma
    değerlerde İngilizce parça korunur, Türkçe parça düşer.

    Sınır: özel harf içermeyen bir Türkçe ifade (ör. "Sanal Makine") elenemez.
    Veride böyle bir örnek yok · çıkarsa elle `full` alanını düzeltmek gerekir.
    """
    parcalar = [p.strip() for p in (full or "").split("·")]
    kalan = [p for p in parcalar if p and not TR_HARF.search(p)]
    return " · ".join(kalan)


def dil_degistir(nav, slug):
    """Nav'daki dil düğmelerini SAYFAYA ÖZEL yap.

    Chrome örnek bir sayfadan kopyalanıyor · o sayfanın dil bağlantıları da
    kopyalanıyordu, yani bütün sayfalar aynı hedefe gidiyordu (2026-08-07: 885
    İngilizce sayfa /dictionary/action/'a işaret ediyordu). Normalize edici bunu
    her gün düzeltiyordu, o yüzden fark edilmemişti · üretilen dillerde
    normalize edici çalışmadığı için kaynağında çözülmeli.

    Karşılığı olmayan dilde o dilin ana sayfasına düşer (404 vermesin).
    """
    return dil_dugmeleri_yaz(nav, dil_hedefleri("dictionary", slug, ROOT, atla={LANG.upper()}))



def build(term, chrome):
    nav, footer, form, vercel = chrome
    nav = dil_degistir(nav, term["slug"])
    slug = term["slug"]
    tp = os.path.join(TR_DIR, slug, "index.html")
    if not os.path.exists(tp):
        return None
    t = open(tp, encoding="utf-8").read()
    toplu_isit(sayfa_metinleri(t))   # sayfanın çevirilerini tek istekte ısıt
    b = t.split("<main", 1)[1].split("</main>")[0]

    baslik = term.get("en") or slug
    full = ingilizce_acilim(term.get("full") or "")
    lead = tr2en(metin(blok(r'<p class="disc-lead">(.*?)</p>', b))) or (term.get(D["kisa_alan"]) or "")
    analoji = metin(blok(r'<div class="dict-analogy">(.*?)</div>', b))
    analoji = analoji.replace("Şöyle düşünün:", "").strip()
    analoji_html = (f'<div class="dict-analogy"><strong>{D["analoji"]}</strong> {esc(tr2en(analoji))}</div>\n'
                    if analoji else "")
    kat = KATEGORI.get(term.get("cat", ""), (term.get("cat") or "Tech").title())
    # "Son güncelleme" rozeti · Türkçe sayfada var, İngilizcede yoktu (parite)
    gt = re.search(r'<time class="dict-time" datetime="([^"]+)"', b)
    zaman = (f'<time class="dict-time" datetime="{gt.group(1)}">{D["son_guncelleme"].format(tarih=tarih_en(gt.group(1)))}</time>'
             if gt else "")
    canon_en = f"{BASE}{D['onek']}/dictionary/{slug}/"
    canon_tr = f"{BASE}/dictionary/{slug}/"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "DefinedTerm", "name": baslik,
        "description": lead, "inLanguage": D["html_lang"], "url": canon_en,
        "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "TreScout Tech Dictionary",
                             "url": f"{BASE}{D['onek']}/dictionary/"},
    }, ensure_ascii=False, indent=2)

    head = (f'<!DOCTYPE html>\n<html lang="{D["html_lang"]}">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{D["nedir"].format(terim=esc(baslik))} · {D["sozluk"]} · TreScout</title>\n'
            f'<meta name="description" content="{esc(lead[:155])}">\n'
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'<link rel="canonical" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="tr" href="{canon_tr}">\n'
            f'<link rel="alternate" hreflang="{D.get("hreflang", LANG)}" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{canon_en}">\n'
            f'<link rel="alternate" type="text/markdown" href="{D["onek"]}/dictionary/{slug}.md">\n'
            f'<meta property="og:title" content="{D["nedir"].format(terim=esc(baslik))}">\n'
            f'<meta property="og:description" content="{esc(lead[:155])}">\n'
            f'<meta property="og:url" content="{canon_en}">\n<meta property="og:type" content="article">\n'
            f'<meta property="og:locale" content="{D["og_locale"]}">\n'
            f'<meta property="og:image" content="{BASE}/og-image.png">\n'
            '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            f'<meta property="og:image:alt" content="{esc(D["nedir"].format(terim=baslik))}">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:site" content="@GetTreScout">\n'
            f'<meta name="twitter:title" content="{esc(D["nedir"].format(terim=baslik))}">\n'
            f'<meta name="twitter:description" content="{esc(lead[:155])}">\n'
            f'<meta name="twitter:image" content="{BASE}/og-image.png">\n'
            f'<script type="application/ld+json">\n{ld}\n</script>\n'
            '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
            '<link rel="stylesheet" href="/assets/site.css">\n'
            '<link rel="stylesheet" href="/assets/discover.css">\n'
            '<link rel="stylesheet" href="/assets/dictionary.css">\n</head>\n')

    terim_accent = f'<span class="disc-accent">{esc(baslik)}</span>'
    h1_baslik = D["nedir"].format(terim=terim_accent)
    govde = (f'<body>\n<a class="skip-link" href="#main">{D["atla"]}</a>\n' + nav +
             '\n<main id="main">\n<article class="disc">\n'
             f'<a class="disc-back" href="{D["onek"]}/dictionary/">{D["sozluk_geri"]}</a>\n'
             f'<div class="disc-top"><span class="disc-eyebrow">{D["sozluk"]} · {esc(kat)}</span>{zaman}</div>\n'
             f'<h1 class="disc-title">{h1_baslik}</h1>\n'
             + (f'<p class="dict-en">{esc(full)}</p>\n' if full else "")
             + f'<p class="disc-lead">{esc(lead)}</p>\n'
             + (lambda s: (s[0] + analoji_html + "".join(s[1:])) if s else analoji_html)(bolumler(b))
             + f'<aside class="disc-cta"><p><strong>{D["sozluk_cta_baslik"]}</strong> {D["sozluk_cta_metin"]}</p>' + make_dict_form(slug) +
             f'<a class="btn btn-ghost disc-cta-all" href="{D["onek"]}/dictionary/">{D["sozluk_tumu"]}</a></aside>\n'
             # Çeviri notu · SAYFANIN DİLİNDE ve "makine çevirisi" diyerek.
             # 2026-08-21'e kadar bu cümle betikte İNGİLİZCE gömülüydü: Fransız,
             # Portekiz, İspanyol ve Alman okur sayfanın ortasında İngilizce bir
             # cümle görüyordu (493 × 5 = 2465 sayfa). Ayrıca yalnız "translated"
             # diyordu · aynı gün makine çevirisinin RAG'i "bez", MCP'yi "PCM"
             # yaptığını bulduk. Okur neyi okuduğunu bilmeli.
             f'<p class="disc-disclaimer">{D["ceviri_notu"]}'
             '<a href="mailto:hello@trescout.com">hello@trescout.com</a>. '
             f'<a href="{canon_tr}">{D["turkce_oku"]}</a></p>\n'
             '</article>\n</main>\n' + footer + '\n<script src="/assets/subscribe.js" defer></script>\n'
             + vercel + '<script src="/assets/telemetry.js" defer></script>\n</body>\n</html>\n')
    return head + govde


def markdown(term, h):
    """Sayfanın .md karşılığı · llms.txt bunu okuyor. İngilizce .md'ler de
    sabit kalıptan üretiliyordu, artık gerçek içerikten."""
    g = h.split("<main", 1)[1].split("</main>")[0]
    baslik = metin(blok(r'<h1 class="disc-title">(.*?)</h1>', g))
    full = ingilizce_acilim(metin(blok(r'<p class="dict-en">(.*?)</p>', g)))
    lead = metin(blok(r'<p class="disc-lead">(.*?)</p>', g))
    sat = [f"# {baslik}", ""]
    if full:
        sat += [f"> {full}", ""]
    sat += [lead, ""]
    an = metin(blok(r'<div class="dict-analogy">(.*?)</div>', g))
    for m in re.finditer(r'<section class="disc-sec"><h2>(.*?)</h2>(.*?)</section>', g, re.S):
        h2, govde = metin(m.group(1)), m.group(2)
        sat.append(f"## {h2}")
        for q, a2 in re.findall(r'<p class="dict-faq-q">(.*?)</p><p class="dict-faq-a">(.*?)</p>', govde, re.S):
            sat += [f"**{metin(q)}**", metin(a2), ""]
        for lnk, ad in re.findall(r'<a href="([^"]+)">(.*?)</a>', govde, re.S):
            sat.append(f"- [{metin(ad)}]({lnk})")
        pm = re.search(r"<p>(.*?)</p>", govde, re.S)
        if pm:
            sat.append(metin(pm.group(1)))
        sat.append("")
        if an and h2 == "Overview":
            sat += [f"*{an}*", ""]
            an = ""
    sat += ["---", D["md_kaynak_sozluk"].format(url=f"{BASE}{D['onek']}/dictionary/{term['slug']}/")]
    return "\n".join(sat) + "\n"


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
        open(os.path.join(EN_DIR, term["slug"] + ".md"), "w", encoding="utf-8").write(markdown(term, h))
        yazilan += 1
        if i % 25 == 0:
            json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
            print(f"  · {i}/{len(terms)} sayfa · önbellek {len(_cache)} kayıt")
    if not DRY:
        json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    if _basarisiz:
        print(f"✗ {_basarisiz} çeviri başarısız · yeni/yeniden üretilen sözlük sayfaları yazılmadı")
        raise SystemExit(1)
    print(f"✅ {yazilan} {LANG} sözlük sayfası · {_yeni} yeni çeviri · önbellek {len(_cache)} kayıt")


main()
