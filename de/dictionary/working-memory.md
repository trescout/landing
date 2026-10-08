# Was ist Working Memory in der KI?

> Englisch: Working Memory · Wortherkunft: altenglisch weorc (Werk/Arbeit) + lateinisch memoria (Gedächtnis)

Working Memory (Arbeitsgedächtnis) bezeichnet in der künstlichen Intelligenz den aktiven, temporären Notizbereich innerhalb des Kontextfensters eines Sprachmodells, der zur Ausführung unmittelbarer Denk- und Dialogschritte dient.

## Definition und Wortherkunft
Sie fungiert als die Werkbank des KI-Systems: Sobald eine Anfrage abgeschlossen oder die Sitzung zurückgesetzt wird, leert sich dieser flüchtige Notizspeicher. Das Kontextfenster bildet den Rahmen, während die darin geladenen Tokens den aktiven Arbeitsspeicher darstellen.

## Alltägliche Anwendung und Praxis
Wesentliche Aufgaben des Arbeitsgedächtnisses:

## Technische Tiefe und Architektur
Verwaltung des Token-Budgets:

## Häufig verwechselt mit
Oft wird es mit dem Langzeitgedächtnis verwechselt. Das Langzeitgedächtnis ist eine dauerhafte Vektordatenbank über Sitzungsgrenzen hinweg. Das Arbeitsgedächtnis ist der flüchtige Arbeitsspeicher, der nach Gesprächsende gelöscht wird.

## Interdisziplinäre Perspektiven
Vergleichbare Prinzipien in anderen Lebensbereichen:

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
- [Memory](/de/dictionary/memory/)
- [Context Window](/de/dictionary/context-window/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/working-memory/
