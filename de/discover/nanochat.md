# Ein Werkzeug zum Trainieren von KI-Modellen

karpathy/nanochat ist ein experimentelles Software-Framework, das zum Trainieren großer Sprachmodelle (LLMs) entwickelt wurde und auf einer einzigen Grafikprozessoreinheit (GPU) läuft. Dieses Projekt umfasst die Prozesse Tokenisierung, Vortraining, Feinabstimmung, Evaluierung und Inferenz und bietet Entwicklern eine minimale und modifizierbare Struktur.

- ★ 59.998
- Python
- GitHub Trending · 2026-11-03

## Was es bringt

- Ermöglicht das Training eines KI-Modells auf einer einzigen Grafikprozessoreinheit.
- Ermöglicht die Verwaltung von Textgenerierungsschritten über die Befehlszeile.
- Bietet flexible Installationsoptionen für verschiedene Hardwaretypen.

## Installation

**Abhängigkeiten installieren**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Ausführung

**Den Trainingsprozess starten**

```
bash runs/speedrun.sh
```

**Mit dem Modell chatten**

```
python -m scripts.chat_cli
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das KI-Tool namens nanochat installieren und ausführen. Installiere zunächst die Abhängigkeiten und aktiviere die virtuelle Umgebung mit den Befehlen uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate. Starte anschließend den Prozess mit dem Befehl bash runs/speedrun.sh und kommuniziere nach Abschluss mit dem Modell, indem du python -m scripts.chat_cli ausführst.

Repository: https://github.com/karpathy/nanochat. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Fine-tuning](https://trescout.com/de/dictionary/fine-tuning/)
- [GPU](https://trescout.com/de/dictionary/gpu/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Entwickler gedacht, die große Sprachmodelle von Grund auf trainieren und testen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/karpathy/nanochat)
- [Auf Türkisch lesen →](https://trescout.com/discover/nanochat/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-03 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/nanochat/
