# What is Assembly?

*Development · Last updated: September 19, 2026*

Assembly refers to two basic concepts in computer science: First, the lowest-level symbolic programming language (Assembly Language) that directly governs the hardware processor (CPU); The second is to turn compiled software modules (.NET assembly) into a single distributable package.

## 1. Low-level programming language (Assembly Language)

The computer processor only understands binary signals (machine code / opcodes) 0 and 1. Assembly language consists of human-readable symbolic abbreviations (mnemonics) corresponding to these raw machine codes:

- MOV: Copies data from one register to another or memory address.
- ADD / SUB: Executes mathematical addition and subtraction operations.
- PUSH / POP: Adds or pulls data to the call stack.
- JMP / JE / JNE: Branches the program flow to another memory address according to the comparison result.

Written assembly codes are directly translated into machine code through converters called Assemblers (nasm, gas); There is no virtual machine layer in between.

***Analogy:** Assembly language is like placing the gears, springs and shafts in a clock one by one with tweezers under a microscope; It provides the highest precision and performance but requires great care. Software assembly means placing this delicate mechanism inside the case and boxing it as a working wristwatch.*

## 2. Processor registers and x86-64 architecture

The most critical registers on a modern 64-bit x86-64 processor are:

- General Purpose Registers: RAX (accumulator and function return), RBX (base data pointer), RCX (loop counter), RDX (input/output data), RDI and RSI (target and source pointers).
- Special Purpose Registers: RSP (Stack Pointer - top of the stack), RBP (Base Pointer - base of the function frame), RIP (Instruction Pointer - address of the next instruction to be executed) and RFLAGS (Zero, Carry flags).

## 3. CISC vs RISC: difference between x86-64 and ARM64

x86-64 architecture works with CISC (Complex Instruction Set) philosophy; It has variable instruction sizes and rich instructions that can operate directly on memory. ARM64 (Apple Silicon, Mobile) is based on RISC (Reduced Instruction Set); It provides great superiority in energy efficiency with its fixed 32-bit command length and Load-Store architecture.

## 4. System calls (Syscall) and Linux x86-64 example

```
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; metnin bellek adresi
    mov rdx, 8          ; metin uzunluğu
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. .NET Assembly and WebAssembly (WASM)

- .NET Assembly: When C# code is compiled, a logical assembly package (Assembly) is created in .dll or .exe format containing CIL/MSIL bytecodes and metadata.
- WebAssembly (WASM): A portable stack virtual machine bytecode that allows C, C++, and Rust code to run in the browser with near-native performance.

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

- [Memory Management](https://trescout.com/en/dictionary/memory-management/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Compilation](https://trescout.com/en/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/en/dictionary/emulator/)

## Related tools

- [Ghidra](https://trescout.com/en/discover/ghidra/)
- [Apollo-11](https://trescout.com/en/discover/apollo-11/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/assembly/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/assembly/
