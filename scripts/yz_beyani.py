#!/usr/bin/env python3
"""Keşif ve sözlük sayfalarında yapay zekâ beyanı (TR + 5 dil).

Raporlar 2026-10-09'dan beri "özetler ve çeviriler yapay zekâ ile hazırlanmaktadır"
diyor (check-ai-disclosure.py). Keşif tanıtımları (README'den Gemini ile) ve sözlük
açıklamaları (Gemini ile) da yapay zekâ ile hazırlanıyor ama sayfa notları bunu
söylemiyordu: TR keşif "yazdığımız metin", TR sözlük "sade dille hazırlandı",
çeviriler yalnız "makine çevirisi" diyordu (2026-10-16 denetimi).

Not metni sayfanın `disc-disclaimer` paragrafında; bu paragraf üretici damgasının
dışında (sayfa_koruma.py _KALIP), toplu değişiklik sayfaları "elle düzenlenmiş"
göstermez. Yeni sayfalar beyanla doğar (discover-sync.py, dict-sync.py, diller.py);
mevcut sayfaları içerik hattı bu betikle günceller.

<div class="dict-disclaimer"> damganın İÇİNDE kalıyor: --uygula, değiştirdiği çeviri
sayfasının damgası değişiklikten önce tutuyorsa damgayı yeniler (yoksa sayfa "elle
düzenlenmiş" görünür ve üretici bırakır; bkz. landing toplu düzenleme notu).

Kullanım:
  python3 scripts/yz_beyani.py             # sıkı: her keşif/sözlük sayfası beyanı taşımalı
  python3 scripts/yz_beyani.py --gecis     # CI: her sayfa beyanlı ya da --uygula ile beyanlanabilir
  python3 scripts/yz_beyani.py --uygula    # eski notları yeni beyanlı notla değiştirir
"""
import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sayfa_koruma import damgalar, damga_yaz, damga_yolu, icerik_damgasi  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DILLER = ("en", "fr", "pt", "es", "de")
# Not paragrafı; eski zengin sözlük çevirilerinde <div class="dict-disclaimer"> (55 sayfa)
NOT = re.compile(r'<(p|div) class="(?:disc|dict)-disclaimer">.*?</\1>', re.S)

# (eski parça, yeni parça) · yeni parça beyanın kendisi
TR = {
    "discover": ("keşfedip Türkçe tanıttı. ",
                 "keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. "),
    "dictionary": ("Bu açıklama TreScout için sade dille hazırlandı",
                   "Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı"),
}
# Diller · keşif: diller.py "ceviri_notu_kisa" eski hâli → güncel hâli (tam metin).
# Sözlük: notun "… for TreScout" kısmına beyan eklenir; sözlük notunun eski
# varyantları da (<div class="dict-disclaimer">, <strong>'suz hâl) böylece kapsanır.
KESIF_ESKI = {
    "en": "This page was <strong>machine-translated</strong> from the Turkish original · the Turkish version prevails.",
    "fr": "Cette page a été <strong>traduite automatiquement</strong> depuis l’original turc · la version turque fait foi.",
    "pt": "Esta página foi <strong>traduzida automaticamente</strong> do original em turco · a versão turca é a que vale.",
    "es": "Esta página se <strong>tradujo automáticamente</strong> del original en turco · prevalece la versión turca.",
    "de": "Diese Seite wurde <strong>maschinell übersetzt</strong> aus dem türkischen Original · maßgeblich ist die türkische Fassung.",
}
SOZLUK = {
    "en": ("for TreScout", "for TreScout with AI"),
    "fr": ("pour TreScout", "pour TreScout avec l’IA"),
    "pt": ("para a TreScout", "para a TreScout com IA"),
    "es": ("para TreScout", "para TreScout con IA"),
    "de": ("für TreScout", "für TreScout mit KI"),
}


def kurallar():
    """{(dil, tür): (eski, yeni)} · dil "" = Türkçe."""
    k = {("", tur): ciftler for tur, ciftler in TR.items()}
    for dil in DILLER:
        D = json.loads(subprocess.run([sys.executable, os.path.join(ROOT, "scripts/diller.py"), "--json", dil],
                                      capture_output=True, text=True, check=True).stdout)
        k[(dil, "discover")] = (KESIF_ESKI[dil], D["ceviri_notu_kisa"])
        k[(dil, "dictionary")] = SOZLUK[dil]
        # Üreticinin yeni sözlük notu beyanı aynı ifadeyle taşımalı (diller.py ile bu tablo ayrışmasın)
        assert SOZLUK[dil][1] in D["ceviri_notu"], f"{dil}: diller.py ceviri_notu beyan ifadesini taşımıyor"
    return k


def main():
    uygula = "--uygula" in sys.argv
    gecis = "--gecis" in sys.argv
    sayac = {"beyanli": 0, "degisti": 0, "beyansiz": []}
    for (dil, tur), (eski, yeni) in kurallar().items():
        onek = f"{dil}/" if dil else ""
        damga = damgalar(damga_yolu(tur, dil)) if dil else {}
        damga_degisti = False
        for yol in sorted(glob.glob(os.path.join(ROOT, onek + tur, "*", "index.html"))):
            h = open(yol, encoding="utf-8").read()
            notlar = [m.group(0) for m in NOT.finditer(h)]
            if any(yeni in n for n in notlar):
                sayac["beyanli"] += 1
                continue
            hedef = next((n for n in notlar if eski in n), None)
            if hedef and uygula:
                slug = os.path.basename(os.path.dirname(yol))
                tutuyordu = dil and damga.get(slug) == icerik_damgasi(h)
                h = h.replace(hedef, hedef.replace(eski, yeni, 1), 1)
                open(yol, "w", encoding="utf-8").write(h)
                if tutuyordu and damga[slug] != icerik_damgasi(h):
                    damga[slug] = icerik_damgasi(h)
                    damga_degisti = True
                sayac["degisti"] += 1
            elif hedef and gecis:
                sayac["beyanli"] += 1
            else:
                sayac["beyansiz"].append(os.path.relpath(yol, ROOT))
        if damga_degisti:
            damga_yaz(damga_yolu(tur, dil), damga)
    if uygula:
        print(f"→ YZ beyanı: {sayac['degisti']} sayfa güncellendi, {sayac['beyanli']} zaten beyanlı")
    if sayac["beyansiz"]:
        print(f"❌ YZ beyanı (keşif/sözlük): {len(sayac['beyansiz'])} sayfanın notu beyanı taşımıyor ve otomatik eklenemiyor")
        for yol in sayac["beyansiz"][:30]:
            print(f"   {yol}")
        sys.exit(1)
    if not uygula:
        print(f"✓ YZ beyanı (keşif/sözlük) · {sayac['beyanli']} sayfa{' (geçiş: eski not --uygula ile beyanlanır)' if gecis else ''}")


if __name__ == "__main__":
    main()
