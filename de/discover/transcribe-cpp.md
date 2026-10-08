# Schnelle Sprachkonvertierung auf lokalen Systemen

Transcribe.cpp ist eine in C++ entwickelte Sprache-zu-Text-Inferenzbibliothek, die mehr als 16 Modellfamilien unterstützt. Mithilfe der ggml-Infrastruktur ermöglicht dieses Tool die effiziente Ausführung verschiedener Audioverarbeitungsmodelle auf lokalen Systemen.

- ★ 1.982
- C++
- GitHub Trending · 2026-07-21

## Aktualisierungen

- **4. Oktober 2026:** Sterne 1,981 → 1,982, neueste Version v0.3.1 (4. Oktober 2026).
- **3. Oktober 2026:** Sterne 1,963 → 1,981, neueste Version v0.3.0 (3. Oktober 2026).
- **27. September 2026:** Sterne 1,865 → 1,963, neueste Version v0.2.4 (25. September 2026).
- **31. August 2026:** Sterne 1,825 → 1,865, neueste Version v0.2.3 (30. August 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte eine lokale Audiodatei mit dem Tool Transcribe.cpp in Text konvertieren. Wie kann ich meine 16-kHz-Mono-Audiodatei im WAV-Format mit dem auf meinem System kompilierten Tool transcribe-cli und der heruntergeladenen Modelldatei im GGUF-Format verarbeiten? Bitte erläutern Sie die für diesen Vorgang erforderliche Befehlsstruktur und die Dateipfade, auf die ich achten sollte.

## Verwandte Begriffe aus dem Glossar

- [Speech-to-Text](https://trescout.com/de/dictionary/speech-to-text/)
- [STT](https://trescout.com/de/dictionary/stt/)
- [GGUF](https://trescout.com/de/dictionary/gguf/)
- [Inference](https://trescout.com/de/dictionary/inference/)
- [CPU](https://trescout.com/de/dictionary/cpu/)
- [GPU](https://trescout.com/de/dictionary/gpu/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die datenschutzorientierte und schnelle Spracherkennungssysteme auf ihrer eigenen Hardware ausführen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/handy-computer/transcribe.cpp)
- [Auf Türkisch lesen →](https://trescout.com/discover/transcribe-cpp/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-21 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/transcribe-cpp/
