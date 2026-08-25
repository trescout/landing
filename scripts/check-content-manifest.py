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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "content-manifest.json")
ASSETS_MANIFEST_PATH = os.path.join(ROOT, "assets", "content-manifest.json")

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
    required_keys = ["schema_version", "generated_at", "git_commit", "locales", "summary", "locale_breakdown", "integrity_checksums"]
    for k in required_keys:
        if k not in manifest:
            print(f"❌ Hata: Manifest zorunlu alan eksik: '{k}'", file=sys.stderr)
            return False

    # 2. Asgari eşik kontrolleri
    summary = manifest.get("summary", {})
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

    # 4. Checksum bütünlük doğrulaması
    checksums = manifest.get("integrity_checksums", {})
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
