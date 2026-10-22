# AI server for Mac computers

Omlx is a next-generation local large language model (LLM) inference server that offers continuous batching and SSD caching capabilities for Mac computers with Apple Silicon (M1/M2/M3/M4) processors. It combines the Apple MLX framework with an OpenAI-compatible API and a macOS menu bar interface.

- ★ 22,973
- Python
- GitHub Trending · 2026-08-18

## Updates

- **October 21, 2026:** Stars 22,855 → 22,973, latest release v0.7.2 (October 21, 2026).
- **October 16, 2026:** Stars 22,825 → 22,855, latest release v0.7.1rc1 (October 15, 2026).
- **October 15, 2026:** Stars 22,655 → 22,825, latest release v0.7.1.dev2 (October 15, 2026).
- **October 9, 2026:** Stars 22,409 → 22,655, latest release v0.7.1.dev1 (October 9, 2026).

## What you get

- Apple MLX and Metal hardware acceleration: Completely eliminates the memory copying bottleneck between the CPU and GPU by directly utilizing Apple Silicon processors' Unified Memory Architecture (UMA).
- Continuous Batching: Combines a large number of concurrent user and agent prompts into a single computation cycle, increasing server throughput by up to 3x.
- SSD caching and Chunked Prefill: Prevents out-of-memory (OOM) crashes in long context windows by storing the key-value (KV) cache on an NVMe SSD.
- OpenAI-compatible standard API: Thanks to the /v1/chat/completions and /v1/models endpoints, it works with zero configuration with tools like Cursor, Open WebUI, Continue, and LangChain.
- macOS menu bar control: Offers the convenience of starting, stopping, and selecting models for the server, as well as monitoring memory consumption with live charts, all without entering the Terminal.

## Installation

**Installation with Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Running it

**Starting the background service**

```
omlx start
```

**Downloading and serving a specific model**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Technical architecture and working principle

- Full utilization of unified memory (UMA): Unlike PCs with discrete graphics cards, up to 128 GB or 192 GB of RAM on Apple Silicon Macs can be directly addressed by the GPU cores. Omlx processes this massive memory pool with zero latency using Metal Shading Language (MSL) kernels.
- Dynamic KV cache management (PagedAttention): Allocates key-value tensors in paged blocks to prevent memory fragmentation across multiple sessions. The used memory is immediately freed when the prompt finishes.
- SSD-overflow cache layer: When the KV cache exceeds RAM in massive context windows like 32K and 128K, Omlx automatically pages out to Apple's high-speed unified SSD storage. This allows the model to continue inference without crashing.

## OpenAI-compatible native API integration

**API Testing with cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Apple Silicon mimarisinin temel avantajı nedir?"}],
    "temperature": 0.7
  }'
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run a local large language model using the Omlx server on my Apple Silicon Mac. Could you explain step by step how to run the server in the background after completing the installation via Homebrew, manage model selection from the menu bar, and connect to this local model via the Cursor code editor or the Python openai library?

Repository: https://github.com/jundot/omlx. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Frequently asked questions

- What is the main difference between Omlx and Ollama? While Ollama generally uses the C++-based llama.cpp infrastructure, Omlx runs directly on the MLX framework developed by Apple. This enables deeper integration with the Metal and neural engine units of Apple Silicon chips, delivering higher token generation speeds, particularly in continuous batching and long contexts.
- Which models can be run with 16 GB or 24 GB of RAM? 4-bit quantized 8B parameter models (Llama 3, Qwen 2.5, Mistral) take up about 5-6 GB of memory and run extremely smoothly on 16 GB Macs. On devices with 24 GB or 36 GB of unified memory, 14B or 32B models can be loaded comfortably.
- Does SSD caching wear down the Mac's disk lifespan? No. Omlx uses smart buffering algorithms to prevent unnecessary write cycles during caching operations. It only engages when the context memory approaches the RAM limit, keeping disk wear to a minimum.
- Does it run on older Intel-based Macs? No. Omlx is specifically optimized for Apple Silicon (ARM architecture) and the Apple MLX framework. It does not run on Intel-based Macs or Windows/Linux x86 computers.

## Related dictionary terms

- [Continuous Batching](https://trescout.com/en/dictionary/continuous-batching/)
- [SSD Caching](https://trescout.com/en/dictionary/ssd-caching/)
- [Context Window](https://trescout.com/en/dictionary/context-window/)
- [Caching](https://trescout.com/en/dictionary/caching/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [RAM](https://trescout.com/en/dictionary/ram/)

- **Who it is for:** Intended for AI developers who want to run large language models (LLMs) at maximum speed and with local privacy on Apple Silicon Macs.
- **License:** Apache-2.0 (Open source license)
- **Framework:** Apple MLX and Python-based local inference engine
- **Hardware:** Apple Silicon M1, M2, M3, M4 series (Pro, Max, Ultra supported)

## Links

- [GitHub repository →](https://github.com/jundot/omlx)
- [Read in Turkish →](https://trescout.com/discover/omlx/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-18: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/omlx/
