# DeepSeek-Ausführungs-Engine auf nativer Hardware

DS4 wurde von Salvatore Sanfilippo, dem Erfinder von Redis, entwickelt und ist eine Inferenz-Engine, die die Ausführung von DeepSeek-Modellen auf lokaler Hardware ermöglicht. Dieses in C-Sprache geschriebene Tool bietet dank Metal-, CUDA- und ROCm-Unterstützung die Möglichkeit, Hochleistungsmodelle auf verschiedenen Grafikprozessoren auszuführen.

- ★ 23.530
- C
- GitHub Trending · 2026-08-03

## Aktualisierungen

- **5. Oktober 2026:** Sterne 22,197 → 23,530.
- **10. September 2026:** Sterne 21,134 → 22,197.
- **11. August 2026:** Sterne 20,117 → 21,134.

## Was es bringt

- Führt leistungsstarke KI-Modelle auf Consumer-Hardware aus
- Ermöglicht die Modellnutzung auch bei begrenzter Speicherkapazität durch Datenstreaming per SSD
- Ermöglicht die Erstellung eines LLM-Servers auf Unternehmensebene mit Multi-GPU-Unterstützung

## Installation

**Passend zu Ihrer Hardware bauen**

```
make                  # macOS Metal
make cuda-spark       # Linux CUDA, DGX Spark / GB10
make cuda-generic     # Linux CUDA, other local CUDA GPUs
make strix-halo       # Linux ROCm, AMD Strix Halo
make cpu              # CPU-only diagnostics build
```

**Laden Sie das Modell herunter**

```
./download_model.sh q2-imatrix   # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix  # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix   # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix  # 512 GB RAM machines, PRO q2 imatrix quant
```

## Ausführung

**Initialisieren Sie das Modell**

```
./download_model.sh q2-imatrix

./ds4 \
  -m ./ds4flash.gguf \
  --ssd-streaming \
  --ssd-streaming-cache-experts 32GB \
  --ctx 32768 \
  --nothink
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Helfen Sie mir, das am besten geeignete DeepSeek- oder GLM-Modell entsprechend den Hardwarefunktionen meines Systems auszuwählen. Welchen Download-Befehl soll ich verwenden und wie kann ich den Speicherengpass überwinden, indem ich die Streaming-Funktion über SSD aktiviere? Erläutern Sie außerdem die grundlegenden Konfigurationseinstellungen, die für die Verwendung dieses von mir installierten künstlichen Intelligenzsystems als lokaler Server erforderlich sind.

## Verwandte Begriffe aus dem Glossar

- [Inference Engine](https://trescout.com/de/dictionary/inference-engine/)
- [Inference](https://trescout.com/de/dictionary/inference/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler und Systemadministratoren, die leistungsstarke Modelle der künstlichen Intelligenz auf ihrer eigenen lokalen Hardware ausführen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/antirez/ds4)
- [Auf Türkisch lesen →](https://trescout.com/discover/ds4/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-03 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ds4/
