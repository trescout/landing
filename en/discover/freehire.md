# Open-source job search engine

Developed in Go, freehire is an open-source (source code accessible to everyone for development) search engine designed for job seekers. It offers a platform that allows users to browse and find job listings.

- ★ 2,661
- Go
- GitHub Trending · 2026-10-22

## Updates

- **October 22, 2026:** Stars 2,643 → 2,661, latest release extension-v0.1.10 (October 21, 2026).

## What you get

- You gain direct and up-to-date access to tech job postings collected directly from companies' career pages without intermediaries.
- By deduplicating repeated postings across different career sites, you can review them in a clean and filterable list.
- You manage your job search process with resume match review and an AI-powered application tracking dashboard.

## Installation

**Setting up the entire system in a container environment and**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Running it

**With a different port if the default port is busy**

```
HIRE_HOST_PORT=8090 make up
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to run the open-source job search platform Freehire on my own system. To start all services and verify the API status using the container management software Docker and the automation tool Make, run the following commands in order: make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Repository: https://github.com/strelov1/freehire. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Localhost](https://trescout.com/en/dictionary/localhost/)
- [API](https://trescout.com/en/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for those who want to track software and technology job postings directly on companies' own career pages without intermediaries, or run their own independent job search engine.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/strelov1/freehire)
- [Read in Turkish →](https://trescout.com/discover/freehire/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-22: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/freehire/
