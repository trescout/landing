# Manageable workflows for your coding agents

Developed by Tencent, LoopForge is a self-hosted workflow tool used to manage the delivery processes of coding agents. It supports local coding assistant processes by orchestrating software such as CodeBuddy, Codex, and Claude Code with scripts and human approval mechanisms.

- ★ 986
- Go
- GitHub Trending · 2026-11-15

## Updates

- **November 15, 2026:** Stars 983 → 986, latest release v0.3.8 (November 12, 2026).

## What you get

- Runs AI coding tools securely in sandboxed workspaces.
- Ensures repeatable deliveries with standard processes and human approval steps.
- Assigns tasks to roles from the chat interface or executes step-by-step workflows.

## Installation

**Cloning the repository and starting the system**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Starting with an alternative image source**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Running it

**Setting up a coding assistant inside the project**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up the LoopForge system to manage coding agent delivery pipelines on my own server. First, clone the repository and start the system by running the command sequence `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh`. If you experience hanging during the download phase, pull the images from the alternative server using the command `MIRROR=ghcr.nju.edu.cn ./start.sh` to complete the startup. To set up the coding assistant within your target project, run the command `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude`.

Repository: https://github.com/Tencent/LoopForge. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [Clone](https://trescout.com/en/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for teams that want to manage AI-powered coding agents within their own infrastructure, with human approval and standard workflows.

## Links

- [GitHub repository →](https://github.com/Tencent/LoopForge)
- [Read in Turkish →](https://trescout.com/discover/loopforge/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-11-15: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/loopforge/
