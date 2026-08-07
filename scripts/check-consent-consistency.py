#!/usr/bin/env python3
"""
Aydınlatma / rıza guard'ı (CI)
==============================
Kayıt formu olan HER sayfada, o sayfanın DİLİNDEKİ aydınlatma metnine bağlantı
ve zorunlu onay kutusu olmalı.

Neden var: 2026-08-06'da İngilizce sözlük sayfasından bir kayıt alındı. O
sayfadaki onay cümlesi aydınlatma metnine hiç atıf yapmıyordu ve İngilizce
aydınlatma metni de yoktu · KVKK m.10 aydınlatmanın verinin ALINDIĞI anda
yapılmasını istiyor, sonradan gönderilen e-posta o anı geri getirmiyor. Kişiden
yeniden rıza istemek zorunda kaldık. Aynı boşluk üçüncü dilde (fr) tekrarlamasın
diye kontrol otomatikleşti.

Kontrol edilenler · her `form.js-subscribe` için:
  1. zorunlu onay kutusu (input[name=consent] required)
  2. onay metninde aydınlatma metnine bağlantı
  3. bağlantı SAYFANIN DİLİNDEKİ metne gidiyor (diller.py · gizlilik_yolu)
  4. bağlantının hedefi diskte var
  5. honeypot alanı (bot koruması) duruyor

Ayrıca SAYFANIN TAMAMINDA: aydınlatma metnine giden her bağlantı o sayfanın
dilindeki metne gitmeli. Bu ikinci kontrol, `build-reports-en.js`in 128 İngilizce
rapor sayfasının footer'ında Türkçe metne bağlanması yüzünden eklendi
(2026-08-07) · form doğruyken footer yanlış olabiliyor.

Kullanım: python3 scripts/check-consent-consistency.py
"""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Türkçe kaynak dil · tablosu diller.py'de yok, yolu burada.
GIZLILIK = {"tr": "/privacy.html"}
GIZLILIK.update({kod: d["gizlilik_yolu"] for kod, d in DILLER.items()})

FORM_DESEN = re.compile(r'<form[^>]*class="[^"]*js-subscribe[^"]*"[\s\S]*?</form>')


def sayfa_dili(html, rel):
    m = re.search(r'<html[^>]*\blang="([a-zA-Z-]+)"', html)
    return (m.group(1) if m else "tr").lower()


sorunlar, form_sayisi, sayfa_sayisi = [], 0, 0
for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
    if "/node_modules/" in p:
        continue
    html = open(p, encoding="utf-8").read()
    rel = os.path.relpath(p, ROOT)
    formlar = FORM_DESEN.findall(html)
    # Aydınlatma metinlerinin KENDİSİ kural dışı · İngilizce ve Fransızca
    # metinler bilerek Türkçe asla bağlanıyor ("bağlayıcı olan Türkçe metindir").
    metnin_kendisi = os.path.basename(rel) == "privacy.html"
    if not formlar and metnin_kendisi:
        continue
    if formlar:
        sayfa_sayisi += 1
    dil_kodu = sayfa_dili(html, rel)
    beklenen = GIZLILIK.get(dil_kodu)
    if beklenen is None:
        sorunlar.append((rel, f"sayfa dili {dil_kodu!r} · diller.py'de tanımlı değil"))
        continue
    for f in formlar:
        form_sayisi += 1
        kaynak = (re.search(r'data-source="([^"]*)"', f) or [None, "?"])[1]
        etiket = f"{rel} [{kaynak}]"
        if not re.search(r'<input[^>]*name="consent"[^>]*required', f):
            sorunlar.append((etiket, "zorunlu onay kutusu yok"))
        baglantilar = re.findall(r'<a[^>]*href="([^"]+)"', f)
        gizlilik = [b for b in baglantilar if "privacy" in b]
        if not gizlilik:
            sorunlar.append((etiket, "onay metninde aydınlatma metni bağlantısı yok"))
        elif gizlilik[0] != beklenen:
            sorunlar.append((etiket, f"aydınlatma bağlantısı {gizlilik[0]} · {dil_kodu} için {beklenen} olmalı"))
        elif not os.path.exists(os.path.join(ROOT, beklenen.lstrip("/"))):
            sorunlar.append((etiket, f"{beklenen} diskte yok"))
        if 'name="website"' not in f:
            sorunlar.append((etiket, "honeypot alanı yok (bot koruması)"))

    # Sayfadaki TÜM aydınlatma bağlantıları · footer dahil, form olmasa da
    if not metnin_kendisi:
        for hedef in set(re.findall(r'href="(/[a-z/]*privacy\.html)"', html)):
            if hedef != beklenen:
                sorunlar.append((rel, f"sayfada {hedef} bağlantısı · {dil_kodu} için {beklenen} olmalı"))

if sorunlar:
    print(f"❌ Aydınlatma/rıza guard'ı: {len(sorunlar)} sorun ({form_sayisi} form · {sayfa_sayisi} sayfa)")
    for ad, ne in sorunlar[:40]:
        print(f"   {ad}: {ne}")
    if len(sorunlar) > 40:
        print(f"   … {len(sorunlar) - 40} sorun daha")
    sys.exit(1)
print(f"✓ Aydınlatma/rıza tutarlı · {form_sayisi} kayıt formu · {sayfa_sayisi} sayfa "
      f"({' · '.join(f'{k}:{v}' for k, v in sorted(GIZLILIK.items()))})")
