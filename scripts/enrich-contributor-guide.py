#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Açık Kaynak Katkı Rehberi Üreticisi (Contributor Guide Engine)
========================================================================
TreScout kataloğundaki açık kaynak projeleri analiz ederek geliştiricilerin
kolayca ilk katkılarını yapabilmeleri için GitHub Good First Issue,
Contributing Guide ve Lisans hakları rehberini üretir.

Kullanım:
    python3 scripts/enrich-contributor-guide.py [--output assets/discover/contributor-guides.json]
"""

import os
import sys
import json
import re
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
OUTPUT_PATH = os.path.join(ROOT, "assets", "discover", "contributor-guides.json")


def parse_github_repo(url_or_slug, tool):
    # Kaynak URL veya slug'dan GitHub owner/repo bul
    cmds = tool.get("cmds", {})
    if isinstance(cmds, dict):
        for _, items in cmds.items():
            if isinstance(items, list):
                for item in items:
                    cmd_str = item.get("komut", "")
                    m = re.search(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', cmd_str)
                    if m:
                        return m.group(1).rstrip('.git')

    guncellemeler = tool.get("guncellemeler", [])
    for g in guncellemeler:
        if "tasindi" in g:
            return g["tasindi"]

    return None


def determine_license_info(meta_str):
    meta_lower = (meta_str or "").lower()
    if "mit" in meta_lower:
        return {
            "name": "MIT",
            "type": "Permissive (Oldukça Özgür)",
            "commercial_use": True,
            "badge": "Ticari Kullanıma Uygun",
            "badge_color": "green"
        }
    elif "apache" in meta_lower:
        return {
            "name": "Apache 2.0",
            "type": "Permissive (Patent Korumalı)",
            "commercial_use": True,
            "badge": "Ticari Kullanıma Uygun",
            "badge_color": "green"
        }
    elif "gpl" in meta_lower or "agpl" in meta_lower:
        return {
            "name": "GPL / AGPL",
            "type": "Copyleft (Türetilen Kod Açılmalı)",
            "commercial_use": False,
            "badge": "Kod Açma Zorunluluğu",
            "badge_color": "yellow"
        }
    return {
        "name": "Açık Kaynak",
        "type": "Belirtilmemiş",
        "commercial_use": True,
        "badge": "Açık Kaynak",
        "badge_color": "blue"
    }


def main():
    parser = argparse.ArgumentParser(description="TreScout Contributor Guide Engine")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    if not os.path.exists(CATALOG_PATH):
        print(f"Hata: Katalog dosyası bulunamadı: {CATALOG_PATH}")
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    guides = {}
    matched_count = 0

    for tool in catalog:
        slug = tool.get("slug", "")
        if not slug:
            continue

        repo = parse_github_repo(slug, tool)
        license_info = determine_license_info(tool.get("meta", ""))

        if repo:
            matched_count += 1
            guides[slug] = {
                "slug": slug,
                "title": tool.get("title", slug),
                "github_repo": repo,
                "good_first_issues_url": f"https://github.com/{repo}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22",
                "help_wanted_url": f"https://github.com/{repo}/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22",
                "contribute_hub_url": f"https://github.com/{repo}/contribute",
                "fork_url": f"https://github.com/{repo}/fork",
                "contributing_guide_url": f"https://github.com/{repo}/blob/main/CONTRIBUTING.md",
                "quick_contribute_cmd": f"git clone https://github.com/{repo}.git && cd {repo.split('/')[-1]}",
                "license": license_info
            }
        else:
            guides[slug] = {
                "slug": slug,
                "title": tool.get("title", slug),
                "github_repo": None,
                "license": license_info
            }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(guides, f, ensure_ascii=False, indent=2)

    print(f"✅ Katkı rehberi başarıyla üretildi: {args.output}")
    print(f"   Toplam araç: {len(catalog)} · Doğrudan GitHub eşleşen: {matched_count}")


if __name__ == "__main__":
    main()
