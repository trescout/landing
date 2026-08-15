# Analyzing long audio recordings with artificial intelligence

Published by Microsoft, VibeVoice was developed as an open source voice AI framework. With its Python-based structure, the system allows users to train their own sound models and integrate them into their applications.

- ★ 51,860
- GitHub Trending · 2026-06-07

## What you get
- Converts up to 60 minutes of audio recording to text at a time.
- It provides speaker ID, timestamp and content details in a structured way.
- Provides user-defined keyword support for custom terms and names.

## Installation
**Install from GitHub**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```


## Running it
**Gradio demo**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Transcription from file**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```


## If you don't write code
I want to analyze the 60-minute audio recording I have using the VibeVoice model. I need to retrieve who the speakers are, when they spoke, and the content they said as a structured text file. I also want to add custom keywords so that the model recognizes technical terms more accurately, how can I structure this process?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/vibevoice/
