# Video production with artificial intelligence in the local system

Developed by Lightricks, LTX-2 offers a Python inference and low-rank adaptation (LoRA) training package for artificial intelligence models that produce audio and video. This toolset allows users to train LTX-2 models with their own data and run model outputs on local systems.

- ★ 9,267
- GitHub Trending · 2026-06-19

## What you get
- Provides audio and video synchronization
- You can train LoRA with your own data
- High quality video production on local system

## Installation
**Clone the repository from GitHub and enter the directory**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Download model weights (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```


## Running it
**run inference pipeline with uv**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```


## If you don't write code
Please create a video using the LTX-2 model that describes the scene I want in detail and includes audio and video synchronization. Have the model produce output by specifying scene details, character's appearance, camera angle and speech text.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ltx-2/
