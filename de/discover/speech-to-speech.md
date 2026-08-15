# Native Open-Source-Sprachagenten

Die von Hugging Face entwickelte Speech-to-Speech-Bibliothek ermöglicht die Erstellung lokaler Sprachagenten mithilfe von Open-Source-Modellen. Mit diesem Python-basierten Tool können Entwickler Echtzeit-Sprachinteraktionssysteme erstellen, die auf dem Gerät ausgeführt werden.

- ★ 12.310
- Python
- GitHub Trending · 2026-07-29

## Was es bringt
- Modulare Audiolinie mit geringer Latenz
- OpenAI Realtime-kompatible WebSocket-Unterstützung
- Möglichkeit, lokal auf unterschiedlicher Hardware zu arbeiten

## Installation
**Grundeinrichtung**

```
pip install speech-to-speech
```

**Installation aus dem Quellcode**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```


## Ausführung
**Starten des Servers**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**Mit dem Kunden in Kontakt treten**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```


## Wenn Sie nicht programmieren
Ich möchte mit diesem Tool meinen eigenen lokalen Sprachagenten einrichten. Welche grundlegenden Schritte muss ich befolgen, um eine Audio-Pipeline mit geringer Latenz unter Verwendung von VAD-, STT-, LLM- und TTS-Komponenten zu erstellen? Mit welchem ​​Befehl kann ich den Server hochfahren und mich mit einem OpenAI Realtime-kompatiblen Client verbinden?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/speech-to-speech/
