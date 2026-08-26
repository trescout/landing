#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · E-Ink Ekran Veri Üreticisi (E-Paper Payload Generator)
================================================================
Günlük teknoloji raporunu ve öne çıkan 3 açık kaynak aracını mikrodenetleyicilerin
(ESP32 / Raspberry Pi Pico) düşük bellekli E-Ink ekranlarında render edebileceği
ultra hafif JSON formatına dönüştürür.

Kullanım:
    python3 scripts/generate-eink-payload.py [--output assets/api/eink-daily.json]
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "reports")
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
OUTPUT_PATH = os.path.join(ROOT, "assets", "api", "eink-daily.json")


def get_latest_report_date():
    if not os.path.isdir(REPORTS_DIR):
        return None
    dates = [d for d in os.listdir(REPORTS_DIR) if re.match(r"^\d{4}-\d{2}-\d{2}$", d)]
    return sorted(dates, reverse=True)[0] if dates else None


def main():
    parser = argparse.ArgumentParser(description="TreScout E-Ink Payload Generator")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    tarih = get_latest_report_date()
    if not tarih:
        print("Hata: Rapor bulunamadı.")
        sys.exit(1)

    rapor_yolu = os.path.join(REPORTS_DIR, tarih, "index.html")
    with open(rapor_yolu, "r", encoding="utf-8") as f:
        html = f.read()

    # Başlık & Editorial
    title_m = re.search(r'<h1 class="rep-title">(.*?)</h1>', html)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else tarih

    editorial_m = re.search(r'<p class="rep-editorial">(.*?)</p>', html)
    editorial = re.sub(r'<[^>]+>', '', editorial_m.group(1)).strip() if editorial_m else ""
    editorial_short = editorial[:140] + "..." if len(editorial) > 140 else editorial

    # Araçlar
    tools = []
    for m in re.finditer(r'<a class="rep-link-item" href="/discover/([^/]+)/">([^<]+)</a>', html):
        slug = m.group(1)
        name = m.group(2).replace("→", "").strip()
        tools.append({"slug": slug, "name": name})

    # Katalogdan detayları çek
    catalog = {}
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            for item in json.load(f):
                catalog[item.get("slug")] = item

    top_items = []
    for t in tools[:3]:
        cat_item = catalog.get(t["slug"], {})
        top_items.append({
            "name": t["name"],
            "stars": f"★ {cat_item.get('stars', 0):,}".replace(",", "."),
            "summary": (cat_item.get("tagline", "")[:60] + "...") if len(cat_item.get("tagline", "")) > 60 else cat_item.get("tagline", ""),
            "cmd": (cat_item.get("cmds", {}).get("kurulum", [{}])[0].get("komut", "").split("\n")[0]) if isinstance(cat_item.get("cmds"), dict) else ""
        })

    payload = {
        "device_target": "Waveshare 2.9inch / 4.2inch E-Paper",
        "date": tarih,
        "display_date": title,
        "refresh_interval_sec": 86400,
        "editorial": editorial_short,
        "top_tools": top_items,
        "qr_url": f"https://trescout.com/reports/{tarih}/",
        "generated_at": datetime.now().isoformat()
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ E-Ink verisi üretildi: {args.output}")
    print(f"   Tarih: {tarih} · Öne çıkan araç sayısı: {len(top_items)}")


if __name__ == "__main__":
    main()
