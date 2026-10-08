#!/usr/bin/env python3
"""
SSS şeması guard'ı (CI) · FAQPage JSON-LD'si sayfada görünen SSS ile aynı olmalı.

Neden gerekti (2026-10-08): Google, FAQPage şemasındaki soru/cevapların sayfada
görünen metinle eşleşmesini istiyor. Elle düzenlenen sayfalarda görünen SSS
değişiyor, <head>'deki şema eski kalıyordu (dictionary/emitter: şemada "Türkçesi
nedir?", sayfada "Türkçe karşılığı nedir?"). Ayrıca Answer.text HTML kabul ettiği
için düz metindeki "<dal>" kaçışlanmadan yazılınca etiket sanılıp düşüyordu
(dictionary/git-push). dict-sync.py artık şemayı görünen metinle aynı temizlikten
geçiriyor; bu guard kaymayı yakalar.

Karşılaştırma: etiketler atılır, sonra HTML varlıkları çözülür. Şemada çıplak
"<dal>" kalırsa metinden düşer ve sayfadakiyle tutmaz · yakalanır.
Statik, hızlı, ağ yok. Kullanım: python3 scripts/check-sss-sema.py
"""
import os, re, sys, json, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GORUNEN = re.compile(r'<p class="(?:dict|disc)-faq-q">(.*?)</p>\s*<p class="(?:dict|disc)-faq-a">(.*?)</p>', re.S)
LDJSON = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def metin(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def sema(sayfa):
    out = []
    for blok in LDJSON.findall(sayfa):
        veri = json.loads(blok)
        for x in veri if isinstance(veri, list) else [veri]:
            if isinstance(x, dict) and x.get("@type") == "FAQPage":
                for q in x.get("mainEntity", []):
                    out.append((metin(q.get("name")), metin((q.get("acceptedAnswer") or {}).get("text"))))
    return out


def main():
    hatalar, n = [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(("node_modules", ".")):
            continue
        sayfa = open(f, encoding="utf-8").read()
        if '"FAQPage"' not in sayfa:
            continue
        n += 1
        try:
            s = sema(sayfa)
        except json.JSONDecodeError as e:
            hatalar.append(f"{rel}: JSON-LD ayrıştırılamadı ({e})")
            continue
        g = [(metin(q), metin(a)) for q, a in GORUNEN.findall(sayfa)]
        if not g:
            hatalar.append(f"{rel}: FAQPage şeması var ama sayfada görünen SSS yok")
            continue
        if len(s) != len(g):
            hatalar.append(f"{rel}: şemada {len(s)} soru, sayfada {len(g)}")
        gorunen = dict(g)
        for q, a in s:
            if q not in gorunen:
                hatalar.append(f"{rel}: şemadaki soru sayfada yok · {q[:70]}")
            elif gorunen[q] != a:
                hatalar.append(f"{rel}: cevap sayfadakiyle tutmuyor · {q[:70]}")
    if hatalar:
        print(f"✗ SSS şeması ↔ sayfa · {len(hatalar)} uyuşmazlık")
        for h in hatalar[:30]:
            print("   ", h)
        print("  → şemayı sayfada görünen SSS metnine eşitleyin (Answer.text'te düz '<' → &lt;)")
        sys.exit(1)
    print(f"✓ SSS şeması ↔ sayfa tutarlı · {n} FAQPage sayfası")


if __name__ == "__main__":
    main()
