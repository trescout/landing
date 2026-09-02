#!/usr/bin/env python3
"""
Birleştirilmiş sözlük terimleri guard'ı (CI)
============================================
2026-08-08'de başlayan canonical sözlük temizliğinde tekil/çoğul ikizler
(agent/agents, plugin/plugins …) kanonik slug'larında birleştirildi: ikiz
sayfalar kaldırıldı, eski URL'ler 301'lendi. Search Console bunları "kullanıcı
tarafından seçilen standart sayfa olmadan kopya" diye işaretliyordu · gövdelerinin
%85'ten fazlası aynıydı. Bu guard teknik route bütünlüğünü denetler; eşleşmenin
anlamsal kararını insan incelemesi ve `duplicate-triage.json` taşır.

Bu guard birleşmenin geri açılmadığını denetler:

  1. Kaldırılan slug'ın sayfası hiçbir dilde geri gelmemiş olmalı
     (günlük hat terimi yeniden yaratırsa yönlendirme kırılır · dict-sync.py
     birlesmis.json'u okuyup engelliyor, burası o korumanın testi)
  2. Manifest'te o slug bulunmamalı
  3. Her kaldırılan slug için vercel.json'da 301 yönlendirme olmalı ·
     hem eğik çizgili hem çizgisiz biçim (Vercel source'u birebir eşleştirir)
  4. Hiçbir sayfa kaldırılan slug'a İÇ BAĞLANTI vermemeli · yönlendirme
     çalışır ama iç bağlantı doğrudan kanonik adrese gitmeli (yönlendirme
     zinciri tarama bütçesi yer, ki bu birleştirmenin sebebiydi)

Kullanım: python3 scripts/check-birlesmis-terimler.py
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER as _DILLER  # noqa: E402
# Dil önekleri tablodan · dördüncü dil eklenince guard onu da denetlesin
DIZIN_ONEKLERI = [""] + [f"{k}/" for k in _DILLER]
URL_ONEKLERI = [""] + [d["onek"] for d in _DILLER.values()]
BIRLESMIS = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
MANIFEST = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
TRIAGE = os.path.join(ROOT, "assets", "dictionary", "duplicate-triage.json")
VERCEL = os.path.join(ROOT, "vercel.json")

if not os.path.exists(BIRLESMIS):
    print("✓ birlesmis.json yok · denetlenecek birleşme kaydı bulunmuyor")
    sys.exit(0)

eslesme = json.load(open(BIRLESMIS, encoding="utf-8"))["eslesme"]
manifest = {t["slug"] for t in json.load(open(MANIFEST, encoding="utf-8"))}
yonlendirme_kaydi = json.load(open(VERCEL, encoding="utf-8")).get("redirects", [])
yonlendirmeler = {r["source"] for r in yonlendirme_kaydi}

sorunlar = []

# Bağlamı insan tarafından incelenmiş, fakat canonical birleştirme yapılmamış
# çiftler. Mapping değildir; yalnız ikiz tarayıcısının aynı issue'yu yeniden
# üretmesini önler.
incelenmis = []
if os.path.exists(TRIAGE):
    incelenmis = json.load(open(TRIAGE, encoding="utf-8")).get("incelenmis", [])
    for sira, kayit in enumerate(incelenmis, 1):
        cift = kayit.get("cift", [])
        if len(cift) != 2 or cift[0] == cift[1]:
            sorunlar.append(f"duplicate-triage #{sira}: iki farklı slug içeren cift gerekli")
            continue
        if any(slug not in manifest for slug in cift):
            sorunlar.append(f"duplicate-triage #{sira}: slug manifest'te yok")
        if tuple(sorted(cift)) in {tuple(sorted((eski, yeni))) for eski, yeni in eslesme.items()}:
            sorunlar.append(f"duplicate-triage #{sira}: canonical mapping ile çakışıyor")
        if kayit.get("karar") != "ayri_tut":
            sorunlar.append(f"duplicate-triage #{sira}: bilinmeyen karar")
for eski, yeni in sorted(eslesme.items()):
    if yeni not in manifest:
        sorunlar.append(f"{eski} → {yeni}: KANONİK terim manifest'te yok")
    if eski in manifest:
        sorunlar.append(f"{eski}: manifest'e geri eklenmiş · birleşme bozuldu")
    for onek in DIZIN_ONEKLERI:
        if os.path.isdir(os.path.join(ROOT, f"{onek}dictionary/{eski}")):
            sorunlar.append(f"{onek}dictionary/{eski}/ · sayfa geri gelmiş")
    for onek in URL_ONEKLERI:
        # Üç biçim de aranıyor · Vercel source'u birebir eşleştirir:
        # slashless, trailing slash ve raw Markdown.
        beklenen = {
            f"{onek}/dictionary/{eski}": f"{onek}/dictionary/{yeni}/",
            f"{onek}/dictionary/{eski}/": f"{onek}/dictionary/{yeni}/",
            f"{onek}/dictionary/{eski}.md": f"{onek}/dictionary/{yeni}.md",
        }
        for kaynak, hedef in beklenen.items():
            kayitlar = [r for r in yonlendirme_kaydi if r.get("source") == kaynak]
            if len(kayitlar) != 1:
                sorunlar.append(f"{kaynak} · tam olarak bir 301 kaydı yok")
            elif kayitlar[0].get("destination") != hedef or kayitlar[0].get("permanent") is not True:
                sorunlar.append(f"{kaynak} · hedef/permanent yanlış (beklenen: {hedef})")

# İç bağlantı taraması
bagli = []
for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
    if "/node_modules/" in p:
        continue
    icerik = open(p, encoding="utf-8").read()
    for eski in eslesme:
        if f"/dictionary/{eski}/" in icerik:
            bagli.append((os.path.relpath(p, ROOT), eski))
            break

if bagli:
    sorunlar.append(f"{len(bagli)} sayfa kaldırılmış slug'a bağlanıyor "
                    f"(ör. {bagli[0][0]} → {bagli[0][1]})")

if sorunlar:
    print(f"❌ Birleştirilmiş terimler guard'ı · {len(sorunlar)} sorun:")
    for s in sorunlar[:30]:
        print(f"   {s}")
    if len(sorunlar) > 30:
        print(f"   … {len(sorunlar) - 30} sorun daha")
    sys.exit(1)

print(f"✓ Birleşmiş terimler tutarlı · {len(eslesme)} canonical mapping, "
      f"{len(eslesme) * len(URL_ONEKLERI)} route ailesi ve "
      f"{len(incelenmis)} bağlam kararı doğrulandı, iç bağlantı temiz")
