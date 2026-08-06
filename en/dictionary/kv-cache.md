# What is KV Cache?

> Key-Value Cache

It is an acceleration method that prevents artificial intelligence from repeating the same operations by keeping the words it has previously processed in its memory.

## Overview
When producing a text, instead of thinking from scratch for each word, artificial intelligence stores the previously processed information in a cache as 'Key' and 'Value' values. This system allows the model to quickly recall the past without having to recalculate it when predicting the next word. Thus, the processing load is reduced and response times are significantly shortened.

*Analogy: While reading a book, it is like taking notes of important points and continuing by looking only at the notes, instead of reading the entire book from the beginning on each page.*

## How it works
While the model is running, it is automatically created in the background and kept in memory. This cache starts to fill up when the user starts a long conversation. When memory becomes full, the system develops strategies to clear old information or make room for new data.

## Where it is used
It is used in the working processes of LLMs and especially in chat interfaces where long texts are produced.

## Commonly confused with
It may be confused with Context Window, but this is not a capacity limit, but a method of using this capacity efficiently.

## Frequently asked questions
**Why is KV Cache important?**
By preventing the artificial intelligence from calculating the same sentence over and over again, it reduces the load on the processor and speeds up the response.

**What happens if the memory becomes full?**
The system may become unable to process new data or begin to forget old information.


## Related terms
- [LLM](/en/dictionary/llm/)
- [Context Window](/en/dictionary/context-window/)
- [Inference](/en/dictionary/inference/)
- [Memory Management](/en/dictionary/memory-management/)

## Related tools
- [LMCache](/en/discover/lmcache/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/kv-cache/
