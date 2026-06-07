#!/usr/bin/env python3
"""
Logo geometri tutarlılık guard'ı (CI).
Sayfalardaki TreScout marka işaretinin (3 radar yayı + T) ŞEKLİ her yerde aynı olmalı.
Boyut (width/height/class), aria, renk/opaklık ve çerçeve (bg rect) bağlama göre meşru
değişebilir → bunları YOK SAYAR. Sadece çekirdek geometriye bakar: yay path'leri (d) +
T'nin crossbar/stem rect koordinatları. Böylece "404'te T-sapı height=36 vs 28" gibi
gerçek sapmayı yakalar, meşru boyut farkını yakalamaz (nav 32px, 404 hero büyük vb).
Kullanım: python3 scripts/check-logo-consistency.py
"""
import os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIG = 'M 20 56 A 30 30 0 0 1 80 56'  # dış radar yayı = marka imzası
CANON = (
    'M 20 56 A 30 30 0 0 1 80 56',
    'M 30 56 A 20 20 0 0 1 70 56',
    'M 40 56 A 10 10 0 0 1 60 56',
    'r 20 56 60 11',     # T crossbar
    'r 44.5 56 11 28',   # T stem
)

def core(svg):
    paths = [d.strip() for d in re.findall(r'd="([^"]+)"', svg)]
    rects = []
    for r in re.findall(r'<rect\b[^>]*>', svg):
        def g(k):
            m = re.search(k + r'="([^"]+)"', r); return m.group(1) if m else '?'
        x, y, w, h = g('x'), g('y'), g('width'), g('height')
        if (x, y, w, h) == ('0', '0', '100', '100'):
            continue  # bg çerçeve (framed/frameless farkı) → yok say
        rects.append(f'r {x} {y} {w} {h}')
    return tuple(sorted(paths + rects))

bad, n = [], 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    t = open(p, encoding='utf-8').read()
    for svg in re.findall(r'<svg[^>]*viewBox="0 0 100 100".*?</svg>', t, re.S):
        if SIG not in svg:
            continue  # marka işareti değil → atla
        n += 1
        if core(svg) != tuple(sorted(CANON)):
            bad.append((os.path.relpath(p, ROOT), core(svg)))
            break

if bad:
    print(f"❌ Logo geometrisi sapmış ({len(bad)} sayfa · beklenen şekil: 3 yay + crossbar 60x11 + stem 11x28):")
    for f, g in bad[:20]:
        print(f"   {f}: {g}")
    sys.exit(1)
print(f"✅ Logo geometrisi tutarlı: {n} marka işareti")
