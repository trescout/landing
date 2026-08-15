# Was ist Environment Variables?

Dabei handelt es sich um kleine Bezeichner, die die Einstellungen und geheimen Schlüssel enthalten, die Programme zur Laufzeit benötigen.

## Definition
Es ermöglicht Ihnen, Informationen auf Systemebene zu behalten, wie z. B. Passwörter, API-Schlüssel oder verschiedene Serveradressen, die Sie nicht in Ihren Code schreiben sollten. Während das Programm läuft, liest es diese Variablen und verhält sich entsprechend. Somit kann derselbe Code in verschiedenen Umgebungen mit unterschiedlichen Einstellungen ausgeführt werden.

## So funktioniert es
Es wird über das Betriebssystem oder eine spezielle Datei definiert und speichert diese Werte beim Start des Programms.

## Wo es eingesetzt wird
Es wird bei Serverinstallationen, Anwendungskonfigurationen und allen Softwareprojekten verwendet, die Sicherheit erfordern.

## Häufig verwechselt mit
Es sollte nicht mit fest codierten Werten verwechselt werden, die in den Code geschrieben werden, da diese Methode ein Sicherheitsrisiko darstellt.

## Häufige Fragen
**Warum sollten wir diese Variablen privat halten?**
Um zu verhindern, dass Ihre Passwörter gefährdet werden, wenn Sie Ihren Code weitergeben.


## Verwandte Begriffe
- [Secrets](/de/dictionary/secrets/)
- [Runtime](/de/dictionary/runtime/)
- [API](/de/dictionary/api/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/environment-variables/
