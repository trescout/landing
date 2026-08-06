#!/usr/bin/env python3
"""
Nav tutarlılık guard'ı (CI)
===========================
nav-actions içeren TÜM sayfalar aynı linkleri içermeli. "Shared component"
(nav) sayfa tipine göre kaymasın → kullanıcının bildirdiği 'link kayboluyor'
bug'ı bir daha kaçmaz. CSP guard gibi statik + hızlı.
Kullanım: python3 scripts/check-nav-consistency.py
"""
import os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# İki dil, iki kanonik set · /en/ altındaki sayfalar İngilizce nav taşır.
# Bir dilin seti değişince BURASI da güncellenmeli, yoksa guard %100 hata verir
# ve gerçek sapmayı gizler (2026-08-05'te tam bunu yaşadık).
EXPECTED_TR = ('Keşif', 'Sözlük', 'Raporlar', 'Karşılaştır', 'EN')
EXPECTED_EN = ('Discover', 'Dictionary', 'Reports Archive', 'Compare', 'TR')

def beklenen(rel_path):
    return EXPECTED_EN if rel_path.startswith('en/') else EXPECTED_TR

def nav_links(p):
    t = open(p, encoding='utf-8').read()
    m = re.search(r'<div class="nav-actions">(.*?)</div>', t, re.S)
    if not m:
        return None
    return tuple(x.strip() for x in re.findall(r'>([^<]+)</a>', m.group(1)) if x.strip())

bad, n = [], 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    links = nav_links(p)
    if links is None:
        continue
    n += 1
    rel = os.path.relpath(p, ROOT)
    if links != beklenen(rel):
        bad.append((rel, links))

if bad:
    print(f"❌ Nav tutarsız ({len(bad)}/{n} sayfa · TR: {' · '.join(EXPECTED_TR)} | EN: {' · '.join(EXPECTED_EN)}):")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Nav tutarlı: {n} sayfa (TR + EN kanonik setlerine uygun)")
