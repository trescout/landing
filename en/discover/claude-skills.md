# Bring expertise to AI coding agents

Developed for Claude Code and various coding agents, this library offers more than 330 skill packages and over 70 special commands in different fields from engineering to marketing. This Python-based toolset provides customizable scripts to standardize AI-based workflows and increase productivity.

- ★ 26,514
- Python
- GitHub Trending · 2026-07-05

## Updates

- **September 27, 2026:** Stars 25,061 → 26,514, latest release v2.12.0 (August 25, 2026).
- **August 27, 2026:** Stars 24,867 → 25,061, latest release v2.12.0 (August 25, 2026).
- **August 24, 2026:** Stars 23,654 → 24,867, latest release v2.9.0 (May 28, 2026).
- **August 2, 2026:** Stars 20,244 → 23,654, latest release v2.9.0 (May 28, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Activate the skill packages in this library for Claude Code or the coding agent you use. Standardize my workflow and increase my productivity using specialized scripts in fields like engineering, marketing, or C-level consulting. Integrate the specific capabilities I need (e.g. security auditing or product development) into my project.

## Related dictionary terms

- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [CLI](https://trescout.com/en/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers and technical teams who want to use artificial intelligence-supported coding tools more efficiently and expertly in their professional workflows.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/alirezarezvani/claude-skills)
- [Read in Turkish →](https://trescout.com/discover/claude-skills/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-05: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/claude-skills/
