#!/usr/bin/env python3
"""
Marka tipografi guard'ı (CI) · yayına giden sayfalarda iki kesin kural:

  1. 🚀 YASAK · hype işareti (AGENTS.md marka bölümü).
  2. Em dash (—) YASAK · Türkçede yok, yerine · , . : kullanılır.

Neden gerekti: 2026-08-06 denetiminde 🚀 **361 keşif sayfasında** çıktı ·
`discover-sync.py` momentum rozetine basıyordu ve kimse fark etmemişti.
Kural dokümanda vardı, kontrol eden yoktu.

Kod blokları hariç: `<pre>` ve `<code>` içindeki metin üçüncü taraf (README'den
alınan kurulum komutları). Oradaki em dash'i düzeltmek komutu bozar · dokunulmaz.

Kullanım: python3 scripts/check-brand-typography.py
Çıkış kodu 1 → ihlal var (CI fail eder).
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOD = re.compile(r"<pre\b.*?</pre>|<code\b.*?</code>", re.S | re.I)
YASAK = (("🚀", "hype işareti · marka kuralı"), ("—", "em dash · Türkçede yok, · kullanın"))


def main():
    ihlal = []
    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, ROOT)
        # Kod bloklarını boşlukla değiştir · satır numaraları kaymasın
        metin = KOD.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), open(p, encoding="utf-8").read())
        for i, satir in enumerate(metin.splitlines(), 1):
            for isaret, sebep in YASAK:
                if isaret in satir:
                    ihlal.append((rel, i, isaret, sebep, satir.strip()[:70]))

    if ihlal:
        print(f"✗ {len(ihlal)} marka tipografi ihlali:")
        for rel, i, isaret, sebep, ornek in ihlal[:15]:
            print(f"   {rel}:{i} · {isaret} ({sebep})\n     {ornek}")
        if len(ihlal) > 15:
            print(f"   … +{len(ihlal)-15} ihlal daha")
        sys.exit(1)
    print("✓ marka tipografisi temiz · 🚀 ve em dash yok")


main()
