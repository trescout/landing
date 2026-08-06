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
    sapan, sayfasiz, komutsuz = [], [], []
    for c in cat:
        beklenen = (c.get("headline") or "").strip()
        p = os.path.join(DISC, c["slug"], "index.html")
        if not os.path.exists(p):
            if beklenen:
                sayfasiz.append(c["slug"])
            continue
        sayfa = open(p, encoding="utf-8").read()
        # Katalogda doğrulanmış kurulum komutu var ama sayfada komut bloğu yok →
        # kayıt güncellenmiş, sayfa yeniden basılmamış. 2026-08-06: Mustafa'nın
        # 10 araca eklediği komutlar haftalardır yayında görünmüyordu.
        cm = c.get("cmds") or {}
        if (cm.get("kurulum") or cm.get("calistirma")) and "disc-cmd" not in sayfa:
            komutsuz.append(c["slug"])
        if not beklenen:
            continue
        m = H1.search(sayfa)
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
    if komutsuz:
        print(f"✗ {len(komutsuz)} kayıtta katalogda komut var ama sayfada komut bloğu yok:")
        print(f"   {', '.join(komutsuz[:10])}")
        print("   Düzeltme: discover-sync --reprocess=<slug,...> ile sayfaları yeniden basın.")
    if sapan or sayfasiz or komutsuz:
        sys.exit(1)
    print(f"✓ katalog ↔ sayfa tutarlı · {len(cat)} kayıt (başlık + komut)")


main()
