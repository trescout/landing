# Was ist Telemetry?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Telemetrie (Fernmessung auf Türkisch) ist die automatische Erfassung von Statusinformationen von Software und Geräten und deren Übermittlung an die Zentrale.

## Definition und Wortherkunft

Das Wort kommt von den griechischen Wurzeln tele (fern) und metron (Maß). Anwendungen senden dem Entwickler Berichte darüber, wie die Software funktioniert: Welche Funktion wird häufig verwendet, wo stürzt die Anwendung ab. Es handelt sich um einen Datenstrom, der für den Benutzer lautlos im Hintergrund fließt.

***Analogie:** Es ist vergleichbar damit, wie Sensoren in einem Auto kontinuierlich die Motortemperatur und den Kraftstoffstand an das Armaturenbrett des Fahrers melden.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Debuggen:** Automatische Erfassung von Absturzberichten.
**Produkturteil:** Vereinfachung der weniger genutzten Schaltfläche.
**Leistung:** Überwachung der Bootzeit von Version zu Version.

## Technische Tiefe und Architektur

Die drei Säulen der Beobachtbarkeit:

**Protokoll:** Ereigniszeilen („Zahlung gestartet“, „Zahlung beendet“).
**Metrisch:** Numerische Metriken (Anzahl der Anfragen, durchschnittliche Latenz).
**Verfolgen:** Eine Aufzeichnung der Reise der Anfrage zwischen Diensten.

Zur Erfassung werden offene Standards wie OpenTelemetry verwendet. Dabei werden zwei Regeln beachtet: Bei hohem Datenaufkommen das Versenden von Proben (Sampling) statt jeder Anfrage und keine Erfassung personenbezogener Daten (E-Mail, Standort). Sie können sehen, welche Daten übertragen werden, und diese im Abschnitt „Einstellungen“ der Anwendung deaktivieren.

## Häufig gemischte Dinge

Es kann mit der Protokollierung verwechselt werden. Protokoll ist die einzelne Ereigniszeile. Eine Metrik ist eine numerische Zusammenfassung. Trace ist die Reise des Verlangens. Unter Telemetrie versteht man das Sammeln und Übertragen dieser drei.

## Einsatz in verschiedenen Disziplinen

**Krankenhaus:** Der Patientenmonitor überträgt den Puls auf den Bildschirm der Krankenschwester.
**Luftfahrt:** Flugdaten in einer Blackbox speichern.
**Energie:** Zähler melden den Verbrauch an die Zentrale.

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

- [Logs](https://trescout.com/de/dictionary/logs/)
- [Observability](https://trescout.com/de/dictionary/observability/)
- [Traces](https://trescout.com/de/dictionary/traces/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/telemetry/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/telemetry/
