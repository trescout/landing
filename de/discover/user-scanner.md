# OSINT-Benutzeranalyse auf mehr als 465 Plattformen

Der auf Python basierende User-Scanner führt Open-Source-Intelligence-Scans (OSINT) in mehr als 465 sozialen Netzwerken, Foren und Code-Repositories mit einem einzigen Benutzernamen oder einer einzigen E-Mail-Adresse durch.

- ★ 5.007
- Python
- GitHub Trending · 2026-08-31

## Aktualisierungen

- **27. September 2026:** Sterne 3,910 → 5,007, neueste Version v1.5.2 (17. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Können Sie Schritt für Schritt erklären, wie ich mit dem User-Scanner-Tool in einem Sicherheitsaudit mehr als 465 Plattformen mit einem einzigen Benutzernamen scannen, die Ergebnisse im JSON-Format exportieren und verdächtige Profile auflisten kann?

## Häufig gestellte Fragen

- Ist die Verwendung von User-Scanner legal? Ja. Der Benutzerscanner fragt nur den öffentlich sichtbaren Kontopräsenzstatus auf öffentlichen Webseiten ab. Es ermöglicht keinen unbefugten Systemzugriff oder das Knacken von Passwörtern.
- Gibt es Tor- oder Proxy-Unterstützung? Ja. Sie können Ihre IP-Adresse maskieren und Geschwindigkeitsbegrenzungen umgehen, indem Sie Anfragen über SOCKS5- oder HTTP-Proxy-Ketten weiterleiten.
- Wie lange dauert es, bis die Ergebnisse vorliegen? Dank der asynchronen Architektur ist das Scannen von mehr als 465 Plattformen je nach Internetverbindung in der Regel in 20 bis 45 Sekunden abgeschlossen.
- Wie funktioniert die E-Mail-Suche? Im E-Mail-Modus werden öffentliche Authentifizierungssignale an den Endpunkten zum Zurücksetzen von Passwörtern oder zur Kontoregistrierung unterstützter Dienste untersucht.

## Verwandte Begriffe aus dem Glossar

- [OSINT](https://trescout.com/de/dictionary/osint/)
- [Proxy](https://trescout.com/de/dictionary/proxy/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Cybersicherheitsforscher, OSINT-Analysten, Experten für Computerforensik und ethische Hacker.
- **Lizenz:** GPL-3.0 (Açık kaynak copyleft lisansı)
- **Framework:** Asynchroner OSINT-Scanner für Python
- **Plattformen:** Linux, macOS, Windows

## Links

- [GitHub-Repository →](https://github.com/kaifcodec/user-scanner)
- [Auf Türkisch lesen →](https://trescout.com/discover/user-scanner/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-31 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/user-scanner/
