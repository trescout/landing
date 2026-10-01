# Was ist Virtual Machines?

Eine Virtual Machine (auf Deutsch: virtuelle Maschine) ist ein unabhängiger Computer, der sich die Hardware teilt.

## Definition und Wortherkunft
Virtual bedeutet virtuell. Mehrere Betriebssysteme laufen auf einer einzigen Maschine. Jedes läuft isoliert mit eigenen Ressourcen und beschädigt das Hauptsystem nicht.

## Wie kann man es kennen und im täglichen Leben anwenden?
Moderator: Mandantenfähiges Hosting (Multi-Tenant).Test: Ausprobieren verschiedener Systeme.Entwicklung: Saubere Testumgebung.

## Technische Tiefe und Architektur
Schichten:

## Häufig gemischte Dinge
Wird für einen Container gehalten. Maschine ist ein vollständiges System, Container ist ein geteilter Kernel. Das eine ist eine Wohnung, das andere eine Wohngemeinschaft.

## Einsatz in verschiedenen Disziplinen
Zimmer: Abteile mit unabhängigen Türen.Wohnung: Gemeinsames Gebäude, privater Bereich.Container: Transport mit Fächern.

## Häufig gestellte Fragen
**Verlangsamt es?**
Es gibt einen Overhead. Bei richtiger Dimensionierung fällt er nicht auf.

**Können Viren übertragen werden?**
Im Allgemeinen nein. Die Isolierung ist stark, der freigegebene Ordner wird überwacht.

**Wie viele Ressourcen werden zugewiesen?**
Wird je nach Aufgabe festgelegt. Wird durch Monitoring schrittweise angepasst.

**Was ist der Unterschied zum Container?**
Die virtuelle Maschine transportiert das System, der Container die Anwendung. Isolierung und Geschwindigkeit werden gegeneinander abgewogen.


## Verwandte Begriffe
- [Containers](/de/dictionary/containers/)
- [Runtime](/de/dictionary/runtime/)
- [Self-hosting](/de/dictionary/self-hosting/)

## Verwandte Werkzeuge
- [Container](/de/discover/container/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/virtual-machines/
