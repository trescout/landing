# Regelsatz für KI-Codieragenten

Ein MIT-lizenziertes Regelwerk und Plugin-System, das bei Agenten-gesteuerten Codieraufgaben Validierung, Fehlerbehandlung, Sicherheit und Barrierefreiheit sicherstellen soll. Regeln werden angewendet, nachdem der betroffene Code gelesen wurde.

- ★ 158.137
- JavaScript
- GitHub Trending · 2026-08-25

## Aktualisierungen

- **8. Oktober 2026:** Sterne 156,385 → 158,137, neueste Version v5.0.0 (8. Oktober 2026).
- **6. Oktober 2026:** Sterne 155,501 → 156,385, neueste Version v4.13.0 (5. Oktober 2026).
- **5. Oktober 2026:** Sterne 152,240 → 155,501, neueste Version v4.12.0 (5. Oktober 2026).
- **3. Oktober 2026:** Sterne 146,524 → 152,240, neueste Version v4.10.3 (3. Oktober 2026).

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

1. Die Ponytail-Integration für den verwendeten Agent-Host einrichten
2. Bestätigen, dass die Installation innerhalb des Hosts aktiv ist
3. Das passende Ponytail-Level auswählen
4. Review- oder Audit-Workflows über Änderungen ausführen

## Sicherer Start

Die Prozentangaben stammen von einem korrigierten agentic Benchmark über 12 Aufgaben in einem realen FastAPI- und React-Repository mit Haiku 4.5 und n=4. In einer separaten adversarial-Schicht wurde 100% Sicherheit berichtet. Die früher berichteten Einzeldurchläufe im Bereich 80–94% sind kein allgemeiner Mittelwert.

## Erster Prompt

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Schreibe so viel Code, wie die Aufgabe verlangt, und überprüfe anschließend die Änderungen auf Validierung, Fehlerbehandlung, Sicherheit und Zugänglichkeit.

## Verwandte Begriffe aus dem Glossar

- [Benchmark](https://trescout.com/de/dictionary/benchmark/)
- [Agentic](https://trescout.com/de/dictionary/agentic/)
- [Token](https://trescout.com/de/dictionary/token/)
- [Agent](https://trescout.com/de/dictionary/agent/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

## Links

- [GitHub-Repository →](https://github.com/DietrichGebert/ponytail)
- [Offizielle README →](https://github.com/DietrichGebert/ponytail)
- [Methode des agentischen Benchmarks →](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)
- [Auf Türkisch lesen →](https://trescout.com/discover/ponytail/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-25 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ponytail/
