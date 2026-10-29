# Leichter Datenbank-Client

Das in Rust entwickelte dbx bietet einen 25 MB großen, leichtgewichtigen Datenbank-Client, der über 100 Datenbanktypen unterstützt. Die Desktop-Anwendung umfasst neben einer Befehlszeilenschnittstelle (CLI) und Docker-Unterstützung auch einen integrierten KI-Assistenten sowie das Model Context Protocol (MCP).

- ★ 28.094
- Rust
- GitHub Trending · 2026-09-29

## Aktualisierungen

- **29. Oktober 2026:** Sterne 27,885 → 28,094, neueste Version v0.6.61 (29. Oktober 2026).
- **27. Oktober 2026:** Sterne 27,769 → 27,885, neueste Version v0.6.58 (27. Oktober 2026).
- **26. Oktober 2026:** Sterne 27,698 → 27,769, neueste Version v0.6.55 (25. Oktober 2026).
- **25. Oktober 2026:** Sterne 27,655 → 27,698, neueste Version v0.6.54 (24. Oktober 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Befolge die notwendigen Schritte, um die dbx-Anwendung zu installieren und auszuführen. Verwende für die Desktop-Anwendung den Befehl brew install --cask dbx und für das Befehlszeilentool npm install -g @dbx-app/cli
# oder via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json. Wenn du es mit Docker ausführen möchtest, verwende den Befehl # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
-v dbx-data:/app/data \
t8y2/dbx:latest.

Repository: https://github.com/t8y2/dbx. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

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

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-29 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/dbx/
