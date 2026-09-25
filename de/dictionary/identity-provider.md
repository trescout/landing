# Was ist ein Identity Provider?

> Zentraler Identitätsdienst

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-22

Ein Identity Provider (IdP / Identitätsanbieter) ist ein zentraler Authentifizierungsdienst, der Benutzeridentitäten verwaltet, verifiziert und über mehrere vernetzte Systeme hinweg bestätigt.

## Definition und Wortherkunft
In modernen Softwarearchitekturen sollten Anwendungen Passwörter nicht mehr separat speichern. Der IdP trennt die Benutzerprüfung von der Geschäftslogik und ermöglicht Single Sign-On (SSO): Einmal authentifizieren, überall sicher zugreifen.

## Alltägliche Anwendung und Praxis
- **Social Login:** Anmelde-Schaltflächen wie 'Mit Google oder GitHub anmelden' in Kundenportalen.
- **Unternehmenszugriffe:** Zentrale Verwaltung von Mitarbeiterkonten und MFA-Richtlinien über Okta oder Microsoft Entra ID.
- **Selbstgehostete Umgebungen:** Verwendung von Keycloak oder Authentik zur Absicherung verteilter Microservice-Landschaften.

## Technische Tiefe und Architektur
Kernelemente und Sicherheitsstandards:- **OpenID Connect (OIDC):** Identitätsschicht auf Basis von OAuth 2.0 mit kryptografisch signierten JSON Web Tokens (JWT).
- **SAML 2.0:** XML-basierter Föderationsstandard in behördlichen und klassischen Enterprise-Strukturen.
- **Multi-Faktor-Authentifizierung (MFA):** Absicherung mittels FIDO2-Sicherheitsschlüsseln, Biometrie und TOTP-Generatoren.

## Häufig verwechselt mit
Wird häufig mit einem Service Provider (SP) oder Autorisierungs-Server verwechselt. Der IdP beantwortet 'Wer bist du?' (Authentifizierung); das Rechtesystem entscheidet 'Was darfst du tun?' (Autorisierung).

## Interdisziplinäre Perspektiven
- **Reisen:** Die Passbehörde, die einen amtlichen Ausweis ausstellt vs. die Grenzkontrolle, die ein Visum prüft.
- **Hotel:** Der Check-in an der Rezeption zur Ausgabe der Schlüsselkarte vs. das Türschloss des Hotelzimmers.
- **Büro:** Der Empfang, der Besucherausweise ausgibt vs. die automatischen Schranken zu den Büros.

## Als Analogie
Er fungiert wie die Hotelrezeption: Sie weisen sich einmalig beim Einchecken aus, erhalten eine codierte Schlüsselkarte und öffnen damit Ihr Zimmer, ohne an jeder Zwischentür erneut den Pass vorzuzeigen.

## Häufige Fragen

**Welcher Hauptvorteil spricht für einen Identity Provider?**  
Passwörter liegen nicht mehr in dutzenden einzelnen Datenbanken; zudem wird komfortables Single Sign-On (SSO) ermöglicht.

**Wie übermittelt der IdP die Identität an angebundene Web-Apps?**  
Über signierte kryptografische Token (ID-Tokens), die die geprüften Identitätsdaten enthalten.

**Kann man einen Identity Provider selbst betreiben?**  
Ja, offene Plattformen wie Keycloak, Authentik und Authelia ermöglichen vollständiges On-Premises-Hosting.

**Was passiert bei einem Ausfall des IdP?**  
Neue Anmeldungen an angebundenen Diensten sind blockiert; Hochverfügbarkeit und Token-Caching sind daher Pflicht.

## Verwandte Begriffe
- [Cloud Computing](/de/dictionary/cloud-computing/)
- [Endpoint](/de/dictionary/endpoint/)
- [Application](/de/dictionary/application/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/identity-provider/
