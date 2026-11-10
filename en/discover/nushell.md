# Command line interface offering structured objects

Developed in Rust, nushell offers a new command line interface (shell) that processes data as structured objects. Having reached the minimum-viable-product level, this project is preferred for daily use, although it may exhibit instability in some commands.

- ★ 41,079
- Rust
- GitHub Trending · 2026-11-07

## Updates

- **November 10, 2026:** Stars 41,012 → 41,079, latest release 0.117.0 (November 10, 2026).
- **November 7, 2026:** Stars 41,011 → 41,012, latest release 0.116.1 (October 4, 2026).

## What you get

- Processes data as structured objects.
- Provides pipeline flow between commands.
- Loads file contents as structured data.

## Installation

**Setup**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Running it

**Listing Directories**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install and use the new command line interface named Nushell. After completing the installation, help me run the ls | where type == "dir" | table command.

Repository: https://github.com/nushell/nushell. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Shell](https://trescout.com/en/dictionary/shell/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Suitable for developers who want to manage data as structured objects in the command line.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/nushell/nushell)
- [Read in Turkish →](https://trescout.com/discover/nushell/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-11-07: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/nushell/
