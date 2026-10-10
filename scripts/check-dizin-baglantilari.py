#!/usr/bin/env python3
"""
Var olmayan sayfaya bağlantı guard'ı (CI).

Çevirisi eksik kalan sözlük/keşif sayfası artık yazılmıyor (dictionary-en.py,
discover-en.py · yarım çeviri yayına gitmesin). Bağlantı veren taraf buna göre
davranmazsa kırık bağlantı çıkıyor: 2026-09-27'de 5 dilin keşif dizininde 27'şer
kart ve 27 TR sayfasındaki "EN" düğmesi 404'e gidiyordu.

SIKI (çıkış kodu 1):
  - dizin sayfalarındaki kartlar (discover/ ve dictionary/ index.html, tüm diller)
  - menüdeki dil düğmeleri (nav-actions içindeki btn-ghost bağlantıları)
  - ana sayfa bağlantıları (index.html, tüm diller · scripts/ana-sayfa.py yalnız var olan
    sayfaya bağlanır; eski radar verisi catalog-home-XX.json 2026-10-10'da kalktı)
  - "ilgili terim/araç" çipleri (dict-related / disc-related) · hat bunları
    scripts/ilgili-temizle.py ile guard'dan önce temizliyor (2026-09-27: 101
    sayfada 141 ölü çip vardı)
RAPOR (çıkış kodu 0, yalnız sayı ve örnek):
  - kalan içerik bağlantıları (düz metin vb.)

Kullanım: python3 scripts/check-dizin-baglantilari.py
"""
import collections, glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ONEKLER = [""] + [f"{k}/" for k in DILLER]
DETAY = re.compile(r'href="(/(?:(?:' + "|".join(DILLER) + r')/)?(?:discover|dictionary)/[^"/#?]+/)"')
ILGILI = re.compile(r'<div class="(?:dict|disc)-related">(.*?)</div>', re.S)
NAV = re.compile(r'<div class="nav-actions">(.*?)</div></div></nav>', re.S)
_var = {}


def var(url):
    if url not in _var:
        _var[url] = os.path.exists(os.path.join(url.strip("/"), "index.html"))
    return _var[url]


siki, rapor = [], collections.Counter()
rapor_ornek = {}
for p in sorted(glob.glob("**/*.html", recursive=True)):
    if "/node_modules/" in p:
        continue
    t = open(p, encoding="utf-8", errors="ignore").read()
    dizin = any(p == f"{o}{b}/index.html" for o in ONEKLER for b in ("discover", "dictionary"))
    ana = p in [f"{o}index.html" for o in ONEKLER]
    nav = NAV.search(t)
    nav_html = nav.group(1) if nav else ""
    ilgili_html = "".join(ILGILI.findall(t))
    for u in set(DETAY.findall(t)):
        if var(u):
            continue
        if dizin:
            siki.append(f"{p}: dizin kartı → {u}")
        elif ana:
            siki.append(f"{p}: ana sayfa bağlantısı → {u} (scripts/ana-sayfa.py)")
        elif u in nav_html:
            siki.append(f"{p}: menü dil düğmesi → {u}")
        elif f'href="{u}"' in ilgili_html:
            siki.append(f"{p}: ilgili çipi → {u} (scripts/ilgili-temizle.py)")
        else:
            rapor[u] += 1
            rapor_ornek.setdefault(u, p)


if rapor:
    print(f"ℹ içerikte var olmayan sayfaya {sum(rapor.values())} bağlantı ({len(rapor)} hedef) · rapor, hattı durdurmaz")
    for u, n in rapor.most_common(5):
        print(f"   {n:3} × {u}  (ör. {rapor_ornek[u]})")
if siki:
    print(f"❌ var olmayan sayfaya bağlantı: {len(siki)}")
    for s in siki[:20]:
        print("  -", s)
    sys.exit(1)
print("✅ dizin kartları, menü dil düğmeleri ve ana sayfa yalnız var olan sayfalara bağlanıyor")
