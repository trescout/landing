# Manage your travel plans together

TREK is a self-hosted travel planning application that offers features like real-time collaboration, interactive maps, and budget management. With progressive web application (PWA) support and single sign-on (SSO) integration, it allows users to organize their travel processes digitally.

- ★ 7,040
- GitHub Trending · 2026-06-26

## What you get

- Create daily travel routes and plans with drag and drop
- Tracking group expenses and dividing them per person
- Automatic travel and budget management with artificial intelligence integration

## Installation

**Quick installation with Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

You are a travel assistant. Using the MCP (Model Context Protocol) tools on TREK, create a 3-day Paris travel plan for me, adjust my budget based on daily spending limits, and create a packing list for what I need to take with me.

Repository: https://github.com/mauriceboe/TREK. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [PWA](https://trescout.com/en/dictionary/pwa/)
- [SSO](https://trescout.com/en/dictionary/sso/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [Model Context Protocol](https://trescout.com/en/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/en/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/en/dictionary/context/)

- **Who it is for:** It is for travelers who want to organize their trips digitally, track their expenses and have full control over their data.
- **License:** AGPL-3.0

## Links

- [GitHub repository →](https://github.com/mauriceboe/TREK)
- [Read in Turkish →](https://trescout.com/discover/trek/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-26: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/trek/
