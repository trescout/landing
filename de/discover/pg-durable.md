# Robustes Prozessmanagement auf PostgreSQL

pg_durable wurde von Microsoft entwickelt und ist eine Bibliothek zur Verwaltung dauerhafter Ausführungsprozesse auf PostgreSQL. Das in Rust geschriebene Tool ermöglicht die fehlertolerante und persistente Ausführung komplexer Arbeitsabläufe innerhalb der Datenbank.

- ★ 2.831
- Rust
- GitHub Trending · 2026-06-08

## Aktualisierungen

- **7. Oktober 2026:** Sterne 2,811 → 2,831, neueste Version v0.2.9 (7. Oktober 2026).
- **12. September 2026:** Sterne 2,800 → 2,811, neueste Version v0.2.8 (11. September 2026).
- **2. September 2026:** Sterne 2,781 → 2,800, neueste Version v0.2.7 (1. September 2026).
- **24. August 2026:** Sterne 2,716 → 2,781, neueste Version v0.2.6 (24. August 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte einen Workflow mit dem pg_durable-Plugin auf PostgreSQL erstellen. Wie sollte ich die Funktion df.start() konfigurieren, um einen fehlertoleranten und dauerhaften Prozess innerhalb der Datenbank zu verwalten? Wie kann ich eine Struktur erstellen, die Daten verarbeitet und im Fehlerfall dort fortfahren kann, wo sie aufgehört hat, indem ich die Operatoren ~> und |=> verwende, die SQL-Schritte verbinden? Bitte erläutern Sie diesen Vorgang anhand von Beispielen mit SQL-Befehlen.

## Verwandte Begriffe aus dem Glossar

- [Durable Execution](https://trescout.com/de/dictionary/durable-execution/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Backend-Entwickler, Datenbankadministratoren und Dateningenieure, die Datenverarbeitungsprozesse direkt auf PostgreSQL fehlertolerant und persistent verwalten möchten.

## Links

- [GitHub-Repository →](https://github.com/microsoft/pg_durable)
- [Auf Türkisch lesen →](https://trescout.com/discover/pg-durable/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-08 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/pg-durable/
