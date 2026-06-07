#!/usr/bin/env python3
"""
Footer tutarlılık guard'ı (CI) · nav guard'ının footer ikizi.
footer-grid içeren TÜM sayfalar aynı "Ürün" linklerini içermeli. Footer farklı
üreticilere (index.html · dict-sync · discover-sync · publish-report) dağıldığı
için sayfa tipine göre kaymasın → "footer sayfadan sayfaya farklı" bug'ı bir daha
kaçmaz. CSP / nav guard'ı gibi statik + hızlı.
Kullanım: python3 scripts/check-footer-consistency.py
"""
import os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED = ('Nasıl Çalışır', 'Keşif', 'Sözlük', 'Raporlar', 'Erken Erişim')

def urun_links(p):
    t = open(p, encoding='utf-8').read()
    if 'class="footer-grid"' not in t:
        return None  # tam footer'ı olmayan sayfa (ör. privacy) atlanır
    m = re.search(r'footer-col-title">Ürün</div>\s*<ul>(.*?)</ul>', t, re.S)
    if not m:
        return None
    return tuple(x.strip() for x in re.findall(r'>([^<]+)</a>', m.group(1)) if x.strip())

bad, n = [], 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    links = urun_links(p)
    if links is None:
        continue
    n += 1
    if links != EXPECTED:
        bad.append((os.path.relpath(p, ROOT), links))

if bad:
    print(f"❌ Footer tutarsız ({len(bad)}/{n} sayfa · beklenen: {' · '.join(EXPECTED)}):")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Footer tutarlı: {n} sayfanın hepsinde {' · '.join(EXPECTED)}")
