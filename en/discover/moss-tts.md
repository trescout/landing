# Produce Natural and Smooth Sounds

MOSS-TTS (MOSI.AI and OpenMOSS); It is an open source model family that provides high fidelity speech and sound reproduction. It offers solutions for scenarios such as long-text speech synthesis, multi-speaker support, and real-time streaming.

- ★ 3,939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## What does it offer?
- It provides high-fidelity speech and voice synthesis.
- It offers multi-speaker support.
- Supports real-time audio streaming.
- It is based on the open source model family.

## How to install, how to use?
**Create conda environment**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Clone and install the repository**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Run Gradio demo**

```
python clis/moss_tts_app.py
```


## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/moss-tts/
