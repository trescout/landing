#!/usr/bin/env python3
"""
TreScout · {LANG} keşif sayfasını Türkçesinden üretir.
============================================================

Neden gerekti: {LANG} keşif sayfası `build-en.js` ile üretiliyordu ve o
betik Türkçe sayfalar zenginleşmeden önce yazılmış bir **SEO kabuğu**: yalnız
başlık + tek cümle + "Project Stats". 2026-08-06 denetimi: Türkçe sayfa medyanı
314 kelime, İngilizce 100 kelime. Kurulum komutları (kod · çeviri bile
gerektirmez) İngilizce tarafta hiç yoktu.

Yöntem · İngilizce raporlarda işe yarayanın aynısı: Türkçe sayfanın içerik
bloklarını okur, düzyazıyı ücretsiz çeviri uç noktasından geçirir (Gemini
kotasından harcamaz), kodu OLDUĞU GİBİ kopyalar, aynı CSS sınıflarıyla basar ·
tasarım paritesi böyle kendiliğinden geliyor.

Çeviriler `assets/discover/en-cache.json`'da saklanır: tekrar çalıştırmak
neredeyse bedava, çeviri değişimi diff'te görünür.

Kullanım:
  python3 scripts/discover-en.py            # tümü (önbellekten)
  python3 scripts/discover-en.py --limit=5  # ilk 5 sayfa
  python3 scripts/discover-en.py --slug=k-skill
  python3 scripts/discover-en.py --dry
"""
import os, re, sys, json, html, time, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import dil, tarih_yaz, chrome as chrome_kur, dil_dugmeleri_yaz, dil_hedefleri
from translation_service import translate_text

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR_DIR = os.path.join(ROOT, "discover")
LANG = next((a.split("=")[1] for a in sys.argv if a.startswith("--lang=")), "en")
D = dil(LANG)
EN_DIR = os.path.join(ROOT, LANG, "discover")
CATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")
BASE = "https://trescout.com"

DRY = "--dry" in sys.argv
LIMIT = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--limit=")), None)
ONLY = next((a.split("=")[1] for a in sys.argv if a.startswith("--slug=")), None)
CACHE = os.path.join(ROOT, "assets", "discover", f"{LANG}-cache.json")

# ── çeviri ────────────────────────────────────────────────────────────────────
_cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
_yeni = 0
_basarisiz = 0


def tr2en(s):
    """Türkçeden hedef dile · Gemini birincil, GTX ikincil; başarısızlıkta None."""
    global _yeni, _basarisiz
    s = (s or "").strip()
    if not s:
        return ""
    if s in _cache:
        return _cache[s]
    out = translate_text(s, LANG)
    if out:
        _cache[s] = out
        _yeni += 1
        time.sleep(0.15)
        return out
    _basarisiz += 1
    print(f"  ! çeviri başarısız (önbelleğe yazılmadı, sayfa korunacak): {s[:60]}")
    return None


