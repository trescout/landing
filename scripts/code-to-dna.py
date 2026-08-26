#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · Kodu Biyolojik DNA Dizilimine Dönüştürücü (Code-to-DNA Synthesizer)
=============================================================================
Açık kaynak yazılımların kaynak kodlarını sentetik biyolojik DNA baz çiftlerine
(A, T, C, G) ve 10.000 yıllık moleküler veri saklama standardı olan FASTA
formatına dönüştürür.

Kullanım:
    python3 scripts/code-to-dna.py [--input scripts/code-to-dna.py] [--output assets/bio/code.fasta]
"""

import os
import sys
import argparse

MAP_2BIT_TO_DNA = {
    "00": "A",  # Adenin
    "01": "C",  # Sitozin
    "10": "G",  # Guanin
    "11": "T"   # Timin
}


def encode_bytes_to_dna(data_bytes):
    dna_seq = []
    for b in data_bytes:
        bits = f"{b:08b}"
        for i in range(0, 8, 2):
            pair = bits[i:i+2]
            dna_seq.append(MAP_2BIT_TO_DNA[pair])
    return "".join(dna_seq)


def calculate_gc_content(dna_str):
    if not dna_str:
        return 0.0
    g_count = dna_str.count("G")
    c_count = dna_str.count("C")
    return round(((g_count + c_count) / len(dna_str)) * 100, 2)


def generate_fasta(title, dna_str):
    gc = calculate_gc_content(dna_str)
    length = len(dna_str)
    lines = [f">TreScout_BioVault_{title} | BasePairs={length}bp | GC_Content={gc}% | Target=Synthetic_DNA_Storage"]

    # FASTA standardı: Her satırda 80 nükleotit
    for i in range(0, length, 80):
        lines.append(dna_str[i:i+80])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="TreScout Code to DNA Synthesizer")
    parser.add_argument("--code", default="fn main() { println!(\"Hello, TreScout Biological DNA!\"); }", help="Kod metni")
    parser.add_argument("--title", default="Ripgrep_Core", help="Proje başlığı")
    parser.add_argument("--output", help="Çıktı FASTA dosyası yolu")
    args = parser.parse_args()

    raw_bytes = args.code.encode("utf-8")
    dna_sequence = encode_bytes_to_dna(raw_bytes)
    fasta_content = generate_fasta(args.title, dna_sequence)

    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(fasta_content)
        print(f"✅ FASTA dosyası üretildi: {args.output}")
    else:
        print("🧬 DÖNÜŞTÜRÜLEN DNA DİZİLİMİ:")
        print(fasta_content[:300] + "...\n")

    print(f"📊 Metrikler: {len(dna_sequence)} Baz Çifti (bp) · GC Oranı: %{calculate_gc_content(dna_sequence)}")


if __name__ == "__main__":
    main()
