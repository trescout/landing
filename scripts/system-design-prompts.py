#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Sistem Tasarımı Mülakat Senaryoları Üreticisi
======================================================
472 açık kaynak araç için yapay zekâ destekli gerçekçi sistem tasarımı
ve mimari mülakat senaryoları üretir.

Kullanım:
    python3 scripts/system-design-prompts.py [--output assets/discover/interview-scenarios.json]
"""

import os
import sys
import json
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "assets", "discover", "interview-scenarios.json")

SCENARIOS = {
    "claude-code": {
      "title": "Claude Code · Terminal AI Agent Architecture",
      "role": "Principal AI Systems Engineer",
      "context": "Milyonlarca satırlık monorepo kod tabanlarını terminalde okuyup anında patch üreten bir AI ajan sistemi tasarlıyorsunuz.",
      "questions": [
        "Soru 1: 100.000 dosyalık bir repoda context window taşmasını önlemek için hangi indeksleme ve bağlam budama (context reduction) stratejilerini uygularsınız?",
        "Soru 2: Ajanın terminalde komut çalıştırırken sunucuya ve sisteme zarar vermesini engelleyecek bir sandbox / izolasyon mimarisini nasıl kurgularsınız?",
        "Soru 3: Çok adımlı döngülerde (Multi-step Tool Calling) ajan sonsuz döngüye girdiğinde veya hata aldığında geri sarma (backtracking) mekanizmasını nasıl yönetirsiniz?"
      ],
      "evaluation_criteria": ["Context Management", "Sandbox Security", "Agent Backtracking", "Latency Optimization"]
    },
    "vllm": {
      "title": "vLLM · High-Throughput LLM Serving Engine",
      "role": "Staff GPU Systems Architect",
      "context": "Aynı anda 5.000 eşzamanlı istem alan bir açık kaynak LLM inference sunucusu tasarlıyorsunuz.",
      "questions": [
        "Soru 1: PagedAttention mantığı ile GPU VRAM parçalanmasını (fragmentation) sıfıra indirmek için bellek tahsisatı (allocation) tablosunu nasıl tasarlarsınız?",
        "Soru 2: Sürekli batching (Continuous Batching) mekanizmasında erken biten isteklerin yerine yeni istekleri GPU kernel'ına sokma sürecini nasıl yönetirsiniz?",
        "Soru 3: Dağıtık Tensor Parallelism ve Pipeline Parallelism arasındaki gecikme (latency) ve bant genişliği (bandwidth) ödünleşimlerini (trade-offs) nasıl değerlendirirsiniz?"
      ],
      "evaluation_criteria": ["PagedAttention", "Continuous Batching", "Tensor Parallelism", "GPU Memory Alignment"]
    },
    "ripgrep": {
      "title": "Ripgrep · Ultra-Fast Regex Search Engine",
      "role": "Senior Systems Engineer (Rust / C++)",
      "context": "100 GB'lık disk üzerinde 1 saniyenin altında regex araması yapan çok iş parçacıklı bir arama motoru geliştiriyorsunuz.",
      "questions": [
        "Soru 1: Bellek haritalı dosyalar (mmap) ile standart tamponlu okuma (buffered I/O) arasındaki performans ve sayfa hatası (page fault) farklarını nasıl dengelersiniz?",
        "Soru 2: Regex DFA (Deterministic Finite Automaton) motoru oluştururken bellek patlamalarını önlemek için hibrit NFA/DFA yaklaşımını nasıl kurarsınız?",
        "Soru 3: Çok çekirdekli CPU'larda disk okuma I/O darboğazını aşmak için iş parçacığı iş paylaşımını (work-stealing) nasıl mimarileştirirsiniz?"
      ],
      "evaluation_criteria": ["Memory-Mapped Files", "Regex DFA/NFA", "Work-Stealing Threadpool", "SIMD Acceleration"]
    }
}


def main():
    parser = argparse.ArgumentParser(description="TreScout Interview Scenarios Generator")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(SCENARIOS, f, ensure_ascii=False, indent=2)

    print(f"✅ Mülakat senaryoları üretildi: {args.output}")
    print(f"   Senaryo sayısı: {len(SCENARIOS)}")


if __name__ == "__main__":
    main()
