# What is Continuous Batching?

It is an optimization method that enables artificial intelligence models to process incoming requests continuously and fluently, without waiting.

## Overview
Normally, AI models process requests in batches and wait for one batch to finish. The continuous grouping method allows the system to include new incoming requests into the process before the current process is finished. In this way, users receive answers faster and without waiting.

*Analogy: It's like a chef in a restaurant who keeps cooking orders from each table, instead of just finishing all the food for one table and then moving on to the next.*

## How it works
As soon as the model's processing capacity becomes empty, new requests waiting in the queue are immediately injected into the system. This ensures that hardware resources operate at full efficiency at all times.

## Where it is used
It is used in the background of chat bots such as ChatGPT and in high-traffic artificial intelligence services.

## Commonly confused with
It may be confused with processing speed alone, but this method is specifically about efficiency.

## Frequently asked questions
**Why is it important?**
It reduces users' waiting time and reduces server costs.

**Is it available on every model?**
No, this is generally a feature of advanced inference engines.


## Related terms
- [Inference Engine](/en/dictionary/inference-engine/)
- [LLM](/en/dictionary/llm/)
- [Inference](/en/dictionary/inference/)

## Related tools
- [Omlx](/en/discover/omlx/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/continuous-batching/
