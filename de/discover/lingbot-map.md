# Erstellen Sie dreidimensionale Szenen aus Streaming-Daten

Lingbot-Map ist ein Feed-Forward-3D-Grundlagenmodell, das zur Rekonstruktion von Szenen aus Streaming-Daten entwickelt wurde. Das Projekt optimiert Visualisierungsprozesse durch die Verarbeitung komplexer Umweltdaten dank seiner in der Python-Sprache entwickelten Architektur.

- ★ 17.060
- Python
- GitHub Trending · 2026-06-29

## Aktualisierungen

- **16. September 2026:** Sterne 16,054 → 17,060.
- **2. August 2026:** Sterne 8,439 → 16,054.

## Was es bringt

- Stabile 3D-Rekonstruktion langer Videosequenzen
- Unterstützung für Streaming-Inferenz mit geringer Latenz
- Architektur der künstlichen Intelligenz, die komplexe Umweltdaten verarbeiten kann

## Installation

**Umgebungsvorbereitung und Grundeinrichtung**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Installieren der erforderlichen Bibliotheken**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

## Ausführung

**Beginn der Beispielszene**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit LingBot-Map eine 3D-Szene aus Streaming-Daten erstellen. Ich habe die Installation abgeschlossen und meine Modelldatei ist fertig. Wie kann ich die Visualisierungsoberfläche in meinem lokalen Browser mit dem Befehl starten, der zum Ausführen der Courthouse-Instanz erforderlich ist?

## Verwandte Begriffe aus dem Glossar

- [Foundation Model](https://trescout.com/de/dictionary/foundation-model/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Forscher und Entwickler, die sich für 3D-Computervision und Streaming-Datenverarbeitung interessieren.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/Robbyant/lingbot-map)
- [Auf Türkisch lesen →](https://trescout.com/discover/lingbot-map/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-29 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/lingbot-map/
