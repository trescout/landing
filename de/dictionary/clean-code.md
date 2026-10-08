# Was ist Clean Code?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Sauberer Code ist der Code, der von Menschen gelesen werden kann.

## Definition und Wortherkunft

Die Maschine führt jeden Code aus, ein Mensch kann nicht jeden Code lesen. Aussagekräftiger Name, kleine Funktion und einfacher Ablauf sorgen für Lesbarkeit. Robert Martin ist der Referenzname dieser Disziplin.

***Analogie:** Es ist, als hätte man die Regale einer Bibliothek nach Genre und Autor geordnet.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Team:** Gemeinsame Codebasis.
**Überprüfung:** Lesbarkeitsprüfung.
**Pflege:** Zurückkehren zum alten Code.

## Technische Tiefe und Architektur

Grundsätze:

**Name:** Der Name, der die Absicht ausdrückt.
**Dimension:** Einzeljobfunktion.
**Wieder:** Das gemeinsame Stück befindet sich an einem Ort.

Beispiel:

```
# önce
def h(a, b):
    return a + a*b
# sonra
def indirimli_fiyat(fiyat, oran):
    return fiyat + fiyat * oran
```

Regel: Das Ausführen von Code ist der erste Schritt, das Lesen von Code ist der zweite Schritt.

## Einsatz in verschiedenen Disziplinen

**Tisch:** Aufgeräumter Arbeitsbereich.
**Regale:** Sortiert nach Genre und Autor.
**Garten:** Beschnittene Zweiganordnung.

## Häufig gestellte Fragen

**Reicht es nicht, um zu arbeiten?**

Es ist nicht genug. Arbeitscode speichert heute, gelesener Code speichert morgen.

**Verlangsamt es?**

Am Anfang ja, in der Wartung nein. Es bringt insgesamt Geld ein.

**Wie wird es gemessen?**

Mit Überprüfungszeit und Fehlerquote. Zahl allein reicht nicht aus.

**Wo soll ich anfangen?**

Aus Name und Funktion. Der berührte Code wird gelöscht.

## Verwandte Begriffe

- [Refactoring](https://trescout.com/de/dictionary/refactoring/)
- [Unit Testing](https://trescout.com/de/dictionary/unit-testing/)
- [Engineering Skills](https://trescout.com/de/dictionary/engineering-skills/)

## Verwandte Werkzeuge

- [Clean Code Javascript](https://trescout.com/de/discover/clean-code-javascript/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/clean-code/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/clean-code/
