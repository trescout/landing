# High-performance object storage system

RustFS was developed as an S3-compatible high-performance object storage system. It offers interoperability and data migration support with other S3-compatible platforms such as MinIO and Ceph.

- ★ 34,330
- Rust
- GitHub Trending · 2026-09-19

## Updates

- **October 3, 2026:** Stars 33,264 → 34,330, latest release 1.0.1 (October 3, 2026).
- **September 19, 2026:** Stars 33,264 → 33,264, latest release 1.0.0 (September 16, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up a high-performance object storage environment using RustFS. How can I manage my data by leveraging the system's S3 compatibility, and what should I pay attention to when scaling on a distributed architecture? Provide me with a step-by-step guide on the installation and basic configuration settings of this Apache 2.0 licensed system.

## Related dictionary terms

- [Object Storage System](https://trescout.com/en/dictionary/object-storage-system/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for system administrators and developers looking for a fast, secure, and S3-compatible storage solution for big data workloads, artificial intelligence projects, and data lakes.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/rustfs/rustfs)
- [Read in Turkish →](https://trescout.com/discover/rustfs/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-19: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/rustfs/
