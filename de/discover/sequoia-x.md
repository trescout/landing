# Automatisierte Aktienauswahl für den chinesischen Aktienmarkt

Sequoia-X ist eine Python-basierte Software, die chinesische Börsendaten verwendet, um Aktien automatisch auf Basis technischer Analyseformeln auszuwählen. Nach Marktschluss führt sie Scans durch und übermittelt die Ergebnisse über die Unternehmens-Messaging-App Feishu.

- ★ 6.376
- Python
- GitHub Trending · 2026-09-03

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
Ich möchte das Tool Sequoia-X verwenden, um Aktien am chinesischen Markt mittels technischer Analysemethoden zu scannen. Nachdem ich die notwendigen Installationen in meiner Python-Umgebung vorgenommen habe, werde ich den Backfill-Modus nutzen, um historische Daten zu laden, und anschließend den täglichen Betriebsmodus, um nach Marktschluss automatische Scans und Benachrichtigungen zu erhalten. Dabei möchte ich sicherstellen, dass die Daten in einer lokalen SQLite-Datenbank gespeichert und die Ergebnisse über Feishu versendet werden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sequoia-x/
