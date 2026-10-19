# Computer control for artificial intelligence agents

CUA provides an open source infrastructure for computer-capable artificial intelligence agents. It brings together sandbox, software development kit (SDK) and benchmark tools under one roof for the purpose of training and evaluating agents that can control desktop operating systems.

- ★ 30,189
- HTML
- GitHub Trending · 2026-06-16

## Updates

- **October 19, 2026:** Stars 30,064 → 30,189, latest release agent-v0.9.1 (October 19, 2026).
- **October 18, 2026:** Stars 29,921 → 30,064, latest release cua-spaces-v0.9.4 (October 18, 2026).
- **October 16, 2026:** Stars 29,802 → 29,921, latest release cua-spaces-v0.9.3 (October 16, 2026).
- **October 15, 2026:** Stars 29,690 → 29,802, latest release cua-spaces-v0.9.2 (October 15, 2026).

## What you get

- Control desktop apps in the background
- Isolated sandboxes for different operating systems
- Benchmarking tools to measure agent performance

## Installation

**Driver installation (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Sandbox SDK installation**

```
pip install cua
```

## Running it

**macOS virtual machine startup**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to develop a computer usage agent using the CUA infrastructure. Help me set up the basic Python structure that will allow my agent to interact with desktop applications in the background, make mouse clicks, and send keyboard input. Create a sample code sketch that runs commands and takes screenshots in a Linux environment using the CUA Sandbox SDK.

Repository: https://github.com/trycua/cua. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Benchmark](https://trescout.com/en/dictionary/benchmark/)
- [Sandbox](https://trescout.com/en/dictionary/sandbox/)
- [SDK](https://trescout.com/en/dictionary/sdk/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for software developers and researchers who develop artificial intelligence agents that perform autonomous tasks on the computer.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/trycua/cua)
- [Read in Turkish →](https://trescout.com/discover/cua/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-16: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/cua/
