# Manage Git worktrees

Worktrunk is a command-line interface (CLI) written in Rust that simplifies Git worktree management. Developed specifically to support parallel AI agent workflows, this tool accelerates working on multiple tasks simultaneously.

- ★ 7,964
- Rust
- GitHub Trending · 2026-09-13

## What you get
- Easily creates workspaces to execute multiple tasks simultaneously
- Accelerates local workflows with automatic hooks
- Supports parallel operation of AI agents

## Installation
**Installation with Homebrew**

```
brew install worktrunk && wt config shell install
```

**Installation via Cargo**

```
cargo install worktrunk && wt config shell install
```


## Running it
**Switching between worktrees**

```
wt switch feat
```

**Creating and initializing a new worktree**

```
wt switch -c -x claude feat
```


## If you don't write code
I want to create a new worktree in my existing Git project using Worktrunk and start a parallel task in this space. How should I use wt commands to manage worktrees as easily as branches, and how can I leverage hooks to automate my workflow?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/worktrunk/
