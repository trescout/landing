#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · NFC Smart Puck NDEF Üreticisi
=======================================
Fiziksel NFC NTAG213/215 etiketleri ve akıllı masaüstü diskleri için standart
NDEF URI ve MIME kayıt yüklerini üretir.

Kullanım:
    python3 scripts/generate-nfc-ndef.py [--output assets/api/nfc-ndef.json]
"""

import os
import sys
import json
import argparse
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "assets", "api", "nfc-ndef.json")


def generate_ndef_payload():
    today_str = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "tag_type": "NFC Forum Type 2 / NTAG213 / NTAG215",
        "action": "instant_audio_briefing",
        "ndef_records": [
            {
                "record_type": "url",
                "uri": f"https://trescout.com/reports/?autoplay=audio&utm_source=nfc_puck&date={today_str}",
                "description": "Dokunulduğunda doğrudan günün 1 dakikalık sesli bültenini başlatır."
            },
            {
                "record_type": "mime",
                "media_type": "application/vnd.trescout.briefing+json",
                "data": {
                    "source": "TreScout Smart Puck v1",
                    "protocol": "touch_to_brief",
                    "date": today_str
                }
            }
        ],
        "generated_at": datetime.now().isoformat()
    }
    return payload


def main():
    parser = argparse.ArgumentParser(description="TreScout NFC NDEF Generator")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    payload = generate_ndef_payload()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ NFC NDEF kaydı üretildi: {args.output}")
    print(f"   Hedef URI: {payload['ndef_records'][0]['uri']}")


if __name__ == "__main__":
    main()
