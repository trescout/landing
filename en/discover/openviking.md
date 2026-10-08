# File system memory for artificial intelligence agents

Developed by Volcengine, OpenViking offers a self-improving context database for AI agents. This system combines agent memory, information retrieval (RAG) processes and abilities under a single roof.

- ★ 39,151
- Python
- GitHub Trending · 2026-08-18

## Updates

- **October 3, 2026:** Stars 38,859 → 39,151, latest release v0.4.23 (October 2, 2026).
- **September 28, 2026:** Stars 38,733 → 38,859, latest release v0.4.22 (September 28, 2026).
- **September 27, 2026:** Stars 37,128 → 38,733, latest release v0.4.21 (September 20, 2026).
- **September 14, 2026:** Stars 36,182 → 37,128, latest release v0.4.20 (September 14, 2026).

## What you get

- Organizes information hierarchically like a file system.
- It reduces the cost of artificial intelligence with layered loading.
- Makes agent history traceable and debuggable.

## Installation

**Server installation and startup**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```

## Running it

**Start a chat with bot support**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Construct context management for an artificial intelligence agent using the OpenViking database. It structures the information via the viking:// protocol by separating the information into L0 summary, L1 overview and L2 detail layers. By placing the agent's memory, resources, and capabilities in this virtual file system, it allows it to navigate directories during interrogation and create long-term memory by learning from past sessions.

## Related dictionary terms

- [RAG](https://trescout.com/en/dictionary/rag/)
- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to combine the memory management, information retrieval processes, and capabilities of AI agents into one organized system.
- **License:** AGPL-3.0

## Links

- [GitHub repository →](https://github.com/volcengine/OpenViking)
- [Read in Turkish →](https://trescout.com/discover/openviking/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-18: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openviking/
