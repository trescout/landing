#!/usr/bin/env python3
"""
Üretilen sayfaların bölüm paritesi guard'ı (CI)
===============================================
Keşif ve sözlük sayfaları Türkçesinden ÜRETİLİYOR · her dilde AYNI SAYIDA
bölüm (<h2>) olmalı. Metin farklı, yapı değil.

Neden gerekli · 2026-08-15'te bulunan hata: Türkçe sayfa güncelleme bloğunu
`<section class="disc-sec"><h2>Güncelleme</h2>` olarak basıyor. discover-en.py
iki yerden birden kuruyordu:
  · guncelleme_en()  → KATALOGDAN, doğru etiket ("Updates") ve sayı biçimi
  · bolumler()       → Türkçe sayfadan kazıyıp makineye çevirerek ("Update")
Sonuç: çevrilmiş 370 sayfada aynı bölüm İKİ KEZ, üstelik iki farklı yazımla ·
beş dilde 1850 sayfa. Türkçesine bakan görmüyor, çünkü orada tek.

Guard bunu yakalar: bir dilde bölüm sayısı Türkçesinden FARKLIYSA ya bir şey
iki kez basılıyor ya da bir bölüm düşmüş. İkisi de hata.

check-sayfa-paritesi.py ELLE yazılan sayfalara bakıyor · bu onun üretilen
sayfalardaki ikizi.

Kullanım: python3 scripts/check-bolum-paritesi.py
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KABUK = re.compile(r"<(nav|footer|script|svg)[\s\S]*?</\1>")
BASLIK = re.compile(r"<h2[^>]*>")


def bolum_sayisi(yol):
    return len(BASLIK.findall(KABUK.sub("", open(yol, encoding="utf-8").read())))


sorunlar = []
denetlenen = 0
for bolum in ("discover", "dictionary"):
    for tr_yol in sorted(glob.glob(os.path.join(ROOT, bolum, "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(tr_yol))
        beklenen = bolum_sayisi(tr_yol)
        for kod in DILLER:
            yol = os.path.join(ROOT, kod, bolum, slug, "index.html")
            if not os.path.exists(yol):
                continue          # eksik sayfa başka guard'ın işi
            denetlenen += 1
            var = bolum_sayisi(yol)
            if var != beklenen:
                sorunlar.append(f"{kod}/{bolum}/{slug}: {var} bölüm · Türkçesinde {beklenen}")

if sorunlar:
    print(f"❌ Bölüm paritesi bozuk ({len(sorunlar)}/{denetlenen} sayfa):")
    for s in sorunlar[:25]:
        print(f"   {s}")
    if len(sorunlar) > 25:
        print(f"   … {len(sorunlar) - 25} sayfa daha")
    print("\n   Fazla bölüm = bir şey İKİ KEZ basılıyor (Türkçe sayfadan kazınan bölüm,")
    print("   üretici tarafından da kuruluyor olabilir · bolumler() atlama listesine bakın).")
    print("   Eksik bölüm = çeviride bir bölüm düşmüş.")
    sys.exit(1)

print(f"✓ Bölüm paritesi tutarlı · {denetlenen} üretilmiş sayfa, "
      f"her biri Türkçesiyle aynı sayıda bölüm taşıyor")
