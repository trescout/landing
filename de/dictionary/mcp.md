# Was ist MCP?

*Glossar · AI · Zuletzt aktualisiert: 22. September 2026*

> Model Context Protocol

MCP (Model Context Protocol) ist ein offenes Protokoll, das es Anwendungen der künstlichen Intelligenz ermöglicht, auf standardisierte Weise eine Verbindung zu externen Daten und Tools herzustellen.

## Definition und Wortherkunft

Anstatt für jede Anwendung separate Verbindungen zu schreiben, wird ein einziger Standard verwendet. Das Protokoll ist ein offener Standard, der entwickelt wurde, um die Interoperabilität des KI-Ökosystems zu erhöhen. Die Steckdosen-Analogie ist treffend: So wie jedes Gerät mit demselben Stecker funktioniert, verbinden sich verschiedene Datenquellen auf die gleiche Weise mit AI.

***Analogie:** Es ist wie ein Steckerstandard; Es ermöglicht die einfache Anbindung verschiedener Datenquellen an künstliche Intelligenz, so wie jedes Gerät mit dem gleichen Stecker funktioniert.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Assistenten:** Die Anwendung für künstliche Intelligenz liest Ihren Kalender und Ihre Dateien.
**Entwicklung:** Verknüpfen des Code-Editors mit dem Repository und der Dokumentation.
**Berichterstattung:** Zusammenfassende Extraktion aus der Live-Datenbank.

## Technische Tiefe und Architektur

Die Architektur besteht aus drei Teilen:

**Husch:** KI-Anwendung (z. B. Desktop-Assistent oder Editor).
**Kunde:** Verbindungsmanager innerhalb des Hosts.
**Server:** Kleines Programm, das Daten oder Tool präsentiert (Dateisystem, Datenbank, GitHub).

Server bieten drei Funktionen:

**Werkzeug:** Funktion, die das Modell aufrufen kann (Dateisuche, Abfrageausführung).
**Ressource:** Daten (Dokument, Schema), die das Modell lesen kann.
**Prompt:** Fertige Aufgabenvorlage.

Eine typische Client-Einstellung ist wie folgt:

```
{
  "mcpServers": {
    "dosya": {
      "command": "npx",
      "args": ["-y", "ornek-mcp-dosya"]
    }
  }
}
```

Sicherheitsregel: Der Server greift nur auf erlaubte Ordner und Prozesse zu. Jede Anfrage des Modells muss die Zustimmung des Benutzers bestehen können.

## Häufig gemischte Dinge

Kann mit API gemischt werden. API ist ein einzelnes Tor, während MCP der Regelsatz ist, der sicherstellt, dass die Daten, die dieses Tor passieren, in einer Standardsprache gesprochen werden. Die API ist serverspezifisch, MCP ist serverübergreifend gleich.

## Einsatz in verschiedenen Disziplinen

**Elektrisch:** Der Steckdosenstandard, dem jedes Gerät entspricht.
**Eisenbahn:** Hakenstandard zum Verbinden von Waggons.
**Sprache:** Gemeinsame Protokollsprache, die in der Diplomatie verwendet wird.

## Häufig gestellte Fragen

**Warum ist MCP notwendig?**

Anstatt für jede Anwendung einen separaten Link zu schreiben, wird die Standardmethode befolgt. Dies vereinfacht Sicherheit und Wartung.

**Ist MCP Open Source?**

Ja. Es handelt sich um einen offenen Standard, verschiedene Anwendungen können ihre eigenen Clients und Server schreiben.

**Warum MCP anstelle von API verwenden?**

Die API ist serverspezifisch und wird separat erlernt. MCP bietet eine gemeinsame Sprache, das Modell stellt eine Verbindung zum neuen Server her.

**Ist es sicher?**

Sein Design ist berechtigungsbasiert, Sie müssen jedoch den Zugriffsbereich des Servers eng halten und eine Genehmigung für Schreibvorgänge benötigen.

## Verwandte Begriffe

- [API](https://trescout.com/de/dictionary/api/)
- [Data Pipeline](https://trescout.com/de/dictionary/data-pipeline/)
- [AI Agent](https://trescout.com/de/dictionary/ai-agent/)

## Verwandte Werkzeuge

- [Langflow](https://trescout.com/de/discover/langflow/)
- [Servers](https://trescout.com/de/discover/servers/)
- [OpenCut](https://trescout.com/de/discover/opencut/)
- [AI Engineering from Scratch](https://trescout.com/de/discover/ai-engineering-from-scratch/)
- [Goose](https://trescout.com/de/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/de/discover/chrome-devtools-mcp/)
- [Codebase Memory MCP](https://trescout.com/de/discover/codebase-memory-mcp/)
- [REA](https://trescout.com/de/discover/rea/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/mcp/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/mcp/
