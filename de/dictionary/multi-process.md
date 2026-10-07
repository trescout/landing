# Was ist Multi-process?

Es ist eine Methode, bei der ein Computerprogramm seine Aufgaben in mehrere völlig unabhängige, jeweils über einen eigenen Speicherbereich verfügende Unterprozesse aufteilt und diese gleichzeitig ausführt.

## Definition
In der herkömmlichen Programmierung läuft eine Anwendung in der Regel sequenziell über einen einzigen Ausführungspfad ab. Bei dem Multi-Prozess-Ansatz erstellt das Betriebssystem hingegen für jede Aufgabe einen separaten Arbeitsbereich. Dank dieser Methode, auf die Sie im TreScout-Glossar häufig stoßen werden, läuft der Betrieb der übrigen Prozesse unbeeinträchtigt weiter, selbst wenn einer von ihnen fehlschlägt und abstürzt.

## So funktioniert es
Auf Betriebssystemebene wird für jeden Prozess eine eigene Speicheradresse zugewiesen. Das Programm leitet aus einem Hauptprozess neue Unterprozesse ab, und diese Prozesse kommunizieren über spezielle Kommunikationskanäle miteinander, um Aufgaben aufzuteilen.

## Wo es eingesetzt wird
Es wird besonders häufig dort eingesetzt, wo jeder Tab in Webbrowsern als separater Prozess ausgeführt wird, in Systemen zur Verarbeitung großer Datenmengen und in Serveranwendungen, die im Hintergrund schwere Berechnungen durchführen.

## Häufig verwechselt mit
Es wird oft mit dem Konzept des Multi-Threding verwechselt. Während beim Multi-Threading Aufgaben durch leichtgewichtige Threads erledigt werden, die sich denselben Speicherbereich teilen, hat beim Multi-Prozess-Verfahren jede Aufgabe ihren eigenen, vollständig isolierten Speicherbereich.

## Häufige Fragen
**Belastet die Verwendung von Multi-Prozess den Computer?**
Ja, da für jeden Prozess separater Speicher und Ressourcen zugewiesen werden, kann dies im Vergleich zu anderen Methoden mehr Computerressourcen verbrauchen.

**In welchen Situationen sollte Multi-Prozess bevorzugt werden?**
Es sollte bei schweren Aufgaben bevorzugt werden, bei denen Sicherheit und Stabilität im Vordergrund stehen und bei denen verhindert werden soll, dass das Scheitern des einen Prozesses die anderen beeinträchtigt.


## Verwandte Begriffe
- [Concurrency](/de/dictionary/concurrency/)
- [Runtime](/de/dictionary/runtime/)
- [Thread-safety](/de/dictionary/thread-safety/)
- [Distributed](/de/dictionary/distributed/)

## Verwandte Werkzeuge
- [Raddebugger](/de/discover/raddebugger/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/multi-process/
