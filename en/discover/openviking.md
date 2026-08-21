# File system memory for artificial intelligence agents

Developed by Volcengine, OpenViking offers a self-improving context database for AI agents. This system combines agent memory, information retrieval (RAG) processes and abilities under a single roof.

- ★ 31,462
- Python
- GitHub Trending · 2026-08-18

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
Construct context management for an artificial intelligence agent using the OpenViking database. It structures the information via the viking:// protocol by separating the information into L0 summary, L1 overview and L2 detail layers. By placing the agent's memory, resources, and capabilities in this virtual file system, it allows it to navigate directories during interrogation and create long-term memory by learning from past sessions.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/openviking/
