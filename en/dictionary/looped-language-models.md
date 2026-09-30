# What is Looped Language Models?

They are looped artificial intelligence models that perform step-by-step reasoning by reusing their own generated outputs as inputs.

## Overview
Unlike traditional single-pass language models, looped language models are structures that reprocess their output across layers or in a circular process. When solving a complex problem, instead of giving the answer all at once, the model takes its own initial draft as input and refines it step by step. This approach deepens reasoning capability without increasing computational cost.

*Analogy: It is similar to an author who writes a first draft of a composition, then rereads their own text to correct mistakes and improve it.*

## How it works
The model generates a tentative response in the first step and feeds this response back into the input layer of the model via an internal memory or loop mechanism. This process continues until a predetermined number of loops or a confidence threshold is reached.

## Where it is used
It is used particularly in solving complex math problems, logical puzzle analyses, and code debugging processes. It is also preferred in AI agents that require deep reasoning.

## Commonly confused with
It should not be confused with traditional recurrent neural networks. While recurrent neural networks process data across a time series, these models rerun the transformer architecture with a cyclic logic.

## Frequently asked questions
**Do these models run slower?**
Yes. Since the same model runs multiple loops, the response generation time may take slightly longer.

**Can the number of loops go on infinitely?**
No. A maximum loop limit is set in the systems to prevent resource consumption.


## Related terms
- [Transformer](/en/dictionary/transformer/)
- [LLM](/en/dictionary/llm/)
- [Looped Transformer](/en/dictionary/looped-transformer/)
- [Inference](/en/dictionary/inference/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/looped-language-models/
