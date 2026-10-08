# Leichter Datenbank-Client

Das in Rust entwickelte dbx bietet einen 25 MB großen, leichtgewichtigen Datenbank-Client, der über 100 Datenbanktypen unterstützt. Die Desktop-Anwendung umfasst neben einer Befehlszeilenschnittstelle (CLI) und Docker-Unterstützung auch einen integrierten KI-Assistenten sowie das Model Context Protocol (MCP).

- ★ 25.183
- Rust
- GitHub Trending · 2026-09-29

## Aktualisierungen

- **8. Oktober 2026:** Sterne 24,988 → 25,183, neueste Version v0.6.36 (8. Oktober 2026).
- **7. Oktober 2026:** Sterne 24,669 → 24,988, neueste Version v0.6.35 (6. Oktober 2026).
- **5. Oktober 2026:** Sterne 24,470 → 24,669, neueste Version v0.6.34 (4. Oktober 2026).
- **4. Oktober 2026:** Sterne 24,157 → 24,470, neueste Version v0.6.33 (4. Oktober 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

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

- [Database Client](https://trescout.com/de/dictionary/database-client/)
- [Local](https://trescout.com/de/dictionary/local/)
- [Database](https://trescout.com/de/dictionary/database/)
- [MCP](https://trescout.com/de/dictionary/mcp/)
- [Agent](https://trescout.com/de/dictionary/agent/)
- [CLI](https://trescout.com/de/dictionary/cli/)

- **Für wen es gedacht ist:** Für Entwickler, die verschiedene Datenbanktypen über eine leichtgewichtige Oberfläche mit KI-Unterstützung verwalten möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/t8y2/dbx)
- [Auf Türkisch lesen →](https://trescout.com/discover/dbx/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-29 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/dbx/
