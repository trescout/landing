# Source control for AI agents

Atlas is a source control system for AI agents used in software development processes. It allows for tracking and querying changes made by multiple coding agents from a single central point.

- ★ 3,058
- Rust
- GitHub Trending · 2026-09-03

## What you get
- Tracks changes made by different coding agents from a single center.
- Enables you to pick up where you left off during task transitions with a shared memory between agents.
- Maps every code change to the rationale and commands of the agent that performed it.

## Installation
**Installing necessary dependencies**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Compiling the application from source code**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```


## If you don't write code
You are a software development assistant. Record all code changes you make using Atlas, along with the decisions you take and the tools you use, together with the session history. If you need to switch between different agents like Claude Code or Codex while working, read the plans and architectural notes from the previous session via the shared memory. Maintain context by referencing files, folders, or past sessions in the codebase using the '@' symbol, and document the reason for every change you make along with the rationale of the relevant session.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/atlas/
