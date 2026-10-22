# Automatisierte Aktienauswahl für den chinesischen Aktienmarkt

Sequoia-X ist eine Python-basierte Software, die chinesische Börsendaten verwendet, um Aktien automatisch auf Basis technischer Analyseformeln auszuwählen. Nach Marktschluss führt sie Scans durch und übermittelt die Ergebnisse über die Unternehmens-Messaging-App Feishu.

- ★ 7.594
- Python
- GitHub Trending · 2026-09-03

## Aktualisierungen

- **27. September 2026:** Sterne 6,376 → 7,594.

## Was es bringt

- Speichert Aktiendaten in einer lokalen Datenbank
- Wendet automatisch mehrere Strategien der technischen Analyse an
- Übermittelt die Ergebnisse zum Tagesende über die Messaging-App Feishu

## Installation

**Installieren der erforderlichen Bibliotheken**

```
pip install .
```

## Ausführung

**Erstmaliges Laden historischer Daten**

```
python main.py --backfill
```

**Täglichen Scan starten**

```
python main.py
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das Tool Sequoia-X verwenden, um Aktien am chinesischen Markt mittels technischer Analysemethoden zu scannen. Nachdem ich die notwendigen Installationen in meiner Python-Umgebung vorgenommen habe, werde ich den Backfill-Modus nutzen, um historische Daten zu laden, und anschließend den täglichen Betriebsmodus, um nach Marktschluss automatische Scans und Benachrichtigungen zu erhalten. Dabei möchte ich sicherstellen, dass die Daten in einer lokalen SQLite-Datenbank gespeichert und die Ergebnisse über Feishu versendet werden.

Repository: https://github.com/sngyai/Sequoia-X. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Investoren gedacht, die am chinesischen Aktienmarkt handeln und ihre Strategien der technischen Analyse automatisieren möchten.

## Links

- [GitHub-Repository →](https://github.com/sngyai/Sequoia-X)
- [Auf Türkisch lesen →](https://trescout.com/discover/sequoia-x/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-03 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sequoia-x/
