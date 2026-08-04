#!/usr/bin/env python3
"""
llms.txt üreteci · AI/LLM site indeksi (llmstxt.org formatı)
============================================================
catalog + sözlük manifestinden TAM indeksi üretir → her keşif/sözlük eklemesinde
güncel kalır (önceden elle yazılıp bayatlıyordu: 6 link / 143 sayfa). Her öğenin
ham .md linkiyle birlikte → AI ajanları doğrudan temiz markdown'a ulaşır.
Action'da içerik adımlarından sonra çalışır. Kullanım: python3 scripts/llms-txt.py
"""
import os, json, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = os.environ.get("DICT_DATE") or datetime.date.today().isoformat()
cat = json.load(open(os.path.join(ROOT, "assets", "discover", "catalog.json"), encoding="utf-8"))
man = json.load(open(os.path.join(ROOT, "assets", "dictionary", "dictionary.json"), encoding="utf-8"))
B = "https://trescout.com"
def clip(s, n=90):
    s = (s or "").strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"

L = ["# TreScout", "",
     "> TreScout, GitHub, Hacker News ve HuggingFace gibi kaynakları her gün tarar, yapay zekâ ile Türkçe özetler ve PDF rapor olarak gönderir. Açık kaynak ve teknoloji trendlerini Türkçe takip etmek isteyenler için.", "",
     f"Son güncelleme: {TODAY} · {len(cat)} araç · {len(man)} terim", "",
     "## Teknoloji Sözlüğü", "",
     "Yapay zekâ ve yazılım terimlerinin sade Türkçe açıklamaları. Her terimin ham Markdown sürümü URL sonuna `.md` eklenerek alınır (örn. " + B + "/dictionary/rag.md).", "",
     f"- [Teknoloji Sözlüğü dizini]({B}/dictionary/)"]
for t in sorted(man, key=lambda x: x["en"].lower()):
    L.append(f"- [{t['en']} nedir?]({B}/dictionary/{t['slug']}/) (ham: {B}/dictionary/{t['slug']}.md): {clip(t.get('kisa', ''))}")
L += ["", "## Keşif", "",
      "Her gün öne çıkan açık kaynak projelerinin Türkçe tanıtımları; gerçek kurulum komutları + yapay zekâ ile kullanım rehberiyle.", "",
      f"- [Keşif dizini]({B}/discover/)"]
for c in sorted(cat, key=lambda x: -(x.get("stars") or 0)):
    L.append(f"- [{c['title']}]({B}/discover/{c['slug']}/) (ham: {B}/discover/{c['slug']}.md): {clip(c.get('tagline', ''))}")
L += ["", "## Raporlar", "", "Günlük teknoloji raporlarının arşivi (PDF).", "", f"- [Raporlar]({B}/reports/)", "",
      "## İletişim", "", "hello@trescout.com", ""]
open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(L))
print(f"llms.txt güncellendi · {len(man)} terim + {len(cat)} araç indekslendi (.md linkleriyle)")

# llms-full.txt üreteci (tam içerik birleştirmesi)
F = ["# TreScout Full Knowledge Base (llms-full.txt)", "",
     "> TreScout, GitHub, Hacker News ve HuggingFace gibi kaynakları her gün tarar, yapay zekâ ile Türkçe özetler ve PDF rapor olarak gönderir.", "",
     f"Son güncelleme: {TODAY} · {len(cat)} araç · {len(man)} terim", "", "---", "",
     "# TEKNOLOJİ SÖZLÜĞÜ (TAM İÇERİK)", ""]
for t in sorted(man, key=lambda x: x["en"].lower()):
    mp = os.path.join(ROOT, "dictionary", f"{t['slug']}.md")
    if os.path.exists(mp):
        F.append(open(mp, encoding="utf-8").read())
        F.append("\n---\n")

F.append("# KEŞİF (TAM İÇERİK)\n")
for c in sorted(cat, key=lambda x: -(x.get("stars") or 0)):
    cp = os.path.join(ROOT, "discover", f"{c['slug']}.md")
    if os.path.exists(cp):
        F.append(open(cp, encoding="utf-8").read())
        F.append("\n---\n")

open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(F))
print(f"llms-full.txt güncellendi · {len(F)} satır tam içerik haritalandı.")

