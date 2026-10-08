# Modelle der künstlichen Intelligenz für physikalische Systeme

Cosmos wurde von NVIDIA entwickelt und ist eine offene Plattform, die Weltmodelle, Datensätze und Tools für physische Systeme wie Roboter und autonome Fahrzeuge bereitstellt. Es stellt eine Infrastruktur bereit, die es Entwicklern erleichtert, physische KI-Anwendungen zu erstellen.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Aktualisierungen

- **2. August 2026:** Sterne 9,173 → 11,343, neueste Version Cosmos3 (1. Juni 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte physische Anwendungen für künstliche Intelligenz mithilfe der NVIDIA Cosmos-Plattform entwickeln. Erläutern Sie im technischen Detail die Möglichkeiten, die die Cosmos 3-Modellfamilie bietet, insbesondere die Unterschiede in der Verwendung von „Reasoner“- und „Generator“-Oberflächen und wie diese Modelle in Szenarien wie Missionsplanung oder Weltsimulation in robotischen und autonomen Systemen konfiguriert werden können. Fassen Sie außerdem Schritt für Schritt den Prozess der Arbeit mit dem Tool „uv“ und der Bibliothek „vllm-omni“ während der Installationsphase unter Berücksichtigung der CUDA-Treiberanforderungen zusammen.

## Verwandte Begriffe aus dem Glossar

- [Physical AI](https://trescout.com/de/dictionary/physical-ai/)
- [Jupyter Notebooks](https://trescout.com/de/dictionary/jupyter-notebooks/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Entwickler, die an physischer KI, Robotersystemen und autonomen Fahrzeugen arbeiten und sich für Weltmodelle und multimodale Datenverarbeitung interessieren.

## Links

- [GitHub-Repository →](https://github.com/NVIDIA/cosmos)
- [Auf Türkisch lesen →](https://trescout.com/discover/cosmos/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-05 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cosmos/
