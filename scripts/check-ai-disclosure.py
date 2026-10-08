#!/usr/bin/env python3
"""Rapor kapak sayfalarında yapay zekâ şeffaflık beyanı guard'ı.

AB Yapay Zekâ Yasası m.50: kamuyu bilgilendirmek için yayımlanan, yapay zekâ
ile üretilmiş metinde bu durum belirtilmeli (2026-10-09, trescout/app#99).
Her rapor kapağı (TR + 5 dil, günlük + tekrarsız) sayfanın dilindeki beyanı
tam bir kez taşımalı. Kaynaklar: TR · app scripts/publish-report.ts,
diğer diller · scripts/diller.py "rapor_yz" (build-reports-en.js basar).
"""
import glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = ("Bu rapordaki özetler ve çeviriler yapay zekâ ile hazırlanmaktadır. Önemli kararlar "
      "vermeden önce, her maddede bulunan bağlantı üzerinden kaynağı kontrol etmenizi öneririz.")

beklenen = {"": TR}
for dil in ("en", "fr", "pt", "es", "de"):
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/diller.py"), "--json", dil],
                         capture_output=True, text=True, check=True).stdout
    beklenen[dil + "/"] = json.loads(out)["rapor_yz"]

sorunlar, sayfa = [], 0
for on, metin in beklenen.items():
    for f in sorted(glob.glob(os.path.join(ROOT, on + "reports/**/index.html"), recursive=True)):
        if not re.search(r"/20\d\d-\d\d-\d\d/index\.html$", f):
            continue
        sayfa += 1
        h = open(f, encoding="utf-8").read()
        bulunan = re.findall(r'<p class="rep-captured rep-ai-note">([^<]*)</p>', h)
        rel = os.path.relpath(f, ROOT)
        if len(bulunan) != 1:
            sorunlar.append((rel, f"beyan {len(bulunan)} kez (1 olmalı)"))
        elif bulunan[0] != metin:
            sorunlar.append((rel, "beyan metni sayfa dilinin kanonik metniyle aynı değil"))

if sorunlar:
    print(f"❌ YZ şeffaflık beyanı: {len(sorunlar)} sorun ({sayfa} rapor sayfası)")
    for ad, ne in sorunlar[:30]:
        print(f"   {ad}: {ne}")
    sys.exit(1)
print(f"✓ YZ şeffaflık beyanı · {sayfa} rapor sayfasının hepsinde")
