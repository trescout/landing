#!/usr/bin/env python3
"""
Elle bakılan çok dilli sayfaların kabuğunu (nav + footer) tazeler.

    python3 scripts/dil-kabuk-tazele.py --lang=fr

Neden gerekli: Türkçe ve İngilizce sayfaların kabuğunu `fix-all-headers-and-
footers.js` normalize ediyor · o betik üretilen dilleri (fr) bilerek atlıyor,
çünkü oralarda kanonik kaynak `diller.py`. Üretilen sayfalar kabuğu her koşuda
tablodan yeniden basıyor, yani kendiliğinden onarılıyor. Ama ELLE yazılan
Fransızca sayfalar (ana sayfa, karşılaştırma) hiçbir üreticiden geçmiyor:
menüye yeni bir bölüm eklenince onlar geride kalıyor ve nav guard'ı kırılıyor.

Bu betik o boşluğu kapatıyor: kabuğu o dilin ÜRETİLMİŞ bir sayfasından alıp
elle yazılan sayfalara basıyor, dil düğmelerini de sayfaya özel yapıyor.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import dil, dil_dugmeleri_yaz  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANG = next((a.split("=")[1] for a in sys.argv if a.startswith("--lang=")), None)
if not LANG:
    raise SystemExit("Kullanım: dil-kabuk-tazele.py --lang=fr")
dil(LANG)  # bilinmeyen dilde anlaşılır hata

# Elle yazılan sayfalar · (yol, o sayfanın diğer dillerdeki karşılıkları)
SAYFALAR = {
    "fr": [
        ("fr/index.html", {"TR": "/", "EN": "/en/", "PT": "/pt/"}),
        ("fr/compare/rss-vs-ai/index.html",
         {"TR": "/compare/rss-vs-ai/", "EN": "/en/compare/rss-vs-ai/", "PT": "/pt/compare/rss-vs-ai/"}),
    ],
    "pt": [
        ("pt/index.html", {"TR": "/", "EN": "/en/", "FR": "/fr/"}),
        ("pt/compare/rss-vs-ai/index.html",
         {"TR": "/compare/rss-vs-ai/", "EN": "/en/compare/rss-vs-ai/", "FR": "/fr/compare/rss-vs-ai/"}),
    ],
}


def uretilmis_kabuk():
    """Kabuğu o dilin üretilmiş bir sayfasından al · kanonik hâl orada."""
    for bolum in ("discover", "dictionary"):
        dizin = os.path.join(ROOT, LANG, bolum)
        if not os.path.isdir(dizin):
            continue
        for ad in sorted(os.listdir(dizin)):
            yol = os.path.join(dizin, ad, "index.html")
            if os.path.exists(yol):
                html = open(yol, encoding="utf-8").read()
                nav = re.search(r"<nav[\s>][\s\S]*?</nav>", html)
                footer = re.search(r"<footer[\s>][\s\S]*?</footer>", html)
                if nav and footer:
                    return nav.group(0), footer.group(0)
    raise SystemExit(f"✗ {LANG}/ altında üretilmiş sayfa yok · önce onları basın.")


nav_kanonik, footer_kanonik = uretilmis_kabuk()
degisen = 0
for yol, hedefler in SAYFALAR.get(LANG, []):
    tam = os.path.join(ROOT, yol)
    if not os.path.exists(tam):
        print(f"  · atlandı (yok): {yol}")
        continue
    t = open(tam, encoding="utf-8").read()
    yeni = re.sub(r"<nav[\s>][\s\S]*?</nav>",
                  lambda m: dil_dugmeleri_yaz(nav_kanonik, hedefler), t, count=1)
    yeni = re.sub(r"<footer[\s>][\s\S]*?</footer>", lambda m: footer_kanonik, yeni, count=1)
    if yeni != t:
        open(tam, "w", encoding="utf-8").write(yeni)
        degisen += 1
        print(f"  · kabuk tazelendi: {yol}")

print(f"✓ {LANG} elle yazılan sayfalar · {degisen} sayfanın kabuğu güncellendi")
