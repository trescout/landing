# Analysieren Sie Android-Apps schnell

ASC ist eine extrem schnelle Android-Decompiler-Schnittstelle, die für Forscher mobiler Anwendungen und KI-Agenten entwickelt wurde. Das in Python geschriebene Tool zielt darauf ab, den Prozess der Analyse komplexer Anwendungsdateien zu beschleunigen.

- ★ 2.600
- Python
- GitHub Trending · 2026-09-16

## Aktualisierungen

- **30. Oktober 2026:** Sterne 2,498 → 2,600, neueste Version dev-0.1.2-post4 (30. Oktober 2026).
- **21. Oktober 2026:** Sterne 2,399 → 2,498, neueste Version dev-0.1.2-post3 (21. Oktober 2026).
- **15. Oktober 2026:** Sterne 2,236 → 2,399, neueste Version dev-0.1.2-post2 (14. Oktober 2026).
- **10. Oktober 2026:** Sterne 1,980 → 2,236, neueste Version dev-0.1.1-post4 (10. Oktober 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Verhalte dich wie ein Forscher für Android-Anwendungen. Hilf mir dabei, eine bestimmte Klasse in einer APK-Datei zu finden, die AndroidManifest.xml-Datei zu analysieren oder nach Referenzen im Code zu suchen, indem du das Droid ASC-Tool verwendest. Verwende bei der Erstellung der Befehle die Befehle getclass, getmanifest und findrefs des Tools mit den korrekten Parametern und erkläre mir, wie ich die Ausgaben interpretieren soll.

Repository: https://github.com/MG1937/ASC. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Decompiler](https://trescout.com/de/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Forscher im Bereich der Sicherheit mobiler Anwendungen und Android-Softwareentwickler.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/MG1937/ASC)
- [Auf Türkisch lesen →](https://trescout.com/discover/asc/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/asc/
