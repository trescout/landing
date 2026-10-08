# Sprachmodell mit 64 Millionen Parametern, das in zwei Stunden von Grund auf trainiert wurde

MiniMind bietet Tokenisierung, Vortraining, überwachte Feinabstimmung (SFT), LoRA- und DPO-Stufen mit bloßen PyTorch-Codes für Entwickler, die die Arbeitsprinzipien großer Sprachmodelle (LLM) verstehen möchten.

- ★ 62.670
- Python
- GitHub Trending · 2026-08-31

## Aktualisierungen

- **27. September 2026:** Sterne 55,708 → 62,670, neueste Version v2 (21. Oktober 2025).

## Was es bringt

- 2-stündiges Training auf Consumer-Hardware: Kompakte Architektur, die in etwa 2 Stunden auf einer einzelnen NVIDIA RTX 3090/4090-Grafikkarte von Grund auf trainiert werden kann.
- Vollständiger LLM-Trainingslebenszyklus: BPE-Tokenisierung, Vortraining, überwachte Feinabstimmung (SFT), LoRA-Anpassung und DPO-Ausrichtungspipeline.
- Minimalistische und lesbare Codebasis: Transparente Transformer-Blöcke, geschrieben in reinem PyTorch, ohne komplexe Abstraktionen von Drittanbietern.
- MoE-Unterstützung (Expert Mix): Möglichkeit, eine 8x-MoE-Architektur von Grund auf sowie dichte Modelle auszuprobieren und auszuführen.
- Hervorragende pädagogische und pädagogische Ressource: Der ideale Leitfaden für Forscher, die empirische Einblicke in das Innenleben großer Sprachmodelle gewinnen möchten.

## Installation

**Klonen des Repositorys und Installieren von Abhängigkeiten**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

## Ausführung

**Beginnen Sie mit dem Vortraining und testen Sie die Modellausgabe**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```

## Technische Architektur und Funktionsweise

- RoPE- und SwiGLU-Aktivierungen: Moderne Architekturstandards mit Rotary Position Embeddings und SwiGLU-Aktivierungsfunktionen.
- Stabiler Gradientenfluss mit RMSNorm: Verwendung einer schnelleren und stabileren RMSNorm-Ebenennormalisierung anstelle der herkömmlichen LayerNorm.
- Flash Attention-Integration: Flash Attention v2-Optimierung zur schnellen Berechnung großer Aufmerksamkeitsmatrizen im GPU-Speicher.

## Ausbildungsstufen: Vorschulung, PFT und DPO

- Stufe 1 – Pretrain (1-pretrain.py): Erlernt Grammatik und allgemeines Weltwissen mit der Logik, den nächsten Token anhand von Rohtexten vorherzusagen.
- Phase 2 – Überwachte Feinabstimmung (2-sft.py): Verwandelt das Modell in einen Assistenten, der Benutzerbefehlen mit Frage-Antwort- und Anweisungsdatensätzen folgt.
- Stufe 3 – DPO-Ausrichtung (4-dpo.py): Optimiert das Modell direkt entsprechend den Benutzerpräferenzen durch gute und schlechte Antwortpaare.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit PyTorch mithilfe des MiniMind-Repositorys ein Sprachmodell mit 64 Millionen Parametern von Grund auf trainieren. Können Sie Schritt für Schritt erklären, wie ich den Tokenizer auf der Grundlage meines eigenen türkischen Textdatensatzes vorbereite, das Skript 1-pretrain.py ausführe und es dann mit LoRA verfeinere?

## Häufig gestellte Fragen

- Wie viel VRAM ist zum Trainieren von MiniMind erforderlich? Das 64-M-Parametermodell kann je nach Stapelgrößeneinstellung bequem auf 6 GB bis 12 GB VRAM trainiert werden; Sogar RTX 3060 oder RTX 4060 reichen aus.
- Funktioniert es auf Apple Silicon (Mac M-Serie)? Ja. Training und Inferenz können auch auf Mac-Computern mit PyTorch MPS-Beschleunigung (Metal Performance Shaders) durchgeführt werden.
- Reichen die Ausgaben des Modells für die tägliche Konversation aus? Der 64M ist ein kleines Modell; Es ist optimiert, um die Sprachstruktur, die Fähigkeit zur Beantwortung grundlegender Fragen und den vollständigen Text anstelle komplexer logischer Argumente zu demonstrieren.
- Welche Datensätze sind fertig? Das Repository bietet Befehle zum automatischen Herunterladen gefilterter offener Datensätze für Chinesisch und Englisch vor dem Training und SFT.

## Verwandte Begriffe aus dem Glossar

- [Tokenizer](https://trescout.com/de/dictionary/tokenizer/)
- [LoRA](https://trescout.com/de/dictionary/lora/)
- [VRAM](https://trescout.com/de/dictionary/vram/)
- [Attention](https://trescout.com/de/dictionary/attention/)
- [Transformer](https://trescout.com/de/dictionary/transformer/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)

- **Für wen es gedacht ist:** KI-Forscher, Ingenieure für maschinelles Lernen, Datenwissenschaftler und Studenten.
- **Lizenz:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Minimalistisches LLM-Framework basierend auf PyTorch
- **Plattformen:** Linux, macOS (Apple Silicon MPS), Windows

## Links

- [GitHub-Repository →](https://github.com/jingyaogong/minimind)
- [Auf Türkisch lesen →](https://trescout.com/discover/minimind/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-31 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/minimind/
