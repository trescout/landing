# Führen Sie riesige KI-Modelle lokal aus

Colibri ist eine auf C basierende Engine, die es ermöglicht, groß angelegte Mixture-of-Experts-Modelle (MoE) mit geringen Hardwareanforderungen auf lokalen Computern auszuführen. Durch das Streaming von Expertenebenen direkt von der Festplatte ermöglicht es den Betrieb hochkapazitiver KI-Modelle auf Hardware mit begrenzten Ressourcen.

- ★ 27.610
- C
- GitHub Trending · 2026-09-11

## Was es bringt
- Führt hochkapazitive Modelle auf Hardware mit begrenzten Ressourcen aus
- Verwaltet VRAM, RAM und Festplattenspeicher wie eine einzige Ebene
- Sorgt für Effizienz durch Streaming von Expertenebenen

## Installation
**Kompilieren aus Quellcode**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
```


## Ausführung
**Chat-Oberfläche starten**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable  (+ make cuda-dsv4-dg-dll on RTX 50)
```


## Wenn Sie nicht programmieren
Ich möchte groß angelegte KI-Modelle mit der Colibri-Engine auf meinem lokalen Computer ausführen. Helfen Sie mir bei der Konfiguration, um meine Hardwareressourcen (VRAM, RAM und NVMe-Festplatte) so effizient wie möglich zu nutzen. Erklären Sie Schritt für Schritt, wie ich Modelle wie GLM oder DeepSeek basierend auf der Speicherkapazität meines Systems optimieren und ausführen kann.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/colibri/
