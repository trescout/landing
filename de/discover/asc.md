# Analysieren Sie Android-Apps schnell

ASC ist eine extrem schnelle Android-Decompiler-Schnittstelle, die für Forscher mobiler Anwendungen und KI-Agenten entwickelt wurde. Das in Python geschriebene Tool zielt darauf ab, den Prozess der Analyse komplexer Anwendungsdateien zu beschleunigen.

- ★ 1.336
- Python
- GitHub Trending · 2026-09-16

## Was es bringt
- Scannt große Anwendungsdateien in Sekunden
- Führt Abfragen direkt auf dem Code durch, ohne den Arbeitsspeicher zu belasten
- Liefert schnelle Ergebnisse ohne unnötige Vorverarbeitung

## Installation
**Installation mit Paketmanager**

```
pip install droidasc
```

**Installation aus dem Quellcode**

```
pip install .
```


## Ausführung
**Öffnen einer Anwendungsdatei über eine grafische Benutzeroberfläche**

```
droidasc app.apk --gui
```

**Exportieren einer bestimmten Klasse**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```


## Wenn Sie nicht programmieren
Verhalte dich wie ein Forscher für Android-Anwendungen. Hilf mir dabei, eine bestimmte Klasse in einer APK-Datei zu finden, die AndroidManifest.xml-Datei zu analysieren oder nach Referenzen im Code zu suchen, indem du das Droid ASC-Tool verwendest. Verwende bei der Erstellung der Befehle die Befehle getclass, getmanifest und findrefs des Tools mit den korrekten Parametern und erkläre mir, wie ich die Ausgaben interpretieren soll.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/asc/
