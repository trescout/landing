# Offene Entwicklungsplattform für Grundlagenmodellforschung

Führt Experimente als abhängige Schritte in topologischer Reihenfolge aus und demonstriert mit TinyStories ein vollständiges Einstiegsbeispiel. Die offene Entwicklungsphilosophie dokumentiert Code, Daten, Entscheidungen und fehlgeschlagene Experimente.

- ★ 1.967
- Python
- GitHub Trending · 2026-08-25

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
- Das offizielle Repository klonen und eine virtuelle Python-Umgebung mit Python 3.12+ erstellen
- Abhängigkeiten mit uv synchronisieren
- Die Umgebungsvariable MARIN_PREFIX konfigurieren
- Den TinyStories-CPU-Offline-Smoketest ausführen

## Sicherer Start

## Erster Prompt
Führe zur ersten Validierung den TinyStories-Offline-Workflow aus, um auf CPU ein kleines Modell zu trainieren.

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


## Links
- GitHub-Repository →
- Installationsdokumentation →
- Erstes Experiment →
- Offizielle README →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/marin/
