# Bring expertise to AI coding agents

Developed for Claude Code and various coding agents, this library offers more than 330 skill packages and over 70 special commands in different fields from engineering to marketing. This Python-based toolset provides customizable scripts to standardize AI-based workflows and increase productivity.

- ★ 29,039
- Python
- GitHub Trending · 2026-07-05

## Updates

- **October 31, 2026:** Stars 29,039 → 29,039, latest release v2.14.5 (October 31, 2026).
- **October 31, 2026:** Stars 28,939 → 29,039, latest release v2.14.4 (October 30, 2026).
- **October 29, 2026:** Stars 28,795 → 28,939, latest release v2.14.3 (October 29, 2026).
- **October 27, 2026:** Stars 28,584 → 28,795, latest release v2.14.2 (October 26, 2026).

## What you get

- More than 350 ready-made skill packs
- Broad expertise from engineering to marketing
- Compatible with 13 different coding tools

## Installation

**Gemini CLI installation**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**OpenClaw installation**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

## Running it

**Convert capabilities for cursor**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 346
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

Activate the skill packages in this library for Claude Code or the coding agent you use. Standardize my workflow and increase my productivity using specialized scripts in fields like engineering, marketing, or C-level consulting. Integrate the specific capabilities I need (e.g. security auditing or product development) into my project.

Repository: https://github.com/alirezarezvani/claude-skills. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [CLI](https://trescout.com/en/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers and technical teams who want to use artificial intelligence-supported coding tools more efficiently and expertly in their professional workflows.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/alirezarezvani/claude-skills)
- [Read in Turkish →](https://trescout.com/discover/claude-skills/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-05: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/claude-skills/
