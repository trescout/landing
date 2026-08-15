# Testen Sie KI-Modelle autonom

SIA ist ein sich selbst verbesserndes KI-Framework, das entwickelt wurde, um die Leistung von KI-Modellen und -Agenten bei bestimmten Benchmark-Aufgaben autonom zu verbessern. Dieses auf Python basierende System ermöglicht es Systemen der künstlichen Intelligenz, ihre Prozesse durch die Analyse ihrer eigenen Ergebnisse zu optimieren.

- ★ 1.478
- Python
- GitHub Trending · 2026-06-12

## Was es bringt
- Es verbessert autonom die Aufgabenleistung von Modellen der künstlichen Intelligenz.
- Meta sorgt für eine zyklische Verfeinerung zwischen Ziel- und Feedback-Agenten.
- Es bietet eine hohe Genauigkeit und Verarbeitungsgeschwindigkeitseffizienz bei Benchmark-Aufgaben.

## Installation
**Installation mit Claude Models**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Einrichtung mit Multi-Provider (OpenHands)**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..."   # for anthropic/* models
export GEMINI_API_KEY="..."      # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..."      # for openai/* models
```


## Ausführung
**Den Selbstheilungszyklus starten**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Visualisierungspanel**

```
sia web
```


## Wenn Sie nicht programmieren
Ich möchte die Leistung eines KI-Agenten mithilfe des SIA-Frameworks verbessern. Welchen Befehl soll ich nach Abschluss der Installation verwenden, um den Selbstverbesserungszyklus zu starten, indem ich eine der verfügbaren Aufgaben (z. B. gpqa) auswähle, und wie soll ich die Ausgaben am Ende des Prozesses interpretieren (target_agent.py, agent_execution.json, Improvement.md)? Wie kann ich außerdem mein eigenes benutzerdefiniertes Aufgabenverzeichnis in das System einbinden?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/sia/
