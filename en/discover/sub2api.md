# Manage AI subscriptions from a single center

Sub2API is an open source intermediary service that provides single-point access and cost sharing to Claude, OpenAI, Gemini and Grok subscriptions.

- ★ 45,041
- Go
- GitHub Trending · 2026-08-23

## Updates

- **October 29, 2026:** Stars 44,674 → 45,041, latest release v0.2.19 (October 28, 2026).
- **October 23, 2026:** Stars 44,184 → 44,674, latest release v0.2.18 (October 23, 2026).
- **October 16, 2026:** Stars 43,885 → 44,184, latest release v0.2.17 (October 16, 2026).
- **October 13, 2026:** Stars 43,558 → 43,885, latest release v0.2.16 (October 13, 2026).

## What you get

- Combines different AI subscriptions in one interface
- Helps you allocate subscription costs efficiently
- Offers the opportunity to work integrated with existing tools

## Installation

**automatic installation**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Installation with Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```

## Running it

**Start the service**

```
docker compose up -d
```

**View administrator password**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

How can I configure different AI services such as Claude, OpenAI, Gemini and Grok through a single API gateway using the Sub2API platform? Explain the basic steps I need to follow to efficiently allocate my subscription quotas and integrate them with my existing software tools. Also, summarize the legal and technical issues I need to pay attention to in order to comply with the terms of service of providers such as Anthropic when using this platform.

Repository: https://github.com/Wei-Shaw/sub2api. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For developers who want to manage multiple AI subscriptions on a single platform and optimize their costs.
- **License:** LGPL-3.0

## Links

- [GitHub repository →](https://github.com/Wei-Shaw/sub2api)
- [Read in Turkish →](https://trescout.com/discover/sub2api/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-23: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/sub2api/
