#!/usr/bin/env python3
"""Search Console dışa aktarımını tek komutla analiz eder (dönemsel yeniden analiz).

Girdi: Search Console → Performans → Dışa aktar → CSV'nin açılmış klasörü
(Sorgular.csv, Sayfa sayısı.csv, Ülkeler.csv, Cihazlar.csv, Grafik.csv, Filtreler.csv).

Çıktı (Markdown):
  1. Özet, dil payı, bölüm payı (keşif/sözlük/rapor/ana sayfa), en çok tıklanan sayfa ve sorgular
  2. --taban ile verilen ölçümle karşılaştırma (ör. landing#338: 22 Türkçe sözlük sayfasının
     arama açıklaması; ~2026-11-05). Sıra düşüp tıklama oranı artmadıysa "geri al" önerir.
  3. Talep: gösterimi yüksek ama karşılığı zayıf sorgular
     a) "X nedir / ne demek / what is X" kalıbında olup sözlükte sayfası OLMAYAN terimler
     b) sözlükte sayfası olan ama ilk sayfada az tıklanan terimler (açıklama adayı)
  Adaylar otomatik eklenmez; karar insanın (DeepLearning.AI AI for Everyone: veri bilimi
  dönemsel yeniden analiz + erdemli veri döngüsü; ders iş listesi H2, H5).

Kullanım:
  python3 scripts/gsc-analiz.py ~/Desktop/trescout-3
  python3 scripts/gsc-analiz.py <klasör> --taban=docs/gsc/taban-2026-10-15-sozluk-aciklama.json --md=rapor.md
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DILLER = ("en", "fr", "pt", "es", "de")
BOLUMLER = (("discover", "keşif"), ("dictionary", "sözlük"), ("reports", "rapor"))
SORU = re.compile(
    r"^(?:what is (?:an? |the )?(?P<a>.+?)|(?P<b>.+?) (?:nedir|ne demek|ne demektir|anlamı|ne işe yarar)"
    r"|(?P<c>.+?) meaning|qu.?est.ce qu.?(?:un |une |le |la )?(?P<d>.+?)|que es (?:un |una |el |la )?(?P<e>.+?)"
    r"|was ist (?:ein |eine |der |die |das )?(?P<f>.+?)|o que (?:é|e) (?:um |uma |o |a )?(?P<g>.+?))\??$", re.I)


def sayi(x):
    x = (x or "0").strip().replace("%", "").replace(",", ".")
    try:
        return float(x)
    except ValueError:
        return 0.0


def oku(klasor, ad):
    yol = os.path.join(klasor, ad)
    if not os.path.exists(yol):
        return []
    with open(yol, encoding="utf-8-sig") as f:
        satirlar = list(csv.reader(f))
    return [dict(anahtar=r[0], tik=sayi(r[1]), gos=sayi(r[2]), to=sayi(r[3]), sira=sayi(r[4]))
            for r in satirlar[1:] if len(r) >= 5]


def topla(rows):
    tik = sum(r["tik"] for r in rows)
    gos = sum(r["gos"] for r in rows)
    sira = sum(r["sira"] * r["gos"] for r in rows) / gos if gos else 0
    return tik, gos, (100 * tik / gos if gos else 0), sira


def yol_of(url):
    return re.sub(r"^https?://[^/]+", "", url) or "/"


def dil_bolum(url):
    p = yol_of(url).strip("/").split("/")
    dil = p[0] if p and p[0] in DILLER else "tr"
    kalan = p[1:] if dil != "tr" else p
    bolum = next((ad for k, ad in BOLUMLER if kalan and kalan[0] == k), "ana sayfa" if not kalan or kalan == [""] else "diğer")
    return dil, bolum


def tablo(baslik, satirlar, kolon):
    out = [f"| {baslik} | Tıklama | Gösterim | Tıklama oranı | Ort. sıra |", "|---|---|---|---|---|"]
    for ad, (tik, gos, to, sira) in satirlar:
        out.append(f"| {ad} | {int(tik)} | {int(gos)} | {to:.2f}% | {sira:.1f} |")
    return "\n".join(out)


def slugify(t):
    t = t.lower().strip()
    for a, b in (("ç", "c"), ("ğ", "g"), ("ı", "i"), ("ş", "s"), ("ö", "o"), ("ü", "u"), ("é", "e"), ("è", "e")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def kesif_sluglari():
    yol = os.path.join(ROOT, "assets", "discover", "catalog.json")
    return {c["slug"] for c in json.load(open(yol, encoding="utf-8"))} if os.path.exists(yol) else set()


def sozlukte_mi(terim, anahtarlar):
    """Tekil/çoğul ve Türkçe ek ("playlistin", "playlistimiz") farkını tolere eder."""
    s = slugify(terim)
    if s in anahtarlar or s + "s" in anahtarlar or s.rstrip("s") in anahtarlar:
        return True
    return any(len(k) >= 5 and s.startswith(k) and len(s) - len(k) <= 4 for k in anahtarlar)


def sozluk_anahtarlari():
    yol = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
    anahtar = set()
    for m in json.load(open(yol, encoding="utf-8")) if os.path.exists(yol) else []:
        anahtar |= {m["slug"], slugify(m.get("en", ""))}
        for parca in (m.get("full") or "").split("·"):
            if parca.strip():
                anahtar.add(slugify(parca))
    birlesmis = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
    if os.path.exists(birlesmis):
        anahtar |= set(json.load(open(birlesmis, encoding="utf-8")).get("eslesme", {}))
    return anahtar


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not argv:
        print(__doc__)
        sys.exit(2)
    klasor = os.path.expanduser(argv[0])
    taban_yol = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--taban=")), None)
    md_yol = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--md=")), None)

    sorgular, sayfalar = oku(klasor, "Sorgular.csv"), oku(klasor, "Sayfa sayısı.csv")
    grafik, ulkeler, cihazlar = oku(klasor, "Grafik.csv"), oku(klasor, "Ülkeler.csv"), oku(klasor, "Cihazlar.csv")
    if not sayfalar:
        sys.exit(f"'{klasor}' içinde 'Sayfa sayısı.csv' yok · Search Console dışa aktarımının açılmış klasörünü verin")
    filtre = {}
    yol = os.path.join(klasor, "Filtreler.csv")
    if os.path.exists(yol):
        filtre = {r[0]: r[1] for r in csv.reader(open(yol, encoding="utf-8-sig")) if len(r) >= 2}

    md = [f"# Search Console analizi · {os.path.basename(os.path.normpath(klasor))}", ""]
    if grafik:
        md.append(f"Dönem: {grafik[0]['anahtar']} → {grafik[-1]['anahtar']} · {filtre.get('Arama türü', '')}")
    tik, gos, to, sira = topla(grafik or sayfalar)
    md += [f"Toplam: **{int(tik)} tıklama**, {int(gos)} gösterim, tıklama oranı %{to:.2f}, ort. sıra {sira:.1f}", ""]
    if len(grafik) >= 60:
        son, onceki = topla(grafik[-30:]), topla(grafik[-60:-30])
        md.append(f"Son 30 gün: {int(son[0])} tıklama (önceki 30 gün {int(onceki[0])}), ort. sıra {son[3]:.1f} (önce {onceki[3]:.1f})")
        md.append("")
    # Sayfa dışa aktarımı en alakalı 1.000 sayfayla sınırlı: dil/bölüm payları bu kümeden
    gruplar = defaultdict(list)
    for r in sayfalar:
        dil, bolum = dil_bolum(r["anahtar"])
        gruplar[("dil", dil)].append(r)
        gruplar[("bolum", bolum)].append(r)
    for tur, baslik in (("dil", "Dil"), ("bolum", "Bölüm")):
        satir = sorted(((k[1], topla(v)) for k, v in gruplar.items() if k[0] == tur), key=lambda x: -x[1][0])
        md += [f"## {baslik} payı (en alakalı {len(sayfalar)} sayfa)", "", tablo(baslik, satir, None), ""]
    md += ["## En çok tıklanan sayfalar", "", tablo("Sayfa", [(f"`{yol_of(r['anahtar'])}`", (r['tik'], r['gos'], r['to'], r['sira']))
                                                             for r in sorted(sayfalar, key=lambda r: -r['tik'])[:15]], None), ""]
    md += ["## En çok tıklanan sorgular", "", tablo("Sorgu", [(r["anahtar"], (r['tik'], r['gos'], r['to'], r['sira']))
                                                             for r in sorted(sorgular, key=lambda r: -r['tik'])[:15]], None), ""]
    if cihazlar:
        md += ["## Cihaz", "", tablo("Cihaz", [(r["anahtar"], (r['tik'], r['gos'], r['to'], r['sira'])) for r in cihazlar], None), ""]
    if ulkeler:
        md += ["## Ülke (ilk 8)", "", tablo("Ülke", [(r["anahtar"], (r['tik'], r['gos'], r['to'], r['sira']))
                                                    for r in sorted(ulkeler, key=lambda r: -r['tik'])[:8]], None), ""]

    # 2) Taban karşılaştırması
    if taban_yol:
        taban = json.load(open(taban_yol, encoding="utf-8"))
        simdi = {yol_of(r["anahtar"]): r for r in sayfalar}
        md += [f"## Karşılaştırma · {taban['ad']}", "", taban.get("not", ""), "",
               "| Sayfa | Tıklama oranı (önce → şimdi) | Sıra (önce → şimdi) | Gösterim (önce → şimdi) | Değerlendirme |",
               "|---|---|---|---|---|"]
        geri = 0
        for s in taban["sayfalar"]:
            r = simdi.get(s["yol"])
            if not r:
                md.append(f"| `{s['yol']}` | %{s['to']:.2f} → yok | {s['sira']:.1f} → yok | {int(s['gos'])} → yok | dışa aktarımda yok |")
                continue
            sira_dustu = r["sira"] > s["sira"] + 2
            to_artti = r["to"] > s["to"]
            karar = "geri al" if sira_dustu and not to_artti else ("iyi" if to_artti and not sira_dustu else "izle")
            geri += karar == "geri al"
            md.append(f"| `{s['yol']}` | %{s['to']:.2f} → %{r['to']:.2f} | {s['sira']:.1f} → {r['sira']:.1f} | "
                      f"{int(s['gos'])} → {int(r['gos'])} | {karar} |")
        md += ["", f"Not: dönem uzunlukları farklıysa gösterim değil oran ve sıra karşılaştırılır. Geri alma önerilen: {geri}", ""]

    # 3) Talep · sözlükte karşılığı olmayan / zayıf kalan sorgular
    anahtarlar, araclar = sozluk_anahtarlari(), kesif_sluglari()
    yok, zayif = [], []
    for r in sorgular:
        m = SORU.match(r["anahtar"].strip())
        if not m:
            continue
        terim = next(g for g in m.groups() if g).strip(" ?")
        if slugify(terim) in araclar:
            continue  # araç adı: keşif sayfası var, sözlük konusu değil
        if sozlukte_mi(terim, anahtarlar):
            if r["gos"] >= 150 and r["sira"] <= 15 and r["to"] < 0.5:
                zayif.append((r, terim))
        elif r["gos"] >= 20:
            yok.append((r, terim))
    md += ["## Talep · sözlükte sayfası olmayan soru kalıbı sorgular", "",
           "Gösterim alıyoruz ama sözlükte karşılığı yok (yeni terim adayı; karar insanın):", "",
           "| Sorgu | Terim | Gösterim | Tıklama | Ort. sıra |", "|---|---|---|---|---|"]
    md += [f"| {r['anahtar']} | {t} | {int(r['gos'])} | {int(r['tik'])} | {r['sira']:.1f} |"
           for r, t in sorted(yok, key=lambda x: -x[0]["gos"])[:25]] or ["| (yok) | | | | |"]
    md += ["", "## Talep · sözlükte var ama ilk sayfada az tıklanan (açıklama adayı)", "",
           "| Sorgu | Terim | Gösterim | Tıklama oranı | Ort. sıra |", "|---|---|---|---|---|"]
    md += [f"| {r['anahtar']} | {t} | {int(r['gos'])} | %{r['to']:.2f} | {r['sira']:.1f} |"
           for r, t in sorted(zayif, key=lambda x: -x[0]["gos"])[:25]] or ["| (yok) | | | | |"]
    metin = "\n".join(md) + "\n"
    if md_yol:
        open(md_yol, "w", encoding="utf-8").write(metin)
        print(f"→ {md_yol}")
    else:
        print(metin)


if __name__ == "__main__":
    main()
