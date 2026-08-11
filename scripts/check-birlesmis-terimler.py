#!/usr/bin/env python3
"""
Birleştirilmiş sözlük terimleri guard'ı (CI)
============================================
2026-08-08'de 19 tekil/çoğul ikizi (agent/agents, plugin/plugins …) kanonik
slug'larında birleştirildi: ikiz sayfalar kaldırıldı, eski URL'ler 301'lendi.
Search Console bunları "kullanıcı tarafından seçilen standart sayfa olmadan
kopya" diye işaretliyordu · gövdelerinin %85'ten fazlası aynıydı.

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
BIRLESMIS = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
MANIFEST = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
VERCEL = os.path.join(ROOT, "vercel.json")

if not os.path.exists(BIRLESMIS):
    print("✓ birlesmis.json yok · denetlenecek birleşme kaydı bulunmuyor")
    sys.exit(0)

eslesme = json.load(open(BIRLESMIS, encoding="utf-8"))["eslesme"]
manifest = {t["slug"] for t in json.load(open(MANIFEST, encoding="utf-8"))}
yonlendirmeler = {r["source"] for r in json.load(open(VERCEL, encoding="utf-8")).get("redirects", [])}

sorunlar = []
for eski, yeni in sorted(eslesme.items()):
    if yeni not in manifest:
        sorunlar.append(f"{eski} → {yeni}: KANONİK terim manifest'te yok")
    if eski in manifest:
        sorunlar.append(f"{eski}: manifest'e geri eklenmiş · birleşme bozuldu")
    for onek in ("", "en/", "fr/"):
        if os.path.isdir(os.path.join(ROOT, f"{onek}dictionary/{eski}")):
            sorunlar.append(f"{onek}dictionary/{eski}/ · sayfa geri gelmiş")
    for onek in ("", "/en", "/fr"):
        # İKİ biçim de aranıyor · Vercel source'u birebir eşleştirdiği için
        # yalnız eğik çizgisiz hâli yazılınca gerçek istekler 404 veriyordu
        # (2026-08-11'de yayına böyle çıktı).
        for kaynak in (f"{onek}/dictionary/{eski}", f"{onek}/dictionary/{eski}/"):
            if kaynak not in yonlendirmeler:
                sorunlar.append(f"{kaynak} · 301 yönlendirmesi yok "
                                "(scripts/redirect-uret.py çalıştırın)")

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

print(f"✓ Birleşmiş terimler tutarlı · {len(eslesme)} ikiz kanonikte birleşik, "
      f"{len(eslesme) * 3} yönlendirme yerinde, iç bağlantı temiz")
