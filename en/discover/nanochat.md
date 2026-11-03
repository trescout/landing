# Tool for training artificial intelligence models

karpathy/nanochat is an experimental software framework developed for training large language models (LLMs) that can run on a single graphics processing unit (GPU). Covering tokenization, pre-training, fine-tuning, evaluation, and inference processes, this project offers developers a minimal and modifiable structure.

- ★ 59,998
- Python
- GitHub Trending · 2026-11-03

## What you get

- Allows you to train an AI model on a single graphics processing unit.
- Enables you to manage text generation steps via the command line.
- Offers flexible setup options for different hardware types.

## Installation

**Installing dependencies**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Running it

**Starting the training process**

```
bash runs/speedrun.sh
```

**Chatting with the model**

```
python -m scripts.chat_cli
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install and run the AI tool named nanochat. First, install the dependencies and activate the virtual environment using the command uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate. Then, start the process with the command bash runs/speedrun.sh, and when it is complete, interact with the model by running python -m scripts.chat_cli.

Repository: https://github.com/karpathy/nanochat. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Fine-tuning](https://trescout.com/en/dictionary/fine-tuning/)
- [GPU](https://trescout.com/en/dictionary/gpu/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for developers who want to train and test large language models from scratch.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/karpathy/nanochat)
- [Read in Turkish →](https://trescout.com/discover/nanochat/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-11-03: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/nanochat/
