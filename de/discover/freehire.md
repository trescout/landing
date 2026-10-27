# Open-Source-Job-Suchmaschine

Freehire, entwickelt in Go, ist eine Open-Source-Suchmaschine (Quellcode ist für jeden zugänglich und erweiterbar), die für Arbeitssuchende konzipiert wurde. Sie bietet eine Plattform, mit der Benutzer Stellenanzeigen durchsuchen und finden können.

- ★ 3.186
- Go
- GitHub Trending · 2026-10-22

## Aktualisierungen

- **27. Oktober 2026:** Sterne 3,063 → 3,186, neueste Version backend-v0.1.1 (26. Oktober 2026).
- **26. Oktober 2026:** Sterne 2,880 → 3,063, neueste Version backend-v0.1.0 (25. Oktober 2026).
- **23. Oktober 2026:** Sterne 2,661 → 2,880, neueste Version extension-v0.1.12 (23. Oktober 2026).
- **22. Oktober 2026:** Sterne 2,643 → 2,661, neueste Version extension-v0.1.10 (21. Oktober 2026).

## Was es bringt

- Erhalten Sie vermittlungsfrei und aktuell Zugang zu Tech-Stellenanzeigen, die direkt von den Karriereseiten der Unternehmen gesammelt wurden.
- Überprüfen Sie doppelte Anzeigen von verschiedenen Karriere-Websites, indem sie dedupliziert und in einer sauberen sowie filterbaren Liste dargestellt werden.
- Verwalten Sie Ihren Jobsuche-Prozess mit der Lebenslauf-Kompatibilitätsprüfung und dem KI-gestützten Bewerbungsverfolgung-Dashboard.

## Installation

**Das gesamte System in einer Container-Umgebung einrichten und**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Ausführung

**Falls der Standardport belegt ist, mit einem anderen Port**

```
HIRE_HOST_PORT=8090 make up
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die Open-Source-Jobbörsen-Plattform Freehire in meinem eigenen System ausführen. Führen Sie nacheinander die folgenden Befehle aus, um alle Dienste mit der Container-Verwaltungssoftware Docker und dem Automatisierungstool Make zu starten und den API-Status zu überprüfen: make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Repository: https://github.com/strelov1/freehire. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Localhost](https://trescout.com/de/dictionary/localhost/)
- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für diejenigen gedacht, die Software- und Technologiestellenanzeigen direkt auf den Karriereseiten von Unternehmen ohne Vermittler verfolgen oder ihre eigene unabhängige Jobbuchmaschine betreiben möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/strelov1/freehire)
- [Auf Türkisch lesen →](https://trescout.com/discover/freehire/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-22 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/freehire/
