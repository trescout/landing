# Inference server for AI agents

Developed by Superlinked, SIE is an open-source inference server and production cluster used to run the models required by AI agents. This Python-based structure aims to manage complex model deployments and provide a scalable infrastructure.

- ★ 3,390
- Python
- GitHub Trending · 2026-09-03

## Updates

- **October 14, 2026:** Stars 3,372 → 3,390, latest release v0.10.1 (October 13, 2026).
- **October 10, 2026:** Stars 3,350 → 3,372, latest release v0.10.0 (October 9, 2026).
- **September 30, 2026:** Stars 3,325 → 3,350, latest release v0.9.0 (September 30, 2026).
- **September 27, 2026:** Stars 3,198 → 3,325, latest release v0.8.3 (September 26, 2026).

## What you get

- Manages open-source models through a single cluster
- Provides easy integration thanks to its OpenAI-compatible interface
- Supports tasks such as search, data extraction, and text generation

## Installation

**SDK installation**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```

## Running it

**First deployment attempt**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run a model for an AI agent via the SIE server. How can I manage the tasks my agent needs, such as search, data extraction, and text generation, through a single API? How can I configure the embedding creation and text generation processes using the OpenAI-compatible endpoints provided by SIE?

Repository: https://github.com/superlinked/sie. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Embedding](https://trescout.com/en/dictionary/embedding/)
- [Inference Server](https://trescout.com/en/dictionary/inference-server/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [SDK](https://trescout.com/en/dictionary/sdk/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to run numerous AI models in a scalable way on their own infrastructure.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/superlinked/sie)
- [Read in Turkish →](https://trescout.com/discover/sie/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-03: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/sie/
