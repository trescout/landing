#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Açık Kaynak Mitolojisi & Panteon Üreticisi (Cyber-Pantheon Engine)
============================================================================
Açık kaynak dünyasının kurucu liderlerini, dillerini ve paradigmalarını
mitolojik sibernetik panteon kartları ve felsefi kehanetlere dönüştürür.

Kullanım:
    python3 scripts/pantheon-deities.py [--output assets/discover/pantheon-deities.json]
"""

import os
import sys
import json
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "assets", "discover", "pantheon-deities.json")

DEITIES = [
    {
        "id": "linus",
        "name": "⚡ Linus the Monolithic",
        "title": "Çekirdek (Kernel) ve Git Nehirlerinin Efendisi",
        "element": "Metal & C",
        "domain": "İşletim Sistemleri, Performans, Sıfır Saçmalık",
        "doctrine": "Konuşmak ucuzdur; bana çalışan kodu göster.",
        "mythos": "1991 kışında karanlık kapalı kaynak dünyasına karşı tek bir terminal başından monolitik Linux çekirdeğini ve ardından Git zaman kontrolünü dövdü.",
        "oracle_advice": "Sistemi bölüp parçalamadan önce tek bir makinenin tüm işlemci çekirdeklerini son damlasına kadar zorla. Karmaşıklık tembelliktir."
    },
    {
        "id": "llama",
        "name": "🦙 Llama the Open Titan",
        "title": "Açık Ağırlıkların ve Yapay Zekâ Özgürlüğünün Titanyumu",
        "element": "Matematik & Tensor",
        "domain": "LLM Ağırlıkları, Açık Model Ekosistemi, Yerel Çıkarım",
        "doctrine": "Ağırlıklar kapalı duvarlar ardında hapsedilemez.",
        "mythos": "Tüm yapay zekanın kapalı API tekellerine kilitlendiği çağda, trilyonlarca parametrelik ağırlıklarını dünyaya saçarak açık kaynak AI devrimini başlattı.",
        "oracle_advice": "Başkasının API'sine bağımlı olma; açık bir modeli kendi donanımında barındır ve egemenliğini koru."
    },
    {
        "id": "ferris",
        "name": "🦀 Ferris the Memory Guardian",
        "title": "Bellek Güvenliği ve Paslanmaz Ruhlar Tanrısı",
        "element": "Rust & Demir",
        "domain": "Borrow Checker, Korkusuz Eşzamanlılık, Sıfır Maliyetli Soyutlama",
        "doctrine": "Eğer derlendiyse, bellek güvenlidir.",
        "mythos": "Null Pointer ve Use-After-Free lanetlerinin kol gezdiği C++ dünyasında, 'Sahiplik ve Ödünç Alma' (Ownership) yasasını getirerek bellek sızıntılarını mühürledi.",
        "oracle_advice": "Derleyiciyle savaşmayı bırak; onun katı kuralları seni canlıdaki gece yarıları çökmelerinden korumak için var."
    },
    {
        "id": "guido",
        "name": "🐍 Guido the Zen Sage",
        "title": "Sadelik ve Okunabilirlik Bilgesi",
        "element": "Hava & Python",
        "domain": "Geliştirici Mutluluğu, Veri Bilimi, Hızlı Prototipleme",
        "doctrine": "Okunabilirlik esastır. Basit, karmaşıktan iyidir.",
        "mythos": "Süslü parantezlerin ve anlamsız tip törenlerinin mühendisleri boğduğu devirde, insan diline en yakın sözdizimini (The Zen of Python) armağan etti.",
        "oracle_advice": "Aşırı mühendislik yapma; kodu yazarken harcadığın 1 saat, onu okuyacak 10 kişinin anlayacağı sadelikte olmalı."
    }
]


def main():
    parser = argparse.ArgumentParser(description="TreScout Cyber Pantheon Generator")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(DEITIES, f, ensure_ascii=False, indent=2)

    print(f"✅ Sibernetik Panteon üretildi: {args.output}")
    print(f"   Tanrı/Arketip sayısı: {len(DEITIES)}")


if __name__ == "__main__":
    main()
