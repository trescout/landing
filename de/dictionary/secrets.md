# Was ist Secrets?

*Glossar · Dev · Zuletzt aktualisiert: 4. Juni 2026*

Dies sind die Passwörter, API-Schlüssel und Zugangscodes, die Softwareanwendungen für den sicheren Betrieb benötigen.

## Definition

Geheimnisse sind geheime Informationen, die ein Programm verwendet, um sich zu authentifizieren, wenn es eine Verbindung zu einem anderen System herstellt. Dies können häufig Datenbankkennwörter, private Schlüssel oder Dienstzugriffstoken sein. Da die Einbettung dieser Informationen in den Code ein Sicherheitsrisiko darstellt, werden sie meist in speziellen Tresorsystemen gespeichert.

***Analogie:** Es ist wie der Schlüssel, mit dem Sie die Tür Ihres Hauses öffnen. Wenn Sie diesen Schlüssel unter die Fußmatte stecken, kann jeder einbrechen, daher müssen Sie ihn in einem sicheren Tresor aufbewahren.*

## So funktioniert es

Anstatt diese vertraulichen Informationen in Codedateien zu schreiben, definieren Entwickler sie mithilfe von Umgebungsvariablen oder vertraulichen Verwaltungstools sicher für die Anwendung.

## Wo es eingesetzt wird

Es wird in Cloud-Diensten, Datenbankverbindungen und Anwendungsauthentifizierungsprozessen verwendet.

## Häufig verwechselt mit

Es kann mit normalen Benutzerkennwörtern verwechselt werden, aber es handelt sich dabei um digitale Identitäten, die für Maschinen und nicht für Menschen entwickelt wurden.

## Häufige Fragen

**Warum werden Geheimnisse nicht im Code gespeichert?**

Wenn Sie Ihren Code weitergeben oder ihn versehentlich ins Internet hochladen, kann jeder an diese Schlüssel gelangen und in Ihre Systeme eindringen.

**Was soll ich tun, wenn Secrets gestohlen wird?**

Sie sollten diesen Schlüssel sofort löschen, einen neuen erstellen und prüfen, ob Ihr System infiziert ist.

## Verwandte Begriffe

- [API](https://trescout.com/de/dictionary/api/)
- [Self-hosting](https://trescout.com/de/dictionary/self-hosting/)
- [Observability](https://trescout.com/de/dictionary/observability/)

## Verwandte Werkzeuge

- [Trivy](https://trescout.com/de/discover/trivy/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/secrets/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/secrets/
