# Was ist Identity Provider?

Ein Identity Provider (auf Deutsch Identitätsanbieter) ist ein zentraler Dienst, der Anmeldungen verifiziert.

## Definition und Wortherkunft
Anstatt für jede Anwendung ein separates Passwort zu verwenden, erfolgt die Anmeldung über eine zentrale Stelle. Die Anwendung fragt den Dienst, wer Sie sind, und erhält eine Bestätigung. Ihr Passwort wird nicht an die Anwendungen weitergegeben, sondern bleibt zentral gespeichert.

## Wie kann man es kennen und im täglichen Leben anwenden?
Unternehmen: Einmalige Anmeldung für alle Systeme.Web: Anmeldung mit sozialem Konto.Institutionell: Mitarbeiterlebenszyklus.

## Technische Tiefe und Architektur
Stream:

## Häufig gemischte Dinge
Es wird für einen Passwort-Manager gehalten. Dieser speichert das Passwort, jener bestätigt die Identität. Einer ist der Tresor, der andere der Notar.

## Einsatz in verschiedenen Disziplinen
Rezeption: Reisepass versus Schlüsselkarte.Notar: Identitätsbeglaubigung.Passkontrolle: Durchgang mit Stempel.

## Häufig gestellte Fragen
**Ist es sicher?**
Ja. Da das Passwort nicht an jede Anwendung weitergegeben wird, verringert sich die Angriffsfläche.

**Was passiert, wenn das System abstürzt?**
Verbundene Anwendungen sind betroffen. Redundanz und ein Notfallzugriffsplan sind unerlässlich.

**Was ist der Unterschied bei SSO?**
SSO ist ein Single-Sign-On-Erlebnis, es ist die Infrastruktur des Anbieters. Das eine ist das Gesicht, das andere das Rückgrat.

**Kann ich es selbst einrichten?**
Ja, es gibt Open-Source-Optionen. Die Disziplin für Patches und Backups liegt bei Ihnen.


## Verwandte Begriffe
- [SSO](/de/dictionary/sso/)
- [OIDC](/de/dictionary/oidc/)
- [RBAC](/de/dictionary/rbac/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/identity-provider/
