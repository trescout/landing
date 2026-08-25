#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Obsidian & Notion "Teknoloji Kasası" (Markdown Vault Generator)
========================================================================
TreScout'taki 470+ açık kaynak aracı ve 530+ sözlük terimini birbirine [[wiki-link]]
bağlantıları ve YAML frontmatter ile bağlı eksiksiz bir Obsidian/Notion Markdown
bilgi kasasına (PKM Vault) dönüştürür ve zip arşivi olarak paketler.

Kullanım:
    python3 scripts/generate-obsidian-vault.py [--output assets/vault/trescout-vault.zip]
"""

import os
import sys
import json
import shutil
import zipfile
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
DICTIONARY_PATH = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
OUTPUT_DIR = os.path.join(ROOT, "assets", "vault")


def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def slugify(text):
    return (text or "").strip().lower().replace(" ", "-").replace("/", "-")


def build_vault(target_dir):
    tools = load_json(CATALOG_PATH)
    dictionary = load_json(DICTIONARY_PATH)

    os.makedirs(target_dir, exist_ok=True)
    tools_dir = os.path.join(target_dir, "Araçlar")
    dict_dir = os.path.join(target_dir, "Sözlük")
    index_dir = os.path.join(target_dir, "İndeks")

    os.makedirs(tools_dir, exist_ok=True)
    os.makedirs(dict_dir, exist_ok=True)
    os.makedirs(index_dir, exist_ok=True)

    # 1. Sözlük Terimlerini Oluştur
    term_slugs = set()
    for term in dictionary:
        slug = term.get("slug", "")
        if not slug:
            continue
        term_slugs.add(slug)

        en_name = term.get("en") or slug
        full_name = term.get("full", "")
        cat = term.get("cat", "genel")
        desc_tr = term.get("kisa", "")
        desc_en = term.get("kisa_en", "")

        aliases = [en_name]
        if full_name:
            aliases.append(full_name)

        aliases_yaml = "\n".join([f"  - \"{a}\"" for a in aliases])

        content = f"""---
title: "{en_name}"
type: sozluk
category: "{cat}"
aliases:
{aliases_yaml}
url: "https://trescout.com/dictionary/{slug}/"
---

# {en_name} {f'({full_name})' if full_name else ''}

> [!NOTE] Tanım
> {desc_tr}

## İngilizce Açıklama
{desc_en}

---
*Kaynak: [TreScout Sözlük](https://trescout.com/dictionary/{slug}/)*
"""
        with open(os.path.join(dict_dir, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")

    # 2. Açık Kaynak Araç Notlarını Oluştur
    for tool in tools:
        slug = tool.get("slug", "")
        if not slug:
            continue

        title = tool.get("title", slug)
        tagline = tool.get("tagline", "")
        stars = tool.get("stars", 0)
        tags = tool.get("tags", [])
        date = tool.get("date", "")
        cmds = tool.get("cmds", {})

        tags_yaml = "\n".join([f"  - \"{t}\"" for t in tags]) if tags else '  - "Açık Kaynak"'

        # Kurulum komutları
        install_blocks = []
        if isinstance(cmds, dict):
            for k, v in cmds.items():
                if isinstance(v, list):
                    for cmd_item in v:
                        c_title = cmd_item.get("baslik", k.capitalize())
                        c_code = cmd_item.get("komut", "")
                        install_blocks.append(f"### {c_title}\n```bash\n{c_code}\n```")

        install_section = "\n\n".join(install_blocks) if install_blocks else "Kurulum komutu belirtilmemiş."

        content = f"""---
title: "{title}"
type: arac
stars: {stars}
discovered: "{date}"
tags:
{tags_yaml}
url: "https://trescout.com/discover/{slug}/"
---

# {title}

**Yıldız Sayısı:** ★ {stars:,}  
**TreScout Keşif Tarihi:** {date}  

## Özet
{tagline}

## Kurulum & Başlangıç Komutları
{install_section}

---
*Detaylı inceleme: [TreScout Keşif Sayfası](https://trescout.com/discover/{slug}/)*
"""
        with open(os.path.join(tools_dir, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")

    # 3. İndeks ve MOC (Map of Content) Dosyaları
    top_tools = sorted(tools, key=lambda x: x.get("stars", 0), reverse=True)[:30]
    top_links = "\n".join([f"- [[{t['slug']}|{t['title']}]] · ★ {t.get('stars', 0):,} — *{t.get('tagline', '')[:60]}...*" for t in top_tools])

    home_moc = f"""---
title: "TreScout Teknoloji Bilgi Kasası"
type: moc
---

# 📡 TreScout Teknoloji Bilgi Kasası

TreScout açık kaynak ekosisteminin tüm güncel verilerini içeren yerel Obsidian kasasına hoş geldiniz.

## 📂 İçindekiler
- **[[Popüler Araçlar]]**: En yüksek yıldıza sahip ilk 30 proje
- **Araç Sayısı:** {len(tools)} açık kaynak projesi (`/Araçlar`)
- **Sözlük Terimi Sayısı:** {len(dictionary)} teknik kavram (`/Sözlük`)

## 🚀 Öne Çıkan Bazı Projeler
{top_links}

---
*Canlı ve güncel veriler için: [trescout.com](https://trescout.com)*
"""
    with open(os.path.join(index_dir, "Anasayfa.md"), "w", encoding="utf-8") as f:
        f.write(home_moc.strip() + "\n")

    with open(os.path.join(index_dir, "Popüler Araçlar.md"), "w", encoding="utf-8") as f:
        f.write(f"# 🌟 En Popüler Açık Kaynak Araçları\n\n{top_links}\n")


def zip_vault(vault_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(vault_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(vault_dir))
                zipf.write(full_path, rel_path)


def main():
    parser = argparse.ArgumentParser(description="TreScout Obsidian Vault Exporter")
    parser.add_argument("--output", help="Çıktı zip dosyası yolu (varsayılan: assets/vault/trescout-vault.zip)")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    zip_output = args.output or os.path.join(OUTPUT_DIR, "trescout-vault.zip")
    temp_vault_dir = os.path.join(OUTPUT_DIR, "TreScout-Vault")

    print("📓 TreScout Obsidian Vault oluşturuluyor...")
    build_vault(temp_vault_dir)

    print("📦 Zip paketi sıkıştırılıyor...")
    zip_vault(temp_vault_dir, zip_output)

    # Geçici klasörü temizle
    shutil.rmtree(temp_vault_dir)

    file_size_kb = round(os.path.getsize(zip_output) / 1024, 1)
    print(f"✅ Obsidian Vault başarıyla oluşturuldu: {zip_output} ({file_size_kb} KB)")


if __name__ == "__main__":
    main()
