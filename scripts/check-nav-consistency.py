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
EXPECTED = ('Keşif', 'Sözlük', 'Raporlar', 'Erken erişim')

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
    if links != EXPECTED:
        bad.append((os.path.relpath(p, ROOT), links))

if bad:
    print(f"❌ Nav tutarsız ({len(bad)}/{n} sayfa · beklenen: {' · '.join(EXPECTED)}):")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Nav tutarlı: {n} sayfanın hepsinde {' · '.join(EXPECTED)}")
