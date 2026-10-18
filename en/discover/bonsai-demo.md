# AI models on local device

The Bonsai demo project provides a toolset designed to simplify the deployment processes of machine learning models. The software helps developers optimize their application processes by turning complex model architectures into manageable workflows.

- ★ 2,706
- Shell
- GitHub Trending · 2026-07-17

## Updates

- **September 19, 2026:** Stars 1,587 → 2,706.

## What you get

- Runs high-performance models locally with low memory usage.
- It offers advanced features such as visual processing and ride-hailing.
- Provides broad compatibility with different hardware architectures.

## Installation

**macOS and Linux installation**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Running it

**Starting the local server**

```
./scripts/start_llama_server.sh    # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run AI models on my local device using the bonsai-demo project. After cloning the git repository required for installation, I need to define my Hugging Face token information and download the dependencies and models with the ./setup.sh command. Then, using the ./scripts/start_llama_server.sh command, I can stand up the local server and interact with the AI ​​via port 8080 through my browser.

Repository: https://github.com/PrismML-Eng/Bonsai-demo. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

If an API key is required, do not ask me to type it into the chat. Show me how to add it to the .env file and ensure this file is not pushed to Git.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Machine Learning](https://trescout.com/en/dictionary/machine-learning/)
- [Shell](https://trescout.com/en/dictionary/shell/)
- [Token](https://trescout.com/en/dictionary/token/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for developers who want to run high-throughput AI models on their native hardware.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/PrismML-Eng/Bonsai-demo)
- [Read in Turkish →](https://trescout.com/discover/bonsai-demo/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-17: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/bonsai-demo/
