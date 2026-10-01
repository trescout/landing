# Was ist Logs?

Ein Log ist eine zeitgestempelte Zeile von Systemereignissen.

## Definition und Wortherkunft
"Log" bedeutet Logbuch eines Schiffes: Der Kapitän schreibt auf, was passiert ist. Auch die Software schreibt im Hintergrund Zeile für Zeile auf, was sie tut. Im Fehlerfall wird das Buch geöffnet und auf die Uhrzeit geschaut. Es ist die erste Quelle für die Systemgesundheit.

## Wie kann man es kennen und im täglichen Leben anwenden?
Moderator: Fehlerbehebung.Anwendung: Absturzbericht.Sicherheit: Ereignisverfolgung.

## Technische Tiefe und Architektur
Regeln für gute Protokollierung:

## Häufig gemischte Dinge
Wird oft mit Trace verwechselt. Ein Log ist eine Ereignisaufzeichnung, ein Trace ist der Pfad des Ereignisses. Das eine ist ein Foto, das andere ein Film.

## Einsatz in verschiedenen Disziplinen
Blackbox: Flugdaten.Tagebuch: Chronologische Notizen.Kassenbon: Transaktionsprotokoll.

## Häufig gestellte Fragen
**Warum werden Logs benötigt?**
Die Ursache eines Absturzes liegt in der Aufzeichnung. Ein System ohne Protokollierung fliegt blind.

**Wo wird es geschrieben?**
In eine Datei oder ein zentrales System. In der Produktion wird eine zentrale Sammlung empfohlen.

**Wie lange wird es aufbewahrt?**
Das hängt von der Richtlinie ab. Das Debugging erfordert Wochen, Audits erfordern Jahre.

**Werden personenbezogene Daten geschrieben?**
Nein. Passwörter und Identitätsdaten werden nicht aufgezeichnet, sondern maskiert.


## Verwandte Begriffe
- [Observability](/de/dictionary/observability/)
- [QA](/de/dictionary/qa/)
- [Traces](/de/dictionary/traces/)

## Verwandte Werkzeuge
- [Grafana](/de/discover/grafana/)
- [Modly](/de/discover/modly/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/logs/
