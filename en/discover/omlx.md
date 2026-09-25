# AI server for Mac computers

Omlx is a next-generation local large language model (LLM) inference server for Apple Silicon (M1/M2/M3/M4) Macs, offering continuous batching and SSD caching capabilities. It combines the Apple MLX framework with an OpenAI-compatible API and a macOS menu bar interface.

- ★ 21,147
- Python
- GitHub Trending · 2026-08-18

## Updates
- August 31, 2026: Stars 20,793 → 21,147, latest release v0.6.4 (August 29, 2026).
- August 27, 2026: Stars 20,069 → 20,793, latest release v0.6.3rc3 (August 24, 2026).
- August 20, 2026: Stars 19,758 → 20,069, latest release v0.6.3rc2 (August 20, 2026).
- August 19, 2026: Stars 19,519 → 19,758, latest release v0.6.3rc1 (August 19, 2026).

## What you get
- Apple MLX and Metal hardware acceleration: Directly leverages Apple Silicon's Unified Memory Architecture (UMA) to completely eliminate memory copying bottlenecks between CPU and GPU.
- Continuous Batching: Combines concurrent requests from multiple users and AI agents into a single compute pass, boosting server throughput by up to 3x.
- SSD caching and chunked prefill: Offloads key-value (KV) cache to fast NVMe SSD during long context windows, preventing Out-Of-Memory (OOM) crashes.
- OpenAI-compatible standard API: Works out-of-the-box with Cursor, Open WebUI, Continue, and LangChain via /v1/chat/completions and /v1/models endpoints.
- macOS menu bar control: Easily start, stop, switch models, and monitor real-time memory usage without opening the terminal.

## Installation

**Installation with Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Running it

**Starting background service**

```
omlx start
```

**Downloading and serving a specific model**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Technical architecture and working principle

Omlx is built upon Apple's MLX machine learning framework. It rests on three key architectural pillars engineered to transcend traditional Mac inference limits (such as llama.cpp or Ollama):
- Full utilization of Unified Memory (UMA): Unlike PCs with discrete graphics cards, Apple Silicon Macs allow GPU cores to address 128 GB or 192 GB of RAM directly. Omlx processes this massive memory pool with zero latency via Metal Shading Language (MSL) kernels.
- Dynamic KV cache management (PagedAttention): Allocates key-value tensors in paged blocks to prevent memory fragmentation during multi-turn chats, immediately freeing memory once prompts finish.
- SSD-spill cache tier: When KV cache in 32K or 128K context windows exceeds physical RAM, Omlx automatically pages to Apple's high-speed NVMe SSD, allowing inference to proceed smoothly without crashes.

## OpenAI-compatible local API integration

When launched, Omlx exposes an OpenAI-compatible REST API locally (default http://localhost:8000). You can seamlessly plug it into code editors and AI agent tools:

**API Test with cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "What is the primary architectural advantage of Apple Silicon?"}],
    "temperature": 0.7
  }'
```

## If you do not code
🤖 If you do not code
I want to run a local large language model using Omlx on my Apple Silicon Mac. After installing via Homebrew, could you explain step by step how to start the background server, manage models from the macOS menu bar, and connect Cursor code editor or a Python script using the openai library to this local model?

- **Who it is for:** AI developers and Mac power users who want maximum inference speed and complete local privacy on Apple Silicon hardware.
- **License:** Apache-2.0 (Open Source License)
- **Framework:** Apple MLX and Python-based local inference engine
- **Hardware:** Apple Silicon M1, M2, M3, M4 series (Pro, Max, Ultra supported)

## Frequently asked questions
- What is the primary difference between Omlx and Ollama? While Ollama typically runs on llama.cpp in C++, Omlx is natively built on Apple's MLX framework. This deeper integration with Metal and the Apple Neural Engine delivers higher token throughput, especially during continuous batching and long context windows.
- Which models can be run with 16 GB or 24 GB of RAM? 4-bit quantized 8B models (Llama 3, Qwen 2.5, Mistral) require roughly 5-6 GB and run smoothly on 16 GB Macs. Devices with 24 GB or 36 GB unified memory can comfortably host 14B or 32B models.
- Does SSD caching degrade Mac SSD lifespan? No. Omlx uses smart buffering to avoid unnecessary write cycles. It activates only when context memory nears physical RAM limits, minimizing disk wear.
- Does it run on older Intel Macs or Windows/Linux PCs? No. Omlx is strictly optimized for Apple Silicon (ARM architecture) and Apple MLX. It does not run on Intel Macs or x86 machines.

## Links
- [GitHub →](https://github.com/jundot/omlx)

## Related dictionary terms
Apple Silicon Continuous Batching LLM Local Open Source

---
Source: TreScout Discover · https://trescout.com/en/discover/omlx/
