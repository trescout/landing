# Offene Entwicklungsplattform für Grundlagenmodellforschung

Führt Experimente als abhängige Schritte in topologischer Reihenfolge aus und demonstriert mit TinyStories ein vollständiges Einstiegsbeispiel. Die offene Entwicklungsphilosophie dokumentiert Code, Daten, Entscheidungen und fehlgeschlagene Experimente.

- ★ 3.089
- Python
- GitHub Trending · 2026-08-25

## Aktualisierungen

- **31. August 2026:** Sterne 1,967 → 3,089.

## Installation

**Offizielles Repository klonen**

```
git clone https://github.com/marin-community/marin.git
```

**Python-Umgebung erstellen**

```
uv venv --python 3.12
```

**Abhängigkeiten installieren**

```
uv sync --all-packages
```

## Ausführung

**CPU Smoke-Test ausführen**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```

## Was macht dieses Werkzeug?

Führt Experimente als abhängige Schritte in topologischer Reihenfolge durch. Das offizielle erste Experiment zeigt das Tokenisieren der TinyStories-Daten und das Trainieren eines kleinen Sprachmodells; die offene Entwicklungsweise dokumentiert dabei Code, Daten, Entscheidungen und auch gescheiterte Läufe.

## Für wen ist es?

Teams, die Forschung zu Datenkuration, -transformation, Filterung, Tokenisierung, Modelltraining und Evaluierung durchführen.

## Was Sie nicht erwarten sollten

Einfache Anwendungsentwicklung außerhalb der Grundlagenmodellforschung oder Nutzer, die keine Python- und Entwicklungsumgebung einrichten möchten.

## Höhepunkte

- Forschungsumfang von Datenverarbeitung über Vortraining, Finetuning bis zur Evaluierung
- Experiment-Workflow, der abhängige Schritte in topologischer Reihenfolge ausführt
- Offene Dokumentation, die auch fehlgeschlagene Experimente und Entwicklungsentscheidungen einschließt

## Ablauf für die erste Nutzung

1. Das offizielle Repository klonen und eine virtuelle Python-Umgebung mit Python 3.12+ erstellen
2. Abhängigkeiten mit uv synchronisieren
3. Die Umgebungsvariable MARIN_PREFIX konfigurieren
4. Den TinyStories-CPU-Offline-Smoketest ausführen

## Sicherer Start

Der CPU-Smoketest dient nur der ersten Validierung. CPU-, GPU- und TPU-Abhängigkeiten können jeweils zusätzliche Hardware-Setups erfordern. WANDB_API_KEY und HF_TOKEN werden nur für zugehörige Monitoring- oder geschlossene Modell-Workflows benötigt.

## Erster Prompt

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Führe zur ersten Validierung den TinyStories-Offline-Workflow aus, um auf CPU ein kleines Modell zu trainieren.

## Verwandte Begriffe aus dem Glossar

- [CPU](https://trescout.com/de/dictionary/cpu/)
- [GPU](https://trescout.com/de/dictionary/gpu/)

## Links

- [GitHub-Repository →](https://github.com/marin-community/marin)
- [Installationsdokumentation →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [Erstes Experiment →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [Offizielle README →](https://github.com/marin-community/marin)
- [Auf Türkisch lesen →](https://trescout.com/discover/marin/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-25 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/marin/
