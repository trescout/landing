# What is Experts Streamed from Disk?

It is a method of loading parts of massive artificial intelligence models from the disk on-the-fly when they do not fit into memory.

## Overview
Artificial intelligence models are sometimes so large that they do not fit into the computer's RAM capacity. In this technique, only the parts of the model (experts) needed at that moment are quickly read from the disk and brought into memory. Thus, very large models can become operational even on limited hardware.

*Analogy: You cannot fit all the books in a giant library onto your desk; therefore, you only take the page you are going to read at that moment from the shelf, read it, and put it back when you are finished.*

## How it works
The system divides the model's weights into small pieces and stores them on the disk. When a user asks a question, the relevant parts of the model are transferred from the disk to memory very quickly, processed, and then the memory is cleared.

## Where it is used
It is used especially by developers who want to run very large language models on home computers and on servers with hardware constraints.

## Commonly confused with
It can be confused with loading the entire model into memory; here, loading only occurs when needed.

## Frequently asked questions
**Does this method reduce speed?**
Yes, since the disk reading process is slower than RAM, there may be some delay in the model's response time.

**Can every model work this way?**
The model must be designed with this architecture; that is, it must have a fragmented (Mixture of Experts) structure.


## Related terms
- [Mixture of Experts](/en/dictionary/mixture-of-experts/)
- [RAM](/en/dictionary/ram/)
- [Inference Engine](/en/dictionary/inference-engine/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/experts-streamed-from-disk/
