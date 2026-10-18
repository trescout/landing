# High performance cores for some Delta Attention

Developed by Moonshot AI, FlashKDA offers high-performance kernels for the Some Delta Attention mechanism. This CUDA-based technology aims to accelerate attention calculations in large language models.

- ★ 1,043
- Cuda
- GitHub Trending · 2026-07-30

## What you get

- CUDA-based accelerated attention calculations
- Working efficiently on large language models
- Kernel structure optimized with CUTLASS

## Installation

**Basic setup**

```
git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda
cd flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation .
```

**Build for all architectures**

```
FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation .
```

## Running it

**Using FLA as a backend**

```
pip install -U flash-linear-attention
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to speed up some Delta Attention calculations using the FlashKDA tool. How can I optimize my model's attention mechanism by using the chunk_kda function under torch.inference_mode(), integrated with the flash-linear-attention library? Please create an application example, taking into account the necessary parameters and hardware requirements I need to pay attention to.

Repository: https://github.com/MoonshotAI/FlashKDA. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Kernels](https://trescout.com/en/dictionary/kernels/)
- [Attention](https://trescout.com/en/dictionary/attention/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for developers who want to accelerate attention calculations on large language models on CUDA.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/MoonshotAI/FlashKDA)
- [Read in Turkish →](https://trescout.com/discover/flashkda/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-30: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/flashkda/
