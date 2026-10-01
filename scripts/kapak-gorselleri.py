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
    raise SystemExit("Kullanım: kapak-gorselleri.py --lang=fr|tr [--yenile]")
# tr: Türkçe kapak (assets/discover/og/<slug>.webp · alan "tagline"). Eskiden
# yalnız discover-sync kayıt AÇILIRKEN basıyordu; tanıtım metni sonradan
# değişince kapak eski kalıyordu.
TAGLINE_ALAN = "tagline" if LANG == "tr" else dil(LANG)["tagline_alan"]
# Kapak hangi metinle basıldı · metin değişince kapak yeniden basılır.
# 2026-10-01: 11 Türkçe kapakta Portekizce/eski açıklama ya da "özet
# üretilemedi" yer tutucusu kalmıştı (ponytail, archify, nitter…); katalog
# metni düzelmiş, kapak 25 Ağustos'tan kalmıştı.
METIN_DOSYASI = os.path.join(OG_DIR, "kapak-metinleri.json")
try:
    kapak_metni = json.load(open(METIN_DOSYASI, encoding="utf-8"))
except (OSError, ValueError):
    kapak_metni = {}

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
    dosya = f"{c['slug']}.webp" if LANG == "tr" else f"{c['slug']}-{LANG}.webp"
    out = os.path.join(OG_DIR, dosya)
    if os.path.exists(out) and not YENILE and kapak_metni.get(dosya, tagline) == tagline:
        varolan += 1
        kapak_metni.setdefault(dosya, tagline)
        continue
    lang_etiketi = (c.get("meta") or "").split("·")[-1].strip() if "·" in (c.get("meta") or "") else ""
    if ds.make_card(c["slug"], c["title"], tagline, c.get("stars") or 0,
                    lang_etiketi, out, dil=LANG):
        basildi += 1
        kapak_metni[dosya] = tagline
    else:
        atlandi += 1

json.dump(kapak_metni, open(METIN_DOSYASI, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
print(f"✓ {LANG} kapak görselleri · {basildi} basıldı · {varolan} zaten vardı · "
      f"{atlandi} atlandı (çeviri yok)")
