# Leichter Datenbank-Client

Das in Rust entwickelte dbx bietet einen 25 MB großen, leichtgewichtigen Datenbank-Client, der über 100 Datenbanktypen unterstützt. Die Desktop-Anwendung umfasst neben einer Befehlszeilenschnittstelle (CLI) und Docker-Unterstützung auch einen integrierten KI-Assistenten sowie das Model Context Protocol (MCP).

- ★ 23.816
- Rust
- GitHub Trending · 2026-09-29

## Was es bringt
- Unterstützt über hundert Datenbanktypen.
- Funktioniert mit Desktop, Docker und Befehlszeile.
- Enthält einen KI-Assistenten und das Model Context Protocol.

## Installation
**Installation der Desktop-Anwendung**

```
brew install --cask dbx
```

**Installation des Befehlszeilentools**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```


## Ausführung
**Laufen mit Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```


## Wenn Sie nicht programmieren
Befolge die notwendigen Schritte, um die dbx-Anwendung zu installieren und auszuführen. Verwende für die Desktop-Anwendung den Befehl brew install --cask dbx und für das Befehlszeilentool npm install -g @dbx-app/cli
# oder via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json. Wenn du es mit Docker ausführen möchtest, verwende den Befehl # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/dbx/
