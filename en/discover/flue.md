# TypeScript framework for AI agents

Developed by the Astro team, Flue stands out as a TypeScript-based sandbox agent framework. This structure allows developers to create artificial intelligence agents in secure and isolated environments.

- ★ 7,625
- TypeScript
- GitHub Trending · 2026-06-06

## What you get
- Creating programmable and headless agents based on TypeScript.
- Fast and scalable working environment with virtual sandbox.
- Versatile deployment across Node.js, Cloudflare, and CI/CD processes.

## Installation
**Node.js Development Server**

```
flue dev --target node
```

**Compilation**

```
flue build --target node          # Node.js server (single bundled .mjs)
flue build --target cloudflare    # Cloudflare Workers + Durable Objects
```


## Running it
**Running the Hello World Workflow**

```
flue run hello --target node \
  --payload '{"text": "Hello world", "language": "French"}'
```


## If you don't write code
I want to develop an artificial intelligence agent using the Flue framework. How can I define a workflow using TypeScript in my project? Specifically, how can I configure the model with the createAgent function and interact with my agent with session.prompt? Using a simple 'hello-world' example, can you explain step by step how I can start an agent at runtime and get results?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/flue/
