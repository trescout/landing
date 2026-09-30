# OSINT-Benutzeranalyse auf mehr als 465 Plattformen

Der auf Python basierende User-Scanner führt Open-Source-Intelligence-Scans (OSINT) in mehr als 465 sozialen Netzwerken, Foren und Code-Repositories mit einem einzigen Benutzernamen oder einer einzigen E-Mail-Adresse durch.

- ★ 5.007
- Python
- GitHub Trending · 2026-08-31

## Was es bringt
- Breite Plattformabdeckung: Überprüfen Sie die Kontopräsenz auf GitHub, Reddit, Twitter, Steam, Telegram und über 465 Websites auf einmal.
- Asynchrones Hochgeschwindigkeits-Scannen: Parallele Abfrage von Hunderten von Zielen in Sekunden mit asyncio- und aiohttp-basierter Architektur.
- Falsch-Positiv-Filterung: Intelligenter Erkennungsmechanismus, der Fehlertexte im Antworttext sowie HTTP-Statuscodes überprüft.
- Export von JSON- und CSV-Berichten: Speichern von Analyseergebnissen in konfigurierten Formaten zur Verwendung in Forensik- und Sicherheitsberichten.
- Datenschutz und lokale Ausführung: Möglichkeit, alle Abfragen vollständig vom lokalen Computer aus auszuführen, ohne sie an Server von Drittanbietern zu senden.

## Installation
**Klonen des Repositorys und Installieren von Abhängigkeiten**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```


## Ausführung
**Scannen Sie den Benutzernamen und die E-Mail-Adresse des Ziels**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```


## Technische Architektur und Funktionsweise
- Datenbankvorlagen (JSON-Site-Manifeste): Modulare Konfiguration mit URL-Mustern, Fehlercodes und Profil-Regexes für 465+ Plattformen.
- Concurrent Request Pooling: Netzwerkbandbreite am effizientesten nutzen, indem DNS-Auflösungen und TCP-Sockets zwischengespeichert werden.
- Benutzerdefinierte HTTP-Header und User-Agent-Rotation: Realistische Browser-Header-Simulation, um WAF- und Ratenlimit-Behinderungen zu vermeiden.

## OSINT-Untersuchungsszenarien und Datenanalyse
- Verletzung und Nachverfolgung personenbezogener Daten: Ordnen Sie mithilfe der Benutzernamenkorrelation zu, auf welchen sozialen Kanälen die geleakten Profile aktiv sind.
- Unternehmenssicherheitsaudits: Stellen Sie fest, ob Unternehmensmitarbeiter mit ihren Firmen-E-Mail-Adressen Konten auf externen Plattformen eröffnen.
- Social-Engineering-Abwehr: Erkennen Sie unautorisierte gefälschte Konten frühzeitig gegen Spear-Phishing-Angriffe.

## Wenn Sie nicht programmieren
Können Sie Schritt für Schritt erklären, wie ich mit dem User-Scanner-Tool in einem Sicherheitsaudit mehr als 465 Plattformen mit einem einzigen Benutzernamen scannen, die Ergebnisse im JSON-Format exportieren und verdächtige Profile auflisten kann?

## Häufig gestellte Fragen
- Ist die Verwendung von User-Scanner legal? Ja. Der Benutzerscanner fragt nur den öffentlich sichtbaren Kontopräsenzstatus auf öffentlichen Webseiten ab. Es ermöglicht keinen unbefugten Systemzugriff oder das Knacken von Passwörtern.
- Gibt es Tor- oder Proxy-Unterstützung? Ja. Sie können Ihre IP-Adresse maskieren und Geschwindigkeitsbegrenzungen umgehen, indem Sie Anfragen über SOCKS5- oder HTTP-Proxy-Ketten weiterleiten.
- Wie lange dauert es, bis die Ergebnisse vorliegen? Dank der asynchronen Architektur ist das Scannen von mehr als 465 Plattformen je nach Internetverbindung in der Regel in 20 bis 45 Sekunden abgeschlossen.
- Wie funktioniert die E-Mail-Suche? Im E-Mail-Modus werden öffentliche Authentifizierungssignale an den Endpunkten zum Zurücksetzen von Passwörtern oder zur Kontoregistrierung unterstützter Dienste untersucht.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/user-scanner/
