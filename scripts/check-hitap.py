#!/usr/bin/env python3
"""Çeviri önbelleklerinde okura hitap tutarlı mı (es/fr/de/pt).

Türkçe kaynak okura "siz" diye hitap ediyor; çeviriler de resmî hitap kullanır
(es "usted", fr "vous", de "Sie", pt "você"). 2026-10-16 ölçümü: İspanyolca sözlük
sayfalarının 215/720'si, keşif sayfalarının 127/628'i "tú" kullanıyordu, bazı
sayfalarda iki hitap bir aradaydı. Kural translation_service.py'de (HITAP,
hitap_ihlali); bu guard önbelleğe yeniden samimi çeviri girmesini yakalar.

Ajan istemleri (keşif sayfasındaki "Kod bilmiyorsanız" metni, okurun yapay zekâ
asistanına yazdığı mesaj) samimi olabilir; denetimin dışında.

Kullanım:
  python3 scripts/check-hitap.py             # önbellek denetimi (ihlal varsa çıkış 1) + sayfa sayımı
  python3 scripts/check-hitap.py --rapor     # CI: kuralın öz sınaması kırar, önbellek/sayfa bilgi
  python3 scripts/check-hitap.py --temizle   # içerik hattı: ihlalli önbellek kayıtlarını siler,
                                             # sayfalar aynı koşuda yeniden çevrilir

Temizlik içerik hattında (dict-sync.yml) Actions önbelleği birleştirildikten SONRA
koşar; yoksa eski önbellek silinen kayıtları geri getirirdi.
"""
import glob
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from translation_service import hitap_ihlali, _SAMIMI  # noqa: E402

DILLER = ("es", "fr", "de", "pt")
TURLER = ("discover", "dictionary")
AJAN = re.compile(r'<p class="disc-ai-text">(.*?)</p>', re.S)


def oz_sinama():
    """Kuralın kendisi: bilinen doğru/yanlış örnekler."""
    vakalar = [
        ("Kendi bulutunuz kurulur.", "Se configura tu propia nube.", "es", True),
        ("Kendi bulutunuz kurulur.", "Se configura su propia nube.", "es", False),
        ("Varlığından haberdar olmadığınız bir bilgisayar.", "Una computadora que ni siquiera sabes que existe.", "es", True),
        ("Bu araç dosyaları yedekler.", "Esta herramienta hace copias de seguridad.", "es", False),
        ("Kurulumu tamamlamama yardım et.", "Ayúdame a completar la instalación, ¿puedes?", "es", False),
        ("Size uygun ayarı seçin.", "Choisissez le réglage qui te convient.", "fr", True),
        ("Size uygun ayarı seçin.", "Choisissez le réglage qui vous convient.", "fr", False),
        ("Ayarlarınızı kaydedin.", "Speichere deine Einstellungen.", "de", True),
        ("Ayarlarınızı kaydedin.", "Speichern Sie Ihre Einstellungen.", "de", False),
        ("Doğal bir ton yakalarsınız.", "Vous obtenez un ton naturel.", "fr", False),
    ]
    hatalar = [v for v in vakalar if hitap_ihlali(v[0], v[1], v[2]) != v[3]]
    for kaynak, ceviri, dil, beklenen in hatalar:
        print(f"✗ öz sınama: {dil} '{ceviri}' → ihlal {not beklenen}, beklenen {beklenen}")
    return not hatalar


def ajan_istemleri():
    istemler = []
    for yol in glob.glob(os.path.join(ROOT, "discover", "*", "index.html")):
        m = AJAN.search(open(yol, encoding="utf-8").read())
        if m:
            istemler.append(html.unescape(m.group(1)).strip())
    return istemler


def ajan_mi(kaynak, istemler):
    k = kaynak.strip()
    return bool(k) and any(k in istem for istem in istemler)


def sayfa_sayimi():
    """Bilgi: ajan istemi dışında samimi hitap geçen çeviri sayfası (önbellek temizlenip
    sayfalar yeniden üretildikçe düşer; elle korunan sayfalar üretilmez)."""
    for dil in DILLER:
        rx = _SAMIMI[dil]
        for tur in TURLER:
            yollar = glob.glob(os.path.join(ROOT, dil, tur, "*", "index.html"))
            sayi = 0
            for yol in yollar:
                s = AJAN.sub(" ", open(yol, encoding="utf-8").read())
                s = re.sub(r'<p class="disc-ai-ek">.*?</p>', " ", s, flags=re.S)  # ajan istemi sabit satırları
                s = re.sub(r"<script.*?</script>|<style.*?</style>|<(nav|footer)[\s\S]*?</\1>", " ", s, flags=re.S)
                if rx.search(html.unescape(re.sub(r"<[^>]+>", " ", s))):
                    sayi += 1
            if yollar:
                print(f"  · {dil}/{tur}: {len(yollar)} sayfanın {sayi}'inde samimi hitap (bilgi)")


def main():
    temizle = "--temizle" in sys.argv
    rapor = "--rapor" in sys.argv
    if not oz_sinama():
        sys.exit(1)
    istemler = ajan_istemleri()
    toplam = 0
    for dil in DILLER:
        for tur in TURLER:
            yol = os.path.join(ROOT, "assets", tur, f"{dil}-cache.json")
            if not os.path.exists(yol):
                continue
            onbellek = json.load(open(yol, encoding="utf-8"))
            ihlal = [k for k, v in onbellek.items()
                     if isinstance(v, str) and hitap_ihlali(k, v, dil) and not ajan_mi(k, istemler)]
            if not ihlal:
                continue
            toplam += len(ihlal)
            print(f"{'·' if temizle or rapor else '✗'} {dil}/{tur}: {len(ihlal)} önbellek kaydı resmî kaynağı samimi hitapla çevirmiş"
                  + (" · silindi" if temizle else ""))
            for k in ihlal[:3]:
                print(f"    TR: {k[:90]}\n    {dil.upper()}: {onbellek[k][:90]}")
            if temizle:
                for k in ihlal:
                    del onbellek[k]
                json.dump(onbellek, open(yol, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    sayfa_sayimi()
    if toplam and not temizle:
        print("  Düzeltmek için: python3 scripts/check-hitap.py --temizle (içerik hattı her koşuda bunu yapar)")
        sys.exit(0 if rapor else 1)
    print(f"✓ Hitap denetimi: {'temizlendi, ' + str(toplam) + ' kayıt yeniden çevrilecek' if temizle and toplam else 'önbelleklerde resmî kaynağa samimi çeviri yok'}")


if __name__ == "__main__":
    main()
