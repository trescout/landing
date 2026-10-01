# What is Assembly?

Assembly refers to two basic concepts in computer science: First, the lowest-level symbolic programming language (Assembly Language) that directly governs the hardware processor (CPU); The second is to turn compiled software modules (.NET assembly) into a single distributable package.

## 1. Low-level programming language (Assembly Language)
The computer processor only understands binary signals (machine code / opcodes) 0 and 1. Assembly language consists of human-readable symbolic abbreviations (mnemonics) corresponding to these raw machine codes:

## 2. Processor registers and x86-64 architecture
The most critical registers on a modern 64-bit x86-64 processor are:

## 3. CISC vs RISC: difference between x86-64 and ARM64
x86-64 architecture works with CISC (Complex Instruction Set) philosophy; It has variable instruction sizes and rich instructions that can operate directly on memory. ARM64 (Apple Silicon, Mobile) is based on RISC (Reduced Instruction Set); It provides great superiority in energy efficiency with its fixed 32-bit command length and Load-Store architecture.

## 4. System calls (Syscall) and Linux x86-64 example

## 5. .NET Assembly and WebAssembly (WASM)

## Frequently asked questions
**What does assembly mean and what does it do?**
Assembly is the lowest-level symbolic programming language that corresponds 1 to 1 to the hardware instruction set of the computer processor. It is used to directly control CPU registers and memory.

**What is the difference between Assembler and Compiler?**
The compiler (C, C++, Rust) analyzes and optimizes and translates complex human logic and loops into machine code. Assembler, on the other hand, converts assembly instructions, which are already symbolic versions of machine code, directly into binary byte code.

**Where is assembly language still used today?**
It is actively used in operating system kernels (bootloader), hardware device drivers, reverse engineering, malware analysis, cyber vulnerability detection and embedded systems (IoT/microcontroller).

**What is the difference between CISC and RISC?**
CISC (x86-64) has a rich instruction set that can perform multiple subprocesses and memory accesses in a single instruction; RISC (ARM), on the other hand, is a simplified and energy-efficient architecture that runs each command in a single clock cycle.


## Related terms
- [Memory Management](/en/dictionary/memory-management/)
- [Runtime](/en/dictionary/runtime/)
- [Compilation](/en/dictionary/compilation/)
- [Apple Silicon](/en/dictionary/apple-silicon/)
- [Emulator](/en/dictionary/emulator/)

## Related tools
- [Ghidra](/en/discover/ghidra/)
- [Apollo-11](/en/discover/apollo-11/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/assembly/
