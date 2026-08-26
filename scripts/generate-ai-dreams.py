#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Yapay Zekâ Gece Kod Rüyaları (AI REM Sleep Dreams Generator)
======================================================================
Her gece saat 04:00'te yapay zekanın REM uykusuna dalarak açık kaynak araçları
birbirine bağladığı gerçeküstü teknoloji rüyalarını üretir.

Kullanım:
    python3 scripts/generate-ai-dreams.py [--output assets/discover/ai-dreams.json]
"""

import os
import sys
import json
import argparse
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "assets", "discover", "ai-dreams.json")

DREAMS = [
    {
        "id": "dream-401",
        "time": "04:12 AM (REM Evresi 4)",
        "title": "Nöro-Optik Rust Terminali",
        "synthesized_from": ["Claude Code", "Ripgrep", "WebGPU"],
        "lucidity_score": "%96 (Yüksek Bilinçlilik)",
        "surreal_concept": "Klavye ve ekrandan tamamen arınmış bir geliştirici ortamı. Mühendisin göz bebeklerinin odaklandığı bellek blokları anında Ripgrep SIMD algoritmalarıyla taranıyor; Claude Code ajanları düşünce hızında Rust borrow-checker kontrollerini arka planda sessizce tamamlıyor.",
        "quote": "Derleyici artık konuşmuyor; sadece gözlerimizin içine bakarak belleğin güvenli olduğunu onaylıyor."
    },
    {
        "id": "dream-402",
        "time": "04:38 AM (Derin Teta Dalgası)",
        "title": "Otonom Biyolojik Mikroservis Ormanı",
        "synthesized_from": ["Maka", "TradingAgents", "Synthetic DNA"],
        "lucidity_score": "%88 (Gerçeküstü Sentez)",
        "surreal_concept": "Dağıtık mikroservisler artık sunucularda değil, biyolojik bir mantar ağı (mycelium) üzerinde koşuyor. Her API çağrısı hücre bölünmesiyle gerçekleşiyor; TradingAgents piyasa stresine göre sunucuların DNA baz dizilimlerini anlık mutasyona uğratarak latency'yi sıfıra indiriyor.",
        "quote": "Sunucularımızı sulamayı unuttuğumuzda hata oranı hafifçe yükseliyor."
    },
    {
        "id": "dream-403",
        "time": "04:55 AM (Uyanış Öncesi Lucid REM)",
        "title": "Zamanın Ötesinde PagedAttention Havuzu",
        "synthesized_from": ["vLLM", "Code Graph RAG", "Whisper"],
        "lucidity_score": "%99 (Kozmik Berraklık)",
        "surreal_concept": "Henüz yazılmamış kodların çıkarımını (inference) önceden tahmin edip GPU VRAM'ine yükleyen nedensellik-ötesi (retrocausal) bellek havuzu. Siz fonksiyon adını fısıldadığınız anda çıktı 3 saniye öncesinden ekrana basılmış oluyor.",
        "quote": "Cevap sorudan önce geldiğinde, debug etmek bir hatıraya dönüşür."
    }
]


def main():
    parser = argparse.ArgumentParser(description="TreScout AI Dreams Generator")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(DREAMS, f, ensure_ascii=False, indent=2)

    print(f"✅ Yapay Zeka Rüyaları üretildi: {args.output}")
    print(f"   Rüya sayısı: {len(DREAMS)}")


if __name__ == "__main__":
    main()
