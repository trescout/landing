# Private Search Engine for Personal Pages and Files

An AGPLv3-licensed private search engine for pages you visit and files you store. It provides full-text indexing, advanced query filters, and optional semantic search.

- ★ 3,574
- Go
- GitHub Trending · 2026-08-25

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
- Download the binary for your platform and make it executable on Linux or macOS
- Start the Hister server in local listen mode
- Open the local web interface
- Install the Chrome or Firefox extension and choose pages to index

## Safe start

## First task prompt
Open the local interface, index selected pages with the browser extension, and verify searches using query filters.

## Related dictionary terms

## Links
- GitHub repository →
- Quickstart →
- Privacy and usage README →
- Usage workflow →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/hister/
