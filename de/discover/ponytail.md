# Regelsatz für KI-Codieragenten

Ein MIT-lizenziertes Regelwerk und Plugin-System, das bei Agenten-gesteuerten Codieraufgaben Validierung, Fehlerbehandlung, Sicherheit und Barrierefreiheit sicherstellen soll. Regeln werden angewendet, nachdem der betroffene Code gelesen wurde.

- ★ 110.483
- JavaScript
- GitHub Trending · 2026-08-25

## Was macht dieses Werkzeug?
Die Regel-Hierarchie wird angewendet, nachdem der von Änderungen betroffene Code gelesen wurde. Ein korrigierter agentic Benchmark berichtete in einem realen FastAPI- und React-Repository über 12 Aufgaben im Vergleich zur no-skill-Baseline mit Haiku 4.5 im Mittel 54 % weniger Codezeilen, 22 % weniger Tokens, 20 % geringere Kosten und 27 % kürzere Laufzeit. Diese Ergebnisse sind auf die angegebenen Testbedingungen beschränkt.

## Für wen ist es?
Nutzer, die in Claude Code, Codex, Gemini CLI und unterstützten Agent-Host-Umgebungen Validierungs-, Sicherheits- und Zugänglichkeitsregeln in Codier-Workflows integrieren möchten.

## Was Sie nicht erwarten sollten
Die Verallgemeinerung spezifischer Benchmark-Ergebnisse auf alle Projekte oder das Anwenden kritischer Produktionsänderungen ohne menschliche Review.

## Höhepunkte
- Aufgabenorientierte Regeln, die unnötigen Code reduzieren sollen
- Review-Ansatz, der Validierung, Fehlerbehandlung, Sicherheit und Zugänglichkeit schützt
- Plugins oder Instruction-Adapter für Claude Code, Codex, Gemini CLI und andere Host-Umgebungen

## Ablauf für die erste Nutzung
- Die Ponytail-Integration für den verwendeten Agent-Host einrichten
- Bestätigen, dass die Installation innerhalb des Hosts aktiv ist
- Das passende Ponytail-Level auswählen
- Review- oder Audit-Workflows über Änderungen ausführen

## Sicherer Start

## Erster Prompt
Schreibe so viel Code, wie die Aufgabe verlangt, und überprüfe anschließend die Änderungen auf Validierung, Fehlerbehandlung, Sicherheit und Zugänglichkeit.

## Installation
**Claude Code Marketplace hinzufügen**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Claude Code-Plugin installieren**

```
/plugin install ponytail@ponytail
```


## Ausführung
**Ponytail-Stufe wählen**

```
/ponytail full
```

**Diff-Überprüfung starten**

```
/ponytail-review
```


## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Offizielle README →
- Methode des agentischen Benchmarks →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ponytail/
