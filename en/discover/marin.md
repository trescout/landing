# Open Development Platform for Foundational Model Research

A research program, software platform, and community for researching and developing foundation models. It documents scope from data processing through pretraining, finetuning, and evaluation.

- ★ 3,089
- Python
- GitHub Trending · 2026-08-25

## Updates

- **August 31, 2026:** Stars 1,967 → 3,089.

## Installation

**Clone the official repository**

```
git clone https://github.com/marin-community/marin.git
```

**Create the Python virtual environment**

```
uv venv --python 3.12
```

**Sync dependencies with uv**

```
uv sync --all-packages
```

## Running it

**Run the CPU smoke test**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```

## What does this tool do?

Runs experiments as dependent steps in topological order. The official first experiment demonstrates tokenizing TinyStories data and training a small language model; the open development approach documents code, data, decisions, and failed experiments.

## Who it is for

Teams researching data curation, transformation, filtering, tokenization, model training, and evaluation.

## What not to expect

Not for simple application development outside foundational model research, or for those unwilling to set up the required Python and development environment.

## Highlights

- Research scope spanning data processing through pretraining, finetuning, and evaluation
- Experiment workflow that executes dependent steps in topological order
- Open documentation covering failed experiments and development decisions

## First-use flow

1. Clone the official repository and create a virtual environment with Python 3.12 or newer
2. Synchronize dependencies with uv
3. Configure the MARIN_PREFIX environment variable
4. Run the offline TinyStories smoke test on CPU

## Safe start

The CPU smoke test is only for initial validation. CPU, GPU, and TPU dependencies may require separate hardware add-ons. WANDB_API_KEY and HF_TOKEN are needed only for respective tracking or closed-model workflows.

## First task prompt

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Run training of a small model on CPU with the offline TinyStories flow as an initial validation.

## Related dictionary terms

- [CPU](https://trescout.com/en/dictionary/cpu/)
- [GPU](https://trescout.com/en/dictionary/gpu/)

## Links

- [GitHub repository →](https://github.com/marin-community/marin)
- [Installation documentation →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [First experiment →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [Official README →](https://github.com/marin-community/marin)
- [Read in Turkish →](https://trescout.com/discover/marin/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-25: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/marin/
