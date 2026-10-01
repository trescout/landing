"""Üretilen çeviri sayfası mevcut sayfayı ZAYIFLATMASIN.

2026-09-27 · hat 19 Eylül'den beri ilk kez push etti ve dictionary-en.py 40
çeviri sözlük sayfasını ezdi. 25 Eylül'de elle/ajanla zenginleştirilmiş sayfalar
(etimoloji, teknik derinlik, sık hatalar...) üreticinin tanımadığı bölümler
taşıyordu; üretici onları hiç çevirmedi, çevrilecek metin kalmadığı için "çeviri
eksik" koruması da devreye girmedi ve en/dictionary/llm, rag, transformer gibi
sayfalar 7 bölümden 1'e düştü.

Kural: diskte bir sayfa varsa, yeni çıktı ondan daha az bölüm (<h2>) taşıyorsa ya
da ana metni %40'tan fazla kısalıyorsa yazılmaz, mevcut hali korunur. Çağıran
loglar. Bedeli: elle zenginleştirilmiş çeviri sayfaları üreticiden güncelleme
almaz, elle bakılır.
"""
import os
import re

_KABUK = re.compile(r"<(nav|footer|script|svg)[\s\S]*?</\1>")
_BASLIK = re.compile(r"<h2[^>]*>")
ASGARI_METIN_ORANI = 0.6


def _olcu(html):
    govde = _KABUK.sub("", html)
    ana = (govde.split("<main", 1) + [""])[1].split("</main>")[0] or govde
    kelime = len(re.sub(r"<[^>]+>", " ", ana).split())
    return len(_BASLIK.findall(govde)), kelime


def zayiflatir(yeni_html, mevcut_yol, kaynak_yol=None):
    """Yeni çıktı mevcut sayfayı zayıflatıyorsa gerekçe döner, yoksa None.

    kaynak_yol: Türkçe kaynak sayfa. Yeni çıktı kaynağın bölüm sayısına
    ulaşıyorsa küçülme meşrudur (kaynak yeniden işlenip kısalmış), engellenmez.
    2026-09-28: archify yeniden işlendi, Türkçesi 7 → 6 bölüm oldu; koruma
    6 bölümlük çevirileri engelledi, eski 7 bölümlük sayfalar kaldı ve bölüm
    paritesi guard'ı "fazla bölüm" diye düştü.
    """
    if not os.path.exists(mevcut_yol):
        return None
    try:
        eski = open(mevcut_yol, encoding="utf-8").read()
    except OSError:
        return None
    eski_bolum, eski_kelime = _olcu(eski)
    yeni_bolum, yeni_kelime = _olcu(yeni_html)
    # Kaynağın bölüm sayısına ulaşan çıktı için YALNIZ bölüm kuralı esner;
    # metin kuralı her zaman geçerli (elle zenginleştirilmiş, Türkçesinden uzun
    # çeviri sayfası daha kısa bir makine çevirisiyle ezilmesin).
    kaynak_yeterli = False
    if kaynak_yol and os.path.exists(kaynak_yol):
        try:
            kaynak_bolum, _ = _olcu(open(kaynak_yol, encoding="utf-8").read())
            kaynak_yeterli = yeni_bolum >= kaynak_bolum
        except OSError:
            pass
    if yeni_bolum < eski_bolum and not kaynak_yeterli:
        return f"bölüm {eski_bolum}→{yeni_bolum}"
    if eski_kelime and yeni_kelime < eski_kelime * ASGARI_METIN_ORANI:
        return f"metin {eski_kelime}→{yeni_kelime} kelime"
    return None
