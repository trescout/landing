# Query your code repository with artificial intelligence

Code-graph-rag combines knowledge graphs and fetch-assisted generation (RAG) to understand and query complex structures in large code repositories. It allows developers to analyze and edit code bases in different languages ​​with the help of artificial intelligence.

- ★ 5,303
- Python
- GitHub Trending · 2026-08-10

## Updates

- **October 31, 2026:** Stars 5,284 → 5,303, latest release v0.4.5 (October 30, 2026).
- **October 26, 2026:** Stars 5,279 → 5,284, latest release v0.3.13 (October 25, 2026).
- **October 24, 2026:** Stars 5,278 → 5,279, latest release v0.3.2 (October 24, 2026).
- **October 23, 2026:** Stars 5,264 → 5,278, latest release v0.2.19 (October 22, 2026).

## What you get

- See complex relationships by turning the codebase into a knowledge graph
- Get answers about code structure by asking questions in natural language
- Make precise changes to code with structured search and editing tools

## Installation

**Installation with package manager**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Alternative installation method**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```

## Running it

**Starting the database**

```
cgr daemon up
```

**Analyze and query the warehouse**

```
cgr start --repo-path /path/to/repo --update-graph
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Analyze my code repository using the Code-Graph-RAG tool. Answer my questions using relationships between functions, classes, and modules in your code base. Suggest changes or optimizations I should make to the code using the structural analysis capabilities provided by the tool.

Repository: https://github.com/vitali87/code-graph-rag. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Monorepo](https://trescout.com/en/dictionary/monorepo/)
- [RAG](https://trescout.com/en/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers who want to understand and query structural relationships in large and complex code repositories and make safe changes with the help of artificial intelligence.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/vitali87/code-graph-rag)
- [Read in Turkish →](https://trescout.com/discover/code-graph-rag/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-10: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/code-graph-rag/
