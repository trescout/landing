# Lange Audioaufnahmen mit künstlicher Intelligenz analysieren

VibeVoice wurde von Microsoft veröffentlicht und als Open-Source-Sprach-KI-Framework entwickelt. Mit seiner Python-basierten Struktur ermöglicht das System Benutzern, eigene Klangmodelle zu trainieren und in ihre Anwendungen zu integrieren.

- ★ 51.860
- GitHub Trending · 2026-06-07

## Aktualisieren
- 2. August 2026: Stern 48.569 → 51.860.

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
Ich möchte meine 60-minütige Audioaufnahme mit dem VibeVoice-Modell analysieren. Ich muss als strukturierte Textdatei abrufen, wer die Sprecher sind, wann sie gesprochen haben und welchen Inhalt sie gesagt haben. Ich möchte auch benutzerdefinierte Schlüsselwörter hinzufügen, damit das Modell technische Begriffe genauer erkennt. Wie kann ich diesen Prozess strukturieren?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vibevoice/
