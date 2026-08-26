#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Kod Bilinçaltı Analizcisi (Code Psychoanalyst Engine)
==============================================================
Karmaşık veya spagetti kodları analiz ederek yazan mühendisin bilinçaltı
kaygılarını ve psikolojik ruh halini esprili bir dille teşhis eder.

Kullanım:
    python3 scripts/analyze-code-trauma.py [--file path/to/messy_code.js]
"""

import sys
import re
import argparse


def psychoanalyze_code(code_str):
    lines = code_str.splitlines()
    total_lines = len(lines)

    nested_ifs = len(re.findall(r'\bif\b', code_str))
    try_catches = len(re.findall(r'\btry\b', code_str))
    any_types = len(re.findall(r'\bany\b', code_str))
    todos = len(re.findall(r'TODO|FIXME|HACK', code_str, re.IGNORECASE))
    comments = len([l for l in lines if l.strip().startswith("//") or l.strip().startswith("#")])

    # Psikolojik Metrik Hesaplamaları
    paranoia_score = min(98, max(20, nested_ifs * 12 + try_catches * 8))
    anxiety_score = min(95, max(30, todos * 15 + (100 if any_types > 3 else 20)))
    burnout_score = min(90, max(15, int(total_lines / 3) + 20))

    diagnosis = []
    if nested_ifs >= 4:
        diagnosis.append("İç içe geçmiş çok sayıda if bloğu: Geliştiricinin geçmişte beklenmeyen bir `null pointer` travması yaşadığını ve evrene karşı derin bir güvensizlik beslediğini gösteriyor.")
    if any_types >= 2:
        diagnosis.append("`any` tipi kullanımı: Tip denetiminden kaçış, kurallara başkaldırı ve teslim tarihinin acımasız baskısı altında benliğini kaybetme belirtisi.")
    if todos >= 1:
        diagnosis.append("TODO / HACK yorumları: 'Bir ara düzeltirim' diyerek sorumluluğu gelecekteki benliğine devreden klasik erteleme (procrastination) savunma mekanizması.")

    if not diagnosis:
        diagnosis.append("Kod nispeten sakin görünüyor ancak yüzeyin altında gizli bir mükemmeliyetçilik ve sessiz bir kontrol arzusu seziliyor.")

    prescription = {
        "recommended_tool": "Zod / Valibot & Claude Code",
        "therapy_note": "Gelen veriyi kapıda tek satırda doğrulayın (schema parsing) ve iç içe if cehennemine son vererek zihninize huzur kazandırın."
    }

    return {
        "paranoia_score": f"%{paranoia_score}",
        "anxiety_score": f"%{anxiety_score}",
        "burnout_score": f"%{burnout_score}",
        "diagnosis": diagnosis,
        "prescription": prescription
    }


def main():
    sample_code = """
    function handleUserData(data) {
      // TODO: burayı refactor et
      if (data) {
        if (data.user) {
          if (data.user.profile) {
            if (data.user.profile.age > 18) {
              try {
                let x: any = data.user.token;
                return x.trim();
              } catch(e) {}
            }
          }
        }
      }
      return null;
    }
    """
    res = psychoanalyze_code(sample_code)
    print("🧠 KOD BİLİNÇALTI TEŞHİS RAPORU:")
    print(f"   Edge-Case Paranoyası: {res['paranoia_score']}")
    print(f"   Canlıya Çıkış Anksiyetesi: {res['anxiety_score']}")
    print(f"   Tükenmişlik Seviyesi: {res['burnout_score']}")
    print("   Teşhis:", " ".join(res['diagnosis']))
    print(f"   Reçete: {res['prescription']['recommended_tool']} — {res['prescription']['therapy_note']}")


if __name__ == "__main__":
    main()
