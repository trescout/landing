# Server and service status monitoring tool

Uptime Kuma is a self-hosted monitoring tool with a graphical interface. Allowing you to track the uptime of websites and services, this JavaScript-based application offers a user-friendly experience.

- ★ 93,936
- JavaScript
- GitHub Trending · 2026-11-14

## Updates

- **November 14, 2026:** Stars 93,934 → 93,936, latest release 2.5.11 (November 12, 2026).

## What you get

- Monitor websites and services in real-time
- Get multi-language and notification support
- Create status pages with a visual interface

## Installation

**Installation with Docker Compose**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Installation with Docker Command**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Running it

**Running with Docker**

```
docker compose up -d
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install the Uptime Kuma monitoring tool. To use Docker Compose, I need to run these commands: mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. Can you help me complete these steps?

Repository: https://github.com/louislam/uptime-kuma. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Suitable for anyone who wants to monitor whether websites and servers are running on their own server.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/louislam/uptime-kuma)
- [Read in Turkish →](https://trescout.com/discover/uptime-kuma/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-11-14: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/uptime-kuma/
