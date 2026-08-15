# Autonomes KI-Kit für Antigravity

Ag-kit ist eine Entwicklungsbibliothek, die die notwendigen Werkzeuge und Strukturen bereitstellt, um autonome Agenten für künstliche Intelligenz (KI-Agenten) in TypeScript-basierten Projekten zu erstellen. Es ermöglicht Entwicklern, schnell Agentensysteme zu entwerfen, die komplexe Arbeitsabläufe verwalten können.

- ★ 8.084
- TypeScript
- GitHub Trending · 2026-07-28

## Was es bringt
- 20 verschiedene KI-Expertenrollen
- Sichere Kontrolle der Befehlsausführung
- Persistentes Speicher- und Workflow-Management

## Installation
**Installation im Projekt**

```
npx @vudovn/ag-kit init
```

**Globale Installation**

```
npm install -g @vudovn/ag-kit
ag-kit init
```


## Ausführung
**Überprüfung des Arbeitsbereichs**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Testen des Sicherheitshakens**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```


## Wenn Sie nicht programmieren
In diesem Projekt habe ich einen Antigravity-Arbeitsbereich eingerichtet und die AG Kit-Tools aktiviert. Ich möchte meine Aufgaben mithilfe der Regeln, Expertenagentenrollen und Arbeitsabläufe verwalten, die im Ordner .agents/ im Projektverzeichnis definiert sind. Stellen Sie sicher, dass der Sicherheitshaken aktiv ist, und planen Sie komplexe Arbeitsabläufe mit den Befehlen /coordinate oder /orchestrate.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ag-kit/
