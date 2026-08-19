# Schnelle Sprachkonvertierung auf lokalen Systemen

Transcribe.cpp ist eine in C++ entwickelte Sprache-zu-Text-Inferenzbibliothek, die mehr als 16 Modellfamilien unterstützt. Mithilfe der ggml-Infrastruktur ermöglicht dieses Tool die effiziente Ausführung verschiedener Audioverarbeitungsmodelle auf lokalen Systemen.

- ★ 1.802
- C++
- GitHub Trending · 2026-07-21

## Was es bringt
- Unterstützung für 16 verschiedene Modellfamilien
- Hohe Leistung auf GPU und CPU
- Effiziente Inferenz mit dem GGUF-Format

## Installation
**Vulkan unterstützte die Linux-Installation**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```


## Wenn Sie nicht programmieren
Ich möchte eine lokale Audiodatei mit dem Tool Transcribe.cpp in Text konvertieren. Wie kann ich meine 16-kHz-Mono-Audiodatei im WAV-Format mit dem auf meinem System kompilierten Tool transcribe-cli und der heruntergeladenen Modelldatei im GGUF-Format verarbeiten? Bitte erläutern Sie die für diesen Vorgang erforderliche Befehlsstruktur und die Dateipfade, auf die ich achten sollte.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/transcribe-cpp/
