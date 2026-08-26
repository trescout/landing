#!/usr/bin/env python3
"""
Bir dilin ana sayfasını (/<dil>/index.html) basar.

Neden ayrı ve neden küçük: Türkçe ana sayfa ürünün tamamını anlatan uzun bir
sayfa · onu her dile çevirmek, her değiştiğinde her dilde bozulması demek.
Bu sayfa yalnız GİRİŞ noktası olduğu için küçük tutuluyor: nav'daki logo ve
"erken erişim" düğmesi buraya geliyor, ziyaretçi buradan keşif ve sözlüğe
dallanıyor. Türkçe ana sayfa çevrildiğinde bu betik onun yerini bırakır.

    python3 scripts/dil-anasayfa.py --lang=fr

Kabuk (nav + footer) o dilin üretilmiş bir detay sayfasından kopyalanır ·
kanonik kaynak fix-all-headers-and-footers.js, dizin sayfası kendi kabuğunu
yazarsa tutarlılık guard'ları kırılır.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import dil, dil_dugmeleri_yaz  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("SITE_URL", "https://trescout.com")

LANG = next((a.split("=")[1] for a in sys.argv if a.startswith("--lang=")), None)
if not LANG:
    raise SystemExit("Kullanım: dil-anasayfa.py --lang=fr")
D = dil(LANG)
if not D.get("ana_h1"):
    raise SystemExit(f"✗ {LANG} için ana sayfa metinleri (ana_h1 …) diller.py'de tanımlı değil.")


def kabuk():
    """Nav + footer'ı o dilin üretilmiş bir sayfasından al."""
    dizin = os.path.join(ROOT, LANG, "discover")
    for ad in sorted(os.listdir(dizin)):
        yol = os.path.join(dizin, ad, "index.html")
        if os.path.exists(yol):
            html = open(yol, encoding="utf-8").read()
            nav = re.search(r"<nav[\s>][\s\S]*?</nav>", html)
            footer = re.search(r"<footer[\s>][\s\S]*?</footer>", html)
            if not (nav and footer):
                raise SystemExit(f"✗ {yol} içinde nav/footer bulunamadı.")
            # Ana sayfada dil düğmeleri o dilin ANA sayfasına gitmeli.
            return dil_dugmeleri_yaz(
                nav.group(0), {"TR": "/", "EN": "/en/", "FR": "/fr/"}
            ), footer.group(0)
    raise SystemExit(f"✗ {LANG}/discover altında üretilmiş sayfa yok · önce detay sayfalarını basın.")


nav, footer = kabuk()
o = D["onek"]

kartlar = "".join(
    f'<a class="disc-card lang-home-card" href="{yol}"><div class="disc-card-body">'
    f'<h2 class="disc-card-title">{ad}</h2><p class="disc-card-tag">{aciklama}</p>'
    f"</div></a>"
    for ad, yol, aciklama in D["ana_kartlar"]
)

# Onay kurgusu ana sayfada İngilizcedekiyle AYNI: onay kutusu ancak aydınlatma
# metni sonuna kadar okunduktan sonra işaretlenebiliyor (index.js scroll-gate
# modal'ı). Alt sayfalardaki sade "yeni sekmede aç" biçimi burada kullanılmıyor ·
# ilk kaydın aydınlatma eksiğiyle alındığı olay (2026-08-06) tam bu formda oldu.
form = (
    f'<form class="cta-form disc-cta-form js-subscribe" data-source="home-{LANG}" action="/api/subscribe" method="post">'
    f'<div class="form-row"><input class="input" type="email" name="email" '
    f'placeholder="{D["form_yer_tutucu"]}" autocomplete="email" required>'
    f'<button class="btn btn-primary" type="submit">{D["form_dugme"]}</button></div>'
    f'<label class="form-consent">'
    f'<input type="checkbox" name="consent" required aria-describedby="consent-hint" data-needs-consent>'
    f'<span>{D["ana_onay"].format(gizlilik=D["gizlilik_yolu"])}</span>'
    f'<span id="consent-hint" class="form-consent-hint">{D["onay_ipucu"]}</span></label>'
    f'<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">'
    f"</form>"
)

