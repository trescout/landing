# Open Development Platform for Foundational Model Research

A research program, software platform, and community for researching and developing foundation models. It documents scope from data processing through pretraining, finetuning, and evaluation.

- ★ 3,089
- Python
- GitHub Trending · 2026-08-25

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
- Clone the official repository and create a virtual environment with Python 3.12 or newer
- Synchronize dependencies with uv
- Configure the MARIN_PREFIX environment variable
- Run the offline TinyStories smoke test on CPU

## Safe start

## First task prompt
Run training of a small model on CPU with the offline TinyStories flow as an initial validation.

## Related dictionary terms

## Links
- GitHub repository →
- Installation documentation →
- First experiment →
- Official README →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/marin/
