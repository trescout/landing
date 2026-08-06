# What is Quantization?

It is a size reduction process to make artificial intelligence models lighter and faster.

## Overview
Quantization is the process of reducing the size of numerical data inside huge artificial intelligence models by reducing their precision. In this way, models can run on lower-equipped devices using much less memory.

*Analogy: It is similar to compressing a very high-resolution photo to reduce the file size without noticeably degrading the image quality. You gain speed by sacrificing some details.*

## How it works
The weights in the model are generally high precision decimal numbers. Quantization rounds these to simpler integers. This process significantly reduces the footprint of the model while causing a very small loss in its intelligence.

## Where it is used
It is used to run large models on mobile phones or personal computers (self-hosting).

## Commonly confused with
It is confused with training the model, but this is an optimization process performed after training.

## Frequently asked questions
**Does the model's intelligence decrease?**
It drops very little, but the gain in speed and efficiency is usually worth it.

**Can every model be quantized?**
Yes, it can be implemented on almost all major language models.


## Related terms
- [SLM](/en/dictionary/slm/)
- [Open Weights](/en/dictionary/open-weights/)
- [Self-hosting](/en/dictionary/self-hosting/)
- [Inference](/en/dictionary/inference/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/quantization/
