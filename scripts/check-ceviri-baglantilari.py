#!/usr/bin/env python3
"""Çeviri keşif/sözlük sayfalarında kaynak bağlantıları Türkçe sayfayla tutarlı mı.

discover-en.py çeviri sayfasını Türkçe sayfayı KAZIYARAK kuruyor; Türkçe yapı biraz
değişince sessizce bozuluyor ve mevcut guard'lar (bölüm sayısı) bunu yakalamıyordu.
2026-10-15'te iki hata bulundu, ikisi de 15 Ağustos'tan beri canlıydı:

1. "Nasıl başlanır" bölümündeki kaynak bağlantısı madde listesi sanıldı: paragraf
   düştü, bağlantı düz metne döndü ("<li>Official source →</li>", 139 araç × 5 dil).
2. Depo adresi sayfadaki ilk bağlantıdan alındı: bazen eski depo ya da web sitesiydi
   (699 sayfada codeRepository ve "GitHub repository" bağlantısı yanlış).

Denetim: (a) disc-links içinde bağlantısız madde yok, (b) çeviri keşif sayfasının
codeRepository'si Türkçe sayfanınkiyle aynı.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from diller import DILLER  # noqa: E402

LISTE = re.compile(r'<ul class="disc-links">(.*?)</ul>', re.S)
MADDE = re.compile(r"<li>(.*?)</li>", re.S)
DEPO = re.compile(r'"codeRepository":\s*"([^"]+)"')


def main() -> int:
    hatalar: list[str] = []
    sayfa = 0
    tr_depo = {}
    for p in (ROOT / "discover").glob("*/index.html"):
        m = DEPO.search(p.read_text(encoding="utf-8"))
        if m:
            tr_depo[p.parent.name] = m.group(1)
    for dil in ["tr", *DILLER]:
        kok = ROOT if dil == "tr" else ROOT / dil
        for tur in ("discover", "dictionary"):
            for p in sorted((kok / tur).glob("*/index.html")):
                html = p.read_text(encoding="utf-8")
                sayfa += 1
                rel = p.relative_to(ROOT).parent
                for liste in LISTE.findall(html):
                    for madde in MADDE.findall(liste):
                        if "<a " not in madde:
                            hatalar.append(f"{rel}: bağlantısız madde {re.sub(r'<[^>]+>', '', madde).strip()!r}")
                if dil != "tr" and tur == "discover":
                    m = DEPO.search(html)
                    beklenen = tr_depo.get(p.parent.name)
                    if m and beklenen and m.group(1) != beklenen:
                        hatalar.append(f"{rel}: codeRepository {m.group(1)} · Türkçede {beklenen}")
    if hatalar:
        print(f"✗ Çeviri bağlantıları tutarsız: {len(hatalar)} sorun")
        for h in hatalar[:15]:
            print("  " + h)
        if len(hatalar) > 15:
            print(f"  … ve {len(hatalar) - 15} sorun daha")
        print("  Düzeltme: scripts/discover-en.py --lang=XX --slug=SLUG (üretici), korunan sayfada elle")
        return 1
    print(f"✓ Çeviri bağlantıları tutarlı: {sayfa} sayfa")
    return 0


if __name__ == "__main__":
    sys.exit(main())
