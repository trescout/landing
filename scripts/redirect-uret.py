#!/usr/bin/env python3
"""
Birleştirilmiş sözlük terimlerinin 301 yönlendirmelerini vercel.json'a yazar.

    python3 scripts/redirect-uret.py [--dry]

Kaynak: `assets/dictionary/birlesmis.json` · orada "artık yayınlanmayan slug →
kanonik slug" eşleşmesi duruyor. Her eşleşme için üç dilin sayfası ve ham
markdown'ı yönlendiriliyor:

    /dictionary/agents/        → /dictionary/agent/
    /en/dictionary/agents/     → /en/dictionary/agent/
    /fr/dictionary/agents/     → /fr/dictionary/agent/
    /dictionary/agents.md      → /dictionary/agent.md          (+ /en/ + /fr/)

Neden yönlendirme, neden silme değil: o URL'ler indekslenmiş ve dış bağlantı
almış olabilir. 301, hem ziyaretçiyi doğru sayfaya götürür hem de arama
motorundaki değeri kanonik sayfaya aktarır. Silsek 404 verirdik.

vercel.json'daki `redirects` bloğu HER ÇALIŞTIRMADA yeniden üretilir · elle
eklenen yönlendirme varsa `KORUNAN` listesine yazın, yoksa silinir.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERCEL = os.path.join(ROOT, "vercel.json")
BIRLESMIS = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
DRY = "--dry" in sys.argv

# Bu betiğin üretmediği, elle eklenmiş yönlendirmeler · kaynağı burada tutulur.
# vercel.json her çalıştırmada yeniden yazıldığı için buraya taşındılar.
KORUNAN = [
    {"source": "/rapor", "destination": "/reports/", "permanent": True},
    {"source": "/rapor/", "destination": "/reports/", "permanent": True},
    {"source": "/rapor/(.*)", "destination": "/reports/$1", "permanent": True},
    {"source": "/security.txt", "destination": "/.well-known/security.txt", "permanent": True},
]

DILLER = ["", "/en", "/fr"]

eslesme = json.load(open(BIRLESMIS, encoding="utf-8"))["eslesme"]

uretilen = []
for eski, yeni in sorted(eslesme.items()):
    for o in DILLER:
        uretilen.append({
            "source": f"{o}/dictionary/{eski}",
            "destination": f"{o}/dictionary/{yeni}/",
            "permanent": True,
        })
        uretilen.append({
            "source": f"{o}/dictionary/{eski}.md",
            "destination": f"{o}/dictionary/{yeni}.md",
            "permanent": True,
        })

cfg = json.load(open(VERCEL, encoding="utf-8"))
onceki = len(cfg.get("redirects", []))
cfg["redirects"] = KORUNAN + uretilen

if DRY:
    print(f"[--dry] {onceki} → {len(cfg['redirects'])} yönlendirme")
    for r in uretilen[:6]:
        print("   ", r["source"], "→", r["destination"])
    sys.exit(0)

with open(VERCEL, "w", encoding="utf-8") as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"✓ vercel.json · {len(cfg['redirects'])} yönlendirme "
      f"({len(eslesme)} terim × {len(DILLER)} dil × 2 biçim)")
