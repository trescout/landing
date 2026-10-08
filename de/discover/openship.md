# App-Bereitstellung auf Ihrem eigenen Server

OpenShip bietet eine Anwendungsverteilungsplattform, die Benutzer auf ihren eigenen Servern hosten können. Dieses mit der TypeScript-Sprache entwickelte Tool ermöglicht Self-Hosting-Prozesse als Alternative zu cloudbasierten Infrastrukturdiensten.

- ★ 14.584
- TypeScript
- GitHub Trending · 2026-07-21

## Aktualisierungen

- **7. Oktober 2026:** Sterne 14,558 → 14,584, neueste Version v0.8.2 (6. Oktober 2026).
- **6. Oktober 2026:** Sterne 13,545 → 14,558, neueste Version v0.8.0 (27. September 2026).
- **29. September 2026:** Sterne 12,541 → 13,545, neueste Version v0.8.0 (27. September 2026).
- **27. September 2026:** Sterne 12,135 → 12,541, neueste Version v0.8.0 (27. September 2026).

## Was es bringt

- Automatisierte CI/CD-Prozesse
- Schneller Übergang vom Code zum Container
- Datenbank- und SSL-Verwaltung

## Installation

**Schnelle Installation über CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Installation mit Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Ausführung

**Starten Sie die Projektbereitstellung**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte ein Projekt mit Openship veröffentlichen. Reicht es im Projektverzeichnis aus, das Verzeichnis mit dem Befehl „openship init“ mit dem Projekt zu verbinden und dann den Befehl „openshipploy“ auszuführen? Können Sie Schritt für Schritt erklären, wie die Datenbank und die SSL-Konfiguration dabei automatisch verwaltet werden?

## Verwandte Begriffe aus dem Glossar

- [Deployment Platform](https://trescout.com/de/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/de/dictionary/ci-cd/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler, die Anwendungen auf ihren eigenen Servern hosten und schnell bereitstellen möchten, ohne sich mit komplexen Konfigurationsdateien herumschlagen zu müssen.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/oblien/openship)
- [Auf Türkisch lesen →](https://trescout.com/discover/openship/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-21 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openship/
