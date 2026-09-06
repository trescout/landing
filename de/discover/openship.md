# App-Bereitstellung auf Ihrem eigenen Server

OpenShip bietet eine Anwendungsverteilungsplattform, die Benutzer auf ihren eigenen Servern hosten können. Dieses mit der TypeScript-Sprache entwickelte Tool ermöglicht Self-Hosting-Prozesse als Alternative zu cloudbasierten Infrastrukturdiensten.

- ★ 12.135
- TypeScript
- GitHub Trending · 2026-07-21

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
Ich möchte ein Projekt mit Openship veröffentlichen. Reicht es im Projektverzeichnis aus, das Verzeichnis mit dem Befehl „openship init“ mit dem Projekt zu verbinden und dann den Befehl „openshipploy“ auszuführen? Können Sie Schritt für Schritt erklären, wie die Datenbank und die SSL-Konfiguration dabei automatisch verwaltet werden?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openship/
