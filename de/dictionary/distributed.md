# Distributed Systems Irrtümer, CAP-Theorem, Konsens und Saga-Muster


**Kategorie:** Dev  

**Zuletzt aktualisiert:** 2026-09-19


Ein verteiltes System (Distributed System) ist ein Verbund unabhängiger Rechnerknoten, die über ein Computernetzwerk kommunizieren und zusammenarbeiten, um für den Anwender wie ein einziges, konsistentes Gesamtsystem zu wirken.


## Etymologie und das Wesen verteilter Systeme
Der Begriff stammt vom lateinischen *distribuere* (aufteilen, zuteilen). Treffend beschrieb es Leslie Lamport : *«Ein verteiltes System ist ein System, bei dem der Ausfall eines Computers, von dessen Existenz man nicht einmal wusste, den eigenen Rechner lahmlegen kann.»* Sie bieten Ausfallsicherheit und Skalierbarkeit um den Preis höherer Komplexität.

## Die 8 Irrtümer verteilter Systeme (Deutsch)
Diese von Sun-Microsystems-Ingenieuren formulierten Fehlannahmen führen bei Nichtbeachtung zum Scheitern von Großprojekten :
- Das Netzwerk ist zuverlässig.
- Die Latenzzeit ist gleich null.
- Die Bandbreite ist unendlich.
- Das Netzwerk ist sicher.
- Die Netzwerktopologie ändert sich nie.
- Es gibt nur einen einzigen Administrator.
- Die Transportkosten sind gleich null.
- Das Netzwerk ist homogen.

## Das CAP-Theorem und das PACELC-Modell
Eric Brewers **CAP-Theorem** belegt, dass verteilte Datenbanken bei einer Netzwerkpartitionierung nur zwei von drei Garantien einhalten können :
- **Konsistenz (C):** Jeder Lesezugriff liefert den neuesten Schreibwert oder einen Fehler.- **Verfügbarkeit (A):** Jeder intakte Knoten antwortet ohne Ausfallgarantie auf aktuelle Daten.- **Partitionstoleranz (P):** Das System übersteht Netzwerktrennungen. Da Netzwerkfehler unausweichlich sind, muss man zwischen CP (z. B. etcd) und AP (z. B. Cassandra) wählen.
Das **PACELC-Modell** erweitert dies : *Tritt eine Partition (P) auf, wähle zwischen Verfügbarkeit (A) und Konsistenz (C) ; andernfalls (Else) wähle zwischen Latenz (L) und Konsistenz (C).*

## Konsensprotokolle: Raft und Paxos
Um bei Übertragungsfehlern eine verbindliche gemeinsame Wahrheit herzustellen :
- **Paxos:** Der mathematisch bewiesene Urvater aller Konsensalgorithmen von Leslie Lamport, berüchtigt für seine schwierige Implementierung.- **Raft:** Speziell auf Verständlichkeit hin entwickelt, zerlegt es Konsens in Leader-Wahl, Log-Replikation und Zustandssicherheit (Herzstück von etcd).

## Das Zeitproblem und logische Uhren
Ohne gemeinsame Atomuhr ist das Bestimmen der exakten zeitlichen Reihenfolge von Ereignissen über Netze hinweg physikalisch unmöglich :
- **Lamport- und Vektor-Uhren:** Abstrakte Zähler, die kausale Abhängigkeiten abbilden, ohne reale Sekunden messen zu müssen.- **Google TrueTime:** Eine Kombination aus Atomuhren und GPS-Empfängern in Rechenzentren, die Zeitunsicherheiten auf wenige Millisekunden eingrenzt.

## Verteiltes Datenmanagement: Das Saga-Pattern
Das veraltete Two-Phase-Commit-Verfahren (2PC) blockiert Ressourcen und skaliert nicht. Moderne Architekturen nutzen das **Saga-Pattern** :
- Eine Abfolge lokaler Datenbanktransaktionen, koordiniert durch einen zentralen Orchestrator oder über Event-Choreografie.
- Schlägt ein Teilschritt fehl, führt das System rückwärts kompensierende Transaktionen aus, um den Ausgangszustand sauber wiederherzustellen.

## Im Vergleich
Ein zentralisiertes System ist wie ein einzelner Koch in einem Foodtruck; ein verteiltes System gleicht einer weltweiten Restaurantkette, in der hunderte Küchen die gleichen Menüs servieren müssen, während Telefonverbindungen ausfallen und Lieferanten im Stau stehen.

## Häufig gestellte Fragen

**Was zeichnet ein verteiltes System aus?**  
Dass mehrere eigenständige Rechner über ein Netzwerk Aufgaben gemeinsam bearbeiten und nach außen wie ein einziger Computer auftreten.

**Warum kann man laut CAP-Theorem nicht Konsistenz und Verfügbarkeit gleichzeitig haben?**  
Weil man bei einer gekappten Verbindung zwischen Servern entweder Anfragen ablehnen muss (Ausfall) oder inkonsistente Daten riskiert.

**Worin liegt der Vorteil von Raft gegenüber Paxos?**  
Raft wurde gezielt daraufhin entworfen, für Softwareentwickler leicht verständlich und fehlerfrei implementierbar zu sein.

**Wie funktioniert das Saga-Pattern?**  
Es unterteilt Geschäftsprozesse in lokale Transaktionen und führt bei Fehlern Ausgleichsoperationen durch, um globale Datenbanksperren zu vermeiden.

## Verwandte Begriffe
- [Cloud Computing](/de/dictionary/cloud-computing/)
- [Network Stack](/de/dictionary/network-stack/)
- [Deployment](/de/dictionary/deployment/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Elasticsearch](/de/discover/elasticsearch/)
- [Cassandra](/de/discover/cassandra/)

---
Quelle: TreScout Technik-Glossar · https://trescout.com/de/dictionary/distributed/
