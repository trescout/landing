# Was ist Userspace?

Ein sicherer Bereich, in dem Benutzeranwendungen ausgeführt werden, ohne den Kernel des Computers zu beeinträchtigen.

## Definition
Betriebssysteme sind in zwei Hauptteile unterteilt: Kernel und Userspace. Im Userspace werden der Browser, der Musikplayer oder die Code-Editoren ausgeführt, die Sie verwenden. Ein Fehler hier führt nicht zum Absturz des gesamten Computers, sondern betrifft nur diese Anwendung.

## So funktioniert es
Anwendungen fordern vom Kernel die Erlaubnis an, auf die zugrunde liegenden Ressourcen des Systems zuzugreifen. Auf diese Weise wird der Rest des Systems geschützt.

## Wo es eingesetzt wird
Es ist ein grundlegendes Konzept in der Softwareentwicklung, Sicherheit und Systemarchitektur.

## Häufig verwechselt mit
Es wird mit dem Kernel-Space verwechselt; Der Kernel dominiert das gesamte System, während der Benutzerbereich begrenzt ist.

## Häufige Fragen
**Warum gibt es diese Unterscheidung?**
Für Sicherheit und Stabilität; Um zu verhindern, dass Anwendungen das System beschädigen.

**Wo läuft der Code, den ich geschrieben habe?**
Die meisten Anwendungen und Codes werden im Userspace ausgeführt.


## Verwandte Begriffe
- [Runtime](/de/dictionary/runtime/)
- [Containers](/de/dictionary/containers/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/userspace/
