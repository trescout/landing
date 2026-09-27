#!/usr/bin/env python3
"""
Üretilen sayfaların bölüm paritesi guard'ı (CI)
===============================================
Keşif ve sözlük sayfaları Türkçesinden ÜRETİLİYOR · her dilde AYNI SAYIDA
bölüm (<h2>) olmalı. Metin farklı, yapı değil.

Neden gerekli · 2026-08-15'te bulunan hata: Türkçe sayfa güncelleme bloğunu
`<section class="disc-sec"><h2>Güncelleme</h2>` olarak basıyor. discover-en.py
iki yerden birden kuruyordu:
  · guncelleme_en()  → KATALOGDAN, doğru etiket ("Updates") ve sayı biçimi
  · bolumler()       → Türkçe sayfadan kazıyıp makineye çevirerek ("Update")
Sonuç: çevrilmiş 370 sayfada aynı bölüm İKİ KEZ, üstelik iki farklı yazımla ·
beş dilde 1850 sayfa. Türkçesine bakan görmüyor, çünkü orada tek.

Guard bunu yakalar: bir dilde bölüm sayısı Türkçesinden FARKLIYSA ya bir şey
iki kez basılıyor ya da bir bölüm düşmüş. İkisi de hata.

check-sayfa-paritesi.py ELLE yazılan sayfalara bakıyor · bu onun üretilen
sayfalardaki ikizi.

2026-09-27 · FAZLA ve EKSİK ayrıldı. Çevirisi yapılamayan sayfa artık yazılmıyor
(dictionary-en.py / discover-en.py, PR #241); Türkçe sayfaya yeni bölüm gelince
(ör. cross-link "İlgili araçlar") çevirisi bir sonraki başarılı koşuya kadar eski
kalıyor. O gün main'de 519 sayfa "eksik" çıktı ve her PR'ın guard'ı kırmızı oldu.
  FAZLA bölüm        → hata (bu guard'ın yakaladığı asıl hata: iki kez basılan bölüm)
  2+ bölüm EKSİK     → hata (sayfa boşalmış: aynı gece 40 çeviri sayfası 7 bölümden
                       1'e düştü · bkz. sayfa_koruma.py)
  1 bölüm EKSİK      → uyarı (tipik çeviri gecikmesi: Türkçeye yeni bölüm geldi,
                       çevirisi sonraki başarılı koşuda gelecek; sayı ve örnek yazılır)
Bedeli: bir üretici tek bir bölümü düşürürse kırmızı değil uyarı olarak görünür.

Kullanım: python3 scripts/check-bolum-paritesi.py
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KABUK = re.compile(r"<(nav|footer|script|svg)[\s\S]*?</\1>")
BASLIK = re.compile(r"<h2[^>]*>")


def bolum_sayisi(yol):
    return len(BASLIK.findall(KABUK.sub("", open(yol, encoding="utf-8").read())))


sorunlar = []          # fazla bölüm · hata
eksikler = []          # eksik bölüm · uyarı (çeviri gecikmesi)
denetlenen = 0
for bolum in ("discover", "dictionary"):
    for tr_yol in sorted(glob.glob(os.path.join(ROOT, bolum, "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(tr_yol))
        beklenen = bolum_sayisi(tr_yol)
        for kod in DILLER:
            yol = os.path.join(ROOT, kod, bolum, slug, "index.html")
            if not os.path.exists(yol):
                continue          # eksik sayfa başka guard'ın işi
            denetlenen += 1
            var = bolum_sayisi(yol)
            if var > beklenen or beklenen - var >= 2:
                sorunlar.append(f"{kod}/{bolum}/{slug}: {var} bölüm · Türkçesinde {beklenen}")
            elif var < beklenen:
                eksikler.append(f"{kod}/{bolum}/{slug}: {var} bölüm · Türkçesinde {beklenen}")

if eksikler:
    print(f"⚠ {len(eksikler)} çeviri sayfası Türkçesinden az bölüm taşıyor · büyük olasılıkla "
          f"çeviri gecikmesi (sonraki başarılı koşuda kapanır). Örnek:")
    for s in eksikler[:5]:
        print(f"   {s}")

if sorunlar:
    print(f"❌ Bölüm paritesi bozuk ({len(sorunlar)}/{denetlenen} sayfa):")
    for s in sorunlar[:25]:
        print(f"   {s}")
    if len(sorunlar) > 25:
        print(f"   … {len(sorunlar) - 25} sayfa daha")
    print("\n   Fazla bölüm = bir şey İKİ KEZ basılıyor (Türkçe sayfadan kazınan bölüm,")
    print("   üretici tarafından da kuruluyor olabilir) · 2+ eksik = sayfa boşalmış.")
    print("   Ayrıntı:")
    print("   üretici tarafından da kuruluyor olabilir · bolumler() atlama listesine bakın).")
    sys.exit(1)

print(f"✓ Bölüm paritesi · {denetlenen} üretilmiş sayfada fazla ya da 2+ eksik bölüm yok"
      + (f" ({len(eksikler)} sayfa 1 bölüm gecikmede)" if eksikler else ", hepsi Türkçesiyle aynı"))
