# What is Tokenizer?

Tokenizer is the basic data processing component that converts natural language texts into numerical tokens (token IDs) that large language models (LLMs) and neural networks can mathematically process.

## 1. Definition and basic problem: Why not direct words?
Large language models (GPT-4, Claude, Llama, etc.) do not read text letter by letter or word by word like a human. Neural networks can only handle matrices, tensors and numbers. Therefore, the text must first be translated into numbers.

## 2. Tokenizer algorithms and mathematical logic
The major tokenizer algorithms at the heart of modern language models are:

## 3. "The Tokenizer Tax" in Turkish
More than 85% of the training data of large language models is in English. This causes the tokenizer dictionary to be filled with predominantly English roots and words.

## 4. Security and Edge Cases: Glitch Tokens
Special tokens that appear in the Tokenizer dictionary but appear rarely or in meaningless contexts in the text body during pre-training of the model are called "Glitch Tokens".

## Frequently asked questions
**What does Tokenizer mean? What is its Turkish equivalent?**
It is called "tokenizer" or "symbolizer" in Turkish. It is software that divides natural language texts into the smallest numerical indexes (tokens) that the artificial intelligence model can understand.

**How many words or letters does 1 token equal?**
In English texts, 1 token is equal to 4 characters or 0.75 words on average (100 words are approximately 130 tokens). In agglutinative languages ​​such as Turkish, one word can hold an average of 2 to 3 tokens due to the fragmentation of suffixes.

**How does BPE (Byte Pair Encoding) work?**
It is a statistical algorithm that builds a fixed-size sub-word dictionary by starting with the most basic characters and combining step by step the character pairs that occur most frequently next to each other in the training set.

**Are tokenizer-free models possible?**
Yes; Recently developed new generation neural network architectures such as MambaByte and MegaByte aim to eliminate language inequality by completely removing the tokenizer layer and processing directly on raw bytes.


## Related terms
- [Token](/en/dictionary/token/)
- [NLP](/en/dictionary/nlp/)
- [Tokenizer-free](/en/dictionary/tokenizer-free/)
- [Prompt Engineering](/en/dictionary/prompt-engineering/)
- [Context](/en/dictionary/context/)

## Related tools
- [Minimind](/en/discover/minimind/)
- [AI Engineering from Scratch](/en/discover/ai-engineering-from-scratch/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/tokenizer/
