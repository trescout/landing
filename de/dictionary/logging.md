# Was ist Logging?

Unter Protokollierung versteht man das chronologische Aufzeichnen der Programmereignisse.

## Definition und Wortherkunft
„Log“ bedeutet protokollieren, aufzeichnen. Wenn das Programm stillschweigend ausfällt, wird aus dem Protokoll gelesen, was es bisher getan hat. Es ist wie die Black Box des Flugzeugs: Es ist der erste Ort, der nach einem Unfall überprüft wird.

## Wie kann man es kennen und im täglichen Leben anwenden?
Moderator: Fehlerbehebung.Produkt: Nutzungsüberwachung.Sicherheit: Ereignisprotokollierung.

## Technische Tiefe und Architektur
Ebenen:

## Häufig gemischte Dinge
Es wird für Observability gehalten. Dabei ist Logging dessen Baustein: Logs sind der Rohstoff, Beobachtbarkeit ist das Produkt.

## Einsatz in verschiedenen Disziplinen
Blackbox: Flugdatenaufzeichnung.Tagebuch: Chronologische Notizen.Kameraaufzeichnung: Veranstaltungsarchiv.

## Häufig gestellte Fragen
**Ist es gut, alles zu speichern?**
Nein. Zu viel verlangsamt die Arbeit und verbirgt das Wichtige, um eine ausgewogene Aufzeichnung zu führen.

**Was ist das Niveau?**
Es ist das Dringlichkeitskennzeichen des Datensatzes. Es fungiert als Filter bei der Suche.

**Wo werden die Aufzeichnungen geschrieben?**
Datei an zentrales System oder Cloud-Dienst senden. In der Produktion wird eine zentrale Sammlung empfohlen.

**Wie lange wird es aufbewahrt?**
Das hängt von der Richtlinie ab. Das Debugging erfordert Wochen, Audits erfordern Jahre.


## Verwandte Begriffe
- [Observability](/de/dictionary/observability/)
- [Traces](/de/dictionary/traces/)
- [Logs](/de/dictionary/logs/)

## Verwandte Werkzeuge
- [OmniRoute](/de/discover/omniroute/)
- [Spdlog](/de/discover/spdlog/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/logging/
