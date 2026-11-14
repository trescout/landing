# Local AI engine TensorFold

ashhart/TensorFold offers an inference engine for large language models (LLMs) with Metal, CUDA, and Vulkan support. Developed in the Zig programming language, this tool allows running models directly on Apple Silicon and NVIDIA GPUs without requiring Python or MLX installation.

- ★ 2,080
- Zig
- GitHub Trending · 2026-11-13

## Updates

- **November 14, 2026:** Stars 1,998 → 2,080, latest release v1.2.8 (November 13, 2026).
- **November 13, 2026:** Stars 1,996 → 1,998, latest release v1.2.7 (November 11, 2026).

## What you get

- Runs large language models directly on Apple Silicon and NVIDIA GPUs.
- Provides service via a binary file without needing Python or MLX installation.
- Allows selecting models and chatting with a local web application.

## Installation

**Installation on Mac**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Running it

**Sending a Request**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install the TensorFold tool on my Mac computer with an Apple Silicon chip, download the Qwen3.5-2B model, and start the server. To do this, you need to run the following commands in order:

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

Then, to verify that the server is running, you can send a request with the following command:

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Repository: https://github.com/ashhart/TensorFold. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Temperature](https://trescout.com/en/dictionary/temperature/)
- [Application](https://trescout.com/en/dictionary/application/)
- [Inference Engine](https://trescout.com/en/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [LLM](https://trescout.com/en/dictionary/llm/)

- **Who it is for:** Designed for developers who want to run large language models on Apple Silicon or NVIDIA GPUs without installing Python.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/ashhart/TensorFold)
- [Read in Turkish →](https://trescout.com/discover/tensorfold/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-11-13: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/tensorfold/
