# What is Memory Management?

*Dictionary · Dev · Last updated: September 19, 2026*

Memory Management is the process of allocating the physical and virtual random access memory (RAM) of the computer among running software, protecting it and returning it to the system when use is finished.

## 1. Memory anatomy: Stack and Heap distinction

When a program is run, the operating system allocates a special virtual memory space (Virtual Address Space) to that process. The two most critical components of this space are Stack and Heap:

```
+------------------------------------+ Yüksek Bellek Adresleri (0xFFFFFFFF)
|           İşletim Sistemi / Kernel |
+------------------------------------+
|  STACK (Aşağıya doğru büyür ↓)     | <-- Yerel değişkenler, fonksiyon çerçeveleri
|                 ↓                  |
|                                    |
|                 ↑                  |
|  HEAP (Yukarıya doğru büyür ↑)     | <-- Dinamik nesneler (malloc, new)
+------------------------------------+
|  BSS (İlklendirilmemiş Global)     |
+------------------------------------+
|  DATA (İlklendirilmiş Statik Veri) |
+------------------------------------+
|  TEXT (Makine Kodu / Talimatlar)   |
+------------------------------------+ Düşük Bellek Adresleri (0x00000000)
```

- Stack: Managed automatically by the CPU architecture (LIFO). It is extremely fast (only the stack pointer register is shifted). However, its size is fixed (1MB - 8MB), and it results in a Stack Overflow during infinite recursion.
- Heap: Managed by the developer or the language's runtime. It is allocated for dynamic objects and can grow up to the size of physical RAM and swap space. If not cleared, it causes memory leaks and fragmentation.

***Analogy:** Stack is the tower of paper documents on your desk; You put the incoming document on top and when you are done, you instantly take the top one, the placement time is zero. Heap is like a big warehouse; You go to the warehouse and ask for an empty shelf for the box, the warehouseman searches for a suitable place, gives you the key, and if you forget to return the shelf to the warehouseman when you are finished, the warehouse will become unusable in a short time.*

## 2. Three basic memory management paradigms

- Manual Memory Management (C, C++): The developer manages memory personally using malloc() and free(). It offers maximum speed and zero latency; however, it carries the risks of leaks, dangling pointers, and Use-After-Free vulnerabilities, which account for over 70% of security flaws in the software world.
- Automatic Garbage Collection (Java, Go, Python, JS): The programmer does not perform deletions; a background GC engine cleans up orphaned objects unreachable from root references using Mark-and-Sweep or Reference Counting algorithms. However, periodic scans can lead to micro-pauses (Stop-The-World).
- Ownership & Borrowing (Rust): The Rust compiler verifies at compile time that every memory block has a single owner. It provides 100% memory safety at C speeds without running a garbage collector.

## 3. OS level memory: Virtual memory and OOM Killer

Modern operating systems use Virtual Memory and Paging architecture to prevent programs from reading each other's memory. The Memory Management Unit (MMU) in the CPU converts virtual addresses to physical addresses in hardware with the help of TLB cache. When physical RAM and swap are completely exhausted, the OOM Killer (Out of Memory Killer) mechanism of the Linux kernel terminates the most aggressive process with SIGKILL to save the system.

## Frequently asked questions

**What does memory management mean? What is its Turkish equivalent?**

Memory Management means "memory management" in Turkish. It is the entire process of allocating, monitoring and releasing RAM resources during the execution of a computer program.

**What is the main difference between Stack and Heap?**

Manages local variables whose stack size is known at compile time with LIFO logic extremely quickly; Heap, on the other hand, is a flexible memory pool that is reserved for objects that grow dynamically at runtime and is more complex to manage.

**How does Garbage Collection work?**

In languages ​​where the software developer does not manually delete (Java, Go, JS, etc.), the engine running in the background detects orphan objects that cannot be reached from the root variables and clears the RAM.

**How to prevent memory leak?**

In manual languages, by writing a free for each malloc or by setting up RAII patterns; In languages ​​with garbage collectors, global array references and event listeners that are not closed are cleared and prevented.

## Related terms

- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [State Management](https://trescout.com/en/dictionary/state-management/)
- [Serialization](https://trescout.com/en/dictionary/serialization/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Assembly](https://trescout.com/en/dictionary/assembly/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/memory-management/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/memory-management/
