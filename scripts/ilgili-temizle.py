#!/usr/bin/env python3
"""
"İlgili terim/araç" çiplerinden var olmayan sayfaya gidenleri kaldırır.

Üreticiler çipi yalnız var olan sayfaya koyuyor, ama yeniden üretilmeyen eski
sayfalar (elle/ajanla zenginleştirilmiş, sayfa_koruma'nın koruduğu çeviriler)
o gün var olmayan ya da sonradan kalkan terimlere bağlı kalıyordu: 2026-09-27'de
101 sayfada 141 çip 404'e gidiyordu (ör. /pt/dictionary/attention-mechanism/).

Yalnız dict-related / disc-related kutularındaki çiplere dokunur; düz metindeki
bağlantılar olduğu gibi kalır. Kutu boşalırsa bölüm (<section>) de kalkar.
Terim sonradan oluşturulursa çip, sayfa yeniden üretildiğinde geri gelir.

Kullanım: python3 scripts/ilgili-temizle.py [--dry]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DRY = "--dry" in sys.argv

KUTU = re.compile(r'(<div class="(?:dict|disc)-related">)(.*?)(</div>)', re.S)
CIP = re.compile(r'<a href="(/(?:[a-z]{2}/)?(?:dictionary|discover)/[^"/#?]+/)"[^>]*>.*?</a>', re.S)
BOS_BOLUM = re.compile(r'<section class="disc-sec"><h2>[^<]*</h2><div class="(?:dict|disc)-related"></div></section>\n?[ \t]*')


def var(url):
    return os.path.exists(os.path.join(url.strip("/"), "index.html"))


def temizle(html):
    sayac = [0]

    def kutu(m):
        def cip(c):
            if var(c.group(1)):
                return c.group(0)
            sayac[0] += 1
            return ""
        return m.group(1) + CIP.sub(cip, m.group(2)) + m.group(3)

    yeni = KUTU.sub(kutu, html)
    return BOS_BOLUM.sub("", yeni), sayac[0]


toplam_cip = toplam_sayfa = 0
for p in sorted(glob.glob("**/*.html", recursive=True)):
    if "node_modules" in p:
        continue
    t = open(p, encoding="utf-8").read()
    if "-related\">" not in t:
        continue
    yeni, n = temizle(t)
    if n:
        toplam_cip += n
        toplam_sayfa += 1
        if not DRY:
            open(p, "w", encoding="utf-8").write(yeni)
print(f"{'(dry) ' if DRY else ''}ilgili çip temizliği: {toplam_sayfa} sayfada {toplam_cip} ölü çip kaldırıldı")
