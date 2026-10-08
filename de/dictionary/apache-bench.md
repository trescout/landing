# Was ist ApacheBench (ab)?

*Glossar · Dev · Zuletzt aktualisiert: 29. September 2026*

> Apache HTTP Server Benchmarking Tool

Es handelt sich um ein Befehlszeilentool, das die Leistung und Grenzen von Webservern bei starkem gleichzeitigem Anforderungsverkehr misst.

## Definition

ApacheBench (ab) ist ein leichtes und beliebtes Tool zur Leistungsmessung, mit dem getestet wird, wie viele Anfragen Webserver in einem bestimmten Zeitraum verarbeiten können. Es meldet die Reaktionsfähigkeit des Systems, indem es Hunderte gleichzeitiger Verbindungen mit einem einzigen Befehl über die Befehlszeile initiiert. Es hilft Entwicklern, Serverkonfigurationen und Codeoptimierungen zu überprüfen.

***Analogie:** Das ist, als würde man 500 Kunden gleichzeitig an die Tür eines Ladens schicken und mit einer Stoppuhr messen, wie viele Leute die Kassierer pro Minute abschneiden können und wie lang die Warteschlange wird.*

## So funktioniert es

Der Benutzer bestimmt die Zieladresse, die über das Terminal getestet werden soll, die Gesamtzahl der Anfragen und die Anzahl der gleichzeitig zu öffnenden Verbindungen (Parallelität). Das Tool leitet identifizierte Anfragen schnell an den Server weiter, erfasst Antwortzeiten und stellt grundlegende Kennzahlen wie Anfragen pro Sekunde (RPS) in tabellarischer Form dar.

## Wo es eingesetzt wird

Es wird bei Auslastungstests vor dem Start der Website, bei Server-Hardware-Vergleichen und bei der Erfolgsmessung von Cache-Optimierungen eingesetzt.

## Häufig verwechselt mit

Im Gegensatz zu fortschrittlichen Lasttest-Tools, die komplexe Benutzerszenarien simulieren, konzentriert es sich nur auf das sequentielle oder gleichzeitige Laden von Lasten auf einer bestimmten HTTP-Verbindung.

## Häufige Fragen

**Ist für die Verwendung von ApacheBench ein Apache-Webserver erforderlich?**

Nein. Es kann eigenständig ausgeführt werden, um Nginx, Node.js oder einen beliebigen HTTP-Server zu testen.

**Welcher Wert wird in Testergebnissen am häufigsten betrachtet?**

Die Anzahl der pro Sekunde abgeschlossenen Anfragen (Anfragen pro Sekunde) und die Antwortverzögerungszeiten in Millisekunden sind die kritischsten Indikatoren.

## Verwandte Begriffe

- [Benchmark](https://trescout.com/de/dictionary/benchmark/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Concurrency](https://trescout.com/de/dictionary/concurrency/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)

## Verwandte Werkzeuge

- [HEY](https://trescout.com/de/discover/hey/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/apache-bench/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/apache-bench/
