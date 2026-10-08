# Lange Audioaufnahmen mit künstlicher Intelligenz analysieren

VibeVoice wurde von Microsoft veröffentlicht und als Open-Source-Sprach-KI-Framework entwickelt. Mit seiner Python-basierten Struktur ermöglicht das System Benutzern, eigene Klangmodelle zu trainieren und in ihre Anwendungen zu integrieren.

- ★ 54.502
- GitHub Trending · 2026-06-07

**Hinweis von TreScout:** Das Repository hat sich nach der Veröffentlichung geändert: Der Teil, der Ton in Text umwandelt, bleibt bestehen, der Teil, der Text in Ton umwandelt, wurde zurückgezogen. Sein besonderes Merkmal ist, dass es lange Datensätze auf einmal verarbeiten kann. Es handelt sich um ein sich schnell änderndes Projekt. Sehen Sie sich den aktuellen Zustand des Lagers an, bevor Sie es Ihrem Unternehmen hinzufügen.

## Aktualisierungen

- **27. September 2026:** Sterne 51,860 → 54,502.
- **2. August 2026:** Sterne 48,569 → 51,860.

## Was es bringt

- Konvertiert bis zu 60 Minuten Audioaufnahme gleichzeitig in Text.
- Es stellt Sprecher-ID, Zeitstempel und Inhaltsdetails auf strukturierte Weise bereit.
- Bietet benutzerdefinierte Schlüsselwortunterstützung für benutzerdefinierte Begriffe und Namen.

## Installation

**Von GitHub installieren**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```

## Ausführung

**Gradio-Demo**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Transkription aus Datei**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte meine 60-minütige Audioaufnahme mit dem VibeVoice-Modell analysieren. Ich muss als strukturierte Textdatei abrufen, wer die Sprecher sind, wann sie gesprochen haben und welchen Inhalt sie gesagt haben. Ich möchte auch benutzerdefinierte Schlüsselwörter hinzufügen, damit das Modell technische Begriffe genauer erkennt. Wie kann ich diesen Prozess strukturieren?

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Anwender, die Langzeit-Audioaufzeichnungen, Besprechungszusammenfassungen oder Podcast-Inhalte schnell und strukturiert in Text umwandeln möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/microsoft/VibeVoice)
- [Auf Türkisch lesen →](https://trescout.com/discover/vibevoice/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-07 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vibevoice/
