# Editierbare Komposition mit KI in der Musikproduktion

YuE ist ein Musikgenerierungssystem, das mit Fähigkeiten wie symbolischer Planung und Zero-Shot-Cover-Produktion ausgestattet ist. Dieses KI-Modell, das Musikbearbeitungsprozesse automatisiert, ermöglicht es Ihnen, komplexe Kompositionen mit agentenbasierten Workflows zu verwalten.

- ★ 8.744
- Python
- GitHub Trending · 2026-09-13

## Was es bringt
- Erstellung von Melodie- und Akkordplänen basierend auf Text- und Stileingaben
- Möglichkeit, Musiknoten zu bearbeiten, bevor sie in Audiodateien umgewandelt werden
- Neuinterpretation und Bearbeitung bestehender Lieder in verschiedenen Stilen

## Installation
**Projekt-Download und Installation**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```


## Ausführung
**Erstellung von Liedern mit bearbeiteten Noten**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```


## Wenn Sie nicht programmieren
Ich möchte ein Lied mit YuE2 erstellen. Bitte erstelle mir einen editierbaren Melodie- und Akkordplan basierend auf meinen Liedtexten und dem gewünschten Musikstil. Erzeuge anschließend eine vollständige Liedaufnahme mit Gesang und instrumentaler Begleitung unter Verwendung dieses Plans. Falls ich eine Notationsdatei habe, ermögliche mir die Bearbeitung unter Verwendung dieser Datei.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/yue/
