# What is Bindings?

They are bridges that enable different programming languages ​​to use each other's libraries.

## Overview
A library is usually written in a single language (e.g. C++). However, if you are using Python, you cannot use that library directly. Binding is an interface that translates that library into a language that Python understands. In this way, you can cross language boundaries and use the best tools in the language you want.

*Analogy: It is like an interpreter translating between two people speaking different languages; one helps the other understand what the other is saying.*

## How it works
Developers create a small layer of code that ports the functions of the main library to the target language. So complex operations in the main library work like a simple command in your own language.

## Where it is used
Most AI models are written in C++, but thanks to Python bindings we can easily use them with Python.

## Commonly confused with
It may be confused with API, but while API communicates over the network, binding is a memory-level connection within the same computer.

## Frequently asked questions
**Why aren't every library written in every language?**
Low-level languages ​​(C++) are preferred for performance, high-level languages ​​(Python) are preferred for ease of use.

**Does binding slow down?**
Although there is usually a slight performance loss, the convenience it provides is worth it.


## Related terms
- [API](/en/dictionary/api/)
- [Framework](/en/dictionary/framework/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [Turbovec](/en/discover/turbovec/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/bindings/
