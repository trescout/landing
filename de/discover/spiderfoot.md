# Open-Source-Tool zum Sammeln von Informationen

SpiderFoot ist ein Python-Tool, das die Sammlung von Open Source Intelligence (OSINT) für Bedrohungsinformationen und Angriffsflächen-Mapping-Prozesse automatisiert. Es ermöglicht die Erkennung von Sicherheitslücken in digitalen Assets durch die Integration verschiedener Datenquellen.

- ★ 23.302
- Python
- GitHub Trending · 2026-06-22

## Aktualisierungen

- **11. Oktober 2026:** Sterne 22,178 → 23,302, neueste Version v4.0 (7. April 2022).
- **16. September 2026:** Sterne 21,076 → 22,178, neueste Version v4.0 (7. April 2022).
- **15. August 2026:** Sterne 20,026 → 21,076, neueste Version v4.0 (7. April 2022).
- **2. August 2026:** Sterne 18,921 → 20,026, neueste Version v4.0 (7. April 2022).

## Was es bringt

- Automatische Datenerfassung mit mehr als 200 Modulen
- Webbasierte Schnittstelle oder Befehlszeilenunterstützung
- Umfassende Angriffsflächenkartierung für digitale Assets

## Installation

**Stabile Versionsinstallation**

```
wget https://github.com/smicallef/spiderfoot/archive/v4.0.tar.gz
 tar zxvf v4.0.tar.gz
 cd spiderfoot-4.0
 pip3 install -r requirements.txt
 python3 ./sf.py -l 127.0.0.1:5001
```

**Installation der Entwicklungsversion**

```
git clone https://github.com/smicallef/spiderfoot.git
 cd spiderfoot
 pip3 install -r requirements.txt
 python3 ./sf.py -l 127.0.0.1:5001
```

## Ausführung

**Starten der Schnittstelle**

```
python3 ./sf.py -l 127.0.0.1:5001
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit dem SpiderFoot-Tool einen OSINT-Scan auf einem Ziel starten. Mein Ziel ist eine Domain/IP-Adresse. Welche Schritte sollte ich befolgen, um mit diesem Tool zu analysieren, wie sichtbar meine digitalen Assets im Internet sind und welche Schwachstellen sie möglicherweise aufweisen? Bitte erläutern Sie, wie die über 200 Module funktionieren und wie ich die Ergebnisse interpretieren soll.

Repository: https://github.com/smicallef/spiderfoot. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [OSINT](https://trescout.com/de/dictionary/osint/)
- [v4.0](https://trescout.com/de/dictionary/v4-0/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Cybersicherheitsexperten, Penetrationstester und verteidigungsorientierte Benutzer, die neugierig auf den Fußabdruck ihres Unternehmens im Internet sind.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/smicallef/spiderfoot)
- [Auf Türkisch lesen →](https://trescout.com/discover/spiderfoot/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-22 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

## Redaktioneller Hinweis

Security and privacy note: Run domain, IP, email, phone, and social-media scans only against authorized targets. Follow third-party API terms, avoid unnecessary personal-data collection, and do not expose the WebUI publicly.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/spiderfoot/
