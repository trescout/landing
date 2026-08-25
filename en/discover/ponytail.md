# Rule Set for AI Coding Agents

An MIT-licensed rule set and plugin system for AI coding agents. Its aim is to preserve validation, error handling, security, and accessibility while writing only the code required for a task.

- ★ 110,483
- JavaScript
- GitHub Trending · 2026-08-25

## What does this tool do?
The rule ladder is applied after reading the code affected by a change. The adjusted agentic benchmark reported, on 12 tasks in a real FastAPI and React repository with Haiku 4.5 versus a no-skill baseline, an average of 54% fewer lines of code, 22% fewer tokens, 20% lower cost, and 27% shorter time. These results are limited to specific test conditions.

## Who it is for
Those who want to add validation, security, and accessibility rules to coding workflows on Claude Code, Codex, Gemini CLI, and other supported agent hosts.

## What not to expect
Not for generalizing specific benchmark results to all projects or for applying critical production changes without human review.

## Highlights
- Task-focused rules aimed at reducing unnecessary code
- A review approach that preserves validation, error handling, security, and accessibility
- Plugins or instruction adapters for Claude Code, Codex, Gemini CLI, and other hosts

## First-use flow
- Install the Ponytail integration for your agent host
- Verify that the installation is active inside the host
- Choose the appropriate Ponytail level
- Run review or audit flows on changes

## Safe start

## First task prompt
Write only the code required by the task, then review changes for validation, error handling, security, and accessibility.

## Installation
**Add the Claude Code marketplace**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Install the Claude Code plugin**

```
/plugin install ponytail@ponytail
```


## Running it
**Select the Ponytail level**

```
/ponytail full
```

**Start diff review**

```
/ponytail-review
```


## Related dictionary terms

## Links
- GitHub repository →
- Official README →
- Agentic benchmark method →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ponytail/
