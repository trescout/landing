# Local Knowledge System for Claude Code

A local-first knowledge system for Claude Code and compatible Agent Skills servers. It converts source materials into citation-backed, linked Obsidian pages.

- ★ 14,822
- Python
- GitHub Trending · 2026-08-25

## Updates

- **September 11, 2026:** Stars 14,727 → 14,822, latest release v2.2.0 (September 10, 2026).
- **September 8, 2026:** Stars 13,706 → 14,727, latest release v2.1.1 (August 25, 2026).
- **August 27, 2026:** Stars 12,404 → 13,706, latest release v2.1.1 (August 25, 2026).

## Installation

**Add the Claude Code marketplace**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Install the claude-obsidian plugin**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Create an init plan for a separate vault**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```

## Running it

**Verify plugin installation**

```
claude plugin list
```

**Start the wiki workflow**

```
/claude-obsidian:wiki
```

## What does this tool do?

Organizes research content with source and claims ledgers, linked pages, and knowledge maps. Parallel agents generate drafts, while an orchestrator applies approved changes as reversible transactions.

## Who it is for

Anyone who wants to build a local, citation-backed Obsidian knowledge base with Claude Code.

## What not to expect

Not for automatic transcript logging, cloud synchronization, a guarantee of factual correctness, or as a replacement for backups and source control.

## Highlights

- Local-first operation model and explicit network egress approach
- Citation-backed, linked pages with source and claims ledgers
- Apply approved changes via reversible transactions

## First-use flow

1. Clone the repository and prepare a Python 3.11 or newer environment
2. Create an init plan for a separate vault and review the JSON plan
3. Check the approved_plan_sha256 value and confirm the full operation
4. Open the vault in Obsidian and run Claude Code with the local plugin
5. Start the wiki flow and use the steps to add sources, query, and explicitly commit changes

## Safe start

The system is not a source of truth. Use backups and source control for data; review network egress and the applied plan.

## First task prompt

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Start a local Obsidian wiki workflow by associating sources with the source and claims ledgers.

## Related dictionary terms

- [Agent Skills](https://trescout.com/en/dictionary/agent-skills/)
- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [Agent](https://trescout.com/en/dictionary/agent/)

## Links

- [GitHub repository →](https://github.com/AgriciDaniel/claude-obsidian)
- [Installation guide →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [Official README →](https://github.com/AgriciDaniel/claude-obsidian)
- [Read in Turkish →](https://trescout.com/discover/claude-obsidian/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-25: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/claude-obsidian/
