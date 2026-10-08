# Native Open-Source-Sprachagenten

Die von Hugging Face entwickelte Speech-to-Speech-Bibliothek ermöglicht die Erstellung lokaler Sprachagenten mithilfe von Open-Source-Modellen. Mit diesem Python-basierten Tool können Entwickler Echtzeit-Sprachinteraktionssysteme erstellen, die auf dem Gerät ausgeführt werden.

- ★ 13.072
- Python
- GitHub Trending · 2026-07-29

## Aktualisierungen

- **7. September 2026:** Sterne 12,310 → 13,072, neueste Version v1.0.0 (6. September 2026).
- **12. August 2026:** Sterne 11,283 → 12,310, neueste Version v0.2.12 (5. August 2026).
- **6. August 2026:** Sterne 10,774 → 11,283, neueste Version v0.2.12 (5. August 2026).
- **4. August 2026:** Sterne 10,402 → 10,774, neueste Version v0.2.11 (3. August 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit diesem Tool meinen eigenen lokalen Sprachagenten einrichten. Welche grundlegenden Schritte muss ich befolgen, um eine Audio-Pipeline mit geringer Latenz unter Verwendung von VAD-, STT-, LLM- und TTS-Komponenten zu erstellen? Mit welchem ​​Befehl kann ich den Server hochfahren und mich mit einem OpenAI Realtime-kompatiblen Client verbinden?

## Verwandte Begriffe aus dem Glossar

- [Voice Agents](https://trescout.com/de/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/de/dictionary/speech-to-speech/)
- [STT](https://trescout.com/de/dictionary/stt/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die native und anpassbare Sprachinteraktionssysteme auf ihrer eigenen Hardware entwickeln möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/huggingface/speech-to-speech)
- [Auf Türkisch lesen →](https://trescout.com/discover/speech-to-speech/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-29 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/speech-to-speech/
