# Native Open-Source-Sprachagenten

Die von Hugging Face entwickelte Speech-to-Speech-Bibliothek ermöglicht die Erstellung lokaler Sprachagenten mithilfe von Open-Source-Modellen. Mit diesem Python-basierten Tool können Entwickler Echtzeit-Sprachinteraktionssysteme erstellen, die auf dem Gerät ausgeführt werden.

- ★ 12.310
- Python
- GitHub Trending · 2026-07-29

## Aktualisieren
- 12. August 2026: Star 11.283 → 12.310, neueste Version v0.2.12 (5. August 2026).
- 6. August 2026: Star 10.774 → 11.283, neueste Version v0.2.12 (5. August 2026).
- 4. August 2026: Star 10.402 → 10.774, neueste Version v0.2.11 (3. August 2026).
- 2. August 2026: Star 7.443 → 10.402, neueste Version v0.2.10 (11. Juni 2026).

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
