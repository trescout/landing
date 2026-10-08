# Analysieren Sie Android-Apps schnell

ASC ist eine extrem schnelle Android-Decompiler-Schnittstelle, die für Forscher mobiler Anwendungen und KI-Agenten entwickelt wurde. Das in Python geschriebene Tool zielt darauf ab, den Prozess der Analyse komplexer Anwendungsdateien zu beschleunigen.

- ★ 1.980
- Python
- GitHub Trending · 2026-09-16

## Aktualisierungen

- **27. September 2026:** Sterne 1,336 → 1,980, neueste Version dev-0.1.1-post2 (21. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Verhalte dich wie ein Forscher für Android-Anwendungen. Hilf mir dabei, eine bestimmte Klasse in einer APK-Datei zu finden, die AndroidManifest.xml-Datei zu analysieren oder nach Referenzen im Code zu suchen, indem du das Droid ASC-Tool verwendest. Verwende bei der Erstellung der Befehle die Befehle getclass, getmanifest und findrefs des Tools mit den korrekten Parametern und erkläre mir, wie ich die Ausgaben interpretieren soll.

## Verwandte Begriffe aus dem Glossar

- [Decompiler](https://trescout.com/de/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Forscher im Bereich der Sicherheit mobiler Anwendungen und Android-Softwareentwickler.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/MG1937/ASC)
- [Auf Türkisch lesen →](https://trescout.com/discover/asc/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/asc/
