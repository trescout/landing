# Editierbare Komposition mit KI in der Musikproduktion

YuE ist ein Musikgenerierungssystem, das mit Fähigkeiten wie symbolischer Planung und Zero-Shot-Cover-Produktion ausgestattet ist. Dieses KI-Modell, das Musikbearbeitungsprozesse automatisiert, ermöglicht es Ihnen, komplexe Kompositionen mit agentenbasierten Workflows zu verwalten.

- ★ 10.749
- Python
- GitHub Trending · 2026-09-13

## Aktualisierungen

- **3. Oktober 2026:** Sterne 9,749 → 10,749, neueste Version yue2-v0.1.6 (9. September 2026).
- **19. September 2026:** Sterne 8,744 → 9,749, neueste Version yue2-v0.1.6 (9. September 2026).
- **15. September 2026:** Sterne 7,463 → 8,744, neueste Version yue2-v0.1.6 (9. September 2026).
- **13. September 2026:** Sterne 7,459 → 7,463, neueste Version yue2-v0.1.6 (9. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte ein Lied mit YuE2 erstellen. Bitte erstelle mir einen editierbaren Melodie- und Akkordplan basierend auf meinen Liedtexten und dem gewünschten Musikstil. Erzeuge anschließend eine vollständige Liedaufnahme mit Gesang und instrumentaler Begleitung unter Verwendung dieses Plans. Falls ich eine Notationsdatei habe, ermögliche mir die Bearbeitung unter Verwendung dieser Datei.

## Verwandte Begriffe aus dem Glossar

- [Zero-shot](https://trescout.com/de/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Musiker und Content-Ersteller, die ihre musikalischen Kompositionen mithilfe von künstlicher Intelligenz planen, Änderungen an Noten vornehmen und originelle Lieder produzieren möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/multimodal-art-projection/YuE)
- [Auf Türkisch lesen →](https://trescout.com/discover/yue/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-13 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/yue/
