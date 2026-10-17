# Secure AI capabilities

Developed by NVIDIA, SkillSpector is a scanning tool that detects vulnerabilities and malicious patterns in the skill packages of artificial intelligence agents. This Python-based software aims to analyze security risks encountered during the development process of agent-based systems.

- ★ 20,396
- Python
- GitHub Trending · 2026-06-12

## Updates

- **October 17, 2026:** Stars 19,418 → 20,396, latest release v2.13.0 (October 16, 2026).
- **October 5, 2026:** Stars 18,381 → 19,418, latest release v2.12.0 (September 23, 2026).
- **September 27, 2026:** Stars 16,828 → 18,381, latest release v2.12.0 (September 23, 2026).
- **September 10, 2026:** Stars 16,595 → 16,828, latest release v2.11.2 (September 9, 2026).

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
