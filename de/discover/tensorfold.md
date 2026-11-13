# Lokale KI-Engine TensorFold

ashhart/TensorFold bietet eine Inferenz-Engine für große Sprachmodelle (LLMs) mit Unterstützung für Metal, CUDA und Vulkan. Das in der Programmiersprache Zig entwickelte Tool ermöglicht das direkte Ausführen von Modellen auf Apple Silicon und NVIDIA-Grafikprozessoren, ohne dass eine Python- oder MLX-Installation erforderlich ist.

- ★ 1.998
- Zig
- GitHub Trending · 2026-11-13

## Aktualisierungen

- **13. November 2026:** Sterne 1,996 → 1,998, neueste Version v1.2.7 (11. November 2026).

## Was es bringt

- Führt große Sprachmodelle direkt auf Apple Silicon und NVIDIA-Grafikprozessoren aus.
- Bietet Dienst über eine Binärdatei an, ohne Python oder MLX installieren zu müssen.
- Ermöglicht die Auswahl von Modellen und das Chatten über eine lokale Webanwendung.

## Installation

**Installation unter Mac**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Ausführung

**Anfrage senden**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das TensorFold-Tool auf meinem Mac mit Apple Silicon-Chip installieren, das Qwen3.5-2B-Modell herunterladen und den Server starten. Dafür musst du nacheinander folgende Befehle ausführen:

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

Anschließend kannst du mit folgendem Befehl eine Anfrage senden, um zu überprüfen, ob der Server läuft:

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Repository: https://github.com/ashhart/TensorFold. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Temperature](https://trescout.com/de/dictionary/temperature/)
- [Application](https://trescout.com/de/dictionary/application/)
- [Inference Engine](https://trescout.com/de/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)
- [Inference](https://trescout.com/de/dictionary/inference/)
- [LLM](https://trescout.com/de/dictionary/llm/)

- **Für wen es gedacht ist:** Es ist für Entwickler gedacht, die große Sprachmodelle auf Apple Silicon oder NVIDIA-Grafikprozessoren ausführen möchten, ohne Python zu installieren.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/ashhart/TensorFold)
- [Auf Türkisch lesen →](https://trescout.com/discover/tensorfold/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-13 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/tensorfold/
