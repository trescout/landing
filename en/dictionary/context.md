# What is Context? AI vs Systems

*Dictionary · AI · Last updated: September 19, 2026*

> English: Context · Etymology: Latin contexere (to weave together)

Context is a foundational concept across computer science, defining either the active prompt memory and token window of large language models, or the operational CPU state, registers, and memory maps in operating systems.

*If you walk up to a friend and simply state 'Yes, they agreed', they will have no idea what you mean; but if you preface it with 'Regarding yesterday's discussion about the movie', you provide the necessary context for comprehension.*

## 1. Context in Artificial Intelligence and LLMs

Large language models do not possess biological memory or ongoing conscious state between API calls. To understand a question, interpret nuance, or continue a conversation, they rely entirely on the **context window**: the active sequence of input tokens (prompts, conversation history, and RAG document chunks) fed into the model during inference. The size of this context determines how much information an AI can reason about simultaneously.

## 2. Context in Operating Systems and Concurrent Programming

In operating systems and systems programming, context represents the exact execution state of a thread or process at any given instant: program counter (PC), CPU registers, stack pointers, and memory page tables. When a multitasking operating system pauses one process to execute another, it performs a **context switch**, saving the old state and loading the new state into CPU hardware.

## Comparative Perspectives Across Disciplines

How context operates across disparate technology layers:

- **Artificial Intelligence:** The token window and KV cache providing dynamic in-memory knowledge during inference.
- **Operating Systems:** Kernel data structures (Process Control Blocks / PCBs) tracking register state during scheduling.
- **Web Frameworks:** Context objects (such as in React, Go, or Express) passing request scopes, cancellation signals, and authorization credentials down the call tree.

## Frequently Asked Questions

**What causes the 'lost in the middle' effect in LLM context windows?**

Language models tend to attend more strongly to the beginning and end of their context window, sometimes failing to retrieve specific facts buried in the middle of massive prompts.

**Why are CPU context switches computationally expensive?**

Because saving and restoring hardware registers incurs CPU overhead, invalidates translation lookaside buffers (TLB), and pollutes processor CPU caches.

**How does the Context API work in React?**

It provides a way to pass data deeply through the component tree without manually threading props at every intermediate level.

**How is the context window represented in Transformer models?**

Through attention matrices that compute pairwise relevance between all tokens within the active context span.

## Related terms

- [Context Window](https://trescout.com/en/dictionary/context-window/)
- [Working Memory](https://trescout.com/en/dictionary/working-memory/)

## Related tools

- [Goose](https://trescout.com/en/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/en/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/en/discover/openclaude/)
- [Code Review Graph](https://trescout.com/en/discover/code-review-graph/)
- [Fastmcp](https://trescout.com/en/discover/fastmcp/)
- [Context Mode](https://trescout.com/en/discover/context-mode/)
- [Unity MCP](https://trescout.com/en/discover/unity-mcp/)
- [DesktopCommanderMCP](https://trescout.com/en/discover/desktopcommandermcp/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/context/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/context/
