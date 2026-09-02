# What is Looped Transformer?

It is an artificial intelligence architecture that reduces memory usage by using the same processing layers repeatedly.

## Overview
While traditional models require a separate processing unit for each layer, this architecture uses the same layer repeatedly in a loop. This reduces the size of the model and consumes less memory. It aims to run large models on smaller devices without sacrificing performance.

*Analogy: It is like having a single team of builders construct each floor one by one instead of hiring a separate team for every floor when building a structure.*

## How it works
Data enters the model and passes through the same layer block several times. With each pass, the data is processed further until the final result is reached.

## Where it is used
It is preferred for low-resource devices or mobile artificial intelligence applications.

## Commonly confused with
It might be confused with the standard transformer architecture, but here the number of layers is physically smaller.

## Frequently asked questions
**Does it run slower?**
Because it reuses layers, it may require slightly more processing time, but it provides memory savings.

**Why isn't every model like this?**
For some complex tasks, having each layer specialized yields better results.


## Related terms
- [Transformer](/en/dictionary/transformer/)
- [Quantization](/en/dictionary/quantization/)
- [SLM](/en/dictionary/slm/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/looped-transformer/
