# Was ist Thread-safety?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Thread Safety (auf Türkisch İş Parçacığı Güvenliği), bedeutet, dass Code Daten nicht beschädigt, wenn er gleichzeitig von mehreren Threads ausgeführt wird.

## Definition und Wortherkunft

Thread bedeutet Thread, safety hingegen Sicherheit. Die Sicherheit bedeutet hier nicht den Schutz vor Hackern, sondern dass die Daten konsistent bleiben: Wenn zwei Prozesse dasselbe Konto zur gleichen Zeit aktualisieren, kann das Ergebnis falsch sein. Thread-sicherer Code regelt dieses Wettrennen. Bankanwendungen, Webserver und alle Software mit mehreren Prozessoren benötigen dies.

***Analogie:** Es ist wie ein Schloss an der Tür in einem Haus mit nur einer Toilette; während jemand drin ist, muss der andere warten.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Bankwesen:** Zwei Auszahlungsanfragen vom selben Konto führen nicht dazu, dass der Saldo negativ wird.
**Ticketverkauf:** Der letzte Sitzplatz sollte nicht an zwei Personen gleichzeitig verkauft werden.
**Zähler:** Der Besucherzähler erhöht sich mit jeder Anfrage um ein volles Inkrement.

## Technische Tiefe und Architektur

Typische Werkzeuge sind:

**Sperren (Mutex/Sperren):** Ein Thread betritt jeweils den kritischen Bereich, der andere wartet.
**Atomare Operation:** Unteilbares Lesen und Schreiben in einem Schritt.
**Unveränderliche Daten:** Daten, die nicht geändert werden können, kommen nicht ins Rennen, sie werden kopiert.
**Messaging:** Kommunikation über eine Warteschlange statt gemeinsamer Daten (z. B. Go-Channels).

Ein kleines Python-Beispiel:

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

Während gesperrte Zeilen ausgeführt werden, kann sich kein anderer Thread dazumischen. Wenn eine Sperre vergessen oder in falscher Reihenfolge erworben wird, kann das Programm hängen bleiben (Deadlock). Aus diesem Grund wird der kritische Bereich kurz gehalten.

## Häufig gemischte Dinge

Es hat nichts mit Cybersicherheit zu tun. Es geht nicht um Hacker, sondern um Datenkonsistenz: Dass zwei Prozesse, die gleichzeitig auf dieselbe Datum zugreifen, sich nicht gegenseitig überschreiben.

## Einsatz in verschiedenen Disziplinen

**Verkehr:** Ampeln, die die Reihenfolge der Überquerung auf einer einspurigen Brücke regeln.
**Küche:** Köche, die sich abwechselnd ein einziges Messer teilen.
**Bibliothek:** Das Weiterreichen eines einzigen Buch-Exemplars über das Ausleihbuch.

## Häufig gestellte Fragen

**Was passiert, wenn es nicht threadsicher ist?**

Daten werden vermischt, Berechnungen schlagen fehl oder die Anwendung stürzt ab. Da der Fehler nicht bei jedem Durchlauf auftritt, ist er schwer zu debuggen.

**Sollte jedem Code eine Sperre hinzugefügt werden?**

Nein. In Single-Thread-Code verursacht eine Sperre unnötigen Overhead. Nur gleichzeitige Abschnitte, die auf gemeinsame Daten zugreifen, werden geschützt.

**Was ist ein Deadlock und wie wird er vermieden?**

Es liegt vor, wenn zwei Prozesse aufeinander warten und blockiert werden. Das stets gleichzeitige Anfordern von Sperren und das Halten des kritischen Bereichs so kurz wie möglich reduzieren das Risiko.

**Kann es durch Tests erkannt werden?**

Es ist schwer zu erkennen, da der Fehler zeitabhängig ist. Es werden Lasttests und spezielle Race-Detectors verwendet.

## Verwandte Begriffe

- [Concurrency](https://trescout.com/de/dictionary/concurrency/)
- [System Programming Language](https://trescout.com/de/dictionary/system-programming-language/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/thread-safety/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/thread-safety/
