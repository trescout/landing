#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Sosyal Medya İnfografik Üreticisi (Weekly Social Asset Generator)
===========================================================================
Haftanın en çok öne çıkan 5 açık kaynak projesini alarak 1200x630px boyutunda
sosyal medya (X / LinkedIn) uyumlu şık bir vektörel infografik (SVG/Web) üretir.

Kullanım:
    python3 scripts/generate-weekly-infographic.py [--output assets/infographics/haftalik.svg]
"""

import os
import sys
import json
import html
import argparse
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(ROOT, "assets", "discover", "catalog.json")
OUTPUT_DIR = os.path.join(ROOT, "assets", "infographics")


def esc(s):
    return html.escape(s or "", quote=True)


def load_top_tools(limit=5):
    if not os.path.exists(CATALOG_PATH):
        return []
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Sıralama: En yüksek yıldız veya en son güncelleme
    sorted_tools = sorted(data, key=lambda x: x.get("stars", 0), reverse=True)
    return sorted_tools[:limit]


def generate_svg_infographic(tools, title="Haftanın Öne Çıkan Açık Kaynak Projeleri", date_str=None):
    if not date_str:
        date_str = datetime.now().strftime("%d %B %Y")

    W = 1200
    H = 630

    cards_svg = []
    card_w = 540
    card_h = 130

    positions = [
        (60, 150),   # 1. Kart (Sol üst)
        (620, 150),  # 2. Kart (Sağ üst)
        (60, 300),   # 3. Kart (Sol orta)
        (620, 300),  # 4. Kart (Sağ orta)
        (60, 450)    # 5. Kart (Sol alt - geniş)
    ]

    for idx, (tool, (x, y)) in enumerate(zip(tools, positions)):
        t_name = esc(tool.get("title", ""))
        t_stars = f"★ {tool.get('stars', 0):,}".replace(",", ".")
        t_desc = esc(tool.get("tagline", "")[:85] + "..." if len(tool.get("tagline", "")) > 85 else tool.get("tagline", ""))
        t_tag = esc(tool.get("tags", ["Açık Kaynak"])[0] if tool.get("tags") else "Açık Kaynak")

        card_width = 1080 if idx == 4 else card_w

        card = f"""
        <g transform="translate({x}, {y})">
          <rect width="{card_width}" height="{card_h}" rx="14" fill="#ffffff" stroke="#E2E8F0" stroke-width="1.5" />
          <circle cx="34" cy="36" r="16" fill="#1B4965" />
          <text x="34" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">{idx+1}</text>
          
          <text x="62" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="bold" fill="#1B4965">{t_name}</text>
          <rect x="{card_width - 110}" y="20" width="95" height="26" rx="13" fill="#FEF3C7" />
          <text x="{card_width - 62}" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="bold" fill="#92400E" text-anchor="middle">{t_stars}</text>
          
          <text x="24" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#475569">{t_desc}</text>
          
          <rect x="24" y="96" width="{len(t_tag)*9 + 18}" height="20" rx="6" fill="#F1F5F9" />
          <text x="33" y="110" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#64748B">{t_tag}</text>
        </g>
        """
        cards_svg.append(card)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#EDF2F7"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1B4965"/>
      <stop offset="100%" stop-color="#2B6CB0"/>
    </linearGradient>
  </defs>

  <!-- Arka Plan -->
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  
  <!-- Üst Dekoratif Çizgi -->
  <rect width="{W}" height="6" fill="url(#headerGrad)"/>

  <!-- Başlık & Logo Bloğu -->
  <g transform="translate(60, 45)">
    <!-- Logo İkonu -->
    <rect x="0" y="0" width="48" height="48" rx="12" fill="#1B4965"/>
    <path d="M 10 27 A 14 14 0 0 1 38 27" fill="none" stroke="#5FA8D3" stroke-width="2" opacity="0.4" stroke-linecap="round"/>
    <path d="M 15 27 A 9 9 0 0 1 33 27" fill="none" stroke="#5FA8D3" stroke-width="2" opacity="0.75" stroke-linecap="round"/>
    <rect x="10" y="27" width="28" height="5" rx="1" fill="#F4D35E"/>
    <rect x="21.5" y="27" width="5" height="13" rx="1" fill="#F4D35E"/>
    
    <text x="62" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="900" fill="#1B4965" letter-spacing="-0.5px">TreScout</text>
    <text x="185" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="700" fill="#64748B">· {esc(title)}</text>
    <text x="{W - 180}" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="600" fill="#94A3B8" text-anchor="end">{esc(date_str)}</text>
  </g>

  <!-- Kartlar -->
  {''.join(cards_svg)}

  <!-- Alt Bilgi / Footer -->
  <g transform="translate(60, 600)">
    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#64748B">🌐 Tüm projeleri ve günlük teknoloji bültenini inceleyin: <tspan fill="#1B4965" font-weight="bold">trescout.com</tspan></text>
    <text x="{W - 120}" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="bold" fill="#1B4965" text-anchor="end">@GetTreScout</text>
  </g>
</svg>"""

    return svg


def main():
    parser = argparse.ArgumentParser(description="TreScout Sosyal Medya İnfografik Üreticisi")
    parser.add_argument("--output", help="Çıktı dosya yolu (varsayılan: assets/infographics/haftalik-ozet.svg)")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = args.output or os.path.join(OUTPUT_DIR, "haftalik-ozet.svg")

    tools = load_top_tools(5)
    if not tools:
        print("Hata: Katalogdan araçlar yüklenemedi.")
        sys.exit(1)

    svg_content = generate_svg_infographic(tools)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ İnfografik başarıyla üretildi: {out_path}")
    print(f"   Boyut: 1200x630px · Vektörel SVG (Sosyal Medya Standart)")


if __name__ == "__main__":
    main()
