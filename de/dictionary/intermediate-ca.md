# Was ist Intermediate CA?

*Entwicklung · Zuletzt aktualisiert: 21. Oktober 2026*

> Intermediate Certificate Authority

Eine zwischen dem Stammszertifikat, das die Identität sicherer Websites verifiziert, und dem Endbenutzer befindliche Zwischenzertifizierungsstelle.

## Definition

Eine Intermediate CA (Zwischenzertifizierungsstelle) ist eine vom Stammzertifizierungsstellen-Anbieter autorisierte Zwischensicherheitsinstitution, die die Grundlage für sichere HTTPS-Verbindungen im Internet bildet. Da die direkte Verwendung des Stammzertifikats auf direkt mit dem Internet verbundenen Servern ein Sicherheitsrisiko darstellt, wird diese Aufgabe an Zwischenzertifikate übertragen. Auf diese Weise kann die Hauptvertrauenskette geschützt und digitale Sicherheitszertifikate sicher an Websites verteilt werden.

***Analogie:** Dies ähnelt dem Fall, dass der Staat nicht direkt von seinem Einwohnermeldeamt aus Personalausweise ausstellt, sondern dem Bezirksamt eine Befugnisurkunde erteilt und die Genehmigungsprozesse darüber abwickelt.*

## So funktioniert es

Wenn Ihr Browser eine Website aufruft, präsentiert der Server Ihnen eine Zertifikatkette. Diese Kette beginnt beim Endbenutzerzertifikat, führt über das Zwischenzertifikat bis hin zum Stammzertifikat, das vorab auf Ihrem Gerät installiert ist, wodurch eine Vertrauensbeziehung hergestellt wird.

## Wo es eingesetzt wird

Es ist aktiv an der SSL/TLS-Zertifikatsverwaltung, Webserver-Konfigurationen und der IT-Sicherheitsinfrastruktur von Unternehmen beteiligt.

## Häufig verwechselt mit

Es ist nicht direkt das Stammzertifikat selbst, sondern die Zwischenstufe, die als Brücke dient, um das Vertrauen zwischen dem Stamm und dem Endpunkt zu transportieren.

## Häufige Fragen

**Warum wird bei einem Zwischenzertifikat nicht direkt das Stammzertifikat verwendet?**

Wenn der private Schlüssel des Stammzertifikats kompromittiert wird, kann die gesamte Internetsicherheit zusammenbrechen; daher wird das Risiko durch Zwischenzertifikate begrenzt.

**Wie verifizieren Browser das Zwischenzertifikat?**

Der Server übermittelt fehlende Zwischenzertifikate an den Browser, und der Browser schließt die Verifizierung mithilfe der integrierten Vertrauenskette ab.

## Verwandte Begriffe

- [End-to-End Encryption](https://trescout.com/de/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/de/dictionary/identity-provider/)
- [OIDC](https://trescout.com/de/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/de/dictionary/vulnerability-scanning/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/intermediate-ca/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/intermediate-ca/
