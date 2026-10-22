# Lightweight database client

Developed in Rust, dbx offers a lightweight database client of 25 MB that supports over 100 database types. Along with a desktop application, command-line interface (CLI), and Docker support, it includes features such as a built-in AI assistant and Model Context Protocol (MCP).

- ★ 27,438
- Rust
- GitHub Trending · 2026-09-29

## Updates

- **October 21, 2026:** Stars 27,338 → 27,438, latest release v0.6.50 (October 20, 2026).
- **October 20, 2026:** Stars 27,216 → 27,338, latest release v0.6.49 (October 19, 2026).
- **October 19, 2026:** Stars 27,082 → 27,216, latest release v0.6.48 (October 19, 2026).
- **October 18, 2026:** Stars 27,027 → 27,082, latest release v0.6.47 (October 17, 2026).

## What you get

- Supports over a hundred database types.
- Works with desktop, Docker, and command line.
- Includes an AI assistant and Model Context Protocol.

## Installation

**Desktop Application Installation**

```
brew install --cask dbx
```

**Command Line Tool Installation**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```

## Running it

**Running with Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Follow the necessary steps to install and run the dbx application. For the desktop app, use the brew install --cask dbx command, and for the command line interface, use the npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json commands. If you want to run it with Docker, run the # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
-v dbx-data:/app/data \
t8y2/dbx:latest command.

Repository: https://github.com/t8y2/dbx. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Database Client](https://trescout.com/en/dictionary/database-client/)
- [Local](https://trescout.com/en/dictionary/local/)
- [Database](https://trescout.com/en/dictionary/database/)
- [MCP](https://trescout.com/en/dictionary/mcp/)
- [Agent](https://trescout.com/en/dictionary/agent/)
- [CLI](https://trescout.com/en/dictionary/cli/)

- **Who it is for:** Designed for developers who want to manage different database types with a lightweight interface and AI support.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/t8y2/dbx)
- [Read in Turkish →](https://trescout.com/discover/dbx/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-29: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/dbx/
