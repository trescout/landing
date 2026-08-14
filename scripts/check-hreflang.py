#!/usr/bin/env python3
"""
hreflang guard'ı (CI)
=====================
Çok dilli her sayfa, diğer dillerdeki sürümlerini bildirmeli.

2026-08-13 denetiminde 2035 sayfada `hreflang="fr"`, 914 sayfada `hreflang="en"`
eksikti: bloklar Fransızca yokken yazılmış ve altı ayrı üreticide tekrarlanıyordu.
Google dil sürümlerini kümeleyemiyor, Fransızca sayfalar "aynı içeriğin çevirisi"
yerine ayrı içerik sayılıyordu.

Denetlenenler:
  1. Diskte karşılığı olan HER dil için hreflang satırı var mı
  2. Hiçbir hreflang diskte olmayan bir sayfaya işaret etmiyor
     (kırık vaat · Google'a "şu dilde de var" deyip 404 vermek)
  3. x-default var mı

Düzeltmesi: python3 scripts/hreflang-normalize.py

Kullanım: python3 scripts/check-hreflang.py
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "hreflang_normalize", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       "hreflang-normalize.py"))
_hn = importlib.util.module_from_spec(_spec)
# Normalize edici yalnız __main__'de yazıyor · içe aktarmak güvenli, yan etkisiz
_spec.loader.exec_module(_hn)

ROOT = _hn.ROOT
sorunlar = []
denetlenen = 0

for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
    if "/node_modules/" in p:
        continue
    rel = os.path.relpath(p, ROOT)
    coz = _hn.coz(rel)
    if not coz:
        continue
    dil, bolum, slug = coz
    beklenen = _hn.blok(bolum, slug)
    if not beklenen:
        continue
    denetlenen += 1
    html = open(p, encoding="utf-8").read()
    mevcut = set(re.findall(r'<link rel="alternate" hreflang="([A-Za-z-]+)" href="([^"]+)"', html))
    beklenen_set = set(re.findall(r'hreflang="([A-Za-z-]+)" href="([^"]+)"', beklenen))

    for kod, url in sorted(beklenen_set - mevcut):
        sorunlar.append(f"{rel}: hreflang={kod} eksik → {url}")
    for kod, url in sorted(mevcut - beklenen_set):
        yol = url.replace("https://trescout.com", "").strip("/")
        hedef = yol if yol.endswith(".html") else (os.path.join(yol, "index.html") if yol else "index.html")
        if not os.path.exists(os.path.join(ROOT, hedef)):
            sorunlar.append(f"{rel}: hreflang={kod} diskte olmayan sayfayı gösteriyor → {url}")
        else:
            sorunlar.append(f"{rel}: hreflang={kod} fazladan/yanlış → {url}")

if sorunlar:
    print(f"❌ hreflang guard'ı · {len(sorunlar)} sorun ({denetlenen} çok dilli sayfa):")
    for s in sorunlar[:30]:
        print(f"   {s}")
    if len(sorunlar) > 30:
        print(f"   … {len(sorunlar) - 30} sorun daha")
    print("\n   Düzeltme: python3 scripts/hreflang-normalize.py")
    sys.exit(1)

print(f"✓ hreflang tutarlı · {denetlenen} çok dilli sayfa, her dil karşılığını bildiriyor")
