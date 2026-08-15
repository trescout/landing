# DeepSeek-Ausführungs-Engine auf nativer Hardware

DS4 wurde von Salvatore Sanfilippo, dem Erfinder von Redis, entwickelt und ist eine Inferenz-Engine, die die Ausführung von DeepSeek-Modellen auf lokaler Hardware ermöglicht. Dieses in C-Sprache geschriebene Tool bietet dank Metal-, CUDA- und ROCm-Unterstützung die Möglichkeit, Hochleistungsmodelle auf verschiedenen Grafikprozessoren auszuführen.

- ★ 21.134
- C
- GitHub Trending · 2026-08-03

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
Helfen Sie mir, das am besten geeignete DeepSeek- oder GLM-Modell entsprechend den Hardwarefunktionen meines Systems auszuwählen. Welchen Download-Befehl soll ich verwenden und wie kann ich den Speicherengpass überwinden, indem ich die Streaming-Funktion über SSD aktiviere? Erläutern Sie außerdem die grundlegenden Konfigurationseinstellungen, die für die Verwendung dieses von mir installierten künstlichen Intelligenzsystems als lokaler Server erforderlich sind.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ds4/
