#!/usr/bin/env python3
"""
TreScout · İçerik Snapshot Manifest Guard (PR A)
================================================
`content-manifest.json` dosyasını okuyup:
1. Şema ve alanların tamlığını,
2. Belirtilen SHA-256 hash'lerinin diskteki güncel dosyalarla birebir eşleştiğini,
3. Dil paritesi ve asgari sayfa eşiklerini (ani içerik silinmelerine karşı koruma),
4. Katalog ve sözlük sayılarının tutarlılığını doğrular.

Hata durumunda exit code 1 döner ve CI / yayını durdurur.

Kullanım:
  python3 scripts/check-content-manifest.py
"""

import os
import sys
import json
import hashlib
import glob
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "content-manifest.json")
ASSETS_MANIFEST_PATH = os.path.join(ROOT, "assets", "content-manifest.json")
CANONICAL_REPORT_RE = re.compile(r"^trescout-rapor-\d{4}-\d{2}-\d{2}\.json$")
FRESH_REPORT_PAGE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Asgari emniyet eşikleri (bu sayıların altına düşülmesi içerik kaybı demektir)
MIN_TOOLS = 400
MIN_TERMS = 500
MIN_TOTAL_HTML = 6000

def sha256_file(filepath):
    if not os.path.isfile(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def count_fresh_report_pages(directory):
    if not os.path.isdir(directory):
        return 0
    count = 0
    for date_dir in glob.glob(os.path.join(directory, "*")):
        if not os.path.isdir(date_dir) or not FRESH_REPORT_PAGE_RE.fullmatch(os.path.basename(date_dir)):
            continue
        if os.path.isfile(os.path.join(date_dir, "index.html")):
            count += 1
    return count


def count_html_in_dir(directory, exclude_top_level=None):
    if not os.path.isdir(directory):
        return 0
    excluded = set(exclude_top_level or [])
    files = glob.glob(os.path.join(directory, "**", "*.html"), recursive=True)
    if not excluded:
        return len(files)
    count = 0
    for filepath in files:
        relative = os.path.relpath(filepath, directory).split(os.sep)
        if not relative or relative[0] not in excluded:
            count += 1
    return count


def check_manifest():
    if not os.path.isfile(MANIFEST_PATH):
        print(f"❌ Hata: {MANIFEST_PATH} bulunamadı! 'python3 scripts/generate-manifest.py' çalıştırın.", file=sys.stderr)
        return False

    if not os.path.isfile(ASSETS_MANIFEST_PATH):
        print(f"❌ Hata: {ASSETS_MANIFEST_PATH} bulunamadı!", file=sys.stderr)
        return False

    try:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print(f"❌ Hata: content-manifest.json geçerli bir JSON değil: {e}", file=sys.stderr)
        return False

    # 1. Zorunlu alan kontrolü
    required_keys = ["schema_version", "generated_at", "source_git_commit", "locales", "summary", "locale_breakdown", "integrity_checksums"]
    for k in required_keys:
        if k not in manifest:
            print(f"❌ Hata: Manifest zorunlu alan eksik: '{k}'", file=sys.stderr)
            return False

    # 2. Şema ve kaynak kimliği
    if manifest.get("schema_version") != "1.1.0":
        print(f"❌ Hata: desteklenen manifest şeması 1.1.0 olmalı: {manifest.get('schema_version')}", file=sys.stderr)
        return False
    source_commit = manifest.get("source_git_commit")
    if source_commit != "unknown" and not re.fullmatch(r"[0-9a-f]{40}", str(source_commit)):
        print(f"❌ Hata: source_git_commit geçerli bir SHA değil: {source_commit}", file=sys.stderr)
        return False

    summary = manifest.get("summary", {})
    required_summary_keys = [
        "discover_tools_count",
        "dictionary_terms_count",
        "report_file_variants_count",
        "canonical_report_dates_count",
        "fresh_report_pages_count",
        "report_pdf_file_variants_count",
        "total_html_pages",
    ]
    for key in required_summary_keys:
        if key not in summary:
            print(f"❌ Hata: Manifest summary alanı eksik: '{key}'", file=sys.stderr)
            return False

    tools_count = summary.get("discover_tools_count", 0)
    terms_count = summary.get("dictionary_terms_count", 0)
    total_html = summary.get("total_html_pages", 0)

    if tools_count < MIN_TOOLS:
        print(f"❌ Hata: Keşif araç sayısı çok düşük ({tools_count} < {MIN_TOOLS})!", file=sys.stderr)
        return False

    if terms_count < MIN_TERMS:
        print(f"❌ Hata: Sözlük terim sayısı çok düşük ({terms_count} < {MIN_TERMS})!", file=sys.stderr)
        return False

    if total_html < MIN_TOTAL_HTML:
        print(f"❌ Hata: Toplam HTML sayfa sayısı çok düşük ({total_html} < {MIN_TOTAL_HTML})!", file=sys.stderr)
        return False

    # 3. Diller ve Parite kontrolü
    expected_locales = ["tr", "en", "fr", "pt", "es", "de"]
    actual_locales = manifest.get("locales", [])
    if set(expected_locales) != set(actual_locales):
        print(f"❌ Hata: Dil listesi uyuşmuyor: Beklenen {expected_locales}, gelen {actual_locales}", file=sys.stderr)
        return False

    breakdown = manifest.get("locale_breakdown", {})
    translated_locales = [loc for loc in expected_locales if loc != "tr"]
    for loc in expected_locales:
        if loc not in breakdown:
            print(f"❌ Hata: '{loc}' dili için kırılım verisi eksik!", file=sys.stderr)
            return False
        st = breakdown[loc]
        if st.get("dictionary_html", 0) < MIN_TERMS - 50:
            print(f"❌ Hata: '{loc}' dilinde sözlük HTML sayısı eksik: {st.get('dictionary_html')}", file=sys.stderr)
            return False
        if st.get("discover_html", 0) < MIN_TOOLS - 50:
            print(f"❌ Hata: '{loc}' dilinde keşif HTML sayısı eksik: {st.get('discover_html')}", file=sys.stderr)
            return False

    # 4. Manifest sayımları disk ile birebir aynı olmalı.
    expected_total = 0
    for loc in expected_locales:
        loc_dir = ROOT if loc == "tr" else os.path.join(ROOT, loc)
        actual = {
            "dictionary_html": count_html_in_dir(os.path.join(loc_dir, "dictionary")),
            "discover_html": count_html_in_dir(os.path.join(loc_dir, "discover")),
            "reports_html": count_html_in_dir(os.path.join(loc_dir, "reports")),
            "total_html": count_html_in_dir(loc_dir, translated_locales) if loc == "tr" else count_html_in_dir(loc_dir),
        }
        expected_total += actual["total_html"]
        if breakdown[loc] != actual:
            print(f"❌ Hata: '{loc}' locale kırılımı disk ile uyuşmuyor: Manifest={breakdown[loc]}, Disk={actual}", file=sys.stderr)
            return False
    if total_html != expected_total:
        print(f"❌ Hata: toplam HTML sayısı disk ile uyuşmuyor: Manifest={total_html}, Disk={expected_total}", file=sys.stderr)
        return False

    reports_json = glob.glob(os.path.join(ROOT, "reports", "*.json"))
    actual_report_variants = len(reports_json)
    actual_canonical_dates = sum(
        1 for path in reports_json if CANONICAL_REPORT_RE.fullmatch(os.path.basename(path))
    )
    reports_pdf = glob.glob(os.path.join(ROOT, "reports", "*.pdf"))
    actual_fresh = count_fresh_report_pages(os.path.join(ROOT, "reports", "tekrarsiz"))
    if summary.get("report_file_variants_count") != actual_report_variants:
        print(f"❌ Hata: rapor dosya varyantı sayısı disk ile uyuşmuyor: Manifest={summary.get('report_file_variants_count')}, Disk={actual_report_variants}", file=sys.stderr)
        return False
    if summary.get("canonical_report_dates_count") != actual_canonical_dates:
        print(f"❌ Hata: canonical rapor tarihi sayısı disk ile uyuşmuyor: Manifest={summary.get('canonical_report_dates_count')}, Disk={actual_canonical_dates}", file=sys.stderr)
        return False
    if summary.get("fresh_report_pages_count") != actual_fresh:
        print(f"❌ Hata: tekrarsız rapor sayfası sayısı disk ile uyuşmuyor: Manifest={summary.get('fresh_report_pages_count')}, Disk={actual_fresh}", file=sys.stderr)
        return False
    if summary.get("report_pdf_file_variants_count") != len(reports_pdf):
        print(f"❌ Hata: PDF dosya varyantı sayısı disk ile uyuşmuyor: Manifest={summary.get('report_pdf_file_variants_count')}, Disk={len(reports_pdf)}", file=sys.stderr)
        return False

    # 5. Checksum bütünlük doğrulaması
    checksums = manifest.get("integrity_checksums", {})
    if sha256_file(MANIFEST_PATH) != sha256_file(ASSETS_MANIFEST_PATH):
        print("❌ Hata: kök ve assets content-manifest.json içerikleri farklı!", file=sys.stderr)
        return False

    for rel_path, expected_hash in checksums.items():
        full_path = os.path.join(ROOT, rel_path)
        if not os.path.isfile(full_path):
            print(f"❌ Hata: Checksum hedef dosyası diskte yok: {rel_path}", file=sys.stderr)
            return False
        current_hash = sha256_file(full_path)
        if current_hash != expected_hash:
            print(f"❌ Hata: SHA-256 bütünlük uyuşmazlığı ({rel_path}): Manifest={expected_hash}, Disk={current_hash}", file=sys.stderr)
            return False

    print(f"✅ content-manifest guard başarılı: {total_html} sayfa, {tools_count} araç, {terms_count} terim, {len(checksums)} SHA-256 dosyası doğrulandı.")
    return True

def main():
    if not check_manifest():
        sys.exit(1)

if __name__ == "__main__":
    main()
