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
          <svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>
          <span>TreScout</span>
        </div>
        <p class="footer-tagline">TreScout tarar, özetler, gönderir. Siz sadece okursunuz.</p>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Ürün</div>
        <ul>
          <li><a href="/#how-it-works">Nasıl Çalışır</a></li>
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
