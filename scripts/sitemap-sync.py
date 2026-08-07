#!/usr/bin/env python3
"""
TreScout · sitemap senkronu
===========================
Diskteki her sayfayı sitemap'e alır, silinmiş sayfaların girdisini çıkarır.

Neden gerekti: Sitemap'i güncelleyen tek bir süreç yoktu. Türkçe sözlük URL'lerini
dict-sync ekliyordu, İngilizce tarafı ise tek seferlik bir betik doldurmuştu ve
o günden sonra güncellenmedi. 2026-08-06 denetiminde 154 sayfa (İngilizce
raporlar, tekrarsız arşiv, yeni sözlük ve keşif sayfaları) sitemap dışındaydı.

Mevcut girdilerin lastmod'una DOKUNMAZ · yalnız eksikleri ekler, ölüleri siler.
Böylece her çalıştırmada tüm arşivin tarihi tazelenmiş gibi görünmez.

Kullanım: python3 scripts/sitemap-sync.py [--dry]
"""
import os, re, sys, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
BASE = "https://trescout.com"
TODAY = os.environ.get("DICT_DATE") or datetime.date.today().isoformat()
DRY = "--dry" in sys.argv

# Yayına girmeyen sayfalar · 404 ve gizlilik metni sitemap'te olmasın diye ayrı tutulur
ATLA = {"/404/", "/en/404/"}


def oncelik(url):
    """changefreq + priority · mevcut sitemap konvansiyonuyla aynı."""
    if url == "/":
        return "weekly", "1.0"
    if url == "/en/":
        return "weekly", "0.9"
    if url in ("/discover/", "/dictionary/", "/reports/", "/reports/tekrarsiz/",
               "/en/discover/", "/en/dictionary/", "/en/reports/", "/en/reports/fresh/"):
        return "weekly", "0.8"
    if url.startswith("/reports/") or url.startswith("/en/reports/"):
        return "monthly", "0.7"
    if url.endswith("privacy.html"):
        return "monthly", "0.3"
    return "monthly", "0.6"


def disk_urls():
    out = set()
    for p in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(os.path.dirname(p), ROOT).replace(os.sep, "/")
        url = "/" if rel == "." else f"/{rel}/"
        if url in ATLA:
            continue
        out.add(url)
    for ek in ("privacy.html", "en/privacy.html"):
        if os.path.exists(os.path.join(ROOT, ek)):
            out.add("/" + ek)
    return out


def main():
    sm = open(SITEMAP, encoding="utf-8").read()
    bloklar = re.findall(r"  <url>.*?</url>\n", sm, re.S)
    mevcut = {}
    for b in bloklar:
        m = re.search(r"<loc>" + re.escape(BASE) + r"([^<]*)</loc>", b)
        if m:
            mevcut[m.group(1)] = b

    hedef = disk_urls()
    eksik = sorted(hedef - set(mevcut))
    olu = sorted(set(mevcut) - hedef)

    for u in eksik:
        cf, pr = oncelik(u)
        mevcut[u] = (f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
                     f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n")
    for u in olu:
        mevcut.pop(u, None)

    print(f"sitemap · disk {len(hedef)} sayfa · eklenen {len(eksik)} · silinen {len(olu)}")
    if eksik:
        print("  eklenen örnek:", eksik[:4])
    if olu:
        print("  silinen örnek:", olu[:4])
    if DRY:
        print("[--dry] yazılmadı.")
        return
    if not eksik and not olu:
        return

    def sirala(u):
        return (u.count("/"), u)

    govde = "".join(mevcut[u] for u in sorted(mevcut, key=sirala))
    yeni = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + govde + "</urlset>\n")
    open(SITEMAP, "w", encoding="utf-8").write(yeni)
    print("✅ sitemap.xml güncellendi")


main()
