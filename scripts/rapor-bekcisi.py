#!/usr/bin/env python3
"""
Rapor bekçisi · günün raporunu son iki haftayla karşılaştırır.

Neden: yazılım tarafı izleniyor (deploy-health, Token Bekçisi, rapor iş akışı hata
verirse e-posta), ama raporun İÇERİĞİ izlenmiyordu. Rapor üreten yol (app
scripts/report.ts) çöken kaynağı yalnız uyarıyla geçiyor ve raporu "complete"
kaydediyor; bir bölüm boş ya da özetler bozuk çıksa koşu yeşil kalırdı.
DeepLearning.AI "Machine Learning in Production": neyin bozulabileceğini sayın, her
biri için girdi ve çıktı ölçüsü koyun, eşik aşılınca haber verin (ders listesi M1).

Kontroller (eşik aşılırsa iş başarısız olur, GitHub e-posta gönderir):
  - kaynak bölümü boşaldı: son 3 raporda madde varken bugün yok (kaynak sustu ya da
    bozuldu). Bilerek durdurulan kaynak (ör. Lobsters, 2026-10-08) bir kez uyarır,
    sonra boş kalmaya devam ettiği için susar.
  - toplam madde son 14 günün medyanının yarısından az
  - özetsiz madde 3'ten ve %20'den fazla
  - özet uzunluğu medyanı son 14 günün 0,6 katından kısa ya da 1,6 katından uzun
    (model ya da istem değişti, yanıt kesiliyor)
  - açılış notu yok ya da çok kısa
Uyarılar (iş başarısız olmaz, koşu özetinde):
  - sözlük boş kaldı (sözlük isteğe bağlı)
  - GitHub'da bir günde olağan dışı yıldız artışı (son 14 günün günlük en yükseğinin
    medyanının 4 katından fazla): yıldız şişirme ya da gerçek patlama, insan bakar.

Kullanım:
  python3 scripts/rapor-bekcisi.py [--tarih=2026-10-16]   # varsayılan: en son rapor
  python3 scripts/rapor-bekcisi.py --varlik               # bugünün (TR) raporu var mı
  python3 scripts/rapor-bekcisi.py --oz-test
"""
import datetime
import glob
import json
import os
import re
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAPORLAR = os.path.join(ROOT, "reports")
DESEN = re.compile(r"trescout-rapor-(\d{4}-\d{2}-\d{2})\.json$")
PENCERE = 14


