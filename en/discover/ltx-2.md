# Video production with artificial intelligence in the local system

Developed by Lightricks, LTX-2 offers a Python inference and low-rank adaptation (LoRA) training package for artificial intelligence models that produce audio and video. This toolset allows users to train LTX-2 models with their own data and run model outputs on local systems.

- ★ 9,567
- GitHub Trending · 2026-06-19

## Updates

- **October 2, 2026:** Stars 9,562 → 9,567, latest release v1.4.2 (October 2, 2026).
- **October 1, 2026:** Stars 9,552 → 9,562, latest release v1.4.1 (September 30, 2026).
- **September 29, 2026:** Stars 9,267 → 9,552, latest release v1.4.0 (September 29, 2026).
- **August 27, 2026:** Stars 8,587 → 9,267, latest release v1.3.0 (August 26, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Please create a video using the LTX-2 model that describes the scene I want in detail and includes audio and video synchronization. Have the model produce output by specifying scene details, character's appearance, camera angle and speech text.

## Related dictionary terms

- [LoRA](https://trescout.com/en/dictionary/lora/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [CLI](https://trescout.com/en/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For users who want to create audio and video AI videos or train models on their own local system.

## Links

- [GitHub repository →](https://github.com/Lightricks/LTX-2)
- [Read in Turkish →](https://trescout.com/discover/ltx-2/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-19: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ltx-2/
