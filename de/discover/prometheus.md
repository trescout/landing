# System- und Service-Überwachungstool Prometheus

Prometheus ist ein Überwachungstool, das System- und Service-Überwachungsvorgänge sowie die Verwaltung einer Zeitreihendatenbank (Time Series Database) ermöglicht. Das System sammelt in festgelegten Intervallen Metriken von Zielen, wertet Regeln aus, zeigt die Ergebnisse an und kann bei definierten Bedingungen Warnungen generieren.

- ★ 67.226
- Go
- GitHub Trending · 2026-11-07

## Aktualisierungen

- **7. November 2026:** Sterne 67,225 → 67,226, neueste Version v3.16.0 (5. November 2026).

## Was es bringt

- sammelt in festgelegten Intervallen Metriken von Zielen
- wertet Regeln aus und zeigt die Ergebnisse an
- kann bei definierten Bedingungen Warnungen generieren

## Installation

**Ausführen mit Docker**

```
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

## Ausführung

**Aus Quellcode kompilieren und ausführen**

```
make build
./prometheus --config.file=your_config.yml
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die System- und Service-Überwachungsanwendung Prometheus mit Docker starten. Führe zu diesem Zweck den Befehl docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus aus.

Repository: https://github.com/prometheus/prometheus. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Time Series Database](https://trescout.com/de/dictionary/time-series-database/)
- [Database](https://trescout.com/de/dictionary/database/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Entwickler und Systemadministratoren, die den Status von Systemen und Diensten überwachen möchten
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/prometheus/prometheus)
- [Auf Türkisch lesen →](https://trescout.com/discover/prometheus/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-07 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/prometheus/
