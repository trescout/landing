# Was ist Working Memory in der KI?

*Glossar · AI · Zuletzt aktualisiert: 22. September 2026*

> Englisch: Working Memory · Wortherkunft: altenglisch weorc (Werk/Arbeit) + lateinisch memoria (Gedächtnis)

Working Memory (Arbeitsgedächtnis) bezeichnet in der künstlichen Intelligenz den aktiven, temporären Notizbereich innerhalb des Kontextfensters eines Sprachmodells, der zur Ausführung unmittelbarer Denk- und Dialogschritte dient.

## Definition und Wortherkunft

Sie fungiert als die Werkbank des KI-Systems: Sobald eine Anfrage abgeschlossen oder die Sitzung zurückgesetzt wird, leert sich dieser flüchtige Notizspeicher. Das Kontextfenster bildet den Rahmen, während die darin geladenen Tokens den aktiven Arbeitsspeicher darstellen.

## Alltägliche Anwendung und Praxis

Wesentliche Aufgaben des Arbeitsgedächtnisses:

- **Dialogführung:** Erinnerung an vorherige Fragen und Antworten im laufenden Gespräch.
- **Denk-Zwischenschritte:** Festhalten von Zwischenergebnissen bei schrittweisen Logikketten (Chain-of-Thought).
- **Tool-Integration:** Temporäres Aufnehmen von Schnittstellen-Rückmeldungen vor Ausgabe der finalen Antwort.

## Technische Tiefe und Architektur

Verwaltung des Token-Budgets:

- **Kapazitätsgrenzen:** Fasst das Fenster 128.000 Tokens und belegt der bisherige Verlauf 100.000, verbleiben 28.000 Tokens für Überlegung und Antwort.
- **KV-Cache:** Transformers speichern vorberechnete Aufmerksamkeitswerte im Grafikspeicher, um Neuberechnungen pro Wort zu vermeiden.
- **Verdrängungsstrategien:** Nähert sich das Limit, fasst das System frühere Abschnitte zusammen oder blendet alte Nachrichten aus.

## Häufig verwechselt mit

Oft wird es mit dem Langzeitgedächtnis verwechselt. Das Langzeitgedächtnis ist eine dauerhafte Vektordatenbank über Sitzungsgrenzen hinweg. Das Arbeitsgedächtnis ist der flüchtige Arbeitsspeicher, der nach Gesprächsende gelöscht wird.

## Interdisziplinäre Perspektiven

Vergleichbare Prinzipien in anderen Lebensbereichen:

- **Mathematik:** Das Schmierblatt für Nebenrechnungen während einer Prüfung, das danach im Papierkorb landet.
- **Werkstatt:** Die Werkbank, auf der Einzelteile während des Zusammenbaus liegen und die abends aufgeräumt wird.
- **Computertechnik:** Schnelle CPU-Register und L1-Cache im Vergleich zur Festplatte.

*Es ist wie ein Notizzettel, auf dem man Zwischenschritte beim Lösen einer schweren Matheaufgabe notiert; ist die Lösung gefunden, wirft man den Zettel weg.*

## Häufige Fragen

**Was geschieht bei einem vollen Arbeitsgedächtnis?**

Das Modell muss frühere Dialogteile kürzen oder zusammenfassen, um nicht den Faden zu verlieren.

**Worin unterscheidet es sich von den Trainingsgewichten?**

Gewichte sind das permanente Wissen aus dem Training; das Arbeitsgedächtnis enthält nur die aktuellen Wörter der laufenden Eingabe.

**Kann man das Arbeitsgedächtnis beliebig vergrößern?**

Nein, da der Rechenaufwand stark ansteigt und Modelle bei extrem langen Texten relevante Fakten in der Textmitte übersehen können.

**Welche Funktion erfüllt der KV-Cache?**

Er speichert die Berechnungen bereits verarbeiteter Wörter im GPU-Speicher und verhindert zeitraubende Doppelberechnungen.

## Verwandte Begriffe

- [Memory](https://trescout.com/de/dictionary/memory/)
- [Context Window](https://trescout.com/de/dictionary/context-window/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/working-memory/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/working-memory/
