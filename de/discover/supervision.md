# Tools für Computer-Vision-Projekte

Supervision wurde von Roboflow entwickelt und bietet wiederverwendbare Hilfstools und Funktionen für Computer-Vision-Projekte. Diese Python-basierte Bibliothek beschleunigt Entwicklungsabläufe, indem sie Standardvorgänge in Prozessen wie der Objekterkennung und -verfolgung erleichtert.

- ★ 49.033
- Python
- GitHub Trending · 2026-06-09

## Aktualisieren
- 6. August 2026: Star 48.545 → 49.033, letzte Version 0.30.0 (4. August 2026).
- 2. August 2026: Star 42.546 → 48.545, letzte Version 0.29.1 (23. Juni 2026).

## Was es bringt
- Es beschleunigt Datenlade- und -verarbeitungsprozesse in Computer-Vision-Projekten.
- Es vereinfacht die Anwendungsentwicklung durch Standardisierung von Vorgängen wie Objekterkennung und -verfolgung.
- Es bietet Visualisierung und Datensatzverwaltung, indem es mit verschiedenen Modellbibliotheken kompatibel ist.

## Installation
**Paketinstallation**

```
pip install supervision
```


## Ausführung
**Markieren eines Objekts auf dem Bild**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```


## Wenn Sie nicht programmieren
Ich habe die Bibliothek mit dem Befehl pip install supervision in einer Python 3.9-Umgebung oder höher installiert. Ich möchte die Ergebnisse der Objekterkennung visualisieren und meinen Datensatz in meinem Computer-Vision-Projekt verwalten. Wie kann ich mithilfe der Supervision-Bibliothek Objekterkennungsergebnisse auf einem Bild markieren und wie kann ich Datensätze in verschiedenen Formaten (COCO, YOLO usw.) laden und konvertieren? Bitte helfen Sie mir, einen Beispielworkflow mit den von der Bibliothek bereitgestellten Annotator- und Datensatz-Hilfstools zu erstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/supervision/
