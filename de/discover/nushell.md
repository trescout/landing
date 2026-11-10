# Befehlszeilenschnittstelle mit strukturierten Objekten

Nushell, entwickelt in Rust, bietet eine neue Befehlszeilenschnittstelle (Shell), die Daten als strukturierte Objekte verarbeitet. Obwohl das Projekt das Minimum-Viable-Product-Niveau erreicht hat und bei einigen Befehlen instabil sein kann, wird es für den täglichen Gebrauch bevorzugt.

- ★ 41.079
- Rust
- GitHub Trending · 2026-11-07

## Aktualisierungen

- **10. November 2026:** Sterne 41,012 → 41,079, neueste Version 0.117.0 (10. November 2026).
- **7. November 2026:** Sterne 41,011 → 41,012, neueste Version 0.116.1 (4. Oktober 2026).

## Was es bringt

- Verarbeitet Daten als strukturierte Objekte.
- Ermöglicht Pipeline-Flüsse zwischen Befehlen.
- Lädt Dateiinhalte als strukturierte Daten.

## Installation

**Installation**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Ausführung

**Ordner auflisten**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die neue Befehlszeilenschnittstelle namens Nushell installieren und verwenden. Helfen Sie mir, nach Abschluss der Installation den Befehl ls | where type == "dir" | table auszuführen.

Repository: https://github.com/nushell/nushell. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Shell](https://trescout.com/de/dictionary/shell/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Entwickler, die Daten in der Befehlszeile als strukturierte Objekte verwalten möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/nushell/nushell)
- [Auf Türkisch lesen →](https://trescout.com/discover/nushell/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-07 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/nushell/