modal = f'''<div class="privacy-modal" id="privacy-modal" role="dialog" aria-modal="true" aria-labelledby="privacy-modal-title" aria-hidden="true">
    <div class="privacy-modal-card">
      <div class="privacy-modal-head">
        <h2 id="privacy-modal-title">{D["modal_baslik"]}</h2>
        <button type="button" class="privacy-modal-x" aria-label="{D["modal_kapat"]}">×</button>
      </div>
      <div class="privacy-modal-body">
        <iframe class="privacy-modal-iframe" src="about:blank" title="{D["modal_baslik"]}"></iframe>
      </div>
      <div class="privacy-modal-foot">
        <span class="privacy-modal-status" aria-live="polite">
          <span class="pulse-arrow" aria-hidden="true">↓</span>
          <span class="privacy-modal-status-text">{D["modal_kaydir"]}</span>
        </span>
        <button type="button" class="privacy-modal-confirm" disabled>{D["modal_onayla"]}</button>
      </div>
    </div>
  </div>'''

html = f"""<!DOCTYPE html>
<html lang="{D["html_lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TreScout · {D["ana_h1"]}</title>
<meta name="description" content="{D["ana_lead"]}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="canonical" href="{BASE}{o}/">
<link rel="alternate" hreflang="tr" href="{BASE}/">
<link rel="alternate" hreflang="en" href="{BASE}/en/">
<link rel="alternate" hreflang="fr" href="{BASE}/fr/">
<link rel="alternate" hreflang="x-default" href="{BASE}/en/">
<meta property="og:title" content="TreScout">
<meta property="og:description" content="{D["ana_lead"]}">
<meta property="og:url" content="{BASE}{o}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="{D["og_locale"]}">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">
<!-- index.css · aydınlatma modal'ının ve onay ipucunun biçimleri burada -->
<link rel="stylesheet" href="/assets/index.css">
</head>
<body>
<a class="skip-link" href="#main">{D["atla"]}</a>
{nav}
<main id="main">
<div class="container container-pad" id="top">
  <div class="disc-index-hero">
    <div class="disc-eyebrow">TreScout</div>
    <h1 class="disc-index-title">{D["ana_h1"]}</h1>
    <p class="disc-index-lead">{D["ana_lead"]}</p>
  </div>

  <h2 class="lang-home-h2">{D["ana_bolum"]}</h2>
  <div class="disc-grid lang-home-grid">{kartlar}</div>

  <aside class="disc-cta"><p><strong>{D["ana_kayit"]}</strong></p>{form}</aside>
  <p class="lang-home-note">{D["ana_not"]}</p>
</div>
</main>
{footer}
{modal}
<!-- Vercel provider’ları yalnızca consent sonrası provider-consent.js yükler. -->
<script type="text/plain" data-consent-src="/_vercel/insights/script.js"></script>
<script type="text/plain" data-consent-src="/_vercel/speed-insights/script.js"></script>
<script src="/assets/provider-consent.js" defer></script>
<!-- index.js · form + scroll-gate modal. Her bölümü kendi elemanını bulamazsa
     erken çıkıyor, bu yüzden ana sayfanın tamamı olmadan da güvenli. -->
<script src="/assets/index.js" defer></script>
</body>
</html>
"""

hedef = os.path.join(ROOT, LANG, "index.html")
# TAM sayfa varsa ezme · 2026-08-08'de Fransızca ana sayfa Türkçesinin tam
# çevirisi oldu (elle bakılıyor, check-sayfa-paritesi.py denetliyor). Bu betik
# yalnız giriş sayfası basıyor; üstüne yazsaydı her günlük koşuda tam sayfa
# silinirdi.
# NOT · desen regex olmalı: id özniteliği class'tan SONRA geliyor
# (<section class="section reveal" id="preview">). Düz metin araması
# "<section id=" bunu kaçırıyordu ve koruma çalışmıyordu.
if os.path.exists(hedef) and re.search(r'<section[^>]*\bid="', open(hedef, encoding="utf-8").read()):
    raise SystemExit(
        f"✗ {o}/index.html TAM sayfa görünüyor (bölümleri var) · üzerine yazılmadı.\n"
        "  Bu betik yalnız giriş sayfası basar. Tam sayfa elle bakılıyor."
    )
os.makedirs(os.path.join(ROOT, LANG), exist_ok=True)
with open(hedef, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Üretildi · {o}/index.html")
