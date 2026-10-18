# Layered memory for AI agents

TencentDB Agent Memory offers a completely local long-term memory solution for artificial intelligence agents with a four-stage process. It performs data storage and recall operations without the need for external application programming interfaces (APIs).

- ★ 28,604
- TypeScript
- GitHub Trending · 2026-07-09

## Updates

- **October 13, 2026:** Stars 27,855 → 28,604, latest release v2.0.3-beta.1 (October 13, 2026).
- **October 9, 2026:** Stars 27,396 → 27,855, latest release v2.0.2 (October 9, 2026).
- **September 28, 2026:** Stars 26,048 → 27,396, latest release v2.0.1 (August 25, 2026).
- **September 7, 2026:** Stars 24,804 → 26,048, latest release v2.0.1 (August 25, 2026).

## What you get

- Reduces token usage by up to 61%
- Increases success rate in complex tasks
- Stores data in a symbolic and layered structure

## Installation

**Package installation**

```
mkdir -p ~/.memory-tencentdb
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest --omit=dev
cp -r node_modules/@tencentdb-agent-memory/memory-tencentdb \
      ~/.memory-tencentdb/tdai-memory-openclaw-plugin
rm -rf "$TEMP_DIR"
```

**Installing dependencies**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npm install --omit=dev
npm install tsx
```

## Running it

**Starting the server**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
  npx tsx src/gateway/server.ts
```

**Verify the connection**

```
curl http://127.0.0.1:8420/health
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Configure the long-term memory of my AI agent using TencentDB Agent Memory. Instead of a flat vector stack of data, use symbolic Mermaid graphs for short-term tasks and a layered memory pyramid L0-L3 for long-term experiences. Enable the agent to store past conversations, atomic facts, and user preferences in this hierarchical structure and recall them whenever needed with full traceability via node_id.

Repository: https://github.com/TencentCloud/TencentDB-Agent-Memory. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Long-term Memory](https://trescout.com/en/dictionary/long-term-memory/)
- [Mermaid](https://trescout.com/en/dictionary/mermaid/)
- [Memory](https://trescout.com/en/dictionary/memory/)
- [Token](https://trescout.com/en/dictionary/token/)
- [Agent](https://trescout.com/en/dictionary/agent/)
- [API](https://trescout.com/en/dictionary/api/)

- **Who it is for:** It is for developers who do not want their AI agents to forget the context and aim to get more consistent results by reducing token costs.

## Links

- [GitHub repository →](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [Read in Turkish →](https://trescout.com/discover/tencentdb-agent-memory/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-09: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/tencentdb-agent-memory/
