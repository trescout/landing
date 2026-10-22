#!/usr/bin/env python3
"""Erken erişim kayıtları hangi kaynaktan ve sayfadan geliyor?

Kaynak ve sayfa yolu yalnız yönetici bildirim e-postasında duruyor (api/subscribe.js:
"Yeni erken erişim kaydı · <kaynak>", gövdede "Kaynak:", "Sayfa:", "Tarih:"); Resend
Audience'ta yalnız adres var, Vercel Analytics'teki early_access_submit olayı da
yalnız rıza veren ziyaretçide sayılıyor. Bu betik bildirim e-postalarının dışa
aktarımını (Gmail/Google Takeout .mbox, Apple Mail .mbox klasörü ya da .eml
dosyaları) okuyup kaynak, bölüm, dil ve sayfa dökümü çıkarır. Bildirimde kişinin
adresi yoktur (#210); betik de adres işlemez.

İsteğe bağlı --gsc=<Search Console klasörü>: bölüm başına tıklama ile kayıt
oranını yan yana koyar ("keşif trafiğin %75'i, kayıt da getiriyor mu?").
DeepLearning.AI "AI for Everyone": iş incelemesi, değer ölçütü (ders iş listesi H3).

Kullanım:
  python3 scripts/kayit-kaynaklari.py ~/Downloads/TreScout-bildirimler.mbox
  python3 scripts/kayit-kaynaklari.py ~/Downloads/eml-klasoru --gsc=~/Desktop/trescout-3
"""
import csv
import email
import email.policy
import mailbox
import os
import re
import sys
from collections import Counter

KONU = re.compile(r"(Yeni erken erişim kaydı|Tekrar kayıt) · (.+)")
DILLER = ("en", "fr", "pt", "es", "de")
BOLUM = {"discover": "keşif", "dictionary": "sözlük", "reports": "rapor"}


def mesajlar(yol):
    yol = os.path.expanduser(yol)
    if os.path.isdir(yol) and not os.path.exists(os.path.join(yol, "mbox")):
        for kok, _, dosyalar in os.walk(yol):
            for ad in dosyalar:
                tam = os.path.join(kok, ad)
                if ad.endswith(".eml"):
                    with open(tam, "rb") as f:
                        yield email.message_from_binary_file(f, policy=email.policy.default)
                elif ad.endswith(".mbox") or ad == "mbox":
                    yield from mailbox.mbox(tam)
    else:
        yield from mailbox.mbox(os.path.join(yol, "mbox") if os.path.isdir(yol) else yol)


def govde(m):
    if m.is_multipart():
        for parca in m.walk():
            if parca.get_content_type() == "text/plain":
                return parca.get_payload(decode=True).decode(parca.get_content_charset() or "utf-8", "replace")
        return ""
    yuk = m.get_payload(decode=True)
    return yuk.decode(m.get_content_charset() or "utf-8", "replace") if isinstance(yuk, bytes) else str(m.get_payload())


def baslik_coz(deger):
    return str(email.header.make_header(email.header.decode_header(deger or "")))


def kayitlar(yol):
    for m in mesajlar(yol):
        konu = baslik_coz(m.get("Subject", ""))
        k = KONU.search(konu)
        if not k:
            continue
        g = govde(m)
        sayfa = re.search(r"^Sayfa: https?://[^/\s]+(\S*)", g, re.M)
        tarih = re.search(r"^Tarih: (\d{4}-\d{2}-\d{2})", g, re.M)
        kaynak = re.search(r"^Kaynak: (.+)$", g, re.M)
        yield {
            "tekrar": k.group(1) == "Tekrar kayıt",
            "kaynak": (kaynak.group(1) if kaynak else k.group(2)).strip(),
            "yol": sayfa.group(1) if sayfa else "",
            "tarih": tarih.group(1) if tarih else "",
        }


def dil_bolum(yol):
    p = [x for x in (yol or "/").split("/") if x]
    dil = p[0] if p and p[0] in DILLER else "tr"
    kalan = p[1:] if dil != "tr" else p
    return dil, (BOLUM.get(kalan[0], "diğer") if kalan else "ana sayfa")


def gsc_bolum_tiklama(klasor):
    yol = os.path.join(os.path.expanduser(klasor), "Sayfa sayısı.csv")
    tik = Counter()
    with open(yol, encoding="utf-8-sig") as f:
        for r in list(csv.reader(f))[1:]:
            _, bolum = dil_bolum(re.sub(r"^https?://[^/]+", "", r[0]))
            tik[bolum] += float(r[1] or 0)
    return tik


def tablo(baslik, sayac, toplam):
    satir = [f"| {baslik} | Kayıt | Pay |", "|---|---|---|"]
    satir += [f"| {k or '(yok)'} | {v} | %{100 * v / toplam:.0f} |" for k, v in sayac.most_common(15)]
    return "\n".join(satir)


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not argv:
        print(__doc__)
        sys.exit(2)
    gsc = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--gsc=")), None)
    tum = list(kayitlar(argv[0]))
    yeni = [k for k in tum if not k["tekrar"]]
    if not yeni:
        sys.exit("Bildirim e-postası bulunamadı (konu: 'Yeni erken erişim kaydı · …').")
    n = len(yeni)
    tarihler = sorted(k["tarih"] for k in yeni if k["tarih"])
    md = [f"# Erken erişim kayıtları · {n} yeni kayıt ({len(tum) - n} tekrar)",
          f"Dönem: {tarihler[0] if tarihler else '?'} → {tarihler[-1] if tarihler else '?'}", ""]
    md += ["## Kaynak (form türü)", "", tablo("Kaynak", Counter(k["kaynak"] for k in yeni), n), ""]
    bolumler = Counter(dil_bolum(k["yol"])[1] for k in yeni)
    md += ["## Bölüm", "", tablo("Bölüm", bolumler, n), ""]
    md += ["## Dil", "", tablo("Dil", Counter(dil_bolum(k["yol"])[0] for k in yeni), n), ""]
    md += ["## Sayfa (ilk 15)", "", tablo("Sayfa", Counter(k["yol"] for k in yeni), n), ""]
    md += ["## Ay", "", tablo("Ay", Counter(k["tarih"][:7] for k in yeni), n), ""]
    if gsc:
        tik = gsc_bolum_tiklama(gsc)
        md += ["## Bölüm başına arama tıklaması ve kayıt", "",
               "Dönemler aynı değilse oran yön gösterir, kesin dönüşüm oranı değildir.", "",
               "| Bölüm | Arama tıklaması | Kayıt | Kayıt / 100 tıklama |", "|---|---|---|---|"]
        for b in sorted(set(tik) | set(bolumler), key=lambda b: -tik.get(b, 0)):
            t, k = tik.get(b, 0), bolumler.get(b, 0)
            md.append(f"| {b} | {int(t)} | {k} | {100 * k / t:.1f} |" if t else f"| {b} | 0 | {k} | · |")
    print("\n".join(md))


if __name__ == "__main__":
    main()
