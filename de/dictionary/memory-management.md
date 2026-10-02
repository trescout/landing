# Was ist Memory Management?

Beim Speichermanagement handelt es sich um den Prozess der Zuteilung des physischen und virtuellen Arbeitsspeichers (RAM) des Computers unter laufender Software, dessen Schutz und die Rückgabe an das System nach Beendigung der Nutzung.

## 1. Gedächtnisanatomie: Stack- und Heap-Unterscheidung
Wenn ein Programm ausgeführt wird, weist das Betriebssystem diesem Prozess einen speziellen virtuellen Speicherraum (Virtual Address Space) zu. Die beiden wichtigsten Komponenten dieses Bereichs sind Stack und Heap:

## 2. Drei grundlegende Speicherverwaltungsparadigmen

## 3. Speicher auf Betriebssystemebene: Virtueller Speicher und OOM Killer
Moderne Betriebssysteme nutzen eine virtuelle Speicher- und Paging-Architektur, um zu verhindern, dass Programme den Speicher anderer Programme auslesen. Die Memory Management Unit (MMU) in der CPU wandelt mithilfe des TLB-Cache virtuelle Adressen in physische Adressen in der Hardware um. Wenn physischer RAM und Swap vollständig erschöpft sind, beendet der OOM-Killer-Mechanismus (Out of Memory Killer) des Linux-Kernels den aggressivsten Prozess mit SIGKILL, um das System zu retten.

## Häufige Fragen
**Was bedeutet Speicherverwaltung? Was ist das türkische Äquivalent?**
Memory Management bedeutet auf Türkisch „Speicherverwaltung“. Dabei handelt es sich um den gesamten Prozess der Zuweisung, Überwachung und Freigabe von RAM-Ressourcen während der Ausführung eines Computerprogramms.

**Was ist der Hauptunterschied zwischen Stack und Heap?**
Verwaltet lokale Variablen, deren Stapelgröße zur Kompilierzeit bekannt ist, mit LIFO-Logik extrem schnell; Heap hingegen ist ein flexibler Speicherpool, der für zur Laufzeit dynamisch wachsende Objekte reserviert ist und komplexer zu verwalten ist.

**Wie funktioniert die Garbage Collection?**
In Sprachen, in denen der Softwareentwickler nicht manuell löscht (Java, Go, JS usw.), erkennt die im Hintergrund laufende Engine verwaiste Objekte, die nicht über die Stammvariablen erreicht werden können, und löscht den RAM.

**Wie kann ein Speicherverlust verhindert werden?**
In manuellen Sprachen, indem Sie für jeden Malloc ein kostenloses Malloc schreiben oder RAII-Muster einrichten; In Sprachen mit Garbage Collectors werden globale Array-Referenzen und Ereignis-Listener, die nicht geschlossen sind, gelöscht und verhindert.


## Verwandte Begriffe
- [Runtime](/de/dictionary/runtime/)
- [State Management](/de/dictionary/state-management/)
- [Serialization](/de/dictionary/serialization/)
- [Network Stack](/de/dictionary/network-stack/)
- [Assembly](/de/dictionary/assembly/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/memory-management/
