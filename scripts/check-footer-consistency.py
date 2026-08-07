#!/usr/bin/env python3
"""
Footer tutarlılık guard'ı (CI) · nav guard'ının footer ikizi.
footer-grid içeren TÜM sayfalar aynı "Ürün" linklerini içermeli. Footer farklı
üreticilere (index.html · dict-sync · discover-sync · publish-report) dağıldığı
için sayfa tipine göre kaymasın → "footer sayfadan sayfaya farklı" bug'ı bir daha
kaçmaz. CSP / nav guard'ı gibi statik + hızlı.
Kullanım: python3 scripts/check-footer-consistency.py

2026-08-07 · iki değişiklik:
  1. Beklenen setler `scripts/diller.py`den türetiliyor (nav guard'ıyla aynı).
  2. Sütun başlığı deseni de oradan geliyordu · önce yalnız "Ürün|Product"
     aranıyordu, Fransızca başlık "Produit" olduğu için 200'den fazla sayfa
     guard'dan SESSİZCE geçiyordu. Guard'ın en kötü hali budur: yeşil yanar ama
     bakmaz. Yeni dil eklerken artık ek adım yok.
"""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER, footer_etiketleri

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_TR = ('Nasıl Çalışır', 'Keşif', 'Sözlük', 'Raporlar', 'Karşılaştır', 'Erken Erişim')

# footer "Ürün" sütunu · bölüm adları + erken erişim bağlantısı (chrome() sırası)
SETLER = {f"{kod}/": footer_etiketleri(d) for kod, d in DILLER.items()}
# Sütun başlığı her dilde farklı · deseni tablodan kur.
BASLIKLAR = ['Ürün'] + [d["footer_urun"] for d in DILLER.values()]
BASLIK_DESEN = re.compile(
    r'footer-col-title">(?:' + '|'.join(re.escape(b) for b in BASLIKLAR) + r')</div>\s*<ul>(.*?)</ul>',
    re.S)


def beklenen(rel_path):
    for onek, s in SETLER.items():
        if rel_path.startswith(onek):
            return s
    return EXPECTED_TR


def urun_links(p):
    t = open(p, encoding='utf-8').read()
    if 'class="footer-grid"' not in t:
        return None  # tam footer'ı olmayan sayfa (ör. privacy) atlanır
    m = BASLIK_DESEN.search(t)
    if not m:
        # Footer var ama "Ürün" sütunu tanınmadı · yeni bir dil başlığı olabilir.
        # Sessizce atlamak yerine hata sayıyoruz, guard kör kalmasın.
        return ('<ürün sütunu tanınmadı>',)
    return tuple(x.strip() for x in re.findall(r'>([^<]+)</a>', m.group(1)) if x.strip())


bad, n = [], 0
sayac = {}
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    links = urun_links(p)
    if links is None:
        continue
    n += 1
    rel = os.path.relpath(p, ROOT)
    dil_kodu = next((k for k in SETLER if rel.startswith(k)), 'tr/')
    sayac[dil_kodu] = sayac.get(dil_kodu, 0) + 1
    if links != beklenen(rel):
        bad.append((rel, links))

if bad:
    print(f"❌ Footer tutarsız ({len(bad)}/{n} sayfa):")
    for onek, s in [('tr/', EXPECTED_TR)] + sorted(SETLER.items()):
        print(f"   beklenen {onek.rstrip('/')}: {' · '.join(s)}")
    for f, l in bad[:40]:
        print(f"   {f}: {l}")
    sys.exit(1)
print(f"✅ Footer tutarlı: {n} sayfa · " + " · ".join(f"{k.rstrip('/')}:{v}" for k, v in sorted(sayac.items())))
