#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Topluluk Sözlük Terimi İçe Aktarıcısı (Community Term Importer)
========================================================================
GitHub Issue veya PR'dan gelen onaylanmış bir topluluk terimini doğrulayıp
assets/dictionary/dictionary.json dosyasına ekler.

Kullanım:
    python3 scripts/import-community-term.py --slug "vector-search" --en "Vector Search" --cat "ai" --kisa "Metin ve verileri anlamsal benzerliklerine göre arama yöntemidir."
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICTIONARY_PATH = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")


def slugify(text):
    text = (text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_]+", "-", text)


def main():
    parser = argparse.ArgumentParser(description="TreScout Community Term Importer")
    parser.add_argument("--slug", help="Terim slug'ı (belirtilmezse --en adından üretilir)")
    parser.add_argument("--en", required=True, help="Terim İngilizce/Global adı")
    parser.add_argument("--full", default="", help="Terim tam açılımı (varsa)")
    parser.add_argument("--cat", default="ai", choices=["ai", "dev", "arch", "db", "sec", "cloud", "genel"], help="Kategori")
    parser.add_argument("--kisa", required=True, help="Kısa Türkçe tanım")
    parser.add_argument("--kisa_en", default="", help="Kısa İngilizce tanım (opsiyonel)")
    args = parser.parse_args()

    slug = args.slug or slugify(args.en)
    if not slug:
        print("Hata: Geçerli bir slug üretilemedi.")
        sys.exit(1)

    if not os.path.exists(DICTIONARY_PATH):
        print(f"Hata: Sözlük dosyası bulunamadı: {DICTIONARY_PATH}")
        sys.exit(1)

    with open(DICTIONARY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Çift kayıt kontrolü
    for item in data:
        if item.get("slug") == slug:
            print(f"⚠️ Uyarı: '{slug}' zaten sözlükte mevcut. Güncelleniyor...")
            item["en"] = args.en
            if args.full:
                item["full"] = args.full
            item["cat"] = args.cat
            item["kisa"] = args.kisa
            if args.kisa_en:
                item["kisa_en"] = args.kisa_en
            break
    else:
        new_entry = {
            "slug": slug,
            "en": args.en,
            "full": args.full,
            "cat": args.cat,
            "kisa": args.kisa,
            "kisa_en": args.kisa_en or args.kisa,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "community_contributed": True
        }
        data.append(new_entry)
        print(f"✅ Yeni topluluk terimi eklendi: {args.en} ({slug})")

    with open(DICTIONARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("💾 dictionary.json başarıyla güncellendi.")


if __name__ == "__main__":
    main()
