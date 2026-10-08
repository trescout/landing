# Assembly: Definition, registers, and system architecture

Assembly refers to two fundamental concepts in computer science: the lowest-level symbolic programming language that directly instructs the central processing unit (CPU), and compiled deployment packages (.NET assemblies) that bundle executable modules.

## 1. Low-Level Programming Language (Assembly Language)
Computer processors only understand binary machine code (0s and 1s, or opcodes). Assembly language replaces raw hexadecimal opcodes with human-readable mnemonics:

## 2. CPU Registers and x86-64 Architecture
In modern 64-bit x86-64 processors, key registers serve specialized and general computational functions:

## 3. CISC vs RISC: x86-64 vs ARM64 Differences
x86-64 architecture follows the CISC (Complex Instruction Set Computer) philosophy, offering variable-length instructions capable of direct memory manipulation. Conversely, ARM64 (Apple Silicon, mobile chipsets) adheres to RISC (Reduced Instruction Set Computer) design with uniform 32-bit instructions and a strict load-store model, maximizing silicon energy efficiency.

## 4. System Calls (Syscalls) and Linux x86-64 Example

## 5. .NET Assemblies and WebAssembly (WASM)

## Frequently asked questions
**What is Assembly language and what is it used for?**
Assembly is a low-level symbolic language that corresponds 1-to-1 with machine instruction sets, used for firmware, OS kernels, high-performance engines, and security analysis.

**What is the difference between an assembler and a compiler?**
A compiler translates abstract high-level languages (C++, Rust) into optimized assembly or machine code, whereas an assembler translates symbolic mnemonics directly into binary opcodes without restructuring algorithms.

**Where is Assembly still used today?**
It is indispensable in operating system bootloaders, device drivers, embedded systems, reverse engineering, exploit development, and real-time graphics optimizations.


## Related terms
- [Memory Management](/en/dictionary/memory-management/)
- [Runtime](/en/dictionary/runtime/)
- [Compilation](/en/dictionary/compilation/)
- [Apple Silicon](/en/dictionary/apple-silicon/)
- [Emulator](/en/dictionary/emulator/)

## Related tools
- [Apollo-11](/en/discover/apollo-11/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/assembly/
