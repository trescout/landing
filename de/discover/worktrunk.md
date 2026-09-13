# Git-Arbeitsbäume verwalten

Worktrunk ist eine in Rust geschriebene Befehlszeilenschnittstelle (CLI), die die Verwaltung von Git-Arbeitsbäumen (Worktrees) vereinfacht. Das Tool wurde speziell zur Unterstützung paralleler KI-Agenten-Workflows entwickelt und beschleunigt die gleichzeitige Arbeit an mehreren Aufgaben.

- ★ 7.379
- Rust
- GitHub Trending · 2026-09-13

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
Ich möchte Worktrunk verwenden, um einen neuen Arbeitsbaum in meinem bestehenden Git-Projekt zu erstellen und eine parallele Aufgabe in diesem Bereich zu starten. Wie sollte ich die wt-Befehle verwenden, um Arbeitsbäume so einfach wie Branches zu verwalten, und wie kann ich Hooks nutzen, um meinen Workflow zu automatisieren?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/worktrunk/
