# Persistent data management in distributed systems

Developed by Deno, Celld offers a self-hosted durable objects infrastructure for distributed systems. This technology, written in Rust language, enables distributing state management among different nodes in a scalable manner.

- ★ 4,937
- Rust
- GitHub Trending · 2026-08-08

## Updates

- **October 2, 2026:** Stars 4,817 → 4,937, latest release v0.6.1 (October 1, 2026).
- **September 27, 2026:** Stars 4,630 → 4,817, latest release v0.6.0 (September 26, 2026).
- **September 15, 2026:** Stars 4,521 → 4,630, latest release v0.5.0 (September 15, 2026).
- **September 6, 2026:** Stars 4,405 → 4,521, latest release v0.4.1 (September 5, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to build a distributed system using Celld. After creating an S3-compatible storage space, explain step by step how the nodes will use this space and how to distribute Wrangler packages. Summarize the technical details in simple language, especially about how nodes discover each other and ensure data consistency over S3.

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

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-08: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/celld/
