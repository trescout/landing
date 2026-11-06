# Was ist Password Authentication?

*Entwicklung · Zuletzt aktualisiert: 6. November 2026*

Es ist der Prozess, bei dem ein Passwort verwendet wird, um die Identität des Benutzers bei der Anmeldung am System zu verifizieren.

## Definition

Die Passwort-Authentifizierung ist eine Methode zur Überprüfung des von einem Benutzer festgelegten geheimen Passworts, um festzustellen, ob er Zugriffsrechte auf ein digitales System hat. Das System fordert den Benutzer auf, zu beweisen, dass er die Person ist, die er zu sein behauptet. Das eingegebene Passwort wird mit dem sicher gespeicherten, verschlüsselten Äquivalent in der Datenbank abgeglichen.

***Analogie:** Das ist vergleichbar damit, den Schlüssel in das Schloss an der Tür zu stecken und zu drehen, um hineinzugehen. Wenn der Schlüssel passt, öffnet sich die Tür, andernfalls bleibt man draußen.*

## So funktioniert es

Benutzername und Passwort werden in den entsprechenden Bildschirm eingegeben und abgesendet. Die Software auf Serverseite speichert das Passwort nicht direkt im Klartext, sondern lässt es durch sichere mathematische Hash-Funktionen laufen. Wenn der Hash des eingegebenen Passworts mit dem Hash in der Datenbank übereinstimmt, wird der Zugriff gewährt.

## Wo es eingesetzt wird

Es wird als grundlegende Sicherheitsebene bei Mitglieder-Logins auf Websites, Computer-Anmeldebildschirmen, Verwaltungskonsole von Cloud-Servern und beim Zugriff auf Unternehmensnetzwerke verwendet.

## Häufig verwechselt mit

Es kann mit Autorisierung verwechselt werden. Die Passwort-Authentifizierung beweist, wer Sie sind, während die Autorisierung festlegt, worauf Sie zugreifen können, sobald Sie im System sind.

## Fragen und Antworten

**Wie werden Passwörter in der Datenbank gespeichert?**

Aus Sicherheitsgründen werden sie niemals im Klartext gespeichert. Sie werden mithilfe spezieller Hashing-Algorithmen und Salt-Techniken irreversibel verschlüsselt.

**Ist sie allein sicher genug?**

Heutzutage wird sie, da sie leicht gestohlen oder erraten werden kann, im Allgemeinen durch zusätzliche Maßnahmen wie die Zwei-Faktor-Authentifizierung unterstützt.

## Verwandte Begriffe

- [SSO](https://trescout.com/de/dictionary/sso/)
- [OIDC](https://trescout.com/de/dictionary/oidc/)
- [RBAC](https://trescout.com/de/dictionary/rbac/)
- [Security Scanner](https://trescout.com/de/dictionary/security-scanner/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/password-authentication/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/password-authentication/
