# What is Multi-process?

*Dictionary · Dev · Last updated: October 7, 2026*

It is a method where a computer program executes tasks simultaneously by dividing them into multiple sub-processes that are completely independent of each other and have their own private memory space.

## Overview

In traditional programming, an application typically runs sequentially along a single thread of execution. In the multi-process approach, however, the operating system creates a separate workspace for each task. Thanks to this method, which you will frequently encounter in the TreScout glossary, if one of the processes encounters an error and crashes, the other processes continue to run unaffected by this situation.

***Analogy:** You can think of this as independent chefs working in the same kitchen but having their own countertops, knives, and ingredients. Even if one of the chefs cuts their hand and stops working, the other chefs can safely continue cooking at their own stations.*

## How it works

At the operating system level, a separate memory address is allocated for each process. The program spawns new sub-processes from a main process, and these processes communicate with each other through dedicated communication channels to share tasks.

## Where it is used

It is frequently used, particularly in web browsers where each tab runs as a separate process, in big data processing systems, and in server applications performing heavy calculations in the background.

## Commonly confused with

It is often confused with the multi-threading concept. While multi-threading handles tasks using lightweight threads that share the same memory space, the multi-process method assigns each task its own completely isolated memory space.

## Frequently asked questions

**Does using multi-process strain the computer?**

Yes, because separate memory and resources are allocated for each process, it can consume more computer resources compared to other methods.

**In which scenarios should multi-process be preferred?**

It should be preferred for heavy workloads where security and stability are paramount, and where you do not want tasks to be affected by each other's crashes.

## Related terms

- [Concurrency](https://trescout.com/en/dictionary/concurrency/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Thread-safety](https://trescout.com/en/dictionary/thread-safety/)
- [Distributed](https://trescout.com/en/dictionary/distributed/)

## Related tools

- [Raddebugger](https://trescout.com/en/discover/raddebugger/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/multi-process/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/multi-process/
