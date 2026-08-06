# What is Prefix Cache?

An acceleration method that prevents artificial intelligence from repeating the same operations by keeping the text beginnings it has previously processed in memory.

## Overview
Artificial intelligence models can read from the beginning each time when processing long texts. Prefix cache saves the unchanging beginning part of this text in memory. Thus, the model uses the literal information instead of rereading that part in its next request.

*Analogy: It's like keeping a photocopy of those pages ready on your desk instead of memorizing the first pages every time you read a book.*

## How it works
The system caches the prefixes of the texts processed by the model. When a similar query comes in, the system immediately uses this part of the cache and processes only the newly added parts.

## Where it is used
It is used in LLM services, conversations that require long context, and high-traffic artificial intelligence applications.

## Commonly confused with
It can be confused with KV cache; While the KV cache holds the internal state of the model, the prefix cache holds text blocks.

## Frequently asked questions
**How much speed does it provide?**
It significantly reduces response time, especially when working on long documents.

**Is it always available?**
Yes, but since it takes up space in memory, it must be managed according to the capacity of the system.


## Related terms
- [KV Cache](/en/dictionary/kv-cache/)
- [Context Window](/en/dictionary/context-window/)
- [Inference](/en/dictionary/inference/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/prefix-cache/
