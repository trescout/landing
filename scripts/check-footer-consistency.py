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
# İki dil, iki kanonik set · /en/ altındaki sayfalar İngilizce footer taşır.
EXPECTED_TR = ('Nasıl Çalışır', 'Keşif', 'Sözlük', 'Raporlar', 'Karşılaştır', 'Erken Erişim')
EXPECTED_EN = ('How It Works', 'Discover', 'Dictionary', 'Reports Archive', 'Compare', 'Early Access')

def beklenen(rel_path):
    return EXPECTED_EN if rel_path.startswith('en/') else EXPECTED_TR

def urun_links(p):
    t = open(p, encoding='utf-8').read()
    if 'class="footer-grid"' not in t:
        return None  # tam footer'ı olmayan sayfa (ör. privacy) atlanır
    m = re.search(r'footer-col-title">(?:Ürün|Product)</div>\s*<ul>(.*?)</ul>', t, re.S)
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
    rel = os.path.relpath(p, ROOT)
    if links != beklenen(rel):
        bad.append((rel, links))

if bad:
    print(f"❌ Footer tutarsız ({len(bad)}/{n} sayfa · TR: {' · '.join(EXPECTED_TR)} | EN: {' · '.join(EXPECTED_EN)}):")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Footer tutarlı: {n} sayfa (TR + EN kanonik setlerine uygun)")
