# Was ist Thread Safety?

> Englisch: Thread Safety · Wortherkunft: altenglisch thraed (Faden) + lateinisch salvus (unversehrt/sicher)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-22

Thread Safety (Threadsicherheit) ist die Eigenschaft von Softwarekomponenten, bei gleichzeitigem Zugriff durch mehrere parallele Threads korrekte Ergebnisse zu liefern und den Speicherzustand konsistent zu halten.

## Definition und Wortherkunft
Der Begriff verbindet Thread (Ausführungsfaden eines Prozessors) mit Datensicherheit. Es geht hierbei nicht um Virenschutz oder Hackerabwehr, sondern um algorithmische Datenkonsistenz: Wenn zwei Threads dieselbe Variable zeitgleich ohne Sperren verändern, entstehen fehlerhafte Zwischenstände und Speicherfehler.

## Alltägliche Anwendung und Praxis
Einsatzbereiche mit zwingender Threadsicherheit:
- **Bankensysteme:** Sicherstellung, dass parallele Abbuchungen das Konto nicht unter den Mindestbestand drücken.- **Ticketreservierung:** Ausschluss von Doppelbuchungen desselben Sitzplatzes in Millisekundenabständen.- **Webserver-Engines:** Paralleles Verarbeiten tausender Nutzeranfragen auf gemeinsamen Cache-Speichern.

## Technische Tiefe und Architektur
Architekturmuster für Threadsicherheit:
- **Gegenseitiger Ausschluss (Mutex / Locks):** Garantiert, dass jeweils nur ein Thread den geschützten Codebereich betreten darf.- **Atomare Operationen:** Hardware-Befehle (z. B. CAS), die Lese- und Schreibvorgänge unteilbar in einem Takt ausführen.- **Unveränderlichkeit (Immutability):** Schreibgeschützte Objekte, die beliebig viele Threads ohne Sperren lesen dürfen.- **Rust-Ownership-Modell:** Automatische Verifikation von Speicherzugriffen durch den Compiler zur Compile-Zeit.

## Häufig verwechselt mit
Oft wird Threadsicherheit mit Cybersicherheit verwechselt. Threadsicherheit wehrt keine Angreifer ab, sondern verhindert logische Softwareabstürze durch unkoordinierte Speicherzugriffe paralleler CPU-Kerne.

## Interdisziplinäre Perspektiven
Parallelen aus der Alltagswelt:
- **Straßenverkehr:** Eine einspurige Brücke mit Wechsellichtampel für beide Fahrtrichtungen.- **Gemeinschaftsküche:** Köche, die ein einzelnes Schneidmesser nacheinander statt gleichzeitig greifen.- **Schalterschlange:** Ein Bankschalter, an dem Kunden strikt nacheinander bedient werden.

## Als Analogie
Es ist wie das Abschließen der Tür einer Gemeinschaftstoilette: Solange eine Person drinnen ist, müssen alle anderen draußen warten, bis die Tür wieder freigegeben wird.

## Häufige Fragen

**Welche Folgen hat mangelnde Threadsicherheit?**  
Es kommt zu Race Conditions (Wettlaufsituationen), die zu unbemerkten Datenverfälschungen und sporadischen Abstürzen führen.

**Beseitigen Locks jedes Parallelitätsproblem?**  
Nicht zwingend; unvorsichtiger Lock-Einsatz kann zu Deadlocks führen, bei denen sich Threads gegenseitig dauerhaft blockieren.

**Wie löst Rust das Problem der Threadsicherheit?**  
Durch strikte Ownership- und Borrowing-Prüfungen zur Übersetzungszeit, wodurch Datenwettläufe bereits im Vorfeld ausgeschlossen werden.

**Warum gelten unveränderliche Datenstrukturen als threadsicher?**  
Weil sie nach ihrer Erzeugung nicht mehr modifiziert werden können und gleichzeitiges Lesen keinerlei Konflikte erzeugt.

## Verwandte Begriffe
- [Concurrency](/de/dictionary/concurrency/)
- [System Programming Language](/de/dictionary/system-programming-language/)
- [Mutex](/de/dictionary/mutex/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/thread-safety/
