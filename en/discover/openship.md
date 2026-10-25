# App deployment on your own server

OpenShip offers an application distribution platform that users can host on their own servers. This tool, developed with the TypeScript language, facilitates self-hosting processes as an alternative to cloud-based infrastructure services.

- ★ 14,928
- TypeScript
- GitHub Trending · 2026-07-21

## Updates

- **October 25, 2026:** Stars 14,787 → 14,928, latest release v0.9.5 (October 24, 2026).
- **October 17, 2026:** Stars 14,772 → 14,787, latest release v0.9.3 (October 17, 2026).
- **October 16, 2026:** Stars 14,714 → 14,772, latest release v0.9.2 (October 16, 2026).
- **October 13, 2026:** Stars 14,701 → 14,714, latest release v0.9.1 (October 13, 2026).

## What you get

- Automated CI/CD processes
- Quick transition from code to container
- Database and SSL management

## Installation

**Quick installation via CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Installation with Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Running it

**Start project deployment**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to publish a project using Openship. While in the project directory, is it enough to connect the directory to the project with the openship init command and then run the openship deploy command? Can you explain step by step how the database and SSL configuration are automatically managed in this process?

Repository: https://github.com/oblien/openship. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Deployment Platform](https://trescout.com/en/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/en/dictionary/ci-cd/)
- [CLI](https://trescout.com/en/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for software developers who want to host applications on their own servers and want to deploy quickly without dealing with complex configuration files.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/oblien/openship)
- [Read in Turkish →](https://trescout.com/discover/openship/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-21: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openship/
