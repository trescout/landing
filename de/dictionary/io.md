# Was ist I/O?

> Input/Output

I/O (Input/Output, Eingabe/Ausgabe) ist der Datenaustausch eines Systems mit der Außenwelt.

## Definition und Wortherkunft
Tastatureingabe, heruntergeladene Datei, auf dem Bildschirm ausgegebenes Ergebnis: Alles sind I/O-Operationen. Das System kommuniziert über diesen Kanal mit der Außenwelt. Es ist wie die Sinne und Hände des Computers.

## Wie kann man es kennen und im täglichen Leben anwenden?
Tastatur: Texteingabe.Netzwerk: Datei-Download.Bildschirm: Ergebnis anzeigen.

## Technische Tiefe und Architektur
Konzepte:

## Einsatz in verschiedenen Disziplinen
Mensch: Eingabe über Augen und Ohren, Ausgabe über Sprache.Restaurant: Bestellannahme, Serviceausgabe.Fabrik: Rohmaterialeingang, Produkt Ausgang.

## Häufig gestellte Fragen
**Warum ist E/A ein Engpass?**
Der Prozessor ist schnell, Festplatte und Netzwerk sind langsam. Wenn die Daten nicht nachkommen, wartet das System, hier entsteht der Engpass.

**Was ist Blocking?**
Es ist ein Aufruf, der wartet, bis das Ergebnis da ist. Er blockiert die Benutzeroberfläche und verschwendet Arbeit auf dem Server.

**Wie wird es beschleunigt?**
Durch Caching, Batch-Lesen und asynchrone Aufrufe. Zuerst wird gemessen, dann wird das schwächste Glied behoben.

**Was hat das mit Async zu tun?**
Es ist ein System, bei dem während des Wartens andere Arbeit erledigt wird. Mit einem einzigen Thread wird viel Arbeit bewältigt.


## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [Data Pipeline](/de/dictionary/data-pipeline/)
- [Streaming Applications](/de/dictionary/streaming-applications/)

## Verwandte Werkzeuge
- [Asio](/de/discover/asio/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/io/
