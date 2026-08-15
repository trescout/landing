# Was ist Secrets?

Dies sind die Passwörter, API-Schlüssel und Zugangscodes, die Softwareanwendungen für den sicheren Betrieb benötigen.

## Definition
Geheimnisse sind geheime Informationen, die ein Programm verwendet, um sich zu authentifizieren, wenn es eine Verbindung zu einem anderen System herstellt. Dies können häufig Datenbankkennwörter, private Schlüssel oder Dienstzugriffstoken sein. Da die Einbettung dieser Informationen in den Code ein Sicherheitsrisiko darstellt, werden sie meist in speziellen Tresorsystemen gespeichert.

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
- [API](/de/dictionary/api/)
- [Self-hosting](/de/dictionary/self-hosting/)
- [Observability](/de/dictionary/observability/)

## Verwandte Werkzeuge
- [Trivy](/de/discover/trivy/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/secrets/
