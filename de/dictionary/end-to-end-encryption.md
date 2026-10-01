# Was ist End-to-End Encryption?

> E2EE

End-to-End-Verschlüsselung ist ein Sicherheitsverfahren, bei dem nur die Endpunkte die Daten lesen können.

## Definition und Wortherkunft
Die Daten werden auf dem Gerät verschlüsselt und am Zielort entschlüsselt. Der Übermittler und der Server können den Inhalt nicht sehen. Es ist der grundlegende Schutz der Privatsphäre. WhatsApp und Signal sind bekannte Beispiele.

## Wie kann man es kennen und im täglichen Leben anwenden?
Nachricht: Private Chats.Datei: Sichere Übertragung.Backup: Verschlüsselte Kopie.

## Technische Tiefe und Architektur
Layout:

## Häufig gemischte Dinge
Man hält es für TLS. TLS schützt auf dem Transportweg, der Server kann es sehen. Bei Ende-zu-Ende kann nicht einmal der Server es sehen. Das eine ist eine gepanzerte Kurierbox, das andere ein versiegelter Umschlag.

## Einsatz in verschiedenen Disziplinen
Verschlossene Box: Der Transporteur kann den Inhalt nicht sehen.Siegel: Ein Umschlag, bei dem man sieht, wenn er geöffnet wurde.Geschlossener Kreislauf: Nach außen abgeschottete Leitung.

## Häufig gestellte Fragen
**Kann es gelesen werden, wenn es gestohlen wird?**
Nein. Die Schlüssel befinden sich an den Endpunkten, der gestohlene Datenhaufen ist bedeutungslos.

**Ist es in jeder Anwendung verfügbar?**
Nein. Es wird über die Einstellungen geprüft, es werden keine Annahmen getroffen.

**Wie funktioniert die Sicherung?**
Ein verschlüsseltes Backup und ein Wiederherstellungscode sind erforderlich. Ohne den Code gibt es keine Wiederherstellung.

**Ist es für Unternehmen geeignet?**
Es wird mit dem Bedarf an Protokollierung und Überprüfung in Einklang gebracht. Eine Richtlinie wird festgelegt.


## Verwandte Begriffe
- [Security Scanner](/de/dictionary/security-scanner/)
- [Linux Server Security](/de/dictionary/linux-server-security/)
- [SSO](/de/dictionary/sso/)

## Verwandte Werkzeuge
- [Croc](/de/discover/croc/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/end-to-end-encryption/
