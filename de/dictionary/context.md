# Was ist Context?

*Künstliche Intelligenz · Zuletzt aktualisiert: 19. September 2026*

Der Kontext ist die Gesamtheit der umgebungsbezogenen und semantischen Informationen, die ein Datum, ein Befehl oder ein Prozess benötigt, um korrekt interpretiert und ausgeführt werden zu können.

## 1. Kontext in künstlicher Intelligenz und LLMs

Große Sprachmodelle (LLM) verfügen nicht über ein dauerhaftes Gedächtnis oder ein Erfahrungsspeichersystem wie Menschen; bei jeder Abfrage "erinnern" sie sich nur an die Daten, die in diesem Moment in das Kontextfenster (context window) aufgenommen wurden.

### Transformer und der Aufmerksamkeitsmechanismus (Self-Attention)

In der Transformer-Architektur wird der Kontext hergestellt, indem die Beziehung eines Wortes am Anfang eines Satzes zu einem Wort am Ende gewichtet wird (Query-, Key-, Value-Vektoren). Das Modell löst auf, ob das Wort "Bank" ein Finanzinstitut oder ein Flussufer ist, indem es nur den Kontext des Satzes betrachtet, in dem es vorkommt.

### Kontextfenster (Context Window) und seine Grenzen

- Token-Kapazität: Die maximale Länge, die ein Modell auf einmal lesen und als Antwort generieren kann (z. B. 8K, 32K, 128K oder 1M+ Token).
- Speicherkosten (KV-Cache): Mit zunehmender Kontextlänge steigt der Speicherbedarf der Aufmerksamkeitsmatrix quadratisch an. Um diese Last zu verringern, werden FlashAttention und KV-Cache-Optimierungen eingesetzt.
- Lost-in-the-Middle-Problem: Untersuchungen zeigen, dass LLMs Informationen am Anfang und am Ende langer Texte besser verarbeiten können als Informationen in der Mitte.
- RAG (Retrieval-Augmented Generation): Anstatt Millionen von Seiten an Unternehmensdaten in das Kontextfenster zu quetschen, werden mithilfe einer Suchmaschine oder einer Vektordatenbank nur die für die Abfrage relevantesten Absätze gefiltert und dem Modell als Kontext bereitgestellt.

***Analogie:** Wenn Sie sich mit einem Freund unterhalten und nur sagen: "Ja, das hat er auch gesagt", wird er Sie nicht verstehen; wenn Sie jedoch sagen: "Ich spreche von dem Film, über den wir gestern gesprochen haben", haben Sie den notwendigen Kontext (Context) geliefert.*

## 2. Kontext in Betriebssystemen und Programmierung

In der Systemprogrammierung bezieht sich "Kontext" auf alle Variablen- und Registerwerte, die den aktuellen Zustand eines Programms während seiner Ausführung vollständig widerspiegeln.

### Kontextwechsel (Context Switching)

Ein Betriebssystem, das Multitasking ausführt, verteilt den CPU-Kern auf verschiedene Prozesse und Threads:

1. Die CPU-Register (RAX, RSP, RIP usw.), der Stack-Pointer und die Speicherseiten des laufenden Prozesses werden im Process Control Block (PCB) gespeichert.
2. Die Register des nächsten Prozesses werden in die CPU zurückgeladen.
3. Kosten: Kontextwechsel sind auf Hardwareebene sehr kostspielig, da sie dazu führen, dass die CPU-L1/L2-Caches und die TLB-Adresszuordnungen (Translation Lookaside Buffer) ungültig werden (Cache-Pollution).

### Kontextverwaltung in Programmiersprachen

- Go (context.Context): Wird verwendet, um Abbruchsignale (Cancellation), Fristen (Deadline) und anforderungsbezogene Metadaten zwischen Netzwerkanfragen oder asynchronen Goroutinen zu übertragen.
- Python (with-Blöcke): Kontextmanager machen Ressourcenbereinigungen, wie das Lesen von Dateien oder das Öffnen und Schließen von Datenbankverbindungen, sicher.
- React (Context API): Globale Zustände tief in den Komponentenbaum zu übertragen, ohne Props einzeln durch Zwischenkomponenten weiterreichen zu müssen (ohne Prop Drilling).

## Vergleich: Das Konzept des Kontexts in verschiedenen Disziplinen

| Bereich | Der vom Kontext repräsentierte Wert | Typische Komponenten | Aufgetretene Probleme |
|---|---|---|---|
| Künstliche Intelligenz (LLM) | Eingabeaufforderung + Chat-Verlauf + Dokumente | Token, Attention-Masken, KV-Cache | Token-Limit, Halluzination, Speicherverbrauch |
| Betriebssysteme | Hardware-Momentaufnahme eines Prozesses | Register, Programmzähler, Seitentabellen | CPU-Latenz, Cache-Misses, TLB-Flush |
| Softwareentwicklung | Anfrage-Lebenszyklus und Umgebungsdaten | Timeout-Signal, Autorisierungs-Token | Speicherleck, nicht abgebrochene asynchrone Aufrufe |

## Fragen und Antworten

**Was bedeutet Context und was ist das deutsche Äquivalent?**

Das deutsche Äquivalent ist "Kontext". Es bezeichnet die Bedingungen, den Hintergrund und die Gesamtheit der damit verbundenen ergänzenden Umstände, in denen sich ein Ausdruck, eine Information oder ein Vorgang befindet.

**Was ist der Unterschied zwischen Prompt und Kontext?**

Ein Prompt ist die direkte Eingabe, Frage oder Handlungsanweisung an die KI ("Erkläre diesen Code"). Der Kontext hingegen sind die zusätzlichen Informationen, der vollständige Code, Umgebungsvariablen oder frühere Konversationen, die bereitgestellt werden, damit das Modell diese Anweisung korrekt ausführen kann.

**Warum ist das Context Window (Kontextfenster) begrenzt?**

In der Transformer-Architektur wird jedes Token mit allen anderen Token kreuzverknüpft. Da diese mathematische Berechnung und der gespeicherte Speicher (KV-Cache) quadratisch mit der Kontextlänge zunehmen, stellt der GPU-Speicher eine hardwareseitige Grenze dar.

**Warum führt ein "Context Switch" im Betriebssystem zu einem Leistungsverlust?**

Beim Wechsel von einem Prozess zum anderen muss die CPU die Register speichern, den Speicherbereich des neuen Prozesses laden und die Prozessor-Caches (L1/L2/L3 und TLB) leeren und neu füllen. Dies führt zu einem direkten Prozessorverlust im Bereich von Mikrosekunden.

**Warum wird das context-Paket in der Sprache Go als erster Parameter an jede Funktion übergeben?**

Der Parameter ctx context.Context in Go verhindert die unnötige Verschwendung von Serverressourcen, indem er sicherstellt, dass Datenbankabfragen und Hintergrundaufgaben im Backend gestoppt werden, wenn eine HTTP-Anfrage abgebrochen wird oder ein Timeout auftritt.

## Verwandte Begriffe

- [Context Window](https://trescout.com/de/dictionary/context-window/)
- [Prompt](https://trescout.com/de/dictionary/prompt/)
- [RAG](https://trescout.com/de/dictionary/rag/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)

## Verwandte Werkzeuge

- [REA](https://trescout.com/de/discover/rea/)
- [Servers](https://trescout.com/de/discover/servers/)
- [Goose](https://trescout.com/de/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/de/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/de/discover/openclaude/)
- [Context Mode](https://trescout.com/de/discover/context-mode/)
- [Code Review Graph](https://trescout.com/de/discover/code-review-graph/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/context/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/context/
