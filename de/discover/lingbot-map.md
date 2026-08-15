# Erstellen Sie dreidimensionale Szenen aus Streaming-Daten

Lingbot-Map ist ein Feed-Forward-3D-Grundlagenmodell, das zur Rekonstruktion von Szenen aus Streaming-Daten entwickelt wurde. Das Projekt optimiert Visualisierungsprozesse durch die Verarbeitung komplexer Umweltdaten dank seiner in der Python-Sprache entwickelten Architektur.

- ★ 16.054
- Python
- GitHub Trending · 2026-06-29

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
Ich möchte mit LingBot-Map eine 3D-Szene aus Streaming-Daten erstellen. Ich habe die Installation abgeschlossen und meine Modelldatei ist fertig. Wie kann ich die Visualisierungsoberfläche in meinem lokalen Browser mit dem Befehl starten, der zum Ausführen der Courthouse-Instanz erforderlich ist?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/lingbot-map/
