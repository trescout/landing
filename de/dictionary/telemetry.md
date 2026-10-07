# Was ist Telemetry?

Telemetrie (Fernmessung auf Türkisch) ist die automatische Erfassung von Statusinformationen von Software und Geräten und deren Übermittlung an die Zentrale.

## Definition und Wortherkunft
Das Wort kommt von den griechischen Wurzeln tele (fern) und metron (Maß). Anwendungen senden dem Entwickler Berichte darüber, wie die Software funktioniert: Welche Funktion wird häufig verwendet, wo stürzt die Anwendung ab. Es handelt sich um einen Datenstrom, der für den Benutzer lautlos im Hintergrund fließt.

## Wie kann man es kennen und im täglichen Leben anwenden?
Debuggen: Automatische Erfassung von Absturzberichten.Produkturteil: Vereinfachung der weniger genutzten Schaltfläche.Leistung: Überwachung der Bootzeit von Version zu Version.

## Technische Tiefe und Architektur
Die drei Säulen der Beobachtbarkeit:

## Häufig gemischte Dinge
Es kann mit der Protokollierung verwechselt werden. Protokoll ist die einzelne Ereigniszeile. Eine Metrik ist eine numerische Zusammenfassung. Trace ist die Reise des Verlangens. Unter Telemetrie versteht man das Sammeln und Übertragen dieser drei.

## Einsatz in verschiedenen Disziplinen
Krankenhaus: Der Patientenmonitor überträgt den Puls auf den Bildschirm der Krankenschwester.Luftfahrt: Flugdaten in einer Blackbox speichern.Energie: Zähler melden den Verbrauch an die Zentrale.

## Häufig gestellte Fragen
**Beeinflusst es meine Privatsphäre?**
In der Regel werden anonyme und aggregierte Daten erhoben. Sie können sehen, welche Daten gesendet werden, und diese im Einstellungsbereich der Anwendung deaktivieren.

**Was ist der Unterschied zur Observability?**
Telemetrie sammelt und übermittelt Daten. Beobachtbarkeit ist die Fähigkeit, anhand der gesammelten Daten das Innere des Systems zu verstehen. Das eine ist das Mittel, das andere das Ziel.

**Kann es geschlossen werden?**
Ja, in den meisten Anwendungen ist es in den Einstellungen deaktiviert. Unternehmensgeräte können gemäß den Richtlinien geöffnet bleiben.

**Ist es mit Kosten verbunden?**
Ja. Es fällt eine Gebühr für den Datentransport und die Datenspeicherung an. Aus diesem Grund erfolgt die Stichprobenentnahme bei hohem Datenverkehr. Einige davon werden gesendet, nicht bei jedem Ereignis.


## Verwandte Begriffe
- [Logs](/de/dictionary/logs/)
- [Observability](/de/dictionary/observability/)
- [Traces](/de/dictionary/traces/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/telemetry/
