# Bring expertise to AI coding agents

Developed for Claude Code and various coding agents, this library offers more than 330 skill packages and over 70 special commands in different fields from engineering to marketing. This Python-based toolset provides customizable scripts to standardize AI-based workflows and increase productivity.

- ★ 23,654
- Python
- GitHub Trending · 2026-07-05

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
Activate the skill packages in this library for Claude Code or the coding agent you use. Standardize my workflow and increase my productivity using specialized scripts in fields like engineering, marketing, or C-level consulting. Integrate the specific capabilities I need (e.g. security auditing or product development) into my project.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/claude-skills/