# ── Türkçe sayfadan blok çıkarma ──────────────────────────────────────────────

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
    global _yeni
    eksik = []
    for s in metinler:
        s = (s or "").strip()
        if s and s not in _cache and "\n" not in s and s not in eksik:
            eksik.append(s)
    if not eksik:
        return
    BLOK = 25          # satır · daha büyüğünde uç nokta segmentleri birleştiriyor
    for i in range(0, len(eksik), BLOK):
        grup = eksik[i:i + BLOK]
        blok = "\n".join(grup)
        if len(blok) > 4000:            # URL sınırı · grubu ikiye böl
            toplu_isit(grup[:len(grup) // 2]); toplu_isit(grup[len(grup) // 2:])
            continue
        url = (f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl={LANG}&dt=t&q="
               + urllib.parse.quote(blok))
        try:
            with urllib.request.urlopen(url, timeout=25) as r:
                d = json.loads(r.read().decode())
            satirlar = "".join(p[0] for p in d[0]).split("\n")
        except Exception:
            continue                     # tr2en tek tek halleder
        if len(satirlar) != len(grup):
            continue                     # hizalama bozuk · bloğu at
        for kaynak, cevrilen in zip(grup, satirlar):
            cevrilen = cevrilen.strip()
            if cevrilen:
                _cache[kaynak] = cevrilen
                _yeni += 1
        time.sleep(0.3)


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
    """HTML parçasından düz metin · &#x27; gibi kaçışları çözer."""
    return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def schema_text(s):
    """Use one text representation for visible copy and Article JSON-LD."""
    return re.sub(r"\s+", " ", html.unescape(str(s or ""))).strip()


def esc(s):
    return (html.escape(s or "", quote=True).replace("&#x27;", "&#39;"))


def sayi_en(s):
    """Türkçe binlik ayırıcıyı hedef dilin biçimine çevir.

    6.780 → İngilizce 6,780 · Fransızca 6 780 (bölünmez boşluk). Çevrilmezse
    okur yanlış anlıyor: İngiliz okur 6.780'i ondalık sanar. Rapor tarafındaki
    build-lang-report.ts ile aynı kural.
    """
    return re.sub(r"\d{1,3}(?:\.\d{3})+",
                  lambda m: m.group(0).replace(".", D["binlik"]), s)


BASLIK_MAP = D["bolumler"]


def cmd_bloklari(sec_html, localized=None):
    """disc-cmd blokları · başlık çevrilir, KOD olduğu gibi kalır."""
    out = ""
    command_labels = (localized or {}).get("commands") or {}
    for m in re.finditer(r'<div class="disc-cmd">.*?<span>(.*?)</span>.*?<pre><code>(.*?)</code></pre>\s*</div>',
                         sec_html, re.S):
        original = metin(m.group(1))
        baslik = command_labels.get(original) or tr2en(original)
        kod = m.group(2)  # zaten kaçışlı · dokunma
        out += ('<div class="disc-cmd"><div class="disc-cmd-head"><span>' + esc(baslik) + '</span>'
                f'<button type="button" class="disc-copy" aria-label="{D["kopyala_komut"]}">{D["kopyala"]}</button></div>'
                '<pre><code>' + kod + '</code></pre></div>')
    return out


def bolumler(t, localized=None):
    """Türkçe sayfadaki disc-sec bölümlerini hedef dile çevirerek yeniden kur."""
    localized = localized or {}
    labels = localized.get("labels") or {}
    field_map = {
        "Bu araç ne yapar?": "overview", "Kimin için?": "best_for", "Ne beklememeli?": "not_for",
        "Öne çıkanlar": "wins", "İlk kullanım akışı": "first_run_steps",
        "Güvenli başlangıç": "safety_note", "İlk görev istemi": "first_prompt",
    }
    def value(key, fallback=""):
        return localized.get(key) or fallback
    out = ""
    # Desen "disc-sec" ile BAŞLAYAN sınıfı kabul eder · tam eşleşme aranırken
    # `class="disc-sec disc-how"` taşıyan 46 Türkçe bölüm ("Nasıl kurulur, nasıl
    # kullanılır?") beş dilde birden SESSİZCE düşüyordu · 47 aracın kurulum
    # anlatımı yalnız Türkçede vardı (2026-08-15).
    # \s* · bazı Türkçe sayfalar <section> ile <h2> arasına satır sonu koyuyor.
    # Desen bitişik beklerken o sayfanın YEDİ bölümü birden düşüyordu
    # (understand-anything · çeviride 9 başlıktan 3'ü kalmıştı).
    for m in re.finditer(r'<section class="disc-sec[^"]*">\s*<h2>(.*?)</h2>(.*?)</section>', t, re.S):
        h2, govde = metin(m.group(1)), m.group(2)
        if h2 == "Bağlantılar":
            continue  # bağlantı bölümünü aşağıda kendimiz kuruyoruz
        if h2 == "Güncelleme":
            # Güncelleme bloğunu guncelleme_en() KATALOGDAN kuruyor · burada da
            # kurulursa sayfa aynı bölümü İKİ KEZ gösteriyor. 2026-08-15'e kadar
            # tam bunu yapıyordu: 370 Türkçe sayfanın çevirisinde "Updates"
            # (tablodan, doğru etiket ve sayı biçimi) ile "Update" (buradan,
            # makine çevirisi) yan yana duruyordu · beş dilde 1850 sayfa.
            continue
        key = field_map.get(h2)
        yeni_h2 = labels.get(key) or BASLIK_MAP.get(h2) or tr2en(h2)
        # Madde listeleri · SINIF ADINA BAKMADAN. Eskiden yalnız "disc-wins"
        # tanınıyordu; aynı yapıdaki "disc-prompts" ve "disc-list" bölümleri
        # else dalına düşüp <p> aranıyordu, bulunamayınca SESSİZCE atılıyordu
        # (2026-08-15). Yeni bir liste sınıfı gelirse burası kendiliğinden alır.
        liste = re.search(r'<(ul|ol) class="(disc-[a-z-]+)">(.*?)</\1>', govde, re.S)
        if liste and 'class="disc-cmd"' not in govde and 'class="disc-related"' not in govde:
            override = value(key)
            if isinstance(override, list):
                maddeler = "".join(f"<li>{esc(str(x))}</li>" for x in override)
            else:
                maddeler = "".join(f"<li>{esc(tr2en(metin(x)))}</li>"
                                   for x in re.findall(r"<li>(.*?)</li>", liste.group(3), re.S))
            out += (f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2>'
                    f'<{liste.group(1)} class="{liste.group(2)}">{maddeler}</{liste.group(1)}></section>\n      ')
        elif 'class="disc-cmd"' in govde or 'class="disc-ai"' in govde:
            # Bir bölüm İKİSİNİ BİRDEN taşıyabiliyor (disc-how böyle: önce ajan
            # istemi, sonra komutlar). Eskiden elif zinciriydi · ikisi bir arada
            # olduğunda komut blokları düşüyordu.
            ic = ""
            if 'class="disc-ai"' in govde:
                istem = value("first_prompt") or tr2en(metin(blok(r'<p class="disc-ai-text">(.*?)</p>', govde)))
                ajan_label = labels.get("prompt_label") or D["ajan_istem"]
                ic += ('<div class="disc-ai"><div class="disc-ai-head">'
                       f'<span>{esc(ajan_label)}</span>'
                       f'<button type="button" class="disc-copy" aria-label="{D["kopyala_istem"]}">{D["kopyala"]}</button></div>'
                       '<p class="disc-ai-text">' + esc(istem) + '</p></div>')
            if 'class="disc-cmd"' in govde:
                ic += cmd_bloklari(govde, localized)
            out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2>{ic}</section>\n      '
        elif 'class="disc-related"' in govde:
            cips = "".join(f'<a href="{D["onek"]}/dictionary/{s}/">{esc(metin(a))}</a>'
                           for s, a in re.findall(r'<a href="/dictionary/([^/]+)/">(.*?)</a>', govde, re.S)
                           if os.path.isdir(os.path.join(ROOT, LANG, "dictionary", s)))
            if cips:
                out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2><div class="disc-related">{cips}</div></section>\n      '
        elif 'class="disc-note"' in govde:
            # Sorumluluk / kullanım notu · gövdesi <div class="disc-note">, <p> DEĞİL.
            # else dalı <p> arıyordu, bulamayınca bölüm sessizce düşüyordu:
            # 131 Türkçe sayfanın notu çevirilerde yalnız 34'ünde vardı ·
            # "gizlilik ve rıza sizin sorumluluğunuzda" uyarısı da bunlardan
            # biri (2026-08-15).
            ic = blok(r'(<div class="disc-note">.*?</div>)', govde)
            duz = (value("safety_note") or tr2en(metin(ic))) if h2 == "Güvenli başlangıç" else tr2en(metin(ic))
            # <strong> vurgusu kaynakta varsa koru · yoksa düz metin
            out += (f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2>'
                    f'<div class="disc-note">{esc(duz)}</div></section>\n      ')
        else:
            p = metin(blok(r"<p>(.*?)</p>", govde))
            link = blok(r'(<ul class="disc-links">.*?</ul>)', govde)
            link = link.replace("Resmî kaynak →", D["resmi_kaynak"])
            if p:
                translated = value(key) or tr2en(p)
                out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2><p>{esc(translated)}</p>{link}</section>\n      '
    return out


def olgular(t):
    """disc-facts · 'Kimin için' / 'Lisans'. Lisans adı çevrilmez (SPDX)."""
    govde = blok(r'<div class="disc-facts">(.*?)</div>\s*(?:<section|<p class="disc-disclaimer")', t)
    if not govde:
        return ""
    out = ""
    for k, v in re.findall(r'<span class="disc-fact-k">(.*?)</span><span class="disc-fact-v">(.*?)</span>', govde, re.S):
        k, v = metin(k), metin(v)
        if k == "Lisans":
            out += f'<div class="disc-fact"><span class="disc-fact-k">{D["lisans"]}</span><span class="disc-fact-v">{esc(v)}</span></div>'
        else:
            etiket = D["kimin_icin"] if k == "Kimin için" else tr2en(k)
            out += (f'<div class="disc-fact"><span class="disc-fact-k">{esc(etiket)}</span>'
                    f'<span class="disc-fact-v">{esc(tr2en(v))}</span></div>')
    return f'<div class="disc-facts">{out}</div>\n      ' if out else ""


def lisans_notu(t):
    """Sayfa düzeyindeki lisans açıklaması · <div class="disc-note"><strong>Lisans:</strong> …

    Bu blok hiçbir <section> içinde DEĞİL, bu yüzden bolumler() görmüyordu ·
    46 Türkçe sayfada var, çevirilerde HİÇ yoktu (2026-08-15). Olgular
    satırında yalnız lisansın ADI ("MIT") duruyor, ne izin verdiği burada
    yazıyor · okur için asıl bilgi bu.
    """
    m = re.search(r'<div class="disc-note"><strong>Lisans:</strong>(.*?)</div>', t, re.S)
    if not m:
        return ""
    return (f'<div class="disc-note"><strong>{esc(D["lisans"])}:</strong> '
            f'{esc(tr2en(metin(m.group(1))))}</div>\n      ')


def guncelleme_en(gs):
    """Katalogdaki yapısal güncelleme katmanları · sayılar ve tarihler veriden, metin sabit."""
    if not gs:
        return ""
    def tarih(iso):
        return tarih_yaz(iso, D)

    li = []
    for g in reversed(gs[-4:]):
        p = []
        if g.get("onceki_yildiz") and g.get("yildiz"):
            p.append(f"{D['yildiz']} {g['onceki_yildiz']:,} → {g['yildiz']:,}")
        elif g.get("yildiz"):
            p.append(f"{D['yildiz']} {g['yildiz']:,}")
        if g.get("surum"):
            t = f" ({tarih(g['surum_tarihi'])})" if g.get("surum_tarihi") else ""
            p.append(f"{D['son_surum']} {esc(g['surum'])}{t}")
        if g.get("tasindi"):
            p.append(f"{D['tasindi']} {esc(g['tasindi'])}")
        if g.get("arsiv"):
            p.append(D["arsiv"])
        if p:
            li.append(f"<li><strong>{tarih(g['tarih'])}:</strong> " + ", ".join(p) + ".</li>")
    if not li:
        return ""
    return (f'<section class="disc-sec disc-updates"><h2>{D["guncellemeler"]}</h2><ul class="disc-update-list">'
            + "".join(li) + "</ul></section>\n      ")


# ── sayfa kurulumu ────────────────────────────────────────────────────────────
# Kayıt formu · BETİKTE tanımlı, sayfadan kopyalanmıyor.
# Önce en_chrome() formu mevcut bir {LANG} keşif sayfasından çekiyordu · o
# sayfalarda hiç form olmadığı için boş dönüyordu ve 397 İngilizce keşif
# sayfasında kaydolma yolu yoktu (2026-08-07). Kısır döngüyü kırmak için
# kanonik hâli burada duruyor.
CTA_FORM = (
    f'<form class="cta-form disc-cta-form js-subscribe" data-source="discover-{LANG}" novalidate>'
    '<div class="form-row">'
    f'<input class="input" type="email" name="email" placeholder="{D["form_yer_tutucu"]}" '
    'autocomplete="email" required>'
    f'<button class="btn btn-primary" type="submit">{D["form_dugme"]}</button></div>'
    '<label class="form-consent"><input type="checkbox" name="consent" required>'
    f'<span>{D["form_onay"].format(gizlilik=D["gizlilik_yolu"])}</span></label>'
    '<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">'
    '</form>'
)


def en_chrome():
    """nav + footer · guard'lar kanonik seti bekliyor.

    İngilizce: mevcut bir sayfadan kopyalanır · o dilin kanonik kaynağı
    fix-all-headers-and-footers.js ve hattaki normalize adımı onu düzeltiyor.

    Diğer diller: DAİMA diller.py tablosundan kurulur. Normalize edici o dilleri
    atlıyor (üretici kanonik), dolayısıyla sayfadan kopyalasaydık bir kere bozulan
    kabuk her gün kendini çoğaltırdı · kırık menü kalıcı olurdu. Tablodan kurunca
    her günlük üretim aynı zamanda onarım oluyor.
    """
    ornek = None
    if LANG == "en" and os.path.isdir(EN_DIR):
        ornek = next((os.path.join(EN_DIR, d, "index.html") for d in sorted(os.listdir(EN_DIR))
                      if os.path.isdir(os.path.join(EN_DIR, d))
                      and os.path.exists(os.path.join(EN_DIR, d, "index.html"))), None)
    if not ornek:
        tr_ornek = next(os.path.join(TR_DIR, d, "index.html") for d in sorted(os.listdir(TR_DIR))
                        if os.path.exists(os.path.join(TR_DIR, d, "index.html")))
        tt = open(tr_ornek, encoding="utf-8").read()
        logo = re.search(r"<svg[^>]*>.*?</svg>", tt, re.S).group(0)
        nav, footer = chrome_kur(D, logo)
        vercel = "".join(re.findall(r'<script[^>]*src="/_vercel[^>]*></script>', tt))
        print(f"  · {LANG}: chrome diller.py tablosundan kuruldu")
        return nav, footer, CTA_FORM, vercel
    t = open(ornek, encoding="utf-8").read()
    nav = re.search(r"<nav>.*?</nav>", t, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", t, re.S).group(0)
    vercel = "".join(re.findall(r'<script[^>]*src="/_vercel[^>]*></script>', t))
    return nav, footer, CTA_FORM, vercel


def dil_degistir(nav, slug):
    """Nav'daki dil düğmelerini SAYFAYA ÖZEL yap.

    Chrome örnek bir sayfadan kopyalanıyor · o sayfanın dil bağlantıları da
    kopyalanıyordu, yani bütün sayfalar aynı hedefe gidiyordu (2026-08-07: 885
    İngilizce sayfa /dictionary/action/'a işaret ediyordu). Normalize edici bunu
    her gün düzeltiyordu, o yüzden fark edilmemişti · üretilen dillerde
    normalize edici çalışmadığı için kaynağında çözülmeli.

    Karşılığı olmayan dilde o dilin ana sayfasına düşer (404 vermesin).
    """
    return dil_dugmeleri_yaz(nav, dil_hedefleri("discover", slug, ROOT, atla={LANG.upper()}))



def build(slug, cat, chrome):
    nav, footer, form, vercel = chrome
    nav = dil_degistir(nav, slug)
    tp = os.path.join(TR_DIR, slug, "index.html")
    if not os.path.exists(tp):
        return None
    t = open(tp, encoding="utf-8").read()
    c = cat.get(slug, {})
    localized = c.get("localized", {}).get(LANG) or {}
    if not localized:
        toplu_isit(sayfa_metinleri(t))   # sayfanın çevirilerini tek istekte ısıt
    # Başlık katalogdan · sayfa <title>'ı eski üretimlerde kalıp dışı olabiliyor
    # (bir sayfada başlık yerine editöryel cümle vardı, İngilizce eyebrow'a Türkçe düşüyordu).
    title = c.get("title") or metin(blok(r"<title>(.*?)</title>", t)).split(" · ")[0]
    headline = schema_text(localized.get("headline") or tr2en(metin(blok(r'<h1 class="disc-title">(.*?)</h1>', t))))
    lead = schema_text(localized.get("lead") or tr2en(metin(blok(r'<p class="disc-lead">(.*?)</p>', t))))
    url = blok(r'<ul class="disc-links"><li><a href="([^"]+)"', t)
    sources = [source for source in (c.get("sources") or []) if isinstance(source, dict) and source.get("url")]
    date = c.get("date", "")
    mom = metin(blok(r'<span class="disc-momentum">(.*?)</span>', t))
    mom_en = sayi_en(mom).replace("bugün", D["bugun"])
    metas = ""
    for li in re.findall(r"<li>(.*?)</li>", blok(r'<ul class="disc-meta">(.*?)</ul>', t), re.S):
        v = sayi_en(metin(li))
        metas += f"<li>{esc(v)}</li>"
    notu = metin(blok(r'<aside class="disc-note"><p><strong>TreScout notu:</strong>(.*?)</p></aside>', t))
    not_html = (f'<aside class="disc-note"><p><strong>{D["trescout_notu"]}</strong> {esc(tr2en(notu))}</p></aside>\n      '
                if notu else "")
    shot = blok(r'(<figure class="disc-shot">.*?</figure>)', t)
    if shot:
        alt = re.search(r'alt="([^"]*)"', shot)
        if alt and alt.group(1):
            shot = shot.replace(f'alt="{alt.group(1)}"', f'alt="{esc(tr2en(html.unescape(alt.group(1))))}"')
        shot += "\n      "

    canon_en = f"{BASE}{D['onek']}/discover/{slug}/"
    canon_tr = f"{BASE}/discover/{slug}/"
    # Kapak metni GÖRSELE gömülü · o dilin kapağı varsa onu ver, yoksa Türkçe
    # kaynağa düş (çeviri henüz geçmemiş yeni kayıt). Bkz. kapak-gorselleri.py
    _kapak = os.path.join(ROOT, "assets", "discover", "og", f"{slug}-{LANG}.webp")
    ogimg = (f"{BASE}/assets/discover/og/{slug}-{LANG}.webp"
             if os.path.exists(_kapak) else f"{BASE}/assets/discover/og/{slug}.webp")
    tagline_en = c.get("tagline_en") or lead
    # Bazı kaynaklar tek cümlelik tagline ile gelir. Arama ve AI özetleyicileri
    # için açıklamayı ürün adıyla bağla; kısa/bağlamsız metadata geri dönmesin.
    if len(tagline_en.strip()) < 90:
        meta_tail = {
            "en": "Explore this open-source project on TreScout.",
            "fr": "Découvrez ce projet open source sur TreScout.",
            "pt": "Explore este projeto open source na TreScout.",
            "es": "Descubra este proyecto de código abierto en TreScout.",
            "de": "Entdecken Sie dieses Open-Source-Projekt auf TreScout.",
        }.get(LANG, "Explore this open-source project on TreScout.")
        tagline_en = f"{tagline_en.strip().rstrip('…').strip()} · {title} · {meta_tail}"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": headline,
        "inLanguage": D["html_lang"], "description": lead,
        "author": {"@type": "Organization", "name": "TreScout", "url": BASE},
        "publisher": {"@type": "Organization", "name": "TreScout"},
        "image": ogimg, "url": canon_en,
        "about": {"@type": "SoftwareSourceCode", "name": title, "codeRepository": url},
    }, ensure_ascii=False, indent=2)

    head = (f'<!DOCTYPE html>\n<html lang="{D["html_lang"]}">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{esc(title)} · {D["kesif"]} · TreScout</title>\n'
            f'<meta name="description" content="{esc(tagline_en)}">\n'
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'<link rel="alternate" type="text/markdown" href="{D["onek"]}/discover/{slug}.md">\n'
            f'<link rel="canonical" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="tr" href="{canon_tr}">\n'
            f'<link rel="alternate" hreflang="{D.get("hreflang", LANG)}" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{canon_en}">\n'
            f'<meta property="og:title" content="{esc(title)}">\n'
            f'<meta property="og:description" content="{esc(tagline_en)}">\n'
            f'<meta property="og:url" content="{canon_en}">\n<meta property="og:type" content="article">\n'
            f'<meta property="og:locale" content="{D["og_locale"]}">\n'
                         f'<meta property="og:image" content="{ogimg}">\n'
             '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
             f'<meta property="og:image:alt" content="{esc(title)}">\n'

            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:site" content="@GetTreScout">\n'
            f'<meta name="twitter:title" content="{esc(title)}">\n'
            f'<meta name="twitter:description" content="{esc(tagline_en)}">\n'
            f'<meta name="twitter:image" content="{ogimg}">\n'
            f'<script type="application/ld+json">\n{ld}\n</script>\n'
            '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
            '<link rel="stylesheet" href="/assets/site.css">\n'
            '<link rel="stylesheet" href="/assets/discover.css">\n</head>\n')

    eyebrow = (f'{D["kesif"]} · GitHub · {esc(title)}' if headline.strip().lower() != title.strip().lower()
               else f'{D["kesif"]} · GitHub')
    govde = ('<body>\n<a class="skip-link" href="#main">Skip to main content</a>\n' + nav +
             '\n<main id="main">\n<article class="disc">\n'
             f'<a class="disc-back" href="{D["onek"]}/discover/">{D["kesif_geri"]}</a>\n'
             f'<div class="disc-top"><span class="disc-eyebrow">{eyebrow}</span>'
             + (f'<span class="disc-momentum">{esc(mom_en)}</span>' if mom_en else "") + '</div>\n'
             f'<h1 class="disc-title">{esc(headline)}</h1>\n<p class="disc-lead">{esc(lead)}</p>\n'
             f'<ul class="disc-meta">{metas}</ul>\n      '
             + not_html + guncelleme_en(c.get("guncellemeler")) + shot + bolumler(t, localized) + olgular(t) + lisans_notu(t)              + f'<section class="disc-sec"><h2>{D["baglantilar"]}</h2><ul class="disc-links">'
             f'<li><a href="{esc(url)}" target="_blank" rel="noopener">{D["depo"]}</a></li>'
             + ''.join(f'<li><a href="{esc(source["url"])}" target="_blank" rel="noopener">{esc(source.get("label_" + LANG) or source.get("label") or D["resmi_kaynak"])} →</a></li>' for source in sources)
             + f'<li><a href="{canon_tr}">{D["turkce_oku"]}</a></li></ul></section>\n'
             # Sorumluluk notunun yanına ÇEVİRİ notu · keşif sayfalarında hiç
             # yoktu (2026-08-21 denetimi). Okur "TreScout bu aracı geliştirmedi"
             # uyarısını görüyordu ama metnin makineden geçtiğini görmüyordu.
             f'<p class="disc-disclaimer">{D["sorumluluk"].format(date=date)} '
             f'{D["ceviri_notu_kisa"]}</p>\n'
             f'<aside class="disc-cta"><p><strong>{D["cta_baslik"]}</strong> {D["cta_metin"]}</p>'
             + form + f'<a class="btn btn-ghost disc-cta-all" href="{D["onek"]}/discover/">{D["kesif_tumu"]}</a></aside>\n'
             '</article>\n</main>\n' + footer + '\n<script src="/assets/discover.js" defer></script>\n'
             '<script src="/assets/subscribe.js" defer></script>\n' + vercel + '</body>\n</html>\n')
    return head + govde


def markdown(slug, h):
    """Sayfanın .md karşılığı · llms.txt ve <link rel=alternate> bunu gösteriyor.
    İngilizce .md'ler 30 kelimelik kabuktu (Türkçesi 262) · aynı içerikten üretilir."""
    g = h.split("<main", 1)[1].split("</main>")[0]
    baslik = metin(blok(r'<h1 class="disc-title">(.*?)</h1>', g))
    lead = metin(blok(r'<p class="disc-lead">(.*?)</p>', g))
    sat = [f"# {baslik}", "", lead, ""]
    for li in re.findall(r"<li>(.*?)</li>", blok(r'<ul class="disc-meta">(.*?)</ul>', g), re.S):
        sat.append(f"- {metin(li)}")
    sat.append("")
    for m in re.finditer(r'<section class="disc-sec"><h2>(.*?)</h2>(.*?)</section>', g, re.S):
        h2, govde = metin(m.group(1)), m.group(2)
        sat.append(f"## {h2}")
        for x in re.findall(r"<li>(.*?)</li>", govde, re.S):
            sat.append(f"- {metin(x)}")
        for c in re.finditer(r'<div class="disc-cmd-head"><span>(.*?)</span>.*?<pre><code>(.*?)</code></pre>', govde, re.S):
            sat += [f"**{metin(c.group(1))}**", "", "```", html.unescape(c.group(2)), "```", ""]
        pm = re.search(r"<p[^>]*>(.*?)</p>", govde, re.S)
        if pm and "disc-cmd" not in govde:
            sat.append(metin(pm.group(1)))
        sat.append("")
    sat += ["---", D["md_kaynak_kesif"].format(url=f"{BASE}{D['onek']}/discover/{slug}/")]
    return "\n".join(sat) + "\n"


def main():
    cat = {c["slug"]: c for c in json.load(open(CATALOG, encoding="utf-8"))}
    chrome = en_chrome()
    sluglar = [ONLY] if ONLY else sorted(cat)
    if LIMIT:
        sluglar = sluglar[:LIMIT]
    yazilan = 0
    for i, slug in enumerate(sluglar, 1):
        h = build(slug, cat, chrome)
        if not h:
            print(f"  ! {slug}: Türkçe sayfa yok · atlandı")
            continue
        if DRY:
            print(f"  ~ {slug}: {len(h.split())} kelime")
            continue
        d = os.path.join(EN_DIR, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)
        open(os.path.join(EN_DIR, slug + ".md"), "w", encoding="utf-8").write(markdown(slug, h))
        yazilan += 1
        if i % 25 == 0:
            json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
            print(f"  · {i}/{len(sluglar)} sayfa · önbellek {len(_cache)} kayıt")
    if not DRY:
        json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"✅ {yazilan} {LANG} keşif sayfası · {_yeni} yeni çeviri · önbellek {len(_cache)} kayıt")


main()
