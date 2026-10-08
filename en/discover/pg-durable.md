# Robust process management on PostgreSQL

Developed by Microsoft, pg_durable is a library designed to manage durable execution processes on PostgreSQL. Written in Rust, the tool enables complex workflows to run within the database in a fault-tolerant and persistent manner.

- ★ 2,831
- Rust
- GitHub Trending · 2026-06-08

## Updates

- **October 7, 2026:** Stars 2,811 → 2,831, latest release v0.2.9 (October 7, 2026).
- **September 12, 2026:** Stars 2,800 → 2,811, latest release v0.2.8 (September 11, 2026).
- **September 2, 2026:** Stars 2,781 → 2,800, latest release v0.2.7 (September 1, 2026).
- **August 24, 2026:** Stars 2,716 → 2,781, latest release v0.2.6 (August 24, 2026).

## What you get

- It manages workflows within the database in a fault-tolerant and persistent manner.
- In case of crash or interruption, it continues operations from the last checkpoint.
- It runs directly on PostgreSQL without requiring additional infrastructure.

## Installation

**Activating the Plugin**

```
CREATE EXTENSION pg_durable;
```

## Running it

**Starting a Workflow**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a workflow using the pg_durable plugin on PostgreSQL. How should I configure the df.start() function to manage a fault-tolerant and persistent process within the database? How can I create a structure that processes data and can continue from where it left off in case of error, using the ~> and |=> operators that connect SQL steps? Please explain this process with examples using SQL commands.

## Related dictionary terms

- [Durable Execution](https://trescout.com/en/dictionary/durable-execution/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for backend developers, database administrators and data engineers who want to manage data processing processes directly on PostgreSQL in a fault-tolerant and persistent way.

## Links

- [GitHub repository →](https://github.com/microsoft/pg_durable)
- [Read in Turkish →](https://trescout.com/discover/pg-durable/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-08: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/pg-durable/
