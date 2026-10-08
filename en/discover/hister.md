# Private Search Engine for Personal Pages and Files

An AGPLv3-licensed private search engine for pages you visit and files you store. It provides full-text indexing, advanced query filters, and optional semantic search.

- ★ 5,740
- Go
- GitHub Trending · 2026-08-25

## Updates

- **September 27, 2026:** Stars 4,602 → 5,740, latest release v0.20.0 (September 24, 2026).
- **September 18, 2026:** Stars 3,574 → 4,602, latest release v0.19.0 (September 3, 2026).
- **September 4, 2026:** Stars 3,100 → 3,574, latest release v0.19.0 (September 3, 2026).
- **August 27, 2026:** Stars 2,620 → 3,100, latest release v0.18.0 (August 23, 2026).

## Installation

**Make the binary executable**

```
chmod +x hister
```

## Running it

**Start the Hister server**

```
./hister listen
```

**Access the local interface**

```
http://127.0.0.1:4433
```

## What does this tool do?

Hister can run locally or on infrastructure you control; it does not require a mandatory cloud service or telemetry. It indexes pages via Chrome and Firefox extensions and offers website crawling and browser history import options. If semantic search is enabled, document text is sent to the selected embeddings endpoint.

## Who it is for

Those who want to query web pages and personal files on a search infrastructure they control.

## What not to expect

Not for use cases that require mandatory cloud service or telemetry, or for browser-indexing flows where sending content to a configured Hister server is not permitted.

## Highlights

- Runs on local or controlled infrastructure without telemetry or mandatory cloud services
- Querying with full-text, field filters, phrases, wildcards, negation, and boosting
- Optional semantic search with web, terminal, TUI, CLI, and MCP clients

## First-use flow

1. Download the binary for your platform and make it executable on Linux or macOS
2. Start the Hister server in local listen mode
3. Open the local web interface
4. Install the Chrome or Firefox extension and choose pages to index

## Safe start

The browser extension sends indexed page content to the configured Hister server (favicon downloading is excluded). Optional semantic search sends document text to the selected embeddings endpoint.

## First task prompt

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Open the local interface, index selected pages with the browser extension, and verify searches using query filters.

## Related dictionary terms

- [TUI](https://trescout.com/en/dictionary/tui/)
- [Binary](https://trescout.com/en/dictionary/binary/)
- [MCP](https://trescout.com/en/dictionary/mcp/)
- [Terminal](https://trescout.com/en/dictionary/terminal/)
- [CLI](https://trescout.com/en/dictionary/cli/)

## Links

- [GitHub repository →](https://github.com/asciimoo/hister)
- [Quickstart →](https://hister.org/docs/quickstart)
- [Privacy and usage README →](https://github.com/asciimoo/hister)
- [Usage workflow →](https://hister.org/posts/how-i-use-hister)
- [Read in Turkish →](https://trescout.com/discover/hister/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-25: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/hister/
