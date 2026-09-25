# Riesige KI-Modelle mit 4 GB VRAM betreiben

AirLLM ist eine bahnbrechende Open-Source-Bibliothek, mit der gewaltige große Sprachmodelle (LLMs) mit 70 Milliarden und 405 Milliarden Parametern auf gewöhnlichen Grafikkarten mit nur 4 GB Videospeicher (VRAM) ausgeführt werden können – ganz ohne teure Unternehmensserver oder GPU-Cluster.

- ★ 33.755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Aktualisierungen
- 6. September 2026: Sterne 33.307 → 33.755, neueste Version v4.0.0 (5. September 2026).
- 31. August 2026: Sterne 31.598 → 33.307, neueste Version v3.3.0 (28. August 2026).
- 19. August 2026: Sterne 30.796 → 31.598, neueste Version v3.2.0 (18. August 2026).
- 12. August 2026: Sterne 29.265 → 30.796, neueste Version v3.1.0 (29. Juli 2026).

## Was es bringt
- 70B-Modelle auf 4 GB VRAM ausführen: Nutzen Sie Spitzenmodelle wie Llama 3 70B, Qwen oder DeepSeek selbst auf Einsteiger-Grafikkarten wie GTX 1650 oder RTX 3050.
- Unterstützung für Llama 3.1 405B: Führen Sie das 405-Milliarden-Parameter-Modell, das sonst teure Rechenzentren benötigt, auf 8 GB VRAM Heimrechnern aus.
- Schichtweise Ausführung (Layer-wise Execution): Lädt Transformer-Schichten nacheinander von der SSD in den Speicher, um den VRAM-Engpass vollständig zu umgehen.
- Bis zu 3x schneller durch Blockkompression: Liest Modellgewichte von der NVMe-SSD in optimierten Blöcken und beschleunigt den Datentransfer zur GPU.
- Volle Präzision ohne Quantisierungsverluste: Befreit von der zwingenden 4-Bit-Kompression und ermöglicht Inferenz in nativer 16-Bit-Präzision (bfloat16).

## Installation

**Mit pip (PyPI)**

```
pip install airllm
```

## Technische Architektur und Funktionsweise

Herkömmliche Inferenz-Engines (wie vLLM, Ollama oder HuggingFace) erfordern, dass alle Modellgewichte gleichzeitig im GPU-Videospeicher (VRAM) liegen. Ein 70B-Modell benötigt in 16-Bit etwa 140 GB VRAM und selbst mit 4-Bit-Quantisierung noch mindestens 35 bis 40 GB. AirLLM verändert diesen Ansatz grundlegend:
- Sequenzielle Struktur von Transformer-Schichten: Ein Transformer-Netzwerk besteht aus ca. 80 hintereinandergeschalteten Schichten. Jede Schicht verarbeitet die Ausgabe der vorherigen. Es ist mathematisch nicht erforderlich, alle Schichten zeitgleich im VRAM zu halten.
- Schichtweises Offloading (Sequential Offloading): AirLLM lädt immer nur die aktuell berechnete Einzelschicht in den VRAM (~1,5 GB). Nach Abschluss des Vorwärtsdurchlaufs wird der Speicher freigegeben und die nächste Schicht von der SSD geholt.
- Kompromiss aus Geschwindigkeit und Speicher: Nicht für reaktionsschnelle Echtzeit-Chats gedacht, aber ein enormes Sparpotenzial für Batch-Analysen, tiefes logisches Schließen, Übersetzungen und Modell-Evaluierungen.
- Speicherabgebildetes Lesen (mmap): Bindet PyTorch-Tensoren via mmap direkt an die NVMe-SSD an und nutzt deren hohe Bandbreite, ohne den RAM des Systems zu überlasten.

## Python-Codebeispiel

AirLLM zeichnet sich durch eine sehr aufgeräumte Python-Syntax aus, die sich nahtlos an die AutoModel-API von HuggingFace anlehnt:

**70B-Modell in Python ausführen**

```python
from airllm import AutoModel

# 70B-Modell mit nur 4 GB VRAM initialisieren
model = AutoModel.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")

input_text = ["Fassen Sie die Zukunft quelloffener KI-Agenten kurz zusammen."]
input_tokens = model.tokenizer(input_text, return_tensors="pt", padding=True)

# Textgenerierung (Schichten werden sequenziell verarbeitet)
generation_output = model.generate(
    input_tokens['input_ids'].cuda(),
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

output = model.tokenizer.decode(generation_output.sequences[0])
print(output)
```

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte die AirLLM-Bibliothek nutzen, um ein Modell mit 70 Milliarden Parametern (z. B. meta-llama/Llama-3-70B-Instruct) auf meiner lokalen Grafikkarte mit 4 GB VRAM auszuführen. Ich habe pip install airllm ausgeführt. Kannst du mir den nötigen Python-Code bereitstellen, um das Modell zu laden, Ausgaben zu generieren und Speicherfehler zu vermeiden? Erkläre bitte auch die Anforderungen an den SSD-Speicherplatz und die nötigen Schritte.

- **Für wen:** Forscher und Entwickler mit Standard-GPUs, die 70B- und 405B-Modelle lokal für Benchmarks und Datenextraktion evaluieren möchten.
- **Lizenz:** Apache-2.0 (Freie Open-Source-Lizenz)
- **Hardware-Anforderungen:** GPU mit mindestens 4 GB VRAM und schnelle NVMe-SSD
- **Ökosystem:** Python, PyTorch und HuggingFace Transformers

## Häufig gestellte Fragen
- Wie schnell generiert AirLLM Token? Da AirLLM Schichten kontinuierlich zwischen SSD und GPU austauscht, hängt die Geschwindigkeit von der Leserate Ihrer NVMe-SSD ab. Auf einer Gen4-SSD erzeugt ein 70B-Modell etwa 1 bis 3 Token pro Sekunde. Für interaktive Chats ist das langsam, ermöglicht aber riesige Modelle ohne zusätzliche Hardwarekosten.
- Wie viel freier SSD-Speicherplatz wird benötigt? Ein 70B-Modell in 16-Bit float benötigt rund 140 GB Speicherplatz (oder 35-40 GB in 4-Bit). Für das 405B-Modell sollten mindestens 800 GB freier NVMe-Speicherplatz bereitstehen.
- Kann ich unquantisierte Originalgewichte verwenden? Ja. Das ist einer der größten Vorteile von AirLLM: Da das VRAM-Problem schichtweise gelöst wird, können Sie die originalen 16-Bit-Gewichte ohne jeden Qualitäts- oder Genauigkeitsverlust betreiben.
- Funktioniert AirLLM auf Apple Silicon Macs oder rein auf der CPU? AirLLM ist primär für CUDA (NVIDIA-GPUs) optimiert. Es gibt experimentelle Unterstützung für CPU und Apple Silicon Metal, die beste Performance liefert jedoch eine NVIDIA-Grafikkarte mit schneller NVMe-SSD.

## Links
- [GitHub →](https://github.com/lyogavin/airllm)

## Verwandte Begriffe aus dem Glossar
VRAM LLM Large Language Models Transformer Open Source

---
Source: TreScout Discover · https://trescout.com/de/discover/airllm/
