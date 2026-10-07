# Was ist Local-first Memory?

> Lokale Speicherarchitektur

Local-first Memory (lokal-prioritärer Speicher) ist ein Software-Architekturmuster, bei dem die primären Daten und der Anwendungszustand direkt auf dem Endgerät des Nutzers gespeichert werden, während die Cloud lediglich zur optionalen Replikation dient.

## Definition und Wortherkunft
Im Gegensatz zu herkömmlichen Cloud-Anwendungen, die ohne aktive Internetverbindung unbenutzbar werden, garantiert der Local-First-Ansatz verzögerungsfreie Reaktionszeiten und uneingeschränkte Offline-Fähigkeit. Datenhoheit und Primärspeicherung liegen auf dem lokalen Rechner.

## Alltägliche Anwendung und Praxis
Wissensmanagement und Notizen: Werkzeuge wie Obsidian oder Logseq, die Markdown-Dateien nativ auf dem lokalen Dateisystem ablegen.Kollaborative Arbeitsflächen: Diagramm- und Designtools, die offline funktionieren und Änderungen beim Wiederverbinden zusammenführen.Lokaler KI-Kontext: Speicherung von Chatverläufen und Vektordatenbanken auf dem Gerät zum Schutz sensibler Daten.

## Technische Tiefe und Architektur
Technische Kernkomponenten:

## Häufig verwechselt mit
Wird häufig mit einfachem Offline-Caching verwechselt. Caching ist lediglich eine flüchtige Notfallkopie, deren Autorität bei der Cloud liegt; bei Local-First ist das lokale Gerät die maßgebliche Datenquelle.

## Interdisziplinäre Perspektiven
Finanzen: Bargeld im eigenen Tresor verwahren vs. ausschließliche Nutzung von Online-Bankkonten.Schreiben: Notizen in einem handgebundenen Notizbuch festhalten vs. Texte in einem Web-Editor tippen.Werkstatt: Eigene Handwerkzeuge im Keller griffbereit haben vs. Werkzeuge bei jedem Einsatz anmieten.

## Häufige Fragen
**Warum gewinnt der Local-First-Ansatz zunehmend an Bedeutung?**
Er verhindert Cloud-Ausfälle, garantiert extrem schnelle Benutzeroberflächen und schützt die Privatsphäre ohne Kompromisse.

**Wie funktioniert die Zusammenarbeit mehrerer Nutzer?**
Über CRDTs (Conflict-free Replicated Data Types), die Bearbeitungskonflikte ohne manuelles Eingreifen mathematisch sauber lösen.

**Kommen bei Local-First überhaupt noch Server zum Einsatz?**
Ja, Server fungieren als verschlüsselte Vermittler und Backups, besitzen jedoch keine Datenhoheit.

**Welche Datenbank-Technologien treiben diese Apps an?**
SQLite (WASM), RxDB, PGlite, ElectricSQL sowie IndexedDB in Kombination mit Yjs oder Automerge.


## Verwandte Begriffe
- [Persönliche Cloud](/de/dictionary/personal-cloud/)
- [Runtime](/de/dictionary/runtime/)
- [Digitale Privatsphäre](/de/dictionary/digital-privacy/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/local-first-memory/
