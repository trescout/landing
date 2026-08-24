# Robustes Prozessmanagement auf PostgreSQL

pg_durable wurde von Microsoft entwickelt und ist eine Bibliothek zur Verwaltung dauerhafter Ausführungsprozesse auf PostgreSQL. Das in Rust geschriebene Tool ermöglicht die fehlertolerante und persistente Ausführung komplexer Arbeitsabläufe innerhalb der Datenbank.

- ★ 2.781
- Rust
- GitHub Trending · 2026-06-08

## Was es bringt
- Es verwaltet Arbeitsabläufe innerhalb der Datenbank fehlertolerant und persistent.
- Im Falle eines Absturzes oder einer Unterbrechung wird der Betrieb ab dem letzten Kontrollpunkt fortgesetzt.
- Es läuft direkt auf PostgreSQL, ohne dass zusätzliche Infrastruktur erforderlich ist.

## Installation
**Aktivierung des Plugins**

```
CREATE EXTENSION pg_durable;
```


## Ausführung
**Starten eines Workflows**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```


## Wenn Sie nicht programmieren
Ich möchte einen Workflow mit dem pg_durable-Plugin auf PostgreSQL erstellen. Wie sollte ich die Funktion df.start() konfigurieren, um einen fehlertoleranten und dauerhaften Prozess innerhalb der Datenbank zu verwalten? Wie kann ich eine Struktur erstellen, die Daten verarbeitet und im Fehlerfall dort fortfahren kann, wo sie aufgehört hat, indem ich die Operatoren ~> und |=> verwende, die SQL-Schritte verbinden? Bitte erläutern Sie diesen Vorgang anhand von Beispielen mit SQL-Befehlen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/pg-durable/
