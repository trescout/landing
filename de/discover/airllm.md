# Führen Sie riesige KI-Modelle mit 4 GB VRAM aus

AirLLM ist eine bahnbrechende Open-Source-Bibliothek, die riesige große Sprachmodelle (LLMs) mit 70 Milliarden und 405 Milliarden Parametern auf Standard-Grafikkarten für Verbraucher mit nur 4 GB Videospeicher (VRAM) ausführt, ohne dass Unternehmensserver oder teure GPU-Cluster erforderlich sind.

- ★ 33.755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Was es bringt
- Ausführen von 70B-Modellen mit 4 GB VRAM: Die Leistungsfähigkeit, hochparametrierte Modelle wie Llama 3 70B, Qwen oder DeepSeek selbst auf Einsteiger-Grafikkarten wie der GTX 1650 oder RTX 3050 auszuführen.
- Unterstützung für 405B Llama 3.1: Die Möglichkeit, Modelle mit 405 Milliarden Parametern, die in Rechenzentren hunderttausende Dollar teure GPU-Cluster erfordern, auf PCs mit 8 GB VRAM auszuführen.
- Schichtbasierte Speicherausführung (Layer-wise Execution): Anstatt das gesamte Modell in den VRAM einzupassen, werden die Schichten nacheinander von der Festplatte in den Arbeitsspeicher geladen und verarbeitet, wodurch der VRAM-Engpass umgangen wird.
- Bis zu 3-fache Geschwindigkeit durch blockbasierte Komprimierung: Beschleunigt die Datenübertragung von der Festplatte zur GPU, indem die Modellgewichte auf der NVMe-SSD in optimierten Blöcken gelesen werden.
- Volle Präzision ohne Einbußen bei der Quantisierungsqualität: Ermöglicht das Inferenzieren sogar in der originalen 16-Bit-Präzision (bfloat16), falls gewünscht, ohne die Notwendigkeit, Gewichte auf 4-Bit zu komprimieren.

## Installation
**Mit pip (PyPI)**

```
pip install airllm
```


## Technische Architektur und Funktionsweise
- Die sequentielle Natur von Transformer-Schichten: Ein Transformer-Netzwerk besteht aus 80 unabhängigen Schichten. Jede Schicht nimmt den Tensor-Output der vorherigen Schicht als Input. Es ist theoretisch nicht zwingend erforderlich, dass sich das gesamte Modell im Speicher befindet.
- Sequenzielles Auslagern (Sequential Offloading): AirLLM lädt nur die jeweils aktuell berechnete einzelne Schicht in den VRAM (ca. 1,5 GB). Sobald die Berechnungen für den Forward Pass der jeweiligen Schicht abgeschlossen sind, wird der Speicher freigegeben und die nächste Schicht von der Festplatte geladen.
- Geschwindigkeits- und Speicher-Kompromiss: Diese Architektur ist nicht für interaktive Chats gedacht, die Dutzende Token pro Sekunde erzeugen; sie ist ein unvergleichliches Einsparungstool für die stapelweise Datenanalyse, tiefgehendes Reasoning, Übersetzung, die Generierung synthetischer Daten und Modellbewertungsprozesse (Evals).
- Speicherabbildbasiertes Dateilesen (mmap): Bindet PyTorch-Tensoren direkt über die mmap-Methode an die Festplatte an und nutzt so direkt die Bandbreite der NVMe-SSD, ohne den System-RAM unnötig zu belasten.

## Beispiel für die Python-Verwendung
AirLLM hat eine extrem einfache Python-Syntax, die der der HuggingFace AutoModel-API sehr ähnlich ist:

## Wenn Sie nicht programmieren
Ich möchte ein Modell mit 70 Milliarden Parametern (zum Beispiel meta-llama/Llama-3-70B-Instruct) mithilfe der AirLLM-Bibliothek auf meiner lokalen Grafikkarte mit 4 GB VRAM-Kapazität ausführen. Ich habe den Befehl pip install airllm für die Installation verwendet. Könntest du den Python-Code erklären, der erforderlich ist, um mein Modell zu laden, Ausgaben mit Texteingaben zu generieren und einen Speicherüberlauf (Out-of-Memory) zu verhindern? Mir ist bewusst, dass ich sicherstellen muss, dass mein Speicherplatz auf der Festplatte ausreicht. Kannst du die Schritte erläutern, die ich befolgen muss?

## Häufig gestellte Fragen
- Wie schnell ist das Ausführen eines Modells mit AirLLM? Da AirLLM Schichten kontinuierlich zwischen Festplatte und GPU überträgt, hängt die Token-Generierungsgeschwindigkeit direkt von der Lesegeschwindigkeit Ihrer NVMe-SSD ab. Auf einer typischen Gen4-SSD läuft ein 70B-Modell mit einer Geschwindigkeit von 1–3 Token pro Sekunde. Diese Geschwindigkeit ist zwar für interaktives Chatten langsam, aber einzigartig, um riesige Modelle lokal ohne Hardwarekosten auszuführen.
- Wie viel freier Speicherplatz ist für AirLLM erforderlich? Ein Modell mit 70B Parametern benötigt im 16-Bit-Float-Format etwa 140 GB Speicherplatz. Bei 4-Bit-quantisierten Versionen sinkt dieser Wert auf etwa 35-40 GB. Für das 405B-Modell müssen hingegen mindestens 800 GB freier NVMe-Speicherplatz eingeplant werden.
- Kann ich die originalen Modellgewichte ohne Quantisierung verwenden? Ja. Einer der größten Vorteile von AirLLM besteht darin, dass die Notwendigkeit einer Quantisierung entfällt. Da VRAM-Einschränkungen auf Schichtbasis gelöst werden, können Sie die originalen 16-Bit-Gewichte ohne jeglichen Verlust an Schlussfolgerungsfähigkeit oder Genauigkeit ausführen.
- Läuft AirLLM auf Apple Silicon Macs oder nur auf der CPU? AirLLM ist grundsätzlich für die CUDA-Beschleunigung (NVIDIA-GPU) optimiert. Es unterstützt jedoch experimentell auch die CPU-Ausführung und MPS-Schichten (Apple Silicon Metal). Die höchste Leistung wird mit einer schnellen NVMe-SSD und einer NVIDIA-Grafikkarte erzielt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/airllm/
