# Was ist Error Tracking?

Ein Nachverfolgungsprozess, der Laufzeitfehler, die in Anwendungen auftreten, in Echtzeit erfasst, gruppiert und an Entwickler meldet.

## Definition
Fehlerverfolgung (Error Tracking) ist ein Überwachungsansatz, der Abstürze und unerwartete Situationen, auf die Benutzer in Live-Software stoßen, automatisch aufzeichnet. Das System dokumentiert Schritt für Schritt die Ursache des Fehlers, Details zum Betriebssystem und die Benutzeraktionen, die den Fehler ausgelöst haben. Auf diese Weise erhalten Softwareteams die Möglichkeit, einzugreifen, bevor Probleme von Benutzern gemeldet werden.

## So funktioniert es
Eine kleine Überwachungsbibliothek, die in die Anwendung integriert ist, überwacht alle nicht abgefangenen Software-Ausnahmen. Wenn eine Störung auftritt, werden der Stack-Trace und Umgebungsdaten verpackt und an den Analysenserver gesendet. Der Server fasst ähnliche Fehler unter einem Dach zusammen und sendet Benachrichtigungen per E-Mail oder Instant Messaging an die Entwickler.

## Wo es eingesetzt wird
Es wird aktiv in mobilen Anwendungen, in denen die Benutzererfahrung kritisch ist, in Single-Page-Webprojekten (SPA) und in Microservice-Architekturen, die im Backend laufen, bevorzugt.

## Häufig verwechselt mit
Es unterscheidet sich von dem Konzept des Loggings, das alle Systemereignisse chronologisch speichert: Die Fehlerverfolgung konzentriert sich direkt auf Ausnahmen und analysiert und gruppiert diese Probleme automatisch.

## Häufige Fragen
**Zeichnen Fehlerverfolgungswerkzeuge vertrauliche Daten von Benutzern auf?**
Korrekt konfigurierte Systeme filtern und maskieren personenbezogene Daten wie Passwörter oder Kreditkarten automatisch, bevor sie an den Server gesendet werden.

**Geht der Fehlerbericht verloren, wenn die Anwendung plötzlich abstürzt?**
Nein, die zum Zeitpunkt des Absturzes gesammelten Informationen werden im lokalen Speicher des Geräts abgelegt und beim erneuten Öffnen der Anwendung an das Zentrum übermittelt.


## Verwandte Begriffe
- [Logging](/de/dictionary/logging/)
- [Observability](/de/dictionary/observability/)
- [Traces](/de/dictionary/traces/)
- [QA](/de/dictionary/qa/)
- [Session Replay](/de/dictionary/session-replay/)

## Verwandte Werkzeuge
- [Sentry](/de/discover/sentry/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/error-tracking/
