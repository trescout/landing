# Layered memory for AI agents

TencentDB Agent Memory offers a completely local long-term memory solution for artificial intelligence agents with a four-stage process. It performs data storage and recall operations without the need for external application programming interfaces (APIs).

- ★ 18,953
- TypeScript
- GitHub Trending · 2026-07-09

## Update
- 10 August 2026: Star 17,887 → 18,953, latest version v2.0.0 (3 August 2026).
- August 8, 2026: Star 16,699 → 17,887, latest version v2.0.0 (August 3, 2026).
- August 7, 2026: Star 15,363 → 16,699, latest version v2.0.0 (August 3, 2026).
- August 6, 2026: Star 12,420 → 15,363, latest version v2.0.0 (August 3, 2026).

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
Configure the long-term memory of my AI agent using TencentDB Agent Memory. Instead of a flat vector stack of data, use symbolic Mermaid graphs for short-term tasks and a layered memory pyramid L0-L3 for long-term experiences. Enable the agent to store past conversations, atomic facts, and user preferences in this hierarchical structure and recall them whenever needed with full traceability via node_id.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/tencentdb-agent-memory/
