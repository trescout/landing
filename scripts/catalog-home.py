#!/usr/bin/env python3
"""
TreScout · ana sayfanın okuduğu hafif katalog türevi.
============================================================

Neden gerekti: ana sayfa keşif radarı ve akış önizlemesi için tam katalogu
(`assets/discover/catalog.json`) indiriyordu · 1,04 MB ham, 240 KB sıkıştırılmış.
Sayfanın kendisi (HTML + CSS + JS) toplam 42 KB, yani veri dosyası sayfanın altı
katıydı. Karşılığında ekrana gelen: radarda 6 kart, akış önizlemesinde 3 kayıt.

Ağırlığın kaynağı ana sayfanın hiç okumadığı alanlar: `guncellemeler` (150 KB),
`localized` (121 KB) ve sayfanın kendi dili dışındaki beş `tagline_XX` (~280 KB).

Bu betik her dil için yalnız o dilin ihtiyacı olan alanları yazar. `tagline`
alanına o dilin metni konur; ana sayfa JS'i zaten
`entry['tagline_' + locale] || entry.tagline` sırasını izlediği için okuma
tarafında ek dal gerekmiyor.

Diller `diller.py`den geliyor · yeni dil eklendiğinde burada iş yok (bkz.
diller.py başlığı, madde 7).

Kullanım:
  python3 scripts/catalog-home.py            # üret
  python3 scripts/catalog-home.py --check    # diskteki dosya güncel mi (guard)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")
HEDEF_DIZIN = os.path.join(ROOT, "assets", "discover")

# Ana sayfa JS'inin (assets/home-interactions.js) gerçekten okuduğu alanlar.
# Yeni bir alan okunacaksa BURAYA da eklenmeli · yoksa kart o alanı boş basar.
ALANLAR = ("slug", "title", "tags", "source", "stars", "date", "last_review")

# Türkçe kaynak dildir · tagline'ı doğrudan `tagline` alanında durur.
DILLER_TUMU = ["tr"] + list(DILLER)


def hedef(dil):
    return os.path.join(HEDEF_DIZIN, f"catalog-home-{dil}.json")


def tagline(kayit, dil):
    if dil == "tr":
        return str(kayit.get("tagline") or "").strip()
    ozel = str(kayit.get(f"tagline_{dil}") or "").strip()
    return ozel or str(kayit.get("tagline") or "").strip()


def ozet(kayitlar, dil):
    cikti = []
    for kayit in kayitlar:
        if not isinstance(kayit, dict):
            continue
        satir = {}
        for alan in ALANLAR:
            deger = kayit.get(alan)
            # Boş alanı hiç yazma · 472 kayıtta kayda değer yer tutuyor.
            if deger not in (None, "", [], {}):
                satir[alan] = deger
        metin = tagline(kayit, dil)
        if metin:
            satir["tagline"] = metin
        if satir.get("slug"):
            cikti.append(satir)
    return cikti


def govde(kayitlar, dil):
    return json.dumps(ozet(kayitlar, dil), ensure_ascii=False, separators=(",", ":")) + "\n"


def main():
    if not os.path.exists(KATALOG):
        print(f"✗ katalog bulunamadı: {KATALOG}")
        return 1
    with open(KATALOG, encoding="utf-8") as f:
        kayitlar = json.load(f)
    if not isinstance(kayitlar, list):
        print("✗ catalog.json bir liste değil")
        return 1

    kontrol = "--check" in sys.argv
    sapan = []
    for dil in DILLER_TUMU:
        yeni = govde(kayitlar, dil)
        yol = hedef(dil)
        if kontrol:
            mevcut = None
            if os.path.exists(yol):
                with open(yol, encoding="utf-8") as f:
                    mevcut = f.read()
            if mevcut != yeni:
                sapan.append(os.path.relpath(yol, ROOT))
            continue
        with open(yol, "w", encoding="utf-8") as f:
            f.write(yeni)
        print(f"  · {os.path.relpath(yol, ROOT)} · {len(kayitlar)} kayıt · {len(yeni.encode('utf-8')) / 1024:.0f} KB")

    if kontrol:
        if sapan:
            print("✗ ana sayfa kataloğu güncel değil: " + ", ".join(sapan))
            print("  düzeltmesi: python3 scripts/catalog-home.py")
            return 1
        print(f"✓ ana sayfa kataloğu {len(DILLER_TUMU)} dilde güncel")
        return 0

    print(f"✓ {len(DILLER_TUMU)} dil yazıldı")
    return 0


if __name__ == "__main__":
    sys.exit(main())
