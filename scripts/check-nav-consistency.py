#!/usr/bin/env python3
"""
Nav tutarlılık guard'ı (CI)
===========================
nav-actions içeren TÜM sayfalar aynı linkleri içermeli. "Shared component"
(nav) sayfa tipine göre kaymasın → kullanıcının bildirdiği 'link kayboluyor'
bug'ı bir daha kaçmaz. CSP guard gibi statik + hızlı.
Kullanım: python3 scripts/check-nav-consistency.py

2026-08-07 · beklenen setler artık ELLE yazılmıyor, `scripts/diller.py`den
türetiliyor. Önceki halinde her yeni dil için buraya set eklemek gerekiyordu ·
unutulursa guard o dili ya %100 hatalı sayıyor ya (footer ikizinde olduğu gibi)
sessizce atlıyordu. Türkçe kaynak dil olduğu için tek elle yazılan set o.
"""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER, nav_etiketleri

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_TR = ('Keşif', 'Sözlük', 'Raporlar', 'Karşılaştır', 'EN', 'FR')

# Üretilen diller · nav = bölüm adları + "TR" düğmesi + erken erişim CTA'sı.
# chrome() bu sırayla basıyor (diller.py), guard aynı sırayı bekliyor.
SETLER = {f"{kod}/": nav_etiketleri(d) for kod, d in DILLER.items()}


def beklenen(rel_path):
    for onek, s in SETLER.items():
        if rel_path.startswith(onek):
            return s
    return EXPECTED_TR


def nav_links(p):
    t = open(p, encoding='utf-8').read()
    m = re.search(r'<div class="nav-actions">(.*?)</div>', t, re.S)
    if not m:
        return None
    return tuple(x.strip() for x in re.findall(r'>([^<]+)</a>', m.group(1)) if x.strip())


bad, n = [], 0
sayac = {}
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    links = nav_links(p)
    if links is None:
        continue
    n += 1
    rel = os.path.relpath(p, ROOT)
    dil_kodu = next((k for k in SETLER if rel.startswith(k)), 'tr/')
    sayac[dil_kodu] = sayac.get(dil_kodu, 0) + 1
    if links != beklenen(rel):
        bad.append((rel, links))

if bad:
    print(f"❌ Nav tutarsız ({len(bad)}/{n} sayfa):")
    for onek, s in [('tr/', EXPECTED_TR)] + sorted(SETLER.items()):
        print(f"   beklenen {onek.rstrip('/')}: {' · '.join(s)}")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Nav tutarlı: {n} sayfa · " + " · ".join(f"{k.rstrip('/')}:{v}" for k, v in sorted(sayac.items())))
