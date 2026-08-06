# What is Token Compression?

It is a technical method that allows artificial intelligence models to work faster and more efficiently by reducing the amount of data they process.

## Overview
Token compression makes the small pieces of data called 'tokens' that artificial intelligence uses when processing texts more condensed and concise. In this way, the model can process much longer texts or complex data using less memory. Essentially, it's like a compression process that discards unnecessary information and keeps what's important.

*Analogy: It's like summarizing a long book and fitting it on one page; The essence of the story remains, but unnecessary details are removed.*

## How it works
The model combines similar or unimportant information while processing data. In this way, the 'attention' mechanism of the model deals with less data and the processing time is shortened.

## Where it is used
It is used in large language models, projects that require long context windows, and systems with hardware constraints.

## Commonly confused with
Can be confused with Quantization; While quantization reduces the weights of the model, token compression compresses the processed data itself.

## Frequently asked questions
**Does token compression reduce quality?**
When done correctly there is no loss of meaning, but excessive compression can cause the model to miss fine details.

**In what cases is it necessary?**
It is used when you need to analyze very long documents and the memory limit of the model is pushed.


## Related terms
- [Token](/en/dictionary/token/)
- [Context Window](/en/dictionary/context-window/)
- [Quantization](/en/dictionary/quantization/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/token-compression/
