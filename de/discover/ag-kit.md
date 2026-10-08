# Autonomes KI-Kit für Antigravity

Ag-kit ist eine Entwicklungsbibliothek, die die notwendigen Werkzeuge und Strukturen bereitstellt, um autonome Agenten für künstliche Intelligenz (KI-Agenten) in TypeScript-basierten Projekten zu erstellen. Es ermöglicht Entwicklern, schnell Agentensysteme zu entwerfen, die komplexe Arbeitsabläufe verwalten können.

- ★ 8.159
- TypeScript
- GitHub Trending · 2026-07-28

## Aktualisierungen

- **31. August 2026:** Sterne 8,084 → 8,159, neueste Version v2026.8.31 (31. August 2026).
- **2. August 2026:** Sterne 8,020 → 8,084, neueste Version v2026.7.27 (26. Juli 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

In diesem Projekt habe ich einen Antigravity-Arbeitsbereich eingerichtet und die AG Kit-Tools aktiviert. Ich möchte meine Aufgaben mithilfe der Regeln, Expertenagentenrollen und Arbeitsabläufe verwalten, die im Ordner .agents/ im Projektverzeichnis definiert sind. Stellen Sie sicher, dass der Sicherheitshaken aktiv ist, und planen Sie komplexe Arbeitsabläufe mit den Befehlen /coordinate oder /orchestrate.

## Verwandte Begriffe aus dem Glossar

- [Agentic](https://trescout.com/de/dictionary/agentic/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler, die den Antigravity-Arbeitsbereich in ihren TypeScript-basierten Projekten verwenden und autonome Agentensysteme entwickeln möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/vudovn/ag-kit)
- [Auf Türkisch lesen →](https://trescout.com/discover/ag-kit/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-28 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ag-kit/
