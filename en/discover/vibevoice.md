# Analyzing long audio recordings with artificial intelligence

Published by Microsoft, VibeVoice was developed as an open source voice AI framework. With its Python-based structure, the system allows users to train their own sound models and integrate them into their applications.

- ★ 54,502
- GitHub Trending · 2026-06-07

**TreScout note:** The repository changed after it was published: The part that converts sound to text remains, the part that converts text to sound has been withdrawn. Its distinguishing feature is that it can process long records at once. It's a fast-changing project, take a look at the current state of the warehouse before adding it to your business.

## Updates

- **September 27, 2026:** Stars 51,860 → 54,502.
- **August 2, 2026:** Stars 48,569 → 51,860.

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to analyze the 60-minute audio recording I have using the VibeVoice model. I need to retrieve who the speakers are, when they spoke, and the content they said as a structured text file. I also want to add custom keywords so that the model recognizes technical terms more accurately, how can I structure this process?

## Related dictionary terms

- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for users who want to quickly and structuredly convert long-term audio recordings, meeting summaries or podcast content into text.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/microsoft/VibeVoice)
- [Read in Turkish →](https://trescout.com/discover/vibevoice/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-07: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/vibevoice/
