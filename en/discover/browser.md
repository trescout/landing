# Fast and lightweight AI browser

Lightpanda is a headless browser written in Zig, specifically developed for AI and automation processes. It aims to accelerate web scraping and web automation tasks by consuming fewer resources compared to traditional browsers.

- ★ 36,899
- Zig
- GitHub Trending · 2026-09-08

## Updates

- **October 23, 2026:** Stars 36,546 → 36,899, latest release 1.0.2 (October 23, 2026).
- **October 15, 2026:** Stars 36,160 → 36,546, latest release 1.0.1 (October 15, 2026).
- **October 9, 2026:** Stars 35,884 → 36,160, latest release 1.0.0 (October 2, 2026).
- **October 3, 2026:** Stars 35,689 → 35,884, latest release nightly (July 16, 2024).

## What you get

- Provides up to 16x less memory consumption compared to traditional browsers.
- Accelerates web scraping processes by processing web pages up to 9x faster.
- Offers AI agent support running directly within the browser.

## Installation

**macOS installation with Homebrew**

```
brew install lightpanda-io/browser/lightpanda
```

**Container setup with Docker**

```
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
```

## Running it

**Get web page as text**

```
./lightpanda fetch --obey-robots --dump html --log-format pretty  --log-level info https://demo-browser.lightpanda.io/campfire-commerce/
```

**Starting the CDP server**

```
./lightpanda serve --obey-robots --log-format pretty  --log-level info --host 127.0.0.1 --port 9222
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

You are a web automation expert. I want you to extract data from the specified website as efficiently as possible using the Lightpanda headless browser. Optimize memory usage, comply with robots.txt rules, and present the obtained data in a structured format. Dynamically adjust the necessary waiting times (wait-selector or wait-ms) to reduce the margin of error while performing the operation.

Repository: https://github.com/lightpanda-io/browser. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Headless Browser](https://trescout.com/en/dictionary/headless-browser/)
- [Web Scraping](https://trescout.com/en/dictionary/web-scraping/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Suitable for developers and AI agent creators who want to save resources in fast data scraping and web automation processes.
- **License:** AGPL-3.0

## Links

- [GitHub repository →](https://github.com/lightpanda-io/browser)
- [Read in Turkish →](https://trescout.com/discover/browser/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-08: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/browser/
