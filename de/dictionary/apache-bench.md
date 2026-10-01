# Was ist ApacheBench (ab)?

> Apache HTTP Server Benchmarking Tool

Es handelt sich um ein Befehlszeilentool, das die Leistung und Grenzen von Webservern bei starkem gleichzeitigem Anforderungsverkehr misst.

## Definition
ApacheBench (ab) ist ein leichtes und beliebtes Tool zur Leistungsmessung, mit dem getestet wird, wie viele Anfragen Webserver in einem bestimmten Zeitraum verarbeiten können. Es meldet die Reaktionsfähigkeit des Systems, indem es Hunderte gleichzeitiger Verbindungen mit einem einzigen Befehl über die Befehlszeile initiiert. Es hilft Entwicklern, Serverkonfigurationen und Codeoptimierungen zu überprüfen.

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
- [Benchmark](/de/dictionary/benchmark/)
- [CLI](/de/dictionary/cli/)
- [Concurrency](/de/dictionary/concurrency/)
- [Deployment](/de/dictionary/deployment/)

## Verwandte Werkzeuge
- [HEY](/de/discover/hey/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/apache-bench/
