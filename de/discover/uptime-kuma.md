# Tool zur Überwachung des Server- und Dienststatus

Uptime Kuma ist ein selbst gehostetes Überwachungstool mit grafischer Benutzeroberfläche. Diese JavaScript-basierte Anwendung ermöglicht die Verfolgung der Betriebszeit von Websites und Diensten und bietet eine benutzerfreundliche Erfahrung.

- ★ 93.936
- JavaScript
- GitHub Trending · 2026-11-14

## Aktualisierungen

- **14. November 2026:** Sterne 93,934 → 93,936, neueste Version 2.5.11 (12. November 2026).

## Was es bringt

- Websites und Dienste in Echtzeit überwachen
- Mehrsprachige und Benachrichtigungsunterstützung erhalten
- Statusseiten zur visuellen Darstellung erstellen

## Installation

**Installation mit Docker Compose**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Installation mit Docker-Befehl**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Ausführung

**Laufen mit Docker**

```
docker compose up -d
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das Überwachungstool Uptime Kuma installieren. Um Docker Compose zu verwenden, muss ich folgenden Befehl ausführen: mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. Kannst du mir helfen, diese Schritte abzuschließen?

Repository: https://github.com/louislam/uptime-kuma. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für alle, die die Verfügbarkeit von Websites und Servern auf einem eigenen Server überwachen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/louislam/uptime-kuma)
- [Auf Türkisch lesen →](https://trescout.com/discover/uptime-kuma/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-14 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/uptime-kuma/
