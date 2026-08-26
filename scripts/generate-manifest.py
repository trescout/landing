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
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
DICT_PATH = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
MANIFEST_OUT = os.path.join(ROOT, "content-manifest.json")
MANIFEST_ASSETS_OUT = os.path.join(ROOT, "assets", "content-manifest.json")
CANONICAL_REPORT_RE = re.compile(r"^trescout-rapor-\d{4}-\d{2}-\d{2}\.json$")
FRESH_REPORT_PAGE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

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

def count_fresh_report_pages(directory):
    """reports/tekrarsiz/YYYY-MM-DD/index.html sayısını sayar."""
    if not os.path.isdir(directory):
        return 0
    count = 0
    for date_dir in glob.glob(os.path.join(directory, "*")):
        if not os.path.isdir(date_dir) or not FRESH_REPORT_PAGE_RE.fullmatch(os.path.basename(date_dir)):
            continue
        if os.path.isfile(os.path.join(date_dir, "index.html")):
            count += 1
    return count


def count_html_in_dir(d, exclude_top_level=None):
    """Dizindeki HTML dosyalarını sayar; gerekirse alt locale ağaçlarını dışarıda bırakır."""
    if not os.path.isdir(d):
        return 0
    excluded = set(exclude_top_level or [])
    files = glob.glob(os.path.join(d, "**", "*.html"), recursive=True)
    if not excluded:
        return len(files)
    count = 0
    for filepath in files:
        relative = os.path.relpath(filepath, d).split(os.sep)
        if not relative or relative[0] not in excluded:
            count += 1
    return count

def build_manifest():
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    git_sha = get_git_commit()

    # Diller
    locales = ["tr", "en", "fr", "pt", "es", "de"]
    translated_locales = [loc for loc in locales if loc != "tr"]

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
    # Tekrarsız raporlar tarih klasörlerinde index.html olarak tutulur;
    # eski *.json glob'u sessizce 0 döndürüyordu.
    fresh_reports_dir = os.path.join(ROOT, "reports", "tekrarsiz")
    fresh_report_pages = count_fresh_report_pages(fresh_reports_dir)
    canonical_report_json = [
        path for path in reports_json
        if CANONICAL_REPORT_RE.fullmatch(os.path.basename(path))
    ]
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
            "total_html": count_html_in_dir(loc_dir, translated_locales) if loc == "tr" else count_html_in_dir(loc_dir)
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

    # source_git_commit, snapshot oluşturulurken checkout edilmiş HEAD'dir.
    # Commit sonrası manifest'in kendi commit SHA'sını taşıması beklenmez.
    manifest = {
        "schema_version": "1.1.0",
        "generated_at": now_utc,
        "source_git_commit": git_sha,
        "content_version": datetime.date.today().isoformat(),
        "locales": locales,
        "summary": {
            "discover_tools_count": len(discover_items),
            "dictionary_terms_count": len(dict_items),
            # Varyant sayısı locale/tekrarsız dosyaları değil root JSON/PDF dosyalarını ifade eder.
            "report_file_variants_count": len(reports_json),
            "canonical_report_dates_count": len(canonical_report_json),
            "fresh_report_pages_count": fresh_report_pages,
            "report_pdf_file_variants_count": len(reports_pdf),
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
