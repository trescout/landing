# What is Caching?

Frequently used data is temporarily stored in memory for quick access.

## Overview
Caching is an acceleration method used to prevent a system from repeatedly calculating the same data or pulling it from a remote source. Data is copied to a quickly accessible area (cache) and served from there when needed. This significantly reduces the overall response time of the system.

*Analogy: It's like carrying a book you use all the time in your bag; You don't have to go to the library and pick up the book from the shelf every time, it is at hand.*

## How it works
When the system requests data, it first looks at the cache; If the data is there, it retrieves it immediately, otherwise it pulls it from the main source and leaves a copy in the cache.

## Where it is used
It is widely used to improve performance in web browsers, applications, and large-scale data centers.

## Commonly confused with
It can be confused with a database, but cache is temporary and fast, while database is permanent and larger.

## Frequently asked questions
**What happens if the cache becomes full?**
Old or rarely used data is deleted and replaced with new data.


## Related terms
- [KV Cache](/en/dictionary/kv-cache/)
- [Prefix Cache](/en/dictionary/prefix-cache/)
- [Database](/en/dictionary/database/)

## Related tools
- [Guava](/en/discover/guava/)
- [Omlx](/en/discover/omlx/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/caching/
