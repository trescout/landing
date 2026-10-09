#!/usr/bin/env python3
"""
Logo geometri tutarlılık guard'ı (CI) · logo v2 (TS işareti, brand-kit logos/v2).
Gezinme çubuğu ve alt bilgideki işaret (kalın sürüm: ufuk çizgisi + S yolu) her sayfada
aynı geometride olmalı. Boyut (width/height) ve renk bağlama göre değişebilir: renk
currentColor ile CSS'ten gelir (site.css · .logo-link svg). Bu yüzden yalnız çekirdek
geometriye bakar: ufuk rect'i + S path'i + çizgi kalınlığı.

Ayrıca eski v1 logosu (kare çerçeve + T + radar yayları) hiçbir sayfada kalmamalı:
v2 geçişinden sonra bir üretici eski kodu yeniden basarsa burada yakalanır. Önceki
guard yalnız v1 imzasını arıyordu; v1 kalmayınca "0 işaret, tutarlı" deyip sessizce
geçecekti, o yüzden işaret sayısı da denetleniyor.
Kullanım: python3 scripts/check-logo-consistency.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1_IMZA = "M 20 56 A 30 30 0 0 1 80 56"  # v1 dış radar yayı
S_YOLU = "M 50 29 C 50 41, 35 40, 35 51 C 35 62, 65 60, 65 71 C 65 77, 58 81, 50 81"  # v2 kalın S
UFUK_YAYI = "M 22.50 27.54 A 77.5 77.5 0 0 1 77.50 27.54"  # T'nin üst çizgisi, halkalarla aynı merkezden kıvrık (2026-10-09)
CANON = (f'd="{UFUK_YAYI}"', f'd="{S_YOLU}"', 'stroke-width="13"', 'stroke-linecap="round"')
DUZ_UFUK = 'rect x="16" y="16" width="68" height="13" rx="6.5"'  # kıvrımdan önceki düz çizgi
CHROME = re.compile(r'class="(?:logo-link|footer-logo)"')


def main():
    bad, eski, chrome_sayfa, isaret_yok, n = [], [], 0, [], 0
    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
        if "/node_modules/" in p:
            continue
        rel = os.path.relpath(p, ROOT)
        t = open(p, encoding="utf-8").read()
        if V1_IMZA in t or DUZ_UFUK in t:
            eski.append(rel)
        svgs = [s for s in re.findall(r"<svg\b.*?</svg>", t, re.S) if S_YOLU in s]
        for svg in svgs:
            n += 1
            eksik = [c for c in CANON if c not in svg]
            if eksik:
                bad.append((rel, eksik))
        if CHROME.search(t):
            chrome_sayfa += 1
            if not svgs:
                isaret_yok.append(rel)

    hata = False
    if eski:
        hata = True
        print(f"❌ Eski logo {len(eski)} sayfada kalmış (v1 kare çerçeve ya da düz ufuk çizgili v2):")
        for f in eski[:20]:
            print(f"   {f}")
    if bad:
        hata = True
        print(f"❌ Logo v2 geometrisi sapmış ({len(bad)} işaret):")
        for f, eksik in bad[:20]:
            print(f"   {f}: eksik {eksik}")
    if isaret_yok:
        hata = True
        print(f"❌ Gezinme/alt bilgi logosu olan {len(isaret_yok)} sayfada v2 işareti yok:")
        for f in isaret_yok[:20]:
            print(f"   {f}")
    if hata:
        sys.exit(1)
    print(f"✅ Logo v2 tutarlı: {n} işaret, {chrome_sayfa} sayfa, eski logo yok")


if __name__ == "__main__":
    main()
