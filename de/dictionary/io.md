# Was ist I/O?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> Input/Output

I/O (Input/Output, Eingabe/Ausgabe) ist der Datenaustausch eines Systems mit der Außenwelt.

## Definition und Wortherkunft

Tastatureingabe, heruntergeladene Datei, auf dem Bildschirm ausgegebenes Ergebnis: Alles sind I/O-Operationen. Das System kommuniziert über diesen Kanal mit der Außenwelt. Es ist wie die Sinne und Hände des Computers.

***Analogie:** Es ist wie die Aufnahme von Informationen aus der Außenwelt und die Reaktion darauf durch einen Menschen; die Augen sind der Eingang, die Sprache ist der Ausgang.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Tastatur:** Texteingabe.
**Netzwerk:** Datei-Download.
**Bildschirm:** Ergebnis anzeigen.

## Technische Tiefe und Architektur

Konzepte:

**Blocking:** Warten, bis der Vorgang abgeschlossen ist.
**Non-blocking:** Ohne Warten fortfahren, Bescheid geben, sobald das Ergebnis da ist.
**Puffer:** Zwischenspeicher, der den Geschwindigkeitsunterschied ausgleicht.
**Engpass:** Das langsamste Glied verlangsamt das gesamte System, meistens die Festplatte oder das Netzwerk.

Beispiel für das Lesen von Dateien:

```
const veri = await fs.readFile("not.txt", "utf8");
```

Diese Zeile wartet nicht, bis die Datei da ist, andere Aufgaben laufen weiter. Sobald das Ergebnis bereit ist, wird fortgefahren.

## Einsatz in verschiedenen Disziplinen

**Mensch:** Eingabe über Augen und Ohren, Ausgabe über Sprache.
**Restaurant:** Bestellannahme, Serviceausgabe.
**Fabrik:** Rohmaterialeingang, Produkt Ausgang.

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

- [API](https://trescout.com/de/dictionary/api/)
- [Data Pipeline](https://trescout.com/de/dictionary/data-pipeline/)
- [Streaming Applications](https://trescout.com/de/dictionary/streaming-applications/)

## Verwandte Werkzeuge

- [Asio](https://trescout.com/de/discover/asio/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/io/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/io/
