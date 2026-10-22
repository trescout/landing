# Efficient AI inference on CPU

Developed by Microsoft, BitNet provides an official inference framework for 1-bit large language models (LLMs). Written in C++, this tool aims to optimize the execution of low-bit precision models.

- ★ 40,731
- C++
- GitHub Trending · 2026-10-12

## What you get

- Runs AI models on standard computer processors with high speed and low energy consumption.
- Allows you to use compressed 1-bit language models on your local device without loss of quality.
- Enables direct chatting with downloaded models thanks to dialogue mode support.

## Installation

**Download the source code**

```
git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet
```

**Prepare the environment and install dependencies**

```
# (Recommended) Create a new conda environment
conda create -n bitnet-cpp python=3.10
conda activate bitnet-cpp

pip install -r requirements.txt
```

## Running it

**Download the model and configure the environment**

```
# Manually download the model and run with local path
huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
```

**Run the model in chat mode**

```
# Run inference with the quantized model
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run a 1-bit artificial intelligence model on my computer using the BitNet infrastructure. First, guide me through cloning the project with the 'git clone --recursive https://github.com/microsoft/BitNet.git' command and navigating into its directory, creating a Python 3.10 environment with the Conda package manager, and installing the requirements. Next, explain step by step, with enough simplicity for someone who does not know coding to understand, how to download the microsoft/BitNet-b1.58-2B-4T-gguf model via the open-source model platform Hugging Face, set it up using 'setup_env.py', and finally launch chat mode using the 'run_inference.py' script.

Repository: https://github.com/microsoft/BitNet. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Inference Framework](https://trescout.com/en/dictionary/inference-framework/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [Clone](https://trescout.com/en/dictionary/clone/)
- [Framework](https://trescout.com/en/dictionary/framework/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for users who want to run fast and lightweight language models on their computer's CPU without needing powerful graphics cards.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/microsoft/BitNet)
- [Read in Turkish →](https://trescout.com/discover/bitnet/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/bitnet/
