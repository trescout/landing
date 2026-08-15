#!/usr/bin/env python3
"""
Elle bakılan sayfaların dil paritesi guard'ı (CI)
=================================================
Keşif ve sözlük sayfaları Türkçesinden ÜRETİLİYOR · biri değişince hepsi
değişiyor, geride kalamıyorlar. Ana sayfa ve karşılaştırma sayfası ise elle
yazılıyor: Türkçesine bir bölüm eklendiğinde İngilizcesi ve Fransızcası sessizce
geride kalıyor ve kimse fark etmiyor.

Bu guard o boşluğu kapatıyor: aynı sayfanın üç dildeki sürümü **aynı yapıyı**
taşımalı. Metin elbette farklı · yapı değil.

Bakılanlar:
  1. <section id="..."> kümesi · bölüm eklenip diğer dillere eklenmemiş mi
  2. <h2> sayısı · bir dilde başlık eklenmiş, diğerinde eklenmemiş mi
  3. kayıt formu sayısı · CTA bir dilde düşmüş mü
  4. SSS (<details>) sayısı · soru eklenmiş, diğer dile geçmemiş mi

Neden yapı, neden metin değil: metin karşılaştırması çeviride her zaman
"farklı" der, guard gürültüye boğulur ve kapatılır. Yapı ise çevrildiğinde
aynı kalmalı · sapma gerçek bir eksik demektir.

Yeni elle yazılan çok dilli sayfa eklerken GRUPLAR'a bir satır ekleyin.

Kullanım: python3 scripts/check-sayfa-paritesi.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Aynı sayfanın dillerdeki karşılıkları · GRUPLAR elle yazılıyordu, her yeni
# dilde iki satıra birden dil eklemek gerekiyordu. Artık diller.py'den türüyor ·
# yeni elle yazılan SAYFA türü eklerken KALIPLAR'a bir satır ekleyin, yeni DİL
# eklerken buraya hiç dokunmayın.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402

KALIPLAR = [
    ("ana sayfa", "index.html"),
    ("karşılaştırma", "compare/rss-vs-ai/index.html"),
]

GRUPLAR = [
    (ad, {"tr": kalip, **{kod: f"{kod}/{kalip}" for kod in DILLER}})
    for ad, kalip in KALIPLAR
]


def imza(yol):
    """Sayfanın yapısal imzası · dile bağlı olmayan ölçüler."""
    html = open(yol, encoding="utf-8").read()
    # Kabuk (nav/footer) dışarıda · onların kendi guard'ı var
    govde = html
    for etiket in ("nav", "footer"):
        govde = re.sub(rf"<{etiket}[\s>][\s\S]*?</{etiket}>", "", govde)
    return {
        "bölümler": tuple(sorted(set(re.findall(r'<section[^>]*id="([^"]+)"', govde)))),
        "h2": len(re.findall(r"<h2[\s>]", govde)),
        "kayıt formu": len(re.findall(r'class="[^"]*js-subscribe', govde)),
        "SSS": len(re.findall(r"<details[\s>]", govde)),
    }


sorunlar = []
for ad, yollar in GRUPLAR:
    imzalar = {}
    for dil, yol in yollar.items():
        tam = os.path.join(ROOT, yol)
        if not os.path.exists(tam):
            sorunlar.append(f"{ad} · {dil} sürümü yok: {yol}")
            continue
        imzalar[dil] = imza(tam)
    if "tr" not in imzalar:
        continue
    kaynak = imzalar["tr"]
    for dil, im in imzalar.items():
        if dil == "tr":
            continue
        for alan, deger in kaynak.items():
            if im[alan] != deger:
                sorunlar.append(
                    f"{ad} · {dil}: {alan} = {im[alan]!r} · Türkçesinde {deger!r}"
                )

if sorunlar:
    print(f"❌ Sayfa paritesi bozuk ({len(sorunlar)} sapma):")
    for s in sorunlar:
        print(f"   {s}")
    print("\n   Türkçe sayfayı değiştirdiyseniz aynı değişikliği diğer dillere de yapın.")
    print("   Bölüm eklemek/çıkarmak üç dilde birden yapılır · biri geride kalırsa burası kırılır.")
    sys.exit(1)

print(f"✓ Sayfa paritesi tutarlı · {len(GRUPLAR)} sayfa grubu × "
      f"{len(GRUPLAR[0][1])} dil (bölüm · h2 · form · SSS)")
