# Was ist Decompiler?

*Glossar · Dev · Zuletzt aktualisiert: 16. September 2026*

Ein Übersetzungstool, das Maschinencode wieder in eine lesbare Programmiersprache umwandelt.

## Definition

Wenn ein Computerprogramm kompiliert wird, wird der für Menschen verständliche Code in Maschinensprache umgewandelt, also in Zahlen, die nur der Prozessor versteht. Ein Decompiler versucht, diesen Prozess umzukehren und diese komplexen und sinnlos erscheinenden Zahlen wieder in ein Quellcodeformat zu bringen, mit dem Entwickler arbeiten können. Dieser Vorgang wird meist dann verwendet, wenn der ursprüngliche Quellcode verloren gegangen ist oder um zu verstehen, wie ein Programm funktioniert.

***Analogie:** Es ist wie eine Übersetzungsmaschine, die ein in einer Fremdsprache geschriebenes Buch wieder in Ihre Muttersprache übersetzt; allerdings kann die Übersetzung manchmal die ursprünglichen Wörter nicht exakt wiedergeben.*

## So funktioniert es

Er nimmt die ausführbare Datei des Programms und analysiert die darin enthaltenen Befehlsfolgen. Anschließend gleicht er diese Befehle mit Programmiersprachenstrukturen ab, die eine ähnliche Funktion haben. Der resultierende Text ist zwar nicht identisch mit dem Originalcode, bietet aber einen Entwurf, der es ermöglicht, die Logik zu verstehen.

## Wo es eingesetzt wird

In der Software-Sicherheitsforschung wird er verwendet, um zu verstehen, wie eine Anwendung funktioniert, oder um alte Software zu aktualisieren, deren Quellcode verloren gegangen ist.

## Häufig verwechselt mit

Er wird oft mit einem Compiler verwechselt; der Compiler übersetzt Code für die Maschine, während der Decompiler Maschinencode für den Menschen übersetzt.

## Häufige Fragen

**Kann ich mit einem Decompiler den exakt gleichen Originalcode erhalten?**

Im Allgemeinen nein; da während der Kompilierung einige Variablennamen und Kommentarzeilen gelöscht werden, kann das Ergebnis etwas komplexer und unbenannt sein.

**Kann jedes Programm dekompiliert werden?**

Technisch gesehen können die meisten dekompiliert werden, aber einige Softwareprogramme sind durch 'Obfuscation', also Code-Verschleierungsmethoden, geschützt, die diesen Prozess erschweren.

## Verwandte Begriffe

- [Compiler](https://trescout.com/de/dictionary/compiler/)
- [Binary](https://trescout.com/de/dictionary/binary/)
- [Software Reverse Engineering](https://trescout.com/de/dictionary/software-reverse-engineering/)

## Verwandte Werkzeuge

- [Ghidra](https://trescout.com/de/discover/ghidra/)
- [ASC](https://trescout.com/de/discover/asc/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/decompiler/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/decompiler/
