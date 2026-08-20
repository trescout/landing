# Persistent data management in distributed systems

Developed by Deno, Celld offers a self-hosted durable objects infrastructure for distributed systems. This technology, written in Rust language, enables distributing state management among different nodes in a scalable manner.

- ★ 4,010
- Rust
- GitHub Trending · 2026-08-08

## What you get
- Provides scalable state management in your own infrastructure.
- It stores each object as an independent SQLite database.
- It establishes inter-node coordination with S3 compatible storage.

## Installation
**Download the tool to your computer**

```
curl -fsSL https://celld.dev/install.sh | sh
```


## Running it
**Resource restricted node**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```


## If you don't write code
I want to build a distributed system using Celld. After creating an S3-compatible storage space, explain step by step how the nodes will use this space and how to distribute Wrangler packages. Summarize the technical details in simple language, especially about how nodes discover each other and ensure data consistency over S3.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/celld/
