# Assembly: Definition, registers, and system architecture

*Dictionary · Dev · Last updated: September 19, 2026*

Assembly refers to two fundamental concepts in computer science: the lowest-level symbolic programming language that directly instructs the central processing unit (CPU), and compiled deployment packages (.NET assemblies) that bundle executable modules.

## 1. Low-Level Programming Language (Assembly Language)

Computer processors only understand binary machine code (0s and 1s, or opcodes). Assembly language replaces raw hexadecimal opcodes with human-readable mnemonics:

- `MOV`: Transfers data between registers or memory addresses.
- `ADD` / `SUB`: Executes arithmetic addition and subtraction directly on registers.
- `PUSH` / `POP`: Adds or removes 64-bit values onto the call stack.
- `JMP` / `JE` / `JNE`: Branches program execution flow based on condition flags.

Assembly source code is assembled directly into binary machine instructions using tools like NASM or GAS without any virtual machine overhead.

## 2. CPU Registers and x86-64 Architecture

In modern 64-bit x86-64 processors, key registers serve specialized and general computational functions:

- **General Purpose Registers:** `RAX` (accumulator and return value), `RBX` (base register), `RCX` (loop counter), `RDX` (I/O and arithmetic), `RDI` and `RSI` (destination and source index pointers for string/block transfers).
- **Special Purpose Registers:** `RSP` (Stack Pointer - points to the top of the stack), `RBP` (Base Pointer - frame base), `RIP` (Instruction Pointer - points to the next instruction), and `RFLAGS` (status flags such as Zero, Carry, and Sign).

## 3. CISC vs RISC: x86-64 vs ARM64 Differences

x86-64 architecture follows the **CISC** (Complex Instruction Set Computer) philosophy, offering variable-length instructions capable of direct memory manipulation. Conversely, ARM64 (Apple Silicon, mobile chipsets) adheres to **RISC** (Reduced Instruction Set Computer) design with uniform 32-bit instructions and a strict load-store model, maximizing silicon energy efficiency.

## 4. System Calls (Syscalls) and Linux x86-64 Example

```
section .text
global _start

_start:
    ; 1. Print message to stdout (sys_write = syscall 1)
    mov rax, 1          ; syscall: sys_write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, msg        ; memory buffer address
    mov rdx, 14         ; message length
    syscall             ; switch to kernel space

    ; 2. Terminate program cleanly (sys_exit = syscall 60)
    mov rax, 60         ; syscall: sys_exit
    xor rdi, rdi        ; return code 0
    syscall

section .data
    msg db "Hello, world!", 10
```

## 5. .NET Assemblies and WebAssembly (WASM)

- **.NET Assembly:** In modern managed runtimes, compiled C# produces Common Intermediate Language (CIL) bytes and metadata packaged as `.dll` or `.exe` assemblies.
- **WebAssembly (WASM):** A portable binary code format executing in browser sandboxes at near-native speed, compiled from languages like Rust, C++, and Go.

*Assembly language is like assembling the gears, escapement, and springs of a mechanical watch with tweezers under a microscope; it offers unmatched precision and control, but requires painstaking attention to detail.*

## Frequently asked questions

**What is Assembly language and what is it used for?**

Assembly is a low-level symbolic language that corresponds 1-to-1 with machine instruction sets, used for firmware, OS kernels, high-performance engines, and security analysis.

**What is the difference between an assembler and a compiler?**

A compiler translates abstract high-level languages (C++, Rust) into optimized assembly or machine code, whereas an assembler translates symbolic mnemonics directly into binary opcodes without restructuring algorithms.

**Where is Assembly still used today?**

It is indispensable in operating system bootloaders, device drivers, embedded systems, reverse engineering, exploit development, and real-time graphics optimizations.

## Related terms

- [Memory Management](https://trescout.com/en/dictionary/memory-management/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Compilation](https://trescout.com/en/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/en/dictionary/emulator/)

## Related tools

- [Apollo-11](https://trescout.com/en/discover/apollo-11/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/assembly/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/assembly/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/assembly/
