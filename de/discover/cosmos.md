# Modelle der künstlichen Intelligenz für physikalische Systeme

Cosmos wurde von NVIDIA entwickelt und ist eine offene Plattform, die Weltmodelle, Datensätze und Tools für physische Systeme wie Roboter und autonome Fahrzeuge bereitstellt. Es stellt eine Infrastruktur bereit, die es Entwicklern erleichtert, physische KI-Anwendungen zu erstellen.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Aktualisieren
- 2. August 2026: Star 9.173 → 11.343, letzte Veröffentlichung Cosmos3 (1. Juni 2026).

## Was es bringt
- Es bietet Weltmodelle, Datensätze und Tools für physische KI-Anwendungen.
- Es kann Text-, Bild-, Audio- und Aktionssequenzen in einer einheitlichen Architektur verarbeiten und produzieren.
- Bietet Prognose-, Planungs- und Simulationsfunktionen für Roboter- und autonome Systeme.

## Installation
**Installation mit vLLM-Omni**

```
uv pip install --torch-backend=cu130 \
  "vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```


## Ausführung
**Videoproduktion**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
  --form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
  --form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
  -o cosmos3_t2v.mp4
```


## Wenn Sie nicht programmieren
Ich möchte physische Anwendungen für künstliche Intelligenz mithilfe der NVIDIA Cosmos-Plattform entwickeln. Erläutern Sie im technischen Detail die Möglichkeiten, die die Cosmos 3-Modellfamilie bietet, insbesondere die Unterschiede in der Verwendung von „Reasoner“- und „Generator“-Oberflächen und wie diese Modelle in Szenarien wie Missionsplanung oder Weltsimulation in robotischen und autonomen Systemen konfiguriert werden können. Fassen Sie außerdem Schritt für Schritt den Prozess der Arbeit mit dem Tool „uv“ und der Bibliothek „vllm-omni“ während der Installationsphase unter Berücksichtigung der CUDA-Treiberanforderungen zusammen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cosmos/
