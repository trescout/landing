# What is Working Memory in AI?

> English: Working Memory · Etymology: Old English weorc (activity) + Latin memoria (mindful recall)

**Category:** AI  
**Last updated:** 2026-09-22

Working memory in artificial intelligence refers to the active, temporary scratchpad information held inside a language model's immediate context window to execute current reasoning steps, multi-turn dialogues, and tool interactions.

## Definition and Etymology
The concept represents the active workbench of an intelligence system: once an inference task completes or a conversation resets, this temporary scratchpad state is wiped clean. The model's context window acts as the container, while the tokens loaded within it constitute the active working memory.

## Everyday Context and Practical Usage
Key functional roles of working memory:
- **Conversational Continuity:** Remembering statements from previous user turns in a multi-message session.- **Reasoning Scratchpad:** Storing intermediate calculations and step-by-step logic during Chain-of-Thought (CoT) prompts.- **Tool Calling & Coordination:** Holding JSON payloads returned by APIs before synthesizing the final response.

## Technical Depth and Architecture
Token budget management in working memory:
- **Context Limits:** If a model features a 128K token context window and conversation history consumes 100K tokens, only 28K tokens remain for reasoning and output.- **Attention Mechanism (KV Cache):** Transformers preserve keys and values in memory caches to prevent redundant matrix recalculation during generation.- **Eviction & Summarization:** When budgets overflow, systems summarize earlier turns or evict stale context slices.

## Commonly Confused With
It is frequently confused with long-term memory. Long-term memory is a persistent user profile stored in external databases or vector stores. Working memory is strictly the transient RAM workbench that empties when the active session terminates.

## Cross-Disciplinary Perspectives
Parallels in other disciplines:
- **Mathematics:** Scratch paper used to scribble intermediate formulas during an exam, discarded after obtaining the answer.- **Carpentry:** The workbench where tools and planks rest while assembling a cabinet, cleared when the job is done.- **Computer Architecture:** Fast CPU registers and L1 cache versus persistent hard drive storage.

## Analogy
It is like scrap paper used to write down intermediate steps while solving a complex math problem; once the final answer is calculated, the paper is thrown away.

## Frequently Asked Questions

**What happens when an AI model's working memory fills up?**  
The system must evict earlier conversation turns, compress the history with summarization, or risk truncation errors.

**How does working memory differ from weights in a model?**  
Weights are permanent parametric knowledge learned during training; working memory is non-parametric dynamic context supplied in the prompt.

**Can an AI expand its working memory indefinitely?**  
No; expanding the context window increases quadratic computational complexity and degrades attention retrieval accuracy (the 'lost in the middle' effect).

**What is the role of KV Cache in working memory?**  
The KV Cache stores precalculated attention representations of previous tokens in GPU memory, avoiding redundant computation during autoregressive generation.

## Related terms
- [Memory](/en/dictionary/memory/)
- [Context Window](/en/dictionary/context-window/)
- [Attention Mechanism](/en/dictionary/attention-mechanism/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/working-memory/
