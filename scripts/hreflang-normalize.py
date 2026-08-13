#!/usr/bin/env python3
"""
hreflang normalize edici · sayfanın diğer dillerdeki sürümlerini bildirir.

    python3 scripts/hreflang-normalize.py [--dry]

Neden ayrı bir normalize edici, neden üreticilere gömülü değil: hreflang blokları
altı ayrı üreticide (üçü landing'de, biri app deposunda, ikisi elle yazılan
sayfalarda) tekrarlanıyordu ve hepsi Fransızca YOKKEN yazılmıştı. 2026-08-13
denetiminde 2035 sayfada `hreflang="fr"`, 914 sayfada `hreflang="en"` eksikti ·
yani Google Fransızca sayfaları "aynı içeriğin çevirisi" olarak kümeleyemiyordu.

Kabuk (nav/footer) için `fix-all-headers-and-footers.js` ne yapıyorsa bu da onu
yapıyor: üretimden SONRA çalışır, her sayfanın hreflang bloğunu kanonik hâle
çeker. Üretici ne basarsa bassın sonuç doğru olur · yeni dil eklenince tek yer
değişir.

KURAL · yalnız DİSKTE OLAN sürüm bildirilir. Karşılığı olmayan dile hreflang
vermek Google'ın gözünde kırık bir vaat · sayfa yoksa satır da yok.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://trescout.com"
DRY = "--dry" in sys.argv
DILLER_TUM = ["tr"] + list(DILLER)          # tr kaynak dil · tabloda yok

# Türkçe yol ↔ diğer dillerdeki yol · rapor varyantlarının adı dilde farklı
BOLUM_YOLU = {
    "dictionary": {"tr": "dictionary", "cev": "dictionary"},
    "discover": {"tr": "discover", "cev": "discover"},
    "reports": {"tr": "reports", "cev": "reports"},
    "reports-fresh": {"tr": "reports/tekrarsiz", "cev": "reports/fresh"},
    "compare": {"tr": "compare/rss-vs-ai", "cev": "compare/rss-vs-ai"},
    "home": {"tr": "", "cev": ""},
    "privacy": {"tr": "privacy.html", "cev": "privacy.html"},
}

HREFLANG_SATIR = re.compile(r'[ \t]*<link rel="alternate" hreflang="[a-z-]+" href="[^"]*">\n?')


def coz(rel):
    """Dosya yolundan (dil, bölüm, slug) çıkar · tanımadığında None."""
    parcalar = rel.split("/")
    dil = "tr"
    if parcalar[0] in DILLER:
        dil, parcalar = parcalar[0], parcalar[1:]
    kalan = "/".join(parcalar)

    if kalan == "index.html":
        return dil, "home", None
    if kalan == "privacy.html":
        return dil, "privacy", None
    if kalan == "compare/rss-vs-ai/index.html":
        return dil, "compare", None
    for bolum in ("dictionary", "discover"):
        if kalan == f"{bolum}/index.html":
            return dil, bolum, None
        m = re.fullmatch(rf"{bolum}/([^/]+)/index\.html", kalan)
        if m:
            return dil, bolum, m.group(1)
    taze_yol = "reports/tekrarsiz" if dil == "tr" else "reports/fresh"
    if kalan == f"{taze_yol}/index.html":
        return dil, "reports-fresh", None
    m = re.fullmatch(rf"{re.escape(taze_yol)}/(\d{{4}}-\d{{2}}-\d{{2}})/index\.html", kalan)
    if m:
        return dil, "reports-fresh", m.group(1)
    if kalan == "reports/index.html":
        return dil, "reports", None
    m = re.fullmatch(r"reports/(\d{4}-\d{2}-\d{2})/index\.html", kalan)
    if m:
        return dil, "reports", m.group(1)
    return None


def url_ve_dosya(dil, bolum, slug):
    yol = BOLUM_YOLU[bolum]["tr" if dil == "tr" else "cev"]
    onek = "" if dil == "tr" else f"{dil}/"
    if bolum == "privacy":
        rel = f"{onek}privacy.html"
        return f"{BASE}/{rel}", rel
    parcalar = [p for p in (onek.rstrip("/"), yol, slug) if p]
    dizin = "/".join(parcalar)
    url = f"{BASE}/{dizin}/" if dizin else f"{BASE}/"
    return url, os.path.join(dizin, "index.html") if dizin else "index.html"


def blok(bolum, slug):
    satirlar, en_url, tr_url = [], None, None
    for dil in DILLER_TUM:
        url, dosya = url_ve_dosya(dil, bolum, slug)
        if not os.path.exists(os.path.join(ROOT, dosya)):
            continue
        satirlar.append(f'<link rel="alternate" hreflang="{dil}" href="{url}">')
        if dil == "en":
            en_url = url
        if dil == "tr":
            tr_url = url
    if len(satirlar) < 2:
        return None                      # tek dilli sayfa · hreflang anlamsız
    # x-default · İngilizce sürüm varsa o, yoksa Türkçe kaynak
    satirlar.append(f'<link rel="alternate" hreflang="x-default" href="{en_url or tr_url}">')
    return "\n".join(satirlar) + "\n"


def normalize(dry=False):
    degisen = kapsam = atlanan = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
        if "/node_modules/" in p:
            continue
        rel = os.path.relpath(p, ROOT)
        coz_sonuc = coz(rel)
        if not coz_sonuc:
            atlanan += 1
            continue
        dil, bolum, slug = coz_sonuc
        yeni = blok(bolum, slug)
        if not yeni:
            continue
        kapsam += 1
        html = open(p, encoding="utf-8").read()
        mevcut = HREFLANG_SATIR.findall(html)
        if mevcut:
            ilk = HREFLANG_SATIR.search(html).start()
            girinti = re.match(r"[ \t]*", html[ilk:]).group(0)
            temiz = HREFLANG_SATIR.sub("", html)
            yeni_girintili = "".join(girinti + s + "\n" for s in yeni.strip().split("\n"))
            html_yeni = temiz[:ilk] + yeni_girintili + temiz[ilk:]
        else:
            # hreflang hiç yok · canonical'ın hemen ardına koy
            m = re.search(r'[ \t]*<link rel="canonical"[^>]*>\n', html)
            if not m:
                continue
            girinti = re.match(r"[ \t]*", m.group(0)).group(0)
            yeni_girintili = "".join(girinti + s + "\n" for s in yeni.strip().split("\n"))
            html_yeni = html[:m.end()] + yeni_girintili + html[m.end():]
        if html_yeni != html and not dry:
            open(p, "w", encoding="utf-8").write(html_yeni)
        if html_yeni != html:
            degisen += 1
    
    print(f"{'[--dry] ' if dry else ''}✓ hreflang · {degisen} sayfa güncellendi "
          f"({kapsam} çok dilli sayfa · {atlanan} yol tanınmadı)")


if __name__ == "__main__":
    normalize(dry=DRY)
