# DeepSeek execution engine on native hardware

Developed by Salvatore Sanfilippo, the creator of Redis, ds4 is an inference engine that allows running DeepSeek models on local hardware. This tool, written in C language, offers the opportunity to run high-performance models on different graphics processors thanks to Metal, CUDA and ROCm support.

- ★ 21,134
- C
- GitHub Trending · 2026-08-03

## Update
- August 11, 2026: Star 20,117 → 21,134.

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
Help me choose the most suitable DeepSeek or GLM model according to the hardware features of my system. Which download command should I use and how can I overcome the memory bottleneck by activating the streaming feature over SSD? Also, explain the basic configuration settings required for me to use this artificial intelligence system I have installed as a local server.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ds4/
