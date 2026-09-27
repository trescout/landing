# What is Memory Management?

Memory Management is the process of allocating the physical and virtual random access memory (RAM) of the computer among running software, protecting it and returning it to the system when use is finished.

## 1. Memory anatomy: Stack and Heap distinction
When a program is run, the operating system allocates a special virtual memory space (Virtual Address Space) to that process. The two most critical components of this space are Stack and Heap:

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
- [Runtime](/en/dictionary/runtime/)
- [State Management](/en/dictionary/state-management/)
- [Serialization](/en/dictionary/serialization/)
- [Network Stack](/en/dictionary/network-stack/)
- [Assembly](/en/dictionary/assembly/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/memory-management/
