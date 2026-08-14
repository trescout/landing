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
B = os.environ.get("SITE_URL") or "https://trescout.com"
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
L += ["", "## Raporlar", "", "Günlük teknoloji raporlarının arşivi (PDF).", "", f"- [Raporlar]({B}/reports/)", ""]

# İngilizce taraf · 2026-08-07'ye kadar llms.txt yalnız Türkçe sayfaları listeliyordu,
# yani 397 keşif + 481 sözlük + rapor arşivinin İngilizcesi yapay zekâ tarayıcılarına
# görünmüyordu. İngilizce sayfalar Türkçesinden üretiliyor (discover-en.py /
# dictionary-en.py) · aynı slug, /en/ önekiyle.
import os as _os
def _var(yol): return _os.path.isdir(_os.path.join(ROOT, yol))
en_terim = [t for t in man if _var(f"en/dictionary/{t['slug']}")]
en_arac  = [c for c in cat if _var(f"en/discover/{c['slug']}")]
L += ["## English", "",
      "The same catalogue in English, translated from the Turkish source. Raw Markdown for any page: append `.md` to the URL.", "",
      f"- [English home]({B}/en/)",
      f"- [Dictionary index]({B}/en/dictionary/)",
      f"- [Discover index]({B}/en/discover/)",
      f"- [Reports archive]({B}/en/reports/)", ""]
for t in sorted(en_terim, key=lambda x: x["en"].lower()):
    L.append(f"- [What is {t['en']}?]({B}/en/dictionary/{t['slug']}/) (raw: {B}/en/dictionary/{t['slug']}.md): {clip(t.get('kisa_en', ''))}")
for c in sorted(en_arac, key=lambda x: -(x.get("stars") or 0)):
    L.append(f"- [{c['title']}]({B}/en/discover/{c['slug']}/) (raw: {B}/en/discover/{c['slug']}.md): {clip(c.get('tagline_en', ''))}")
# Fransızca taraf · sayfalar aşamalı üretiliyor, bu yüzden yalnız DİSKTE OLAN
# sayfalar listeleniyor · yarım üretimde llms.txt 404'e link vermesin diye.
fr_terim = [t for t in man if _var(f"fr/dictionary/{t['slug']}")]
fr_arac  = [c for c in cat if _var(f"fr/discover/{c['slug']}")]
if fr_terim or fr_arac:
    L += ["", "## Français", "",
          "Le même catalogue en français, traduit depuis la source turque. Markdown brut : ajoutez `.md` à l'URL.", "",
          f"- [Accueil]({B}/fr/)",
          f"- [Glossaire]({B}/fr/dictionary/)",
          f"- [Découvrir]({B}/fr/discover/)"]
    if _var("fr/reports"):
        L.append(f"- [Archive des rapports]({B}/fr/reports/)")
    L.append("")
    for t_ in sorted(fr_terim, key=lambda x: x["en"].lower()):
        L.append(f"- [Qu'est-ce que {t_['en']} ?]({B}/fr/dictionary/{t_['slug']}/) (brut: {B}/fr/dictionary/{t_['slug']}.md): {clip(t_.get('kisa_fr', ''))}")
    for c in sorted(fr_arac, key=lambda x: -(x.get("stars") or 0)):
        L.append(f"- [{c['title']}]({B}/fr/discover/{c['slug']}/) (brut: {B}/fr/discover/{c['slug']}.md): {clip(c.get('tagline_fr', ''))}")

pt_terim = [t for t in man if _var(f"pt/dictionary/{t['slug']}")]
pt_arac  = [c for c in cat if _var(f"pt/discover/{c['slug']}")]
if pt_terim or pt_arac:
    L += ["", "## Português", "",
          "O mesmo catálogo em português, traduzido da fonte em turco. Markdown bruto: acrescente `.md` à URL.", "",
          f"- [Início]({B}/pt/)",
          f"- [Glossário]({B}/pt/dictionary/)",
          f"- [Descobrir]({B}/pt/discover/)"]
    if _var("pt/reports"):
        L.append(f"- [Arquivo de relatórios]({B}/pt/reports/)")
    L.append("")
    for t_ in sorted(pt_terim, key=lambda x: x["en"].lower()):
        L.append(f"- [O que é {t_['en']}?]({B}/pt/dictionary/{t_['slug']}/) (bruto: {B}/pt/dictionary/{t_['slug']}.md): {clip(t_.get('kisa_pt', ''))}")
    for c in sorted(pt_arac, key=lambda x: -(x.get("stars") or 0)):
        L.append(f"- [{c['title']}]({B}/pt/discover/{c['slug']}/) (bruto: {B}/pt/discover/{c['slug']}.md): {clip(c.get('tagline_pt', ''))}")

