# Was ist Durable Execution?

Es handelt sich um ein System, das es ermöglicht, dass ein Prozess sicher dort fortgesetzt werden kann, wo er aufgehört hat, selbst wenn ein Fehler oder eine Unterbrechung vorliegt.

## Definition
Wenn ein Computerprogramm während der Ausführung ausfällt oder ausfällt, wird normalerweise alles gelöscht und Sie müssen von vorne beginnen. Die dauerhafte Ausführung zeichnet jeden Schritt des Programms auf und merkt sich, wo er zum Zeitpunkt der Unterbrechung aufgehört hat. Auf diese Weise können Transaktionen, die Stunden dauern, sicher abgeschlossen werden.

## So funktioniert es
Das System sichert den Status des Programms ständig in einer Datenbank. Wenn ein Fehler auftritt, startet das System den Prozess vom letzten gesicherten Punkt aus neu.

## Wo es eingesetzt wird
Es wird für Banküberweisungen, lange Datenverarbeitungsprozesse und komplexe Workflows mit künstlicher Intelligenz eingesetzt.

## Häufig verwechselt mit
Es kann mit der automatischen Speicherung verwechselt werden, aber dadurch bleibt die gesamte Betriebslogik des Programms erhalten, nicht nur die Datei.

## Häufige Fragen
**Sollte jedes Programm langlebig sein?**
Für kurze Transaktionen wird es nicht benötigt, ist aber für kritische Transaktionen, die mehrere Stunden dauern, unerlässlich.

**Warum ist es so wichtig?**
Im Falle eines Fehlers ist es Zeit- und Geldverschwendung, den gesamten Prozess von vorne zu beginnen.


## Verwandte Begriffe
- [State Management](/de/dictionary/state-management/)
- [Runtime](/de/dictionary/runtime/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/durable-execution/
