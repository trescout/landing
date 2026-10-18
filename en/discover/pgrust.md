# PostgreSQL rewritten with Rust

The pgrust project, in which the PostgreSQL database management system was rewritten with the Rust programming language, successfully completes all regression tests. This work aims to modernize the database architecture with a language focused on memory safety.

- ★ 5,030
- Rust
- GitHub Trending · 2026-07-12

## Updates

- **September 16, 2026:** Stars 4,964 → 5,030, latest release v0.3 (September 15, 2026).
- **September 10, 2026:** Stars 3,957 → 4,964, latest release v0.2-release (July 30, 2026).
- **August 2, 2026:** Stars 2,171 → 3,957, latest release v0.2-release (July 30, 2026).

## What you get

- Disk compatibility with Postgres 18.3
- More than 46 thousand regression test successes
- Modern architecture focused on memory security

## Installation

**Quick trial with Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

What is the main purpose of the Pgrust project, how is disk compatibility with existing PostgreSQL ensured, and how is artificial intelligence-supported programming used in the development of the project? Tell us about the compatibility of the current version of Pgrust with Postgres 18.3 and its success in regression testing.

Repository: https://github.com/malisper/pgrust. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Memory](https://trescout.com/en/dictionary/memory/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for developers and database researchers who want to modernize the PostgreSQL architecture with the Rust language.
- **License:** AGPL-3.0

## Links

- [GitHub repository →](https://github.com/malisper/pgrust)
- [Read in Turkish →](https://trescout.com/discover/pgrust/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/pgrust/
