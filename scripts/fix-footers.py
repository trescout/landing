#!/usr/bin/env python3
"""
Tek seferlik footer hizalama (migration).
footer-grid içeren TÜM sayfaların <footer>'ını kanonik footer ile değiştirir.
Üreticiler (dict-sync / discover-sync / publish-report) bundan sonra zaten kanonik
üretir; bu script geçmişte üretilmiş sayfaları da hizalar.
check-footer-consistency.py guard'ı tekrar kaymasını engeller.
Kullanım: python3 scripts/fix-footers.py
"""
import os, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FOOTER = """<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand-block">
        <div class="footer-logo">
          <svg width="30" height="30" viewBox="12 14 76 76" aria-hidden="true"><path d="M 22.50 27.54 A 77.5 77.5 0 0 1 77.50 27.54" fill="none" stroke="currentColor" stroke-width="13" stroke-linecap="round"/><path d="M 50 29 C 50 41, 35 40, 35 51 C 35 62, 65 60, 65 71 C 65 77, 58 81, 50 81" fill="none" stroke="currentColor" stroke-width="13" stroke-linecap="round"/></svg>
        </div>
        <p class="footer-tagline">TreScout tarar, özetler, yayımlar. Siz sadece okursunuz.</p>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Ürün</div>
        <ul>
          <li><a href="/how-it-works/">Nasıl Çalışır</a></li>
          <li><a href="/discover/">Keşif</a></li>
          <li><a href="/dictionary/">Sözlük</a></li>
          <li><a href="/reports/">Raporlar</a></li>
          <li><a href="/#top">Erken Erişim</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">İletişim</div>
        <ul>
          <li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li>
          <li><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Sosyal medya</div>
        <ul>
          <li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 TreScout · Tüm hakları saklıdır.</span>
    </div>
  </div>
</footer>"""

n = 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/node_modules/' in p:
        continue
    t = open(p, encoding='utf-8').read()
    if 'class="footer-grid"' not in t:
        continue  # bare footer'lı sayfalara (privacy vb.) dokunma
    new = re.sub(r'<footer[^>]*>.*?</footer>', lambda m: FOOTER, t, count=1, flags=re.S)
    if new != t:
        open(p, 'w', encoding='utf-8').write(new)
        n += 1
print("hizalanan sayfa:", n)
