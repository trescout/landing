# Was ist Compiler?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Ein Compiler ist ein Programm, das den von Ihnen geschriebenen Code in Maschinensprache übersetzt, die der Computer ausführen kann.

## Definition und Wortherkunft

Compile bedeutet übersetzen oder sammeln. Computer verstehen ausschließlich Sequenzen aus 0 und 1. Entwickler schreiben jedoch in einer lesbaren Sprache. Der Compiler fungiert als Übersetzer zwischen diesen beiden Welten: Er durchdringt den Code und wandelt ihn bei Fehlerfreiheit in eine ausführbare Datei um.

***Analogie:** Es ist, als würde man ein auf Englisch verfasstes Rezept in schriftliche Anweisungen für einen Koch umwandeln, der kein Englisch spricht, und zwar in einer Sprache, die er verstehen kann.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Anwendungsinstallation:** Die kompilierte Version des heruntergeladenen Programms wird ausgeführt.
**Fehlermeldungen:** Der Compiler warnt Sie, wenn Sie ein Semikolon vergessen haben.
**Spiel-Engines:** Separate Kompilierungsausgabe für jede Plattform.

## Technische Tiefe und Architektur

Die Kompilierung läuft in vier Phasen ab:

**Lexikalische und syntaktische Analyse:** Der Code wird in Fragmente zerlegt, die Satzstruktur wird herausgearbeitet.
**Semantische Prüfung:** Es wird nach undefinierten Variablen und Typeninkompatibilitäten gesucht.
**Optimierung:** Äquivalenter, aber schnellerer Code wird erzeugt.
**Code-Generierung:** Prozessorspezifischer Maschinencode wird geschrieben.

Die Kompilierung in der Sprache C sieht wie folgt aus:

```
gcc merhaba.c -o merhaba
./merhaba
```

Die erste Zeile übersetzt, die zweite führt aus. Der Interpreter hingegen führt zeilenweise aus und erzeugt keine separate Ausgabedatei.

## Einsatz in verschiedenen Disziplinen

**Interpretation:** Die Unterscheidung zwischen simultaner Übersetzung (Interpreter) und schriftlicher Übersetzung (Compiler).
**Druckerei:** Umwandlung des Entwurfs in eine Druckplatte.
**Küche:** Verwandlung des Rezepts in ein bereits zubereitetes Gericht.

## Häufig gestellte Fragen

**Ist der Compiler jeder Sprache unterschiedlich?**

Ja. Jede Sprache benötigt einen Compiler oder Interpreter, der ihren eigenen Regeln entspricht. Einige Sprachen verwenden beides zusammen.

**Worin besteht der Unterschied zum Interpreter?**

Ein Compiler übersetzt den Code im Voraus und erzeugt eine Datei, danach läuft das Programm schnell. Ein Interpreter übersetzt Zeile für Zeile und führt ihn aus, er ist flexibel, aber normalerweise langsam.

**Was ist JIT?**

Just-in-Time-Kompilierung übersetzt während der Laufzeit häufig verwendete Teile in Maschinencode. Das ist ein Mittelweg zwischen beiden, den Java und JavaScript nutzen.

**Wer hat den ersten Compiler kompiliert?**

Das ist die Frage nach dem Huhn und dem Ei. Die ersten Compiler wurden manuell in Maschinencode geschrieben, spätere wurden mit dem vorherigen Compiler kompiliert (Bootstrapping).

## Verwandte Begriffe

- [Rust](https://trescout.com/de/dictionary/rust/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Compile-time](https://trescout.com/de/dictionary/compile-time/)

## Verwandte Werkzeuge

- [Llvm Project](https://trescout.com/de/discover/llvm-project/)
- [SWC](https://trescout.com/de/discover/swc/)
- [FMT](https://trescout.com/de/discover/fmt/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/compiler/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/compiler/
