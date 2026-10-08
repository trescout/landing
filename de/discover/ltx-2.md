# Videoproduktion mit künstlicher Intelligenz im lokalen System

LTX-2 wurde von Lightricks entwickelt und bietet ein Python-Inferenz- und Low-Rank-Adaptions-Trainingspaket (LoRA) für Modelle der künstlichen Intelligenz, die Audio und Video produzieren. Mit diesem Toolset können Benutzer LTX-2-Modelle mit ihren eigenen Daten trainieren und Modellausgaben auf lokalen Systemen ausführen.

- ★ 9.567
- GitHub Trending · 2026-06-19

## Aktualisierungen

- **2. Oktober 2026:** Sterne 9,562 → 9,567, neueste Version v1.4.2 (2. Oktober 2026).
- **1. Oktober 2026:** Sterne 9,552 → 9,562, neueste Version v1.4.1 (30. September 2026).
- **29. September 2026:** Sterne 9,267 → 9,552, neueste Version v1.4.0 (29. September 2026).
- **27. August 2026:** Sterne 8,587 → 9,267, neueste Version v1.3.0 (26. August 2026).

## Was es bringt

- Bietet Audio- und Videosynchronisation
- Sie können LoRA mit Ihren eigenen Daten trainieren
- Hochwertige Videoproduktion auf lokalem System

## Installation

**Klonen Sie das Repository von GitHub und geben Sie das Verzeichnis ein**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Modellgewichte herunterladen (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```

## Ausführung

**Führen Sie die Inferenzpipeline mit UV aus**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Bitte erstellen Sie ein Video mit dem LTX-2-Modell, das die gewünschte Szene detailliert beschreibt und eine Audio- und Videosynchronisierung umfasst. Lassen Sie das Modell eine Ausgabe erstellen, indem Sie Szenendetails, das Aussehen der Figur, den Kamerawinkel und den Sprachtext angeben.

## Verwandte Begriffe aus dem Glossar

- [LoRA](https://trescout.com/de/dictionary/lora/)
- [Inference](https://trescout.com/de/dictionary/inference/)
- [CLI](https://trescout.com/de/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Benutzer, die Audio- und Video-KI-Videos erstellen oder Modelle auf ihrem eigenen lokalen System trainieren möchten.

## Links

- [GitHub-Repository →](https://github.com/Lightricks/LTX-2)
- [Auf Türkisch lesen →](https://trescout.com/discover/ltx-2/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-19 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ltx-2/
