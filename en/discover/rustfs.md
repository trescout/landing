# High-performance object storage system

RustFS was developed as an S3-compatible high-performance object storage system. It offers interoperability and data migration support with other S3-compatible platforms such as MinIO and Ceph.

- ★ 35,371
- Rust
- GitHub Trending · 2026-09-19

## Updates

- **October 26, 2026:** Stars 35,063 → 35,371, latest release 1.0.4 (October 25, 2026).
- **October 18, 2026:** Stars 35,038 → 35,063, latest release 1.0.3 (October 17, 2026).
- **October 17, 2026:** Stars 34,330 → 35,038, latest release 1.0.2 (October 16, 2026).
- **October 3, 2026:** Stars 33,264 → 34,330, latest release 1.0.1 (October 3, 2026).

## What you get

- Provides high speed and memory safety with the Rust language
- Works seamlessly with existing tools thanks to its S3-compatible structure
- Offers unrestricted commercial use with the Apache 2.0 license

## Installation

**Start with the installation script**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Run the latest version with Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```

## Running it

**Start the system using Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up a high-performance object storage environment using RustFS. How can I manage my data by leveraging the system's S3 compatibility, and what should I pay attention to when scaling on a distributed architecture? Provide me with a step-by-step guide on the installation and basic configuration settings of this Apache 2.0 licensed system.

Repository: https://github.com/rustfs/rustfs. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Object Storage System](https://trescout.com/en/dictionary/object-storage-system/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for system administrators and developers looking for a fast, secure, and S3-compatible storage solution for big data workloads, artificial intelligence projects, and data lakes.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/rustfs/rustfs)
- [Read in Turkish →](https://trescout.com/discover/rustfs/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-19: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/rustfs/
