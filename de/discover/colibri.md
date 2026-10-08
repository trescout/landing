# Führen Sie riesige KI-Modelle lokal aus

Colibri ist eine auf C basierende Engine, die es ermöglicht, groß angelegte Mixture-of-Experts-Modelle (MoE) mit geringen Hardwareanforderungen auf lokalen Computern auszuführen. Durch das Streaming von Expertenebenen direkt von der Festplatte ermöglicht es den Betrieb hochkapazitiver KI-Modelle auf Hardware mit begrenzten Ressourcen.

- ★ 40.157
- C
- GitHub Trending · 2026-09-11

## Aktualisierungen

- **7. Oktober 2026:** Sterne 39,698 → 40,157, neueste Version v2.0.0 (6. Oktober 2026).
- **5. Oktober 2026:** Sterne 37,791 → 39,698, neueste Version v1.12.1 (24. September 2026).
- **27. September 2026:** Sterne 36,260 → 37,791, neueste Version v1.12.1 (24. September 2026).
- **19. September 2026:** Sterne 34,474 → 36,260, neueste Version v1.11.0 (13. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte groß angelegte KI-Modelle mit der Colibri-Engine auf meinem lokalen Computer ausführen. Helfen Sie mir bei der Konfiguration, um meine Hardwareressourcen (VRAM, RAM und NVMe-Festplatte) so effizient wie möglich zu nutzen. Erklären Sie Schritt für Schritt, wie ich Modelle wie GLM oder DeepSeek basierend auf der Speicherkapazität meines Systems optimieren und ausführen kann.

## Verwandte Begriffe aus dem Glossar

- [Mixture of Experts](https://trescout.com/de/dictionary/mixture-of-experts/)
- [VRAM](https://trescout.com/de/dictionary/vram/)
- [RAM](https://trescout.com/de/dictionary/ram/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Forscher und Entwickler, die große Sprachmodelle mit begrenzten Hardwareressourcen auf ihrem eigenen Computer ausführen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/JustVugg/colibri)
- [Auf Türkisch lesen →](https://trescout.com/discover/colibri/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-11 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/colibri/
