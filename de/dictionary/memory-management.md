# Memory Management Stack, Heap, Garbage Collection und OS-Speicher


**Kategorie:** Dev  

**Zuletzt aktualisiert:** 2026-09-19


Speicherverwaltung (Memory Management) bezeichnet das Zusammenspiel von Anwendungscode und Betriebssystem zur effizienten Zuteilung, Überwachung und Freigabe des Arbeitsspeichers (RAM) während der Programmausführung.


## 1. Speicheranatomie: Der Unterschied zwischen Stack und Heap
Ein laufendes Computerprogramm gliedert seinen Arbeitsspeicher in zwei funktionale Bereiche :
- **Stack-Speicher (Stapelspeicher):** Eine hochoptimierte LIFO-Struktur (Last-In, First-Out), die direkt vom Prozessor-Stackpointer (RSP) gesteuert wird. Sie enthält Funktionsaufrufe und lokale Variablen. Speicheranforderung und -freigabe erfolgen extrem schnell und automatisch mit dem Verlassen des Gültigkeitsbereichs.- **Heap-Speicher (Haufenspeicher):** Ein dynamischer Speicherbereich für komplexe Datenstrukturen, deren Lebensdauer oder Größe zur Compile-Zeit unbekannt ist. Die Zuweisung erfolgt über Systemaufrufe (wie malloc oder new) und ist flexibler, aber langsamer als der Stack.

## 2. Drei zentrale Paradigmen der Speicherverwaltung
Moderne Programmiersprachen lassen sich drei Hauptansätzen zuordnen :
- **Manuelle Speicherverwaltung (C, C++):** Entwickler fordern Speicherblöcke per <code>malloc()</code> an und müssen diese diszipliniert mit <code>free()</code> freigeben. Dies erlaubt höchste Performance, birgt jedoch Risiken für Speicherlecks (Memory Leaks) und Sicherheitslücken.- **Automatische Garbage Collection (Java, Go, JavaScript, Python):** Ein Hintergrunddienst (Garbage Collector) analysiert Objektreferenzen und gibt nicht mehr benötigte Speicherblöcke automatisch frei, was mitunter kurze Ausführungspausen verursacht.- **Ownership- und Borrowing-System (Rust):** Rust garantiert Speichersicherheit ohne Garbage Collector, indem der Compiler Eigentumsregeln zur Compile-Zeit prüft und Speicher deterministisch freigibt, sobald eine Variable ihren Gültigkeitsbereich verlässt.

## 3. Betriebssystemebene: Virtueller Speicher und OOM Killer
Unterhalb der Anwendungsprogramme verwaltet der Betriebssystemkern den physikalischen RAM mithilfe der Hardware-MMU (Memory Management Unit) :
- **Virtueller Speicher und Paging:** Jeder Prozess erhält einen isolierten Adressraum, der in 4-KB-Seiten (Pages) unterteilt ist und von der MMU auf reale RAM-Bausteine abgebildet wird.- **Page Faults und Swapping:** Werden Daten angefordert, die temporär auf die Festplatte ausgelagert wurden, löst das Betriebssystem einen Page Fault aus und lädt die Daten zurück in den RAM.- **Out of Memory (OOM) Killer:** Ist der physikalische Speicher restlos erschöpft, beendet der Linux-Kernel über den OOM Killer gezielt speicherintensive Prozesse, um einen totalen Systemabsturz abzuwenden.

## Im Vergleich
Stack-Speicher ist wie ein Stapel Teller, von dem man blitzschnell den obersten Teller nimmt oder ablegt; Heap-Speicher gleicht einer großen Lagerhalle, in der man Kisten beliebiger Größe anmietet und den Überblick behalten muss, um nichts zu vergessen.

## Häufig gestellte Fragen

**Was ist der Hauptunterschied zwischen Stack und Heap?**  
Der Stack ist blitzschnell, automatisch und an Funktionsblöcke gebunden; der Heap ist flexibel und groß, erfordert aber manuelle Pflege oder einen Garbage Collector.

**Was versteht man unter einem Speicherleck (Memory Leak)?**  
Ein Fehler, bei dem angeforderter Heap-Speicher nach Gebrauch nicht freigegeben wird, sodass der RAM-Verbrauch stetig ansteigt, bis das Programm abstürzt.

**Wie erreicht Rust Speichersicherheit ohne Garbage Collector?**  
Durch das Ownership- und Borrow-Checker-Prinzip, bei dem der Compiler bereits beim Übersetzen den genauen Zeitpunkt der Speicherfreigabe festlegt.

**Welche Aufgabe hat der Linux OOM Killer?**  
Er beendet gezielt speicherintensive Programme, wenn der gesamte Arbeitsspeicher belegt ist, um das Einfrieren des Betriebssystems zu verhindern.

## Verwandte Begriffe
- [Runtime](/de/dictionary/runtime/)
- [State Management](/de/dictionary/state-management/)
- [Serialization](/de/dictionary/serialization/)
- [Network Stack](/de/dictionary/network-stack/)
- [Assembly](/de/dictionary/assembly/)

---
Quelle: TreScout Technik-Glossar · https://trescout.com/de/dictionary/memory-management/
