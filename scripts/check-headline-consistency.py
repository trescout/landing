#!/usr/bin/env python3
"""
Başlık tutarlılık guard'ı (CI) · katalogdaki `headline` ile detay sayfasının H1'i aynı olmalı.

Neden gerekti: 2026-08-06 denetiminde 30 keşif sayfasının H1'i katalogdan geride
kalmıştı. Katkı PR'ları bayat dal yüzünden alan bazlı taşınıyor (bkz. landing#64) ·
taşıma kataloğu düzeltiyor ama sayfayı yeniden basmıyordu. Sonuç: yayında hâlâ
"Web Sunucunuzu yapay zekâyla Hızlandırın" (nginx) yazıyordu, katalogda düzeltilmişti.

Nav / footer / logo guard'larının kardeşi: statik, hızlı, ağ yok.
Kullanım: python3 scripts/check-headline-consistency.py
"""
import os, re, sys, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")
DISC = os.path.join(ROOT, "discover")
H1 = re.compile(r'<h1 class="disc-title">(.*?)</h1>', re.S)


def main():
    cat = json.load(open(CATALOG, encoding="utf-8"))
    sapan, sayfasiz = [], []
    for c in cat:
        beklenen = (c.get("headline") or "").strip()
        if not beklenen:
            continue
        p = os.path.join(DISC, c["slug"], "index.html")
        if not os.path.exists(p):
            sayfasiz.append(c["slug"])
            continue
        m = H1.search(open(p, encoding="utf-8").read())
        # H1 kaçışlı yazılır (' → &#x27;) · karşılaştırmadan önce çöz
        if m and html.unescape(m.group(1)).strip() != beklenen:
            sapan.append((c["slug"], html.unescape(m.group(1)).strip(), beklenen))

    if sayfasiz:
        print(f"✗ {len(sayfasiz)} katalog kaydının detay sayfası yok: {', '.join(sayfasiz[:6])}")
    if sapan:
        print(f"✗ {len(sapan)} sayfanın H1'i katalogla uyuşmuyor:")
        for slug, bulunan, beklenen in sapan[:10]:
            print(f"   {slug}\n     sayfa   : {bulunan}\n     katalog : {beklenen}")
        if len(sapan) > 10:
            print(f"   … +{len(sapan)-10} sayfa daha")
        print("   Düzeltme: katalog doğruysa sayfaları yeniden bas (discover-sync `_set_page_headline`).")
    if sapan or sayfasiz:
        sys.exit(1)
    print(f"✓ başlık tutarlı · {len(cat)} kayıt")


main()
