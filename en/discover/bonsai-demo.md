# AI models on local device

The Bonsai demo project provides a toolset designed to simplify the deployment processes of machine learning models. The software helps developers optimize their application processes by turning complex model architectures into manageable workflows.

- ★ 1,587
- Shell
- GitHub Trending · 2026-07-17

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
I want to run AI models on my local device using the bonsai-demo project. After cloning the git repository required for installation, I need to define my HuggingFace token information and download the dependencies and models with the ./setup.sh command. Then, using the ./scripts/start_llama_server.sh command, I can stand up the local server and interact with the AI ​​via port 8080 through my browser.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/bonsai-demo/
