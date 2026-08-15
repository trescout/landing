# Videoproduktion mit künstlicher Intelligenz im lokalen System

LTX-2 wurde von Lightricks entwickelt und bietet ein Python-Inferenz- und Low-Rank-Adaptions-Trainingspaket (LoRA) für Modelle der künstlichen Intelligenz, die Audio und Video produzieren. Mit diesem Toolset können Benutzer LTX-2-Modelle mit ihren eigenen Daten trainieren und Modellausgaben auf lokalen Systemen ausführen.

- ★ 8.587
- GitHub Trending · 2026-06-19

## Aktualisieren
- 12. August 2026: Star 8.554 → 8.587, neueste Version v1.2.0 (11. August 2026).
- 10. August 2026: Stern 7.550 → 8.554.

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
Bitte erstellen Sie ein Video mit dem LTX-2-Modell, das die gewünschte Szene detailliert beschreibt und eine Audio- und Videosynchronisierung umfasst. Lassen Sie das Modell eine Ausgabe erstellen, indem Sie Szenendetails, das Aussehen der Figur, den Kamerawinkel und den Sprachtext angeben.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ltx-2/
