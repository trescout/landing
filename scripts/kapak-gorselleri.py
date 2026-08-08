#!/usr/bin/env python3
"""
Keşif kapak görsellerini hedef dilde üretir.

    python3 scripts/kapak-gorselleri.py --lang=fr
    python3 scripts/kapak-gorselleri.py --lang=en --yenile   # var olanları da yeniden bas

Neden gerekli: Kapak kartındaki metin GÖRSELE gömülü (Pillow ile çiziliyor).
2026-08-08'e kadar proje başına tek dosya vardı ve İngilizce ile Fransızca
sayfalarda da Türkçe üst etiket ("KEŞİF · GİTHUB"), Türkçe tanıtım cümlesi ve
Türkçe sayı biçimi (35.132) görünüyordu. Sosyal paylaşımda çıkan OG görseli de
buydu. Artık her dil kendi dosyasını kullanıyor:

    assets/discover/og/<slug>.webp        Türkçe (kaynak · discover-sync.py basar)
    assets/discover/og/<slug>-en.webp     İngilizce
    assets/discover/og/<slug>-fr.webp     Fransızca

Tanıtım cümlesi katalogdaki `tagline_<dil>` alanından geliyor · o alan yoksa
(yeni kayıt, çeviri henüz geçmemiş) görsel ÜRETİLMEZ, sayfa Türkçe kapağa düşer.
Bu bilinçli: yarım çeviriyle görsel basmaktansa kaynak görseli göstermek daha
dürüst, ertesi gün çeviri gelince görsel de gelir.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import dil  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OG_DIR = os.path.join(ROOT, "assets", "discover", "og")
CATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")

LANG = next((a.split("=")[1] for a in sys.argv if a.startswith("--lang=")), None)
YENILE = "--yenile" in sys.argv
if not LANG:
    raise SystemExit("Kullanım: kapak-gorselleri.py --lang=fr [--yenile]")
D = dil(LANG)
TAGLINE_ALAN = D["tagline_alan"]

# make_card discover-sync.py içinde · betiğin yan etkisi olmadan al
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "discover_sync", os.path.join(ROOT, "scripts", "discover-sync.py"))
ds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ds)   # main() yalnız __main__'de çalışıyor

cat = json.load(open(CATALOG, encoding="utf-8"))
basildi = atlandi = varolan = 0
for c in cat:
    tagline = (c.get(TAGLINE_ALAN) or "").strip()
    if not tagline:
        atlandi += 1
        continue
    out = os.path.join(OG_DIR, f"{c['slug']}-{LANG}.webp")
    if os.path.exists(out) and not YENILE:
        varolan += 1
        continue
    lang_etiketi = (c.get("meta") or "").split("·")[-1].strip() if "·" in (c.get("meta") or "") else ""
    if ds.make_card(c["slug"], c["title"], tagline, c.get("stars") or 0,
                    lang_etiketi, out, dil=LANG):
        basildi += 1
    else:
        atlandi += 1

print(f"✓ {LANG} kapak görselleri · {basildi} basıldı · {varolan} zaten vardı · "
      f"{atlandi} atlandı (çeviri yok)")
