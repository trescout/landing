# What is Borrow Checker?

*Dictionary · Dev · Last updated: October 13, 2026*

The mechanism that prevents programs written in the Rust language from making memory errors and controls how data is used.

## Overview

The borrow checker is one of the most important parts of the Rust compiler and guarantees the safe use of memory. It meticulously examines whether multiple places are modifying the same data at the same time in your code, and whether the lifespan of the data is sufficient. When it finds a situation that does not comply with the safety rules, it does not allow the program to run and warns you.

***Analogy:** It is a strict tracking log in a sensitive laboratory that ensures only a single researcher can borrow a special piece of equipment at a time and return it when they are finished.*

## How it works

It activates in the background when you try to compile your code. It looks at the ownership rules and borrowing durations of variables. If it detects data sharing that violates the rules, it stops compilation and shows where the error is.

## Where it is used

In system programming, it actively works during the compilation phase for Rust projects that want to prevent memory leaks and crashes right from the start.

## Commonly confused with

It is different from normal debuggers; it works while the code is being written and compiled, not while the program is running.

## Frequently asked questions

**Why is it so strict?**

It takes precautions at an early stage to completely eliminate memory crashes at runtime.

**Does it cause it to run slowly?**

No, it only runs during the compilation phase and creates no extra overhead at runtime.

## Related terms

- [Rust](https://trescout.com/en/dictionary/rust/)
- [Compiler](https://trescout.com/en/dictionary/compiler/)
- [Thread-safety](https://trescout.com/en/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/en/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/en/dictionary/memory-management/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/borrow-checker/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/borrow-checker/
