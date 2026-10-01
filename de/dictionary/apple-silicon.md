# Was ist Apple Silicon?

Apple Silicon ist eine von Apple intern entwickelte, ARM-basierte Hochleistungs-SoC-Prozessorfamilie (System on a Chip) für Mac- und iPad-Geräte, die CPU, GPU, Neural Engine und Unified Memory auf einer einzigen Siliziumplatte vereint.

## Konzeptionelle Entstehung, Geschichte und der große Wechsel von x86 zu ARM
"Silicon" (Silizium) ist das chemische Basiselement, das bei der Herstellung von Halbleiter-Mikrochips verwendet wird. Apple Silicon hingegen steht für das kundenspezifische Mikroprozessordesign von Apple, mit dem die Abhängigkeit des Unternehmens von Drittanbieter-Chipherstellern (Intel, Motorola, IBM) beendet und eigene Hardware und Software vertikal integriert werden.

## System-on-a-Chip (SoC) und Unified Memory Architecture (UMA)
In einem herkömmlichen Desktop- oder Laptop-Computer ist die Hardware modular aufgebaut: Es gibt einen separaten CPU-Sockel auf dem Motherboard, eine riesige dedizierte Grafikkarte (GPU) in einem PCIe-Steckplatz, separate RAM-Module und Motherboard-Brücken. Um ein von der CPU verarbeitetes Bild auf dem Bildschirm auszugeben, müssen Daten über den Motherboard-Bus vom RAM in den eigenen VRAM der GPU kopiert werden. Dies führt zu Latenz und hohem Stromverbrauch.

## Kern-Anatomie, Beschleuniger und Rosetta 2
Die reine Leistungs- und Effizienzbalance von Apple Silicon basiert auf drei grundlegenden technischen Komponenten:

## Häufige Fragen
**Was bedeutet Apple Silicon und welche Prozessoren umfasst es?**
Es ist die von Apple selbst entwickelte ARM-basierte System-on-Chip (SoC)-Prozessorfamilie. Sie umfasst die A-Serie-Chips in iPhones und iPads sowie die M-Serie-Prozessoren (M1, M2, M3, M4 und deren Varianten), die Mac-Computer antreiben.

**Warum unterscheidet sich die Unified Memory Architecture (UMA) von herkömmlichem RAM und VRAM?**
In herkömmlichen Systemen verfügt die CPU über einen separaten System-RAM und die Grafikkarte über einen separaten VRAM, wobei Daten zwischen den beiden kopiert werden. Bei UMA befindet sich der Speicher direkt im Prozessor-Package; CPU, GPU und die KI-Engine greifen ohne Kopierlatenz und ohne Verzögerungskosten auf denselben Speicherpool zu.

**Funktionieren ältere Intel-Anwendungen auf einem Mac mit Apple Silicon-Prozessor?**
Ja, dank der in das macOS-Betriebssystem integrierten Rosetta-2-Übersetzungs-Engine wird die große Mehrheit der für Intel (x86_64) geschriebenen Anwendungen vom Benutzer unbemerkt mit hoher Geschwindigkeit ausgeführt.

**Warum ist Apple Silicon bei der Entwicklung nativer künstlicher Intelligenz (LLM) so beliebt?**
Weil dank der Unified Memory Architecture riesige Speicherpools wie 64 GB, 96 GB oder 128 GB direkt von der GPU als VRAM genutzt werden können. Dies ermöglicht die lokale Ausführung riesiger Sprachmodelle mit 70B+ Parametern ohne teure Server-GPUs.


## Verwandte Begriffe
- [Runtime](/de/dictionary/runtime/)
- [Computer Science](/de/dictionary/computer-science/)
- [Assembly](/de/dictionary/assembly/)
- [Memory Management](/de/dictionary/memory-management/)
- [Emulator](/de/dictionary/emulator/)
- [Cloud Computing](/de/dictionary/cloud-computing/)

## Verwandte Werkzeuge
- [Minimind](/de/discover/minimind/)
- [Container](/de/discover/container/)
- [Airllm](/de/discover/airllm/)
- [Omlx](/de/discover/omlx/)
- [Palmier Pro](/de/discover/palmier-pro/)
- [Openmed](/de/discover/openmed/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/apple-silicon/
