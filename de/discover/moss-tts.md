# Erzeugen Sie natürliche und sanfte Klänge

MOSS-TTS (MOSI.AI und OpenMOSS); Es handelt sich um eine Open-Source-Modellfamilie, die eine hochauflösende Sprach- und Tonwiedergabe bietet. Es bietet Lösungen für Szenarien wie Langtext-Sprachsynthese, Unterstützung mehrerer Sprecher und Echtzeit-Streaming.

- ★ 3.939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## Was bietet es?
- Es bietet eine High-Fidelity-Sprach- und Stimmsynthese.
- Es bietet Unterstützung für mehrere Lautsprecher.
- Unterstützt Echtzeit-Audio-Streaming.
- Es basiert auf der Open-Source-Modellfamilie.

## Wie installiere ich, wie verwende ich?
**Erstellen Sie eine Conda-Umgebung**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Klonen und installieren Sie das Repository**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Führen Sie die Gradio-Demo aus**

```
python clis/moss_tts_app.py
```


## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/moss-tts/
