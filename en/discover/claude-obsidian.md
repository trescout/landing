# Local Knowledge System for Claude Code

A local-first knowledge system for Claude Code and compatible Agent Skills servers. It converts source materials into citation-backed, linked Obsidian pages.

- ★ 13,706
- Python
- GitHub Trending · 2026-08-25

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
- Clone the repository and prepare a Python 3.11 or newer environment
- Create an init plan for a separate vault and review the JSON plan
- Check the approved_plan_sha256 value and confirm the full operation
- Open the vault in Obsidian and run Claude Code with the local plugin
- Start the wiki flow and use the steps to add sources, query, and explicitly commit changes

## Safe start

## First task prompt
Start a local Obsidian wiki workflow by associating sources with the source and claims ledgers.

## Related dictionary terms

## Links
- GitHub repository →
- Installation guide →
- Official README →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/claude-obsidian/
