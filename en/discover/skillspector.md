# Secure AI capabilities

Developed by NVIDIA, SkillSpector is a scanning tool that detects vulnerabilities and malicious patterns in the skill packages of artificial intelligence agents. This Python-based software aims to analyze security risks encountered during the development process of agent-based systems.

- ★ 23,142
- Python
- GitHub Trending · 2026-06-12

## Updates

- **October 29, 2026:** Stars 22,512 → 23,142, latest release v2.13.2 (October 28, 2026).
- **October 27, 2026:** Stars 21,040 → 22,512, latest release v2.13.1 (October 23, 2026).
- **October 23, 2026:** Stars 20,396 → 21,040, latest release v2.13.1 (October 23, 2026).
- **October 17, 2026:** Stars 19,418 → 20,396, latest release v2.13.0 (October 16, 2026).

## What you get

- AI detects vulnerabilities and malicious patterns in agent capabilities.
- It offers two-stage security scanning with static analysis and optional AI assessment.
- It allows verifying the security of agents with risk scoring and detailed reporting.

## Installation

**Cloning the repository and creating a virtual environment**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Complete the setup**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```

## Running it

**Scan local directory**

```
skillspector scan ./my-skill/
```

**Scan the Git repository**

```
skillspector scan https://github.com/user/my-skill
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to security screen an AI agent skill using the SkillSpector tool. How do I use the 'skillspector scan ./my-skill/' command to scan for talent in a local directory and what parameters should I add to the command to save the scan results in 'report.json' in JSON format?

Repository: https://github.com/NVIDIA/SkillSpector. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers who develop AI agents and want to analyze the security risks of the capability packages they use.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/NVIDIA/SkillSpector)
- [Read in Turkish →](https://trescout.com/discover/skillspector/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/skillspector/
