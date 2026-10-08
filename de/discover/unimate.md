# Animieren Sie verschiedene Charakterskelette mit einem einzigen Modell

UniMate ist eine Animationstechnologie, die dazu dient, verschiedene Skelettstrukturen über ein einziges Modell zu animieren. Diese auf der SIGGRAPH Asia 2026 vorgestellte Arbeit zielt darauf ab, Charakteranimationsprozesse zu standardisieren.

- ★ 1.166
- Python
- GitHub Trending · 2026-10-02

## Was es bringt

- Animiert verschiedene Skelettstrukturen wie Menschen, Tiere und Objekte mit einem einzigen KI-Modell.
- Bietet umfassende Animationsunterstützung mit dem groß angelegten UniML3D-Datensatz.
- Beschleunigt den Arbeitsablauf durch die Standardisierung von Charakteranimationsprozessen.

## Installation

**Umgebungsvorbereitung**

```
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools<81"
pip install -r requirements.txt --no-build-isolation
```

## Ausführung

**Erstellung von Beispielanimationen**

```
python -m unimate.inference.sample \
    --exp_dir outputs/uniml3d_60frames_graph_adaln \
    --test_cases_json test_cases.json \
    --num_repetitions 3
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Wie kann ich mit dem UniMate-Projekt meine Charaktermodelle mit unterschiedlichen Skelettstrukturen in einem Standardformat animieren? Erklären Sie den Prozess der Animationserstellung Schritt für Schritt unter Verwendung des vom Projekt bereitgestellten UniML3D-Datensatzes und der vortrainierten Checkpoints.

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für 3D-Künstler und Entwickler, die Charakteranimationsprozesse automatisieren und zwischen verschiedenen Skelettstrukturen wechseln möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/Friedrich-M/UniMate)
- [Auf Türkisch lesen →](https://trescout.com/discover/unimate/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-02 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/unimate/
