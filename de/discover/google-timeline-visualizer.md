# Verwandeln Sie Ihren Standortverlauf in ein bewegtes Video

Mit dem Google Timeline Visualizer, der die von Google lokalisierten historischen Daten visualisiert, können Reiserouten schon seit langem auf einer Karte analysiert werden. Entworfen mit der Kotlin-Sprache, ist diese Ferramenta, deren Lebensläufe Menschen aus der Geschichte der Lokalisierung in bedeutungsvolle Grafiken umwandeln.

- ★ 2.596
- Kotlin
- GitHub Trending · 2026-08-20

## Was es bringt
- Konvertiert Google Maps-Verlaufsdaten in MP4-Video
- Animiert Reiserouten auf der Karte
- Schützt die Privatsphäre durch die Verarbeitung personenbezogener Daten auf dem Gerät

## Installation
**Installieren Sie die erforderlichen Abhängigkeiten und führen Sie sie aus**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Entwicklungstools konfigurieren**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```


## Wenn Sie nicht programmieren
Ich möchte mit der Timeline.json-Datei, die ich habe, ein Video erstellen, das meine Reisen zeigt. Welchen Befehl sollte ich nach der Installation der erforderlichen Abhängigkeiten in der Python-Umgebung verwenden, um meine 2025-Daten in eine Datei mit dem Namen „my_trip_2025.mp4“ mit „stabiler“ Kamerabewegung und „ausgewogenen“ Komprimierungseinstellungen zu konvertieren?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/google-timeline-visualizer/
