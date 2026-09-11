# Run massive AI models locally

Colibri is a C-based engine that enables running large-scale Mixture of Experts (MoE) models on local computers with low hardware requirements. By streaming expert layers from the disk, it makes it possible to run high-capacity AI models on limited hardware.

- ★ 27,610
- C
- GitHub Trending · 2026-09-11

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
I want to run large-scale AI models on my local computer using the Colibri engine. Configure it to use my hardware resources (VRAM, RAM, and NVMe disk) in the most efficient way possible. Explain step-by-step how I can optimize and run models like GLM or DeepSeek according to my system's memory capacity.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/colibri/
