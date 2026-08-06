# What is Vector Database?

It is a special type of database where artificial intelligence stores data so that it can quickly find it based on its meaning.

## Overview
A vector database is a special storage system that stores data as numerical vectors that represent their meaning, rather than traditional rows and columns. This structure allows artificial intelligence to find the most relevant data among millions of data within milliseconds.

*Analogy: A traditional database is like an alphabetical catalog in a library. Vector database is like a concept map in a person's mind; It works like when you think of an idea, all of your memories associated with it come to your mind at the same time.*

## How it works
First, the data is converted into numerical vectors using the embedding method. When a query is made, the database measures the distance between the vector of the query and the vectors of the data. The ones with the shortest distance, that is, the ones closest in meaning, are returned as results.

## Where it is used
It is used in smart search systems, recommendation engines and RAG systems where artificial intelligence creates long-term memory.

## Commonly confused with
It is confused with classical databases such as SQL, but classical databases look for exact matches while vector databases look for similarities.

## Frequently asked questions
**Is it slower than classic databases?**
No, it is much faster than classical methods for similarity searches in very large data sets.

**What data can be stored?**
Any data whose meaning can be converted into vector, such as text, image, audio or video, can be stored.


## Related terms
- [Embedding](/en/dictionary/embedding/)
- [RAG](/en/dictionary/rag/)
- [Knowledge Graph](/en/dictionary/knowledge-graph/)
- [Memory Engine](/en/dictionary/memory-engine/)

## Related tools
- [Zvec](/en/discover/zvec/)
- [Turbovec](/en/discover/turbovec/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/vector-database/
