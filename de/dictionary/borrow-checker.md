# Was ist Borrow Checker?

*Glossar · Dev · Zuletzt aktualisiert: 13. Oktober 2026*

Der Mechanismus, der in der Programmiersprache Rust geschriebene Programme vor Speicherfehlern schützt und die Verwendung von Daten überwacht.

## Definition

Der Borrow Checker ist einer der wichtigsten Bestandteile des Rust-Compilers und garantiert die sichere Verwendung des Speicherbereichs. Er prüft sorgfältig, ob in Ihrem Code mehrere Stellen gleichzeitig auf dieselbe Datenmenge zugreifen und ob die Lebensdauer der Daten ausreicht. Wenn er eine Situation findet, die gegen die Sicherheitsregeln verstößt, lässt er das Programm nicht ausführen und warnt Sie.

***Analogie:** Es ist ein striktes Kontrollbuch in einem sensiblen Labor, das sicherstellt, dass jeweils nur ein Forscher ein spezielles Gerät ausleihen und es nach getaner Arbeit zurückbringen kann.*

## So funktioniert es

Er schaltet sich im Hintergrund ein, wenn Sie versuchen, Ihren Code zu kompilieren. Er überprüft die Eigentumsregeln und Ausleihdauern von Variablen. Wenn er eine regelwidrige Datenfreigabe feststellt, stoppt er die Kompilierung und zeigt an, wo sich der Fehler befindet.

## Wo es eingesetzt wird

Er arbeitet aktiv in der Kompilierungsphase von Rust-Projekten, die in der Systemprogrammierung Speicherlecks und Abstürze von vornherein verhindern möchten.

## Häufig verwechselt mit

Er unterscheidet sich von normalen Debuggern; er arbeitet nicht zur Laufzeit des Programms, sondern während des Schreibens und Kompilierens des Codes.

## Häufige Fragen

**Warum ist er so streng?**

Er greift in einer frühen Phase ein, um Speicherabstürze zur Laufzeit vollständig zu eliminieren.

**Führt er zu einer langsameren Ausführung?**

Nein, er arbeitet nur während der Kompilierungsphase und erzeugt zur Laufzeit keine zusätzlichen Kosten.

## Verwandte Begriffe

- [Rust](https://trescout.com/de/dictionary/rust/)
- [Compiler](https://trescout.com/de/dictionary/compiler/)
- [Thread-safety](https://trescout.com/de/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/de/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/de/dictionary/memory-management/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/borrow-checker/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/borrow-checker/
