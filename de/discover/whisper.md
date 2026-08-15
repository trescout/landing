# Transkribieren Sie Geräusche mit künstlicher Intelligenz

Whisper wurde von OpenAI entwickelt und ist ein Spracherkennungsmodell, das durch eine groß angelegte Lernmethode mit schwacher Aufsicht trainiert wird. Es bietet hohe Genauigkeitsraten bei der Konvertierung und Übersetzung mehrsprachiger Audiodaten in Text.

- ★ 106.452
- Python
- GitHub Trending · 2026-06-07

## Was es bringt
- Konvertieren Sie Audiodateien mit hoher Genauigkeit in Text.
- Übersetzen von Gesprächen aus verschiedenen Sprachen ins Englische.
- Spracherkennung und Sprachaktivitätserkennung in Audioinhalten.

## Installation
**Systemabhängigkeiten**

```
sudo apt update && sudo apt install ffmpeg
```

**Zusätzlicher Installationsbedarf**

```
pip install setuptools-rust
```


## Ausführung
**Konvertieren Sie eine Audiodatei in Text**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Transkription in einer bestimmten Sprache**

```
whisper japanese.wav --language Japanese
```


## Wenn Sie nicht programmieren
Ich möchte meine Audiodatei mit dem Whisper-Tool in Text umwandeln. Ich habe die notwendigen Installationen auf meinem System vorgenommen. Welche grundlegende Befehlsstruktur muss ich im Terminal eingeben, um den Inhalt meiner Audiodatei in Text zu übersetzen, und wie sollte ich den Sprachspezifikationsparameter für Audiodateien in verschiedenen Sprachen verwenden?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/whisper/
