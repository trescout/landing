# Autonomous AI kit for Antigravity

Ag-kit is a development library that provides the necessary tools and structures to create autonomous artificial intelligence agents (AI agents) in TypeScript-based projects. It allows developers to quickly design agent systems that can manage complex workflows.

- ★ 8,159
- TypeScript
- GitHub Trending · 2026-07-28

## What you get
- 20 different expert AI roles
- Secure command execution control
- Persistent memory and workflow management

## Installation
**Installation in the project**

```
npx @vudovn/ag-kit init
```

**Global installation**

```
npm install -g @vudovn/ag-kit
ag-kit init
```


## Running it
**Workspace verification**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Testing the security hook**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```


## If you don't write code
In this project, I set up the Antigravity workspace and activated the AG Kit tools. I want to manage my tasks using the rules, expert agent roles and workflows defined in the .agents/ folder in the project directory. Make sure the security hook is active and plan complex workflows with the /coordinate or /orchestrate commands.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ag-kit/
