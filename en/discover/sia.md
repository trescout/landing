# Test AI models autonomously

SIA is a self-improving AI framework developed to autonomously improve the performance of AI models and agents on specific benchmark tasks. This Python-based system enables artificial intelligence systems to optimize their processes by analyzing their own outputs.

- ★ 1,478
- Python
- GitHub Trending · 2026-06-12

## What you get

- It autonomously improves the task performance of artificial intelligence models.
- Meta provides cyclic refinement between target and feedback agents.
- It offers high accuracy and processing speed efficiency in benchmark tasks.

## Installation

**Installation with Claude Models**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Setup with Multi Provider (OpenHands)**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..."   # for anthropic/* models
export GEMINI_API_KEY="..."      # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..."      # for openai/* models
```

## Running it

**Starting the Self-Healing Cycle**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Visualization Panel**

```
sia web
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to improve the performance of an AI agent using the SIA framework. After completing the installation, which command should I use to start the self-improvement cycle by selecting one of the available tasks (e.g. gpqa) and how should I interpret the outputs at the end of the process (target_agent.py, agent_execution.json, improvement.md)? Also, how can I include my own custom task directory in the system?

## Related dictionary terms

- [Benchmark](https://trescout.com/en/dictionary/benchmark/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for developers and researchers who want to optimize the performance of AI models through autonomous improvement processes.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/hexo-ai/sia)
- [Read in Turkish →](https://trescout.com/discover/sia/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/sia/
