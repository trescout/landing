# Ready-made design rules for coding assistants

elayadesign/ai-design-skills offers a collection of design skills consisting of markdown rule files readable by AI coding tools (Claude Code, Cursor, Codex, Windsurf). This project provides a guiding resource for AI-powered tools to standardize design processes.

- ★ 9,826
- GitHub Trending · 2026-10-28

## What you get

- Enables AI tools to generate consistent landing pages and visual systems from scratch
- Gathers design standards such as typography, color, spacing, and animation into a single file
- Enables coding assistants to write more consistent interfaces using project-specific rules

## Installation

**Adding to the Claude Code rules folder**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Install for the AI code editor Cursor**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to teach design rules to my AI coding tool. To download the necessary rules file for the Cursor code editor, please run the following commands in order: `mkdir -p .cursor/rules` and then `curl -o .cursor/rules/\<skill-name>.md \
https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. Don't forget to replace the `\<skill-name>` part here with `landing-page-design`, which is the rule we want to download.

Repository: https://github.com/elayadesign/ai-design-skills. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Markdown](https://trescout.com/en/dictionary/markdown/)
- [Skill](https://trescout.com/en/dictionary/skill/)
- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for product owners and developers who want to develop aesthetic and consistent web interfaces using AI-powered code editors.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/elayadesign/ai-design-skills)
- [Read in Turkish →](https://trescout.com/discover/ai-design-skills/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-28: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ai-design-skills/
