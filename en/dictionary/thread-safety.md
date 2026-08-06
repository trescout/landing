# What is Thread-safety?

A security feature of a program that prevents data from being corrupted when performing multiple operations at the same time.

## Overview
Computers do many things at once. If two different processes try to change the same data at the same time, chaos will occur. This feature allows processes to wait for each other or run sequentially.

*Analogy: In a house where there is only one toilet, it is like putting a lock on the door; While one is inside, the other has to wait.*

## How it works
Data access rules are determined while the program is being written. While one process uses the data, the others appear to have a 'locked' status on it.

## Where it is used
It is mandatory for banking applications, web servers and all multi-tasking software.

## Commonly confused with
It's not just about security (hacking), it's about data consistency.

## Frequently asked questions
**What happens if it is not thread-safe?**
Your data gets messed up, apps crash, or miscalculations occur.


## Related terms
- [Concurrency](/en/dictionary/concurrency/)
- [System Programming Language](/en/dictionary/system-programming-language/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/thread-safety/
