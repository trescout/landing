# Was ist Kontext (Context)? KI vs. Betriebssysteme

*Glossar · AI · Zuletzt aktualisiert: 19. September 2026*

> Englisch: Context · Wortherkunft: lateinisch contexere (zusammenweben, verknüpfen)

Kontext (Context) ist ein universeller Grundbegriff der Informatik, der entweder das aktive Eingabe- und Erinnerungsfenster großer Sprachmodelle oder den hardwarespezifischen Prozessorzustand bei der Prozessverwaltung von Betriebssystemen bezeichnet.

*Wenn Sie zu einem Freund sagen 'Ja, er hat zugestimmt', versteht er Sie nicht; sagen Sie jedoch 'Bezüglich unseres Gesprächs von gestern über den Urlaubsplan', liefern Sie den notwendigen Kontext für das Verständnis.*

## 1. Der Kontext in Künstlicher Intelligenz und LLMs

Große Sprachmodelle besitzen zwischen einzelnen API-Abfragen kein fortlaufendes Bewusstsein. Um Fragen präzise zu beantworten, sind sie vollständig auf ihr **Kontextfenster** angewiesen: die Abfolge aller Tokens (Systemanweisungen, bisheriger Chatverlauf und RAG-Textauszüge), die der Anfrage mitgegeben werden. Die Größe dieses Fensters bestimmt, wie viele Zusammenhänge das Modell gleichzeitig erfassen kann.

## 2. Kontext in Betriebssystemen und Systemprogrammierung

In Betriebssystemen beschreibt der Kontext den vollständigen Zustand eines CPU-Kerns bei der Programmausführung: Hardware-Register, Programmzähler (PC) und Speichertabellen. Wenn das System von einem Thread zu einem anderen wechselt, führt es einen **Kontextwechsel (Context Switch)** durch, indem es den alten Zustand sichert und den neuen in die Prozessorregister lädt.

## Gegenüberstellung verschiedener Fachdisziplinen

Einsatzformen des Begriffs in der Softwaretechnik:

- **KI-Sprachmodelle:** Token-Puffer und KV-Cache als unmittelbares Arbeitsgedächtnis während der Inferenz.
- **Betriebssysteme:** Process Control Blocks (PCB) zur Sicherung von CPU-Registern beim Multitasking.
- **Web-Frameworks:** Kontext-Objekte (in Go oder React) zur hierarchischen Weitergabe von Abbruchsignalen und Authentifizierungsdaten.

## Häufige Fragen

**Was bedeutet das Phänomen 'lost in the middle' bei KI-Modellen?**

Dass Sprachmodelle Fakten am Anfang und am Ende langer Eingabetexte deutlich zuverlässiger erfassen als in der Mitte großer Textblöcke.

**Warum sind CPU-Kontextwechsel rechenintensiv?**

Weil das Sichern und Wiederherstellen von Registerwerten Prozessorzyklen kostet und schnelle CPU-Caches entwertet werden.

**Welchen Nutzen hat die Context-API in React?**

Sie erlaubt die direkte Übergabe globaler Daten (wie Anmeldezustaende oder Farbschemata) an tiefe Unterkomponenten ohne manuelle Parameterweitergabe.

**Wie verarbeitet die Transformer-Architektur den Kontext?**

Über Aufmerksamkeitsmatrizen, die berechnen, wie stark jedes Wort im Eingabefenster semantisch mit allen anderen Wörtern zusammenhängt.

## Verwandte Begriffe

- [Context Window](https://trescout.com/de/dictionary/context-window/)
- [Working Memory](https://trescout.com/de/dictionary/working-memory/)

## Verwandte Tools

- [Goose](https://trescout.com/de/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/de/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/de/discover/openclaude/)
- [Code Review Graph](https://trescout.com/de/discover/code-review-graph/)
- [Fastmcp](https://trescout.com/de/discover/fastmcp/)
- [Context Mode](https://trescout.com/de/discover/context-mode/)
- [Unity MCP](https://trescout.com/de/discover/unity-mcp/)
- [DesktopCommanderMCP](https://trescout.com/de/discover/desktopcommandermcp/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/context/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/context/
