# Persistent data management in distributed systems

Developed by Deno, Celld offers a self-hosted durable objects infrastructure for distributed systems. This technology, written in Rust language, enables distributing state management among different nodes in a scalable manner.

- ★ 6,043
- Rust
- GitHub Trending · 2026-08-08

## Updates

- **October 22, 2026:** Stars 5,067 → 6,043, latest release v0.6.3 (October 21, 2026).
- **October 8, 2026:** Stars 4,937 → 5,067, latest release v0.6.2 (October 7, 2026).
- **October 2, 2026:** Stars 4,817 → 4,937, latest release v0.6.1 (October 1, 2026).
- **September 27, 2026:** Stars 4,630 → 4,817, latest release v0.6.0 (September 26, 2026).

## What you get

- Provides scalable state management in your own infrastructure.
- It stores each object as an independent SQLite database.
- It establishes inter-node coordination with S3 compatible storage.

## Installation

**Download the tool to your computer**

```
curl -fsSL https://celld.dev/install.sh | sh
```

## Running it

**Resource restricted node**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to build a distributed system using Celld. After creating an S3-compatible storage space, explain step by step how the nodes will use this space and how to distribute Wrangler packages. Summarize the technical details in simple language, especially about how nodes discover each other and ensure data consistency over S3.

Repository: https://github.com/denoland/celld. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [State Management](https://trescout.com/en/dictionary/state-management/)
- [Durable Objects](https://trescout.com/en/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for developers who work on distributed systems and want to establish scalable state management on their own servers.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/denoland/celld)
- [Read in Turkish →](https://trescout.com/discover/celld/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-08: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/celld/
