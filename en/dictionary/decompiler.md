# What is Decompiler?

It is a translation tool that converts machine code back into a readable software language.

## Overview
When a computer program is compiled, code that is understandable to humans is converted into machine language, i.e., numbers that only the processor can understand. A decompiler reverses this process, attempting to restore these complex and seemingly meaningless numbers back into a source code format that developers can work on. This process is generally used in cases where the original source code is lost or to understand how a program works.

*Analogy: It is like a translation machine that translates a book written in a foreign language back into your native language; however, the translation may not always perfectly match the original words.*

## How it works
It takes the executable file of the program and analyzes the command sequences within it. Then, it matches these commands with programming language structures that perform similar functions. The resulting text, while not an exact replica of the original code, provides a draft that allows you to understand its logic.

## Where it is used
It is used in software security research to understand how an application works or to update old software for which the source code has been lost.

## Commonly confused with
It is confused with a compiler; a compiler translates code into machine language, while a decompiler translates machine code into human-readable language.

## Frequently asked questions
**Can I get the exact same original code with a decompiler?**
Generally no; because some variable names and comment lines are deleted during compilation, so the resulting output may be somewhat more complex and anonymous.

**Can every program be decompiled?**
Technically most can be, but some software is protected by 'obfuscation' methods, which make this process difficult.


## Related terms
- [Compiler](/en/dictionary/compiler/)
- [Binary](/en/dictionary/binary/)
- [Software Reverse Engineering](/en/dictionary/software-reverse-engineering/)

## Related tools
- [ASC](/en/discover/asc/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/decompiler/
