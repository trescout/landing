#!/usr/bin/env python3
"""
TreScout · İçerik Snapshot Manifest Üreticisi (PR A)
===================================================
Tüm içerik envanterini (sözlük, keşif, raporlar, diller, sitemap, llms.txt)
ve kritik dosyaların SHA-256 bütünlük özetlerini toplayarak
kök dizinde `content-manifest.json` ve `assets/content-manifest.json` üretir.

Kullanım:
  python3 scripts/generate-manifest.py
"""

import os
import sys
import json
import glob
import hashlib
import datetime
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
DICT_PATH = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
MANIFEST_OUT = os.path.join(ROOT, "content-manifest.json")
MANIFEST_ASSETS_OUT = os.path.join(ROOT, "assets", "content-manifest.json")

def sha256_file(filepath):
    """Dosyanın SHA-256 hash'ini döndürür."""
    if not os.path.isfile(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def get_git_commit():
    """Mevcut git commit SHA'sını alır."""
    env_sha = os.environ.get("GITHUB_SHA")
    if env_sha:
        return env_sha
    try:
        res = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return res.stdout.strip()
    except Exception:
        return "unknown"

def count_html_in_dir(d):
    """Dizindeki HTML dosyalarını sayar."""
    if not os.path.isdir(d):
        return 0
    return len(glob.glob(os.path.join(d, "**", "*.html"), recursive=True))

def build_manifest():
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    git_sha = get_git_commit()

    # Diller
    locales = ["tr", "en", "fr", "pt", "es", "de"]

    # Katalog / Keşif analizi
    discover_items = []
    if os.path.isfile(CATALOG_PATH):
        try:
            with open(CATALOG_PATH, "r", encoding="utf-8") as f:
                discover_items = json.load(f)
        except Exception as e:
            print(f"Uyarı: catalog.json okunamadı: {e}", file=sys.stderr)

    # Sözlük analizi
    dict_items = []
    if os.path.isfile(DICT_PATH):
        try:
            with open(DICT_PATH, "r", encoding="utf-8") as f:
                dict_items = json.load(f)
        except Exception as e:
            print(f"Uyarı: dictionary.json okunamadı: {e}", file=sys.stderr)

    # Raporlar
    reports_json = glob.glob(os.path.join(ROOT, "reports", "*.json"))
    reports_fresh_json = glob.glob(os.path.join(ROOT, "reports", "tekrarsiz", "*.json"))
    reports_pdf = glob.glob(os.path.join(ROOT, "reports", "*.pdf"))

    # Dil bazında sayfa sayıları
    locale_stats = {}
    for loc in locales:
        loc_dir = ROOT if loc == "tr" else os.path.join(ROOT, loc)
        dict_dir = os.path.join(loc_dir, "dictionary")
        disc_dir = os.path.join(loc_dir, "discover")
        rep_dir = os.path.join(loc_dir, "reports")

        locale_stats[loc] = {
            "dictionary_html": count_html_in_dir(dict_dir),
            "discover_html": count_html_in_dir(disc_dir),
            "reports_html": count_html_in_dir(rep_dir),
            "total_html": count_html_in_dir(loc_dir)
        }

    # Kritik dosya SHA256 bütünlüğü
    checksum_targets = {
        "discover_catalog_json": os.path.join(ROOT, "assets", "discover", "catalog.json"),
        "dictionary_json": os.path.join(ROOT, "assets", "dictionary", "dictionary.json"),
        "sitemap_xml": os.path.join(ROOT, "sitemap.xml"),
        "llms_txt": os.path.join(ROOT, "llms.txt"),
        "llms_full_txt": os.path.join(ROOT, "llms-full.txt"),
        "llms_en_txt": os.path.join(ROOT, "llms-en.txt"),
        "vercel_json": os.path.join(ROOT, "vercel.json"),
    }

    checksums = {}
    for key, path in checksum_targets.items():
        rel = os.path.relpath(path, ROOT)
        h = sha256_file(path)
        if h:
            checksums[rel] = h

    manifest = {
        "schema_version": "1.0.0",
        "generated_at": now_utc,
        "git_commit": git_sha,
        "content_version": datetime.date.today().isoformat(),
        "locales": locales,
        "summary": {
            "discover_tools_count": len(discover_items),
            "dictionary_terms_count": len(dict_items),
            "reports_count": len(reports_json),
            "reports_fresh_count": len(reports_fresh_json),
            "reports_pdf_count": len(reports_pdf),
            "total_html_pages": sum(st["total_html"] for st in locale_stats.values()),
        },
        "locale_breakdown": locale_stats,
        "integrity_checksums": checksums,
    }

    return manifest

def main():
    manifest = build_manifest()
    content = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"

    with open(MANIFEST_OUT, "w", encoding="utf-8") as f:
        f.write(content)
    with open(MANIFEST_ASSETS_OUT, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ content-manifest.json üretildi ({manifest['summary']['total_html_pages']} HTML sayfa, "
          f"{manifest['summary']['discover_tools_count']} araç, {manifest['summary']['dictionary_terms_count']} terim)")

if __name__ == "__main__":
    main()
