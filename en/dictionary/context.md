# What is Context?

*Artificial Intelligence · Last updated: September 19, 2026*

Context is the whole of the environmental and semantic information that a data, command or process needs to be interpreted and executed correctly.

## 1. Artificial Intelligence and Context in LLMs

Large language models (LLM) do not have permanent memory or experience memory like humans; In each query, it "remembers" only the data currently included in the context window.

### Transformer and Self-Attention Mechanism

In the Transformer architecture, context is established by weighting the relationship of a word at the beginning of the sentence with a word at the end (Query/Query, Key/Key, Value/Value vectors). The model deciphers whether the word “bank” means a financial institution or a riverbank simply by looking at the context of the sentence in which it occurs.

### Context Window and Its Boundaries

- Token Capacity: The maximum length that a model can read and respond to at one time (e.g. 8K, 32K, 128K or 1M+ tokens).
- Memory Cost (KV Cache): As the context gets longer, the memory requirement of the attention matrix increases quadratically. FlashAttention and KV-Cache optimizations are used to alleviate this load.
- Lost in the Middle Problem: Research shows that LLMs focus better on information at the beginning and end of long texts than on information in the middle.
- RAG (Retrieval-Augmented Generation): Instead of fitting millions of pages of corporate data into the context window, only the paragraphs most relevant to the query are filtered by the search engine or vector database and transferred to the model as context.

***Analogy:** When you're chatting with a friend, if you just say, "Yes, that's what he said," he won't understand you; However, if you say, "I'm talking about that movie we talked about yesterday," you will provide the necessary context.*

## 2. Context in Operating Systems and Programming

In system programming, "context" refers to all variable and register values ​​that fully reflect the current state of a program during its execution.

### Context Switching

A multitasking operating system shares the CPU core among different processes and threads:

1. The CPU registers (RAX, RSP, RIP, etc.), stack pointer and memory pages of the running process are saved in the Process Control Block (PCB).
2. The registers of the next operation are loaded back into the CPU.
3. Cost: Context switching is very costly at the hardware level; because it causes CPU L1/L2 caches and TLB (Translation Lookaside Buffer) address maps to become invalid (cache pollution).

### Context Management in Languages

- Go (context.Context): Used to carry cancellation signals, deadlines, and metadata within the scope of the request between network requests or asynchronous goroutines.
- Python (with blocks): Context Managers secure resource sanitization operations such as reading files or opening/closing database connections.
- React (Context API): It is a method of transmitting global state in depth without passing props to intermediate components one by one in the component tree (without prop drilling).

## Comparison: Concept of Context in Different Disciplines

| Area | The Value Represented by Context | Typical Components | Problems Encountered |
|---|---|---|---|
| Artificial Intelligence (LLM) | Login prompt + History chat + Documents | Tokens, Attention Masks, KV Cache | Token limit, Hallucination, Memory consumption |
| Operating Systems | Hardware current state of a process | Registers, Program Counter, Page Tables | CPU latency, Cache misses, TLB flush |
| Software Development | Request lifecycle and environment data | Timeout signal, Authorization token | Memory leak, Asynchronous calls not being canceled |

## Questions and answers

**What does context mean, what is its Turkish equivalent?**

Its Turkish equivalent is "context". It means the set of conditions, background and integral situations associated with any statement, data or operation.

**What is the difference between Prompt and Context?**

A prompt is an input, question, or action instruction given directly to the AI ​​(“Explain this code”). Context is the additional information, the entire code, environment variables or past conversations provided for the model to carry out this instruction correctly.

**Why is the Context Window limited?**

In the Transformer architecture, each token is cross-linked with all other tokens. This mathematical calculation and stored memory (KV-Cache) creates a hardware limit on GPU memory, as it increases directly with the square of the context length.

**Why does "Context Switch" cause performance loss in the operating system?**

When moving from one process to another, the CPU must save its registers, load the memory space of the new process, and the processor caches (L1/L2/L3 and TLB) must be flushed and repopulated. This situation directly leads to processor loss in the order of microseconds.

**Why is the context package given as the first parameter to every function in Go language?**

In Go, the ctx context.Context parameter prevents unnecessary consumption of server resources by ensuring that database queries and background jobs are stopped when an HTTP request is canceled or times out.

## Related terms

- [Context Window](https://trescout.com/en/dictionary/context-window/)
- [Prompt](https://trescout.com/en/dictionary/prompt/)
- [RAG](https://trescout.com/en/dictionary/rag/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)

## Related tools

- [REA](https://trescout.com/en/discover/rea/)
- [Servers](https://trescout.com/en/discover/servers/)
- [Goose](https://trescout.com/en/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/en/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/en/discover/openclaude/)
- [Context Mode](https://trescout.com/en/discover/context-mode/)
- [Code Review Graph](https://trescout.com/en/discover/code-review-graph/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/context/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/context/
