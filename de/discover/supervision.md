# Tools für Computer-Vision-Projekte

Supervision wurde von Roboflow entwickelt und bietet wiederverwendbare Hilfstools und Funktionen für Computer-Vision-Projekte. Diese Python-basierte Bibliothek beschleunigt Entwicklungsabläufe, indem sie Standardvorgänge in Prozessen wie der Objekterkennung und -verfolgung erleichtert.

- ★ 51.154
- Python
- GitHub Trending · 2026-06-09

## Aktualisierungen

- **8. Oktober 2026:** Sterne 51,146 → 51,154, neueste Version 0.30.9 (8. Oktober 2026).
- **7. Oktober 2026:** Sterne 51,118 → 51,146, neueste Version 0.30.8 (6. Oktober 2026).
- **4. Oktober 2026:** Sterne 51,075 → 51,118, neueste Version 0.30.7 (4. Oktober 2026).
- **29. September 2026:** Sterne 51,054 → 51,075, neueste Version 0.30.6 (29. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich habe die Bibliothek mit dem Befehl pip install supervision in einer Python 3.9-Umgebung oder höher installiert. Ich möchte die Ergebnisse der Objekterkennung visualisieren und meinen Datensatz in meinem Computer-Vision-Projekt verwalten. Wie kann ich mithilfe der Supervision-Bibliothek Objekterkennungsergebnisse auf einem Bild markieren und wie kann ich Datensätze in verschiedenen Formaten (COCO, YOLO usw.) laden und konvertieren? Bitte helfen Sie mir, einen Beispielworkflow mit den von der Bibliothek bereitgestellten Annotator- und Datensatz-Hilfstools zu erstellen.

## Verwandte Begriffe aus dem Glossar

- [Computer Vision](https://trescout.com/de/dictionary/computer-vision/)
- [Computer Vision](https://trescout.com/de/dictionary/cv/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Python-Entwickler, die Objekterkennungs- und -verfolgungsprozesse in Computer-Vision-Projekten standardisieren möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/roboflow/supervision)
- [Auf Türkisch lesen →](https://trescout.com/discover/supervision/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-09 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/supervision/