es_terim = [t for t in man if _var(f"es/dictionary/{t['slug']}")]
es_arac  = [c for c in cat if _var(f"es/discover/{c['slug']}")]
if es_terim or es_arac:
    L += ["", "## Español", "",
          "El mismo catálogo en español, traducido de la fuente en turco. Markdown en bruto: añada `.md` a la URL.", "",
          f"- [Inicio]({B}/es/)",
          f"- [Glosario]({B}/es/dictionary/)",
          f"- [Descubrir]({B}/es/discover/)"]
    if _var("es/reports"):
        L.append(f"- [Archivo de informes]({B}/es/reports/)")
    L.append("")
    for t_ in sorted(es_terim, key=lambda x: x["en"].lower()):
        L.append(f"- [¿Qué es {t_['en']}?]({B}/es/dictionary/{t_['slug']}/) (bruto: {B}/es/dictionary/{t_['slug']}.md): {clip(t_.get('kisa_es', ''))}")
    for c in sorted(es_arac, key=lambda x: -(x.get("stars") or 0)):
        L.append(f"- [{c['title']}]({B}/es/discover/{c['slug']}/) (bruto: {B}/es/discover/{c['slug']}.md): {clip(c.get('tagline_es', ''))}")

L += ["", "## İletişim", "", "hello@trescout.com", ""]
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

# llms-en.txt üreteci (İngilizce dinamik indeks)
E = ["# TreScout (English Index)", "",
     "> TreScout scans GitHub, Hacker News, HuggingFace and Lobsters every day, summarizes the highlights and collects them in one daily report (web + PDF, Turkish and English).", "",
     f"Last updated: {TODAY} · {len(cat)} tools · {len(man)} terms", "",
     "## Tech Dictionary", "",
     "Plain-language definitions of AI and software terms. Append `.md` to any URL for raw Markdown (e.g. " + B + "/en/dictionary/rag.md).", "",
     f"- [Tech Dictionary index]({B}/en/dictionary/)"]
for t in sorted(man, key=lambda x: x["en"].lower()):
    # 2026-08-07 · burada kisa (Türkçe) yazılıyordu · İngilizce indekste Türkçe açıklama
    E.append(f"- [What is {t['en']}?]({B}/en/dictionary/{t['slug']}/) (raw: {B}/en/dictionary/{t['slug']}.md): {clip(t.get('kisa_en') or t.get('kisa', ''))}")
E += ["", "## Discover", "",
      "Daily highlights of trending open-source projects with setup commands and AI-powered usage guides.", "",
      f"- [Discover index]({B}/en/discover/)"]
for c in sorted(cat, key=lambda x: -(x.get("stars") or 0)):
    E.append(f"- [{c['title']}]({B}/en/discover/{c['slug']}/) (raw: {B}/en/discover/{c['slug']}.md): {clip(c.get('tagline_en') or c.get('tagline', ''))}")
E += ["", "## Reports", "", "Archive of daily tech reports (PDF).", "", f"- [Reports]({B}/reports/)", "",
      "## AI Crawlers & API Access", "",
      "Every dictionary term and open-source project page is served as both HTML and plain Markdown:",
      f"- Append `.md` to any dictionary or discover URL to fetch raw Markdown.",
      "- Use `Accept: text/markdown` HTTP request headers.", "",
      "## Contact", "", "hello@trescout.com", ""]
open(os.path.join(ROOT, "llms-en.txt"), "w", encoding="utf-8").write("\n".join(E))
print(f"llms-en.txt güncellendi · {len(man)} term + {len(cat)} tool indekslendi (EN)")