def raporlari_oku(klasor: str) -> dict[str, dict]:
    out = {}
    for yol in glob.glob(os.path.join(klasor, "trescout-rapor-*.json")):
        m = DESEN.search(yol)
        if not m:
            continue
        try:
            j = json.load(open(yol, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(j.get("sections"), list):
            out[m.group(1)] = j
    return out


def olcumler(rapor: dict) -> dict:
    bolumler = {s.get("sourceName"): s.get("items") or [] for s in rapor["sections"]}
    maddeler = [i for v in bolumler.values() for i in v]
    ozetler = [(i.get("summary") or "").strip() for i in maddeler]
    yildiz = [((i.get("snapshot") or {}).get("metadata") or {}).get("extra", {}) or {} for i in bolumler.get("github", [])]
    gunluk = [(e.get("starsToday"), m.get("title")) for e, m in zip(yildiz, bolumler.get("github", [])) if isinstance(e.get("starsToday"), int)]
    editorial = rapor.get("editorial") or ""
    if isinstance(editorial, dict):
        editorial = editorial.get("text") or ""
    return {
        "kaynak": {k: len(v) for k, v in bolumler.items()},
        "madde": len(maddeler),
        "ozetsiz": sum(1 for o in ozetler if not o),
        "ozet_medyan": statistics.median([len(o) for o in ozetler if o]) if any(ozetler) else 0,
        "acilis": len(editorial.strip()),
        "sozluk": len(rapor.get("glossary") or []),
        "yildiz_enfazla": max(gunluk, default=(0, "")),
    }


def denetle(tarih: str, raporlar: dict[str, dict]) -> tuple[list[str], list[str]]:
    """(hatalar, uyarilar) · hata iş akışını kırar, uyarı yalnız özete yazılır."""
    if tarih not in raporlar:
        return [f"{tarih} raporu yok"], []
    bugun = olcumler(raporlar[tarih])
    onceki = [olcumler(raporlar[t]) for t in sorted(t for t in raporlar if t < tarih)[-PENCERE:]]
    hatalar, uyarilar = [], []
    if len(onceki) < 3:
        return hatalar, [f"karşılaştırma için yeterli geçmiş yok ({len(onceki)} rapor)"]

    for kaynak, n in bugun["kaynak"].items():
        if n == 0 and all(o["kaynak"].get(kaynak, 0) > 0 for o in onceki[-3:]):
            hatalar.append(f"{kaynak} bölümü boş (son 3 raporda vardı) · kaynak sustu ya da bozuldu; bilerek durdurulduysa yok sayın")
    medyan = statistics.median(o["madde"] for o in onceki)
    if bugun["madde"] < medyan / 2:
        hatalar.append(f"madde sayısı {bugun['madde']} · son {len(onceki)} raporun medyanı {medyan:g}")
    if bugun["ozetsiz"] > 3 and bugun["ozetsiz"] > 0.2 * bugun["madde"]:
        hatalar.append(f"özetsiz madde {bugun['ozetsiz']}/{bugun['madde']} (özetleyici, düzeltme turu ya da kota)")
    uzunluk = statistics.median(o["ozet_medyan"] for o in onceki if o["ozet_medyan"])
    if bugun["ozet_medyan"] and not 0.6 * uzunluk <= bugun["ozet_medyan"] <= 1.6 * uzunluk:
        hatalar.append(f"özet uzunluğu medyanı {bugun['ozet_medyan']:g} karakter · olağan {uzunluk:g} (model/istem değişti ya da yanıt kesiliyor)")
    if bugun["acilis"] < 80:
        hatalar.append(f"açılış notu {bugun['acilis']} karakter (yok ya da yarım)")

    if bugun["sozluk"] == 0 and statistics.median(o["sozluk"] for o in onceki) > 0:
        uyarilar.append("sözlük boş (sözlük isteği başarısız olmuş olabilir)")
    tepe = statistics.median(o["yildiz_enfazla"][0] for o in onceki)
    sayi, depo = bugun["yildiz_enfazla"]
    if tepe and sayi > 4 * tepe:
        nokta = lambda n: f"{n:,.0f}".replace(",", ".")
        uyarilar.append(f"{depo}: bugün +{nokta(sayi)} yıldız · son {len(onceki)} günün günlük tepesi medyanı {nokta(tepe)} (şişirme mi gerçek mi, bakın)")
    return hatalar, uyarilar


def bugun_tr() -> str:
    return (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)).date().isoformat()


def yaz(baslik: str, hatalar: list[str], uyarilar: list[str]) -> None:
    satirlar = [f"## Rapor bekçisi · {baslik}"]
    satirlar += [f"- ✗ {h}" for h in hatalar] + [f"- ⚠ {u}" for u in uyarilar]
    if not hatalar and not uyarilar:
        satirlar.append("- ✓ olağan")
    metin = "\n".join(satirlar) + "\n"
    print(metin)
    for u in uyarilar:
        print(f"::warning title=Rapor bekçisi::{u}")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(metin)


def oz_test() -> None:
    def rapor(gh=12, hn=5, ozet="x" * 280, ozetsiz=0, acilis="y" * 200, sozluk=16, yildiz=500):
        gh_maddeler = [{"title": f"a/{i}", "summary": ozet, "snapshot": {"metadata": {"extra": {"starsToday": yildiz if i == 0 else 100}}}} for i in range(gh)]
        hn_maddeler = [{"title": f"h{i}", "summary": "" if i < ozetsiz else ozet} for i in range(hn)]
        return {"editorial": acilis, "glossary": [{}] * sozluk,
                "sections": [{"sourceName": "github", "items": gh_maddeler}, {"sourceName": "hackernews", "items": hn_maddeler},
                             {"sourceName": "lobsters", "items": []}]}
    gecmis = {f"2026-10-{g:02d}": rapor() for g in range(1, 15)}
    sorunsuz = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor()})
    assert sorunsuz == ([], []), sorunsuz
    h, _ = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(hn=0)})
    assert any(x.startswith("hackernews bölümü boş") for x in h), h
    assert not any("lobsters" in x for x in h), h  # zaten boş olan kaynak susar
    h, _ = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(gh=3, hn=2)})
    assert any(x.startswith("madde sayısı") for x in h), h
    h, _ = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(hn=5, ozetsiz=5, gh=10)})
    assert any(x.startswith("özetsiz madde 5/15") for x in h), h
    h, _ = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(ozet="z" * 120)})
    assert any(x.startswith("özet uzunluğu") for x in h), h
    h, _ = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(acilis="")})
    assert any(x.startswith("açılış notu") for x in h), h
    h, u = denetle("2026-10-15", {**gecmis, "2026-10-15": rapor(sozluk=0, yildiz=41034)})
    assert h == [] and any("sözlük boş" in x for x in u) and any("a/0: bugün +41.034 yıldız" in x for x in u), (h, u)
    assert denetle("2026-10-16", gecmis)[0] == ["2026-10-16 raporu yok"]
    print("✓ rapor bekçisi öz testi geçti")


def main() -> int:
    if "--oz-test" in sys.argv:
        oz_test()
        return 0
    raporlar = raporlari_oku(RAPORLAR)
    if "--varlik" in sys.argv:
        tarih = bugun_tr()
        hatalar = [] if tarih in raporlar else [f"{tarih} raporu henüz yayınlanmadı (günlük rapor iş akışına bakın)"]
        yaz(f"{tarih} varlık", hatalar, [])
        return 1 if hatalar else 0
    arg = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--tarih=")), "")
    tarih = arg or max(raporlar, default="")
    if not tarih:
        print("rapor bulunamadı", file=sys.stderr)
        return 1
    hatalar, uyarilar = denetle(tarih, raporlar)
    yaz(tarih, hatalar, uyarilar)
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.exit(main())
