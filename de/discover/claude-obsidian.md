# Lokales Wissenssystem für Claude Code

Organisiert Forschungsinhalte als Quellen- und Anspruchsbücher, verlinkte Seiten und Wissenskarten. Genehmigte Änderungen werden von einem Orchestrator in rückrollbaren Transaktionen angewendet.

- ★ 14.822
- Python
- GitHub Trending · 2026-08-25

## Aktualisierungen

- **11. September 2026:** Sterne 14,727 → 14,822, neueste Version v2.2.0 (10. September 2026).
- **8. September 2026:** Sterne 13,706 → 14,727, neueste Version v2.1.1 (25. August 2026).
- **27. August 2026:** Sterne 12,404 → 13,706, neueste Version v2.1.1 (25. August 2026).

## Installation

**Claude Code Marketplace hinzufügen**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Das Claude-obsidian-Plugin installieren**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Einen separaten Vault-Plan erstellen**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```

## Ausführung

**Plugin-Installation überprüfen**

```
claude plugin list
```

**Wiki-Workflow starten**

```
/claude-obsidian:wiki
```

## Was macht dieses Werkzeug?

Organisiert Forschungsinhalte mit Quellen- und Anspruchsregistern, verlinkten Seiten und Wissenskarten. Parallele Agenten generieren Entwürfe, während ein Orchestrator bestätigte Änderungen als rückrollbare Transaktionen anwendet, sodass Änderungen geprüft und zurückgenommen werden können.

## Für wen ist es?

Alle, die mit Claude Code eine lokal gehostete, nach Quellen zitierende Wissensbasis in Obsidian aufbauen möchten.

## Was Sie nicht erwarten sollten

Automatische Transkriptaufzeichnung, Cloud-Synchronisation, Garantie der inhaltlichen Richtigkeit oder Ersatz für Backup- und Source-Control-Workflows.

## Höhepunkte

- Lokal-priorisiertes Arbeitsmodell und explizite Ausgabekontrolle über das Netzwerk
- Quellen- und Anspruchsregister mit zitierenden, verlinkten Seiten
- Angewandte, bestätigte Änderungen werden als rückrollbare Transaktionen ausgeführt

## Ablauf für die erste Nutzung

1. Repository klonen und eine Python 3.11+-Umgebung einrichten
2. Einen Initialplan für ein separates Vault erstellen und die JSON-Plan-Datei prüfen
3. Den Wert approved_plan_sha256 kontrollieren und den vollständigen Ablauf bestätigen
4. Das Vault in Obsidian öffnen und das lokale Plugin mit Claude Code ausführen
5. Den Wiki-Workflow starten und die Schritte Hinzufügen von Quellen, Abfragen und explizitem Speichern verwenden

## Sicherer Start

Dieses System ist keine einzige Quelle der Wahrheit. Verwenden Sie zusätzliche Backups und Source-Control für Ihre Daten; prüfen Sie Netzwerk-Ausgaben und den angewendeten Plan.

## Erster Prompt

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Starte einen lokalen Obsidian-Wiki-Workflow, wobei Quellen mit Quellen- und Anspruchsregistern verknüpft werden.

## Verwandte Begriffe aus dem Glossar

- [Agent Skills](https://trescout.com/de/dictionary/agent-skills/)
- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [Agent](https://trescout.com/de/dictionary/agent/)

## Links

- [GitHub-Repository →](https://github.com/AgriciDaniel/claude-obsidian)
- [Installationsanleitung →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [Offizielle README →](https://github.com/AgriciDaniel/claude-obsidian)
- [Auf Türkisch lesen →](https://trescout.com/discover/claude-obsidian/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-25 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/claude-obsidian/
