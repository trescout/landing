# DeepSeek execution engine on native hardware

Developed by Salvatore Sanfilippo, the creator of Redis, ds4 is an inference engine that allows running DeepSeek models on local hardware. This tool, written in C language, offers the opportunity to run high-performance models on different graphics processors thanks to Metal, CUDA and ROCm support.

- ★ 23,530
- C
- GitHub Trending · 2026-08-03

## Updates

- **October 5, 2026:** Stars 22,197 → 23,530.
- **September 10, 2026:** Stars 21,134 → 22,197.
- **August 11, 2026:** Stars 20,117 → 21,134.

## What you get

- Runs high-performance AI models on consumer-grade hardware
- Allows model usage even with limited memory capacity by streaming data via SSD
- Enables creating enterprise-level LLM server with multi-GPU support

## Installation

**Build to suit your hardware**

```
make                  # macOS Metal
make cuda-spark       # Linux CUDA, DGX Spark / GB10
make cuda-generic     # Linux CUDA, other local CUDA GPUs
make strix-halo       # Linux ROCm, AMD Strix Halo
make cpu              # CPU-only diagnostics build
```

**Download the model**

```
./download_model.sh q2-imatrix   # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix  # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix   # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix  # 512 GB RAM machines, PRO q2 imatrix quant
```

## Running it

**Initialize the model**

```
./download_model.sh q2-imatrix

./ds4 \
  -m ./ds4flash.gguf \
  --ssd-streaming \
  --ssd-streaming-cache-experts 32GB \
  --ctx 32768 \
  --nothink
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Help me choose the most suitable DeepSeek or GLM model according to the hardware features of my system. Which download command should I use and how can I overcome the memory bottleneck by activating the streaming feature over SSD? Also, explain the basic configuration settings required for me to use this artificial intelligence system I have installed as a local server.

## Related dictionary terms

- [Inference Engine](https://trescout.com/en/dictionary/inference-engine/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers and system administrators who want to run high-performance artificial intelligence models on their own local hardware.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/antirez/ds4)
- [Read in Turkish →](https://trescout.com/discover/ds4/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-03: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ds4/
