# Git-Arbeitsbäume verwalten

Worktrunk ist eine in Rust geschriebene Befehlszeilenschnittstelle (CLI), die die Verwaltung von Git-Arbeitsbäumen (Worktrees) vereinfacht. Das Tool wurde speziell zur Unterstützung paralleler KI-Agenten-Workflows entwickelt und beschleunigt die gleichzeitige Arbeit an mehreren Aufgaben.

- ★ 8.444
- Rust
- GitHub Trending · 2026-09-13

## Aktualisierungen

- **28. September 2026:** Sterne 8,424 → 8,444, neueste Version v0.80.0 (27. September 2026).
- **27. September 2026:** Sterne 7,964 → 8,424, neueste Version v0.79.0 (21. September 2026).
- **17. September 2026:** Sterne 7,379 → 7,964, neueste Version v0.78.0 (16. September 2026).
- **13. September 2026:** Sterne 7,376 → 7,379, neueste Version v0.77.0 (8. September 2026).

## Was es bringt

- Erstellt Arbeitsbereiche einfach, um mehrere Aufgaben gleichzeitig auszuführen
- Beschleunigt lokale Workflows mit automatischen Hooks
- Unterstützt die parallele Arbeit von KI-Agenten

## Installation

**Installation mit Homebrew**

```
brew install worktrunk && wt config shell install
```

**Installation mit Cargo**

```
cargo install worktrunk && wt config shell install
```

## Ausführung

**Zwischen Arbeitsbäumen wechseln**

```
wt switch feat
```

**Neuen Arbeitsbaum erstellen und initialisieren**

```
wt switch -c -x claude feat
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte Worktrunk verwenden, um einen neuen Arbeitsbaum in meinem bestehenden Git-Projekt zu erstellen und eine parallele Aufgabe in diesem Bereich zu starten. Wie sollte ich die wt-Befehle verwenden, um Arbeitsbäume so einfach wie Branches zu verwalten, und wie kann ich Hooks nutzen, um meinen Workflow zu automatisieren?

## Verwandte Begriffe aus dem Glossar

- [Worktree](https://trescout.com/de/dictionary/worktree/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Entwickelt für Entwickler, die gleichzeitig an mehreren Softwareaufgaben oder KI-Agenten arbeiten.

## Links

- [GitHub-Repository →](https://github.com/max-sixty/worktrunk)
- [Auf Türkisch lesen →](https://trescout.com/discover/worktrunk/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-13 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/worktrunk/
