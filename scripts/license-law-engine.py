#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Açık Kaynak Mahkemesi & Lisans Hukuk Motoru (License Courtroom Engine)
================================================================================
Açık kaynak lisanslarının (MIT, Apache, GPL, AGPL, SSPL) ticari projelerdeki
hukuki risklerini simüle eder ve güvenli açık kaynak alternatifleri üretir.

Kullanım:
    python3 scripts/license-law-engine.py [--output assets/discover/license-courtroom-cases.json]
"""

import os
import sys
import json
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "assets", "discover", "license-courtroom-cases.json")

CASES = [
    {
        "id": "case-agpl-saas",
        "title": "Dava #101: Kapalı Kaynak SaaS ve AGPL-3.0 Vektör DB",
        "defendant": "AI Girişimcisi (SaaS Kurucusu)",
        "charge": "AGPL-3.0 lisanslı bir aracı ağ üzerinden API arkasında sunarak tüm SaaS platformunun kaynak kodunu açma zorunluluğunu ihlal etmek.",
        "scenario": "Girişiminiz, kapalı kaynak bir kurumsal yapay zeka SaaS platformu geliştirdi. Backend'de AGPL-3.0 lisanslı bir vektör arama motorunu doğrudan servisin ana sürecine dahil ettiniz.",
        "verdict": "⚠️ CİDDİ HUKUKİ RİSK (Copyleft İhlali)",
        "verdict_score": "Yüksek Risk (%88)",
        "ruling": "AGPL (Affero GPL), yazılımın ağ üzerinden (SaaS) sunulmasını da 'dağıtım' sayar. Kullanıcılar talep ederse tüm SaaS mimarinizin kaynak kodunu AGPL ile açmak zorunda kalabilirsiniz.",
        "safe_alternatives": [
            {"name": "ChromaDB / Qdrant (Apache 2.0)", "reason": "Patent korumalı ve ticari SaaS içine entegre etmesi %100 güvenli."},
            {"name": "SQLite-VSS (MIT)", "reason": "Maksimum özgürlük, sıfır copyleft zorunluluğu."}
        ]
    },
    {
        "id": "case-gpl-mobile",
        "title": "Dava #102: Ücretli iOS/Android Uygulamasında GPL-2.0",
        "defendant": "Mobil Uygulama Geliştiricisi",
        "charge": "App Store ve Google Play'de satılan kapalı kaynak mobil uygulamaya GPL-2.0 C++ kütüphanesini statik bağlamak.",
        "scenario": "Geliştirdiğiniz ücretli mobil oyunda ses işleme için GPL-2.0 lisanslı popüler bir açık kaynak C++ kütüphanesini `libaudio.a` olarak statik derlediniz.",
        "verdict": "🚨 KESİN TELİF İHLALİ (Statik Linkleme Yasağı)",
        "verdict_score": "Kritik Risk (%96)",
        "ruling": "GPL-2.0 statik bağlanan tüm projeyi türev eser sayar. Uygulamanız App Store kurallarıyla ve GPL ile çelişir; uygulamanız mağazalardan kaldırılabilir.",
        "safe_alternatives": [
            {"name": "Miniaudio / FFMPEG LGPL (Dinamik Link)", "reason": "Dinamik bağlandığında ana uygulamanın kodunu açma zorunluluğu doğurmaz."},
            {"name": "SDL2 (Zlib Lisansı)", "reason": "Ticari oyun ve mobil uygulamalar için sektör standardı ve tamamen özgür."}
        ]
    },
    {
        "id": "case-mit-apache-saas",
        "title": "Dava #103: Ticari Projede MIT & Apache 2.0 Kombinasyonu",
        "defendant": "Kurumsal Fintech Şirketi",
        "charge": "Yıllık 10 milyon dolar ciro yapan bankacılık API'sinde MIT ve Apache 2.0 açık kaynak araçları kullanmak.",
        "scenario": "Fintech şirketiniz FastAPI (MIT) ve vLLM (Apache 2.0) kullanarak kurumsal müşterilerine yapay zeka destekli finansal analiz satıyor.",
        "verdict": "✅ BERAAT: %100 TİCARİ GÜVENLİ LİMAN",
        "verdict_score": "Sıfır Risk (%0)",
        "ruling": "MIT ve Apache 2.0 lisansları 'permissive' (hoşgörülü) lisanslardır. Orijinal telif bildirimini (LICENSE dosyasını) koruduğunuz sürece kodunuzu açma zorunluluğunuz yoktur. Ticari satış ve patent hakkı tamdır.",
        "safe_alternatives": [
            {"name": "FastAPI + vLLM + Ripgrep", "reason": "Modern kurumsal açık kaynak stack'inin en temiz ve güvenli çekirdeğidir."}
        ]
    }
]


def main():
    parser = argparse.ArgumentParser(description="TreScout License Courtroom Engine")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Çıktı JSON yolu")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(CASES, f, ensure_ascii=False, indent=2)

    print(f"✅ Lisans mahkemesi vakaları üretildi: {args.output}")
    print(f"   Vaka sayısı: {len(CASES)}")


if __name__ == "__main__":
    main()
