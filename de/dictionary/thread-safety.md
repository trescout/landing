# Was ist Thread-safety?

Eine Sicherheitsfunktion eines Programms, die verhindert, dass Daten beschädigt werden, wenn mehrere Vorgänge gleichzeitig ausgeführt werden.

## Definition
Computer erledigen viele Dinge gleichzeitig. Wenn zwei verschiedene Prozesse gleichzeitig versuchen, dieselben Daten zu ändern, entsteht Chaos. Mit dieser Funktion können Prozesse aufeinander warten oder nacheinander ausgeführt werden.

## So funktioniert es
Beim Schreiben des Programms werden Regeln für den Datenzugriff festgelegt. Während ein Prozess die Daten nutzt, scheinen die anderen einen „gesperrten“ Status zu haben.

## Wo es eingesetzt wird
Es ist für Bankanwendungen, Webserver und alle Multitasking-Software obligatorisch.

## Häufig verwechselt mit
Es geht nicht nur um Sicherheit (Hacking), sondern auch um die Datenkonsistenz.

## Häufige Fragen
**Was passiert, wenn es nicht threadsicher ist?**
Ihre Daten geraten durcheinander, Apps stürzen ab oder es kommt zu Fehlberechnungen.


## Verwandte Begriffe
- [Concurrency](/de/dictionary/concurrency/)
- [System Programming Language](/de/dictionary/system-programming-language/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/thread-safety/
