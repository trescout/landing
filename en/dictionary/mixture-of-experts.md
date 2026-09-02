# What is Mixture of Experts?

> MoE

It is a system that solves complex tasks by distributing them into sub-sections, each specialized in a different subject.

## Overview
In this structure, instead of the entire model answering every question, only the sections (experts) relevant to that specific question are activated. This allows the model to be massive in size while only running the necessary parts. As a result, you get both smarter and faster responses.

*Analogy: It is like being referred to a relevant specialist, such as a cardiologist or neurologist, based on your complaint in a hospital instead of every patient seeing a general surgeon.*

## How it works
When a question is asked, a 'routing' mechanism determines which area of expertise the question falls into. Only those experts process the question and generate an answer.

## Where it is used
It is used in most modern large artificial intelligence models to increase efficiency.

## Commonly confused with
It might be confused with a single model processing all the data.

## Frequently asked questions
**How are the experts selected?**
During training, the model learns which experts are better at which subjects.

**Does this method slow down the model?**
On the contrary, it is faster because only the relevant parts are activated.


## Related terms
- [LLM](/en/dictionary/llm/)
- [AI Models](/en/dictionary/ai-models/)
- [Inference](/en/dictionary/inference/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/mixture-of-experts/
