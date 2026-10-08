# Run massive AI models locally

Colibri is a C-based engine that enables running large-scale Mixture of Experts (MoE) models on local computers with low hardware requirements. By streaming expert layers from the disk, it makes it possible to run high-capacity AI models on limited hardware.

- ★ 40,157
- C
- GitHub Trending · 2026-09-11

## Updates

- **October 7, 2026:** Stars 39,698 → 40,157, latest release v2.0.0 (October 6, 2026).
- **October 5, 2026:** Stars 37,791 → 39,698, latest release v1.12.1 (September 24, 2026).
- **September 27, 2026:** Stars 36,260 → 37,791, latest release v1.12.1 (September 24, 2026).
- **September 19, 2026:** Stars 34,474 → 36,260, latest release v1.11.0 (September 13, 2026).

## What you get

- Runs high-capacity models on limited hardware
- Manages VRAM, RAM, and disk memory as a single layer
- Provides efficiency by streaming expert layers

## Installation

**Compiling from source code**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
```

## Running it

**Launch chat interface**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable  (+ make cuda-dsv4-dg-dll on RTX 50)
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run large-scale AI models on my local computer using the Colibri engine. Configure it to use my hardware resources (VRAM, RAM, and NVMe disk) in the most efficient way possible. Explain step-by-step how I can optimize and run models like GLM or DeepSeek according to my system's memory capacity.

## Related dictionary terms

- [Mixture of Experts](https://trescout.com/en/dictionary/mixture-of-experts/)
- [VRAM](https://trescout.com/en/dictionary/vram/)
- [RAM](https://trescout.com/en/dictionary/ram/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Designed for researchers and developers who want to run large language models on their own computers with limited hardware resources.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/JustVugg/colibri)
- [Read in Turkish →](https://trescout.com/discover/colibri/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-11: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/colibri/
