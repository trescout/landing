# Lokales Wissenssystem für Claude Code

Organisiert Forschungsinhalte als Quellen- und Anspruchsbücher, verlinkte Seiten und Wissenskarten. Genehmigte Änderungen werden von einem Orchestrator in rückrollbaren Transaktionen angewendet.

- ★ 13.706
- Python
- GitHub Trending · 2026-08-25

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
- Repository klonen und eine Python 3.11+-Umgebung einrichten
- Einen Initialplan für ein separates Vault erstellen und die JSON-Plan-Datei prüfen
- Den Wert approved_plan_sha256 kontrollieren und den vollständigen Ablauf bestätigen
- Das Vault in Obsidian öffnen und das lokale Plugin mit Claude Code ausführen
- Den Wiki-Workflow starten und die Schritte Hinzufügen von Quellen, Abfragen und explizitem Speichern verwenden

## Sicherer Start

## Erster Prompt
Starte einen lokalen Obsidian-Wiki-Workflow, wobei Quellen mit Quellen- und Anspruchsregistern verknüpft werden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Installationsanleitung →
- Offizielle README →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/claude-obsidian/
