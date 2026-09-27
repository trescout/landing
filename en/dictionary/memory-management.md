# Memory Management Stack, Heap, garbage collection, and OS memory


**Category:** Dev  

**Last updated:** 2026-09-19


Memory management is the software and operating system mechanism that governs how volatile random-access memory (RAM) is dynamically allocated, tracked, and safely reclaimed during an application's lifecycle.


## 1. Memory Anatomy: The Division Between Stack and Heap
A computer program organizes its allocated runtime memory into two distinct primary structures:
- **Stack Memory:** A fast, contiguous LIFO (Last-In, First-Out) memory structure managed directly by the CPU instruction pointer. It holds function call frames, local primitive variables, and pointer addresses. Allocation is instantaneous as it merely increments the Stack Pointer register (RSP), and deallocation occurs automatically when a function scope returns.- **Heap Memory:** A large, unstructured pool of volatile memory used for dynamic runtime allocations whose sizes or lifespans cannot be known at compile time. Requesting heap memory involves calling system allocators (like malloc), traversing memory fragmentation structures, and returning pointers, making it slower than stack operations.

## 2. Three Core Paradigms of Memory Management
Across programming languages, memory management adheres to three primary paradigms:
- **Manual Memory Management (C, C++):** Developers explicitly allocate heap blocks using <code>malloc()</code> or <code>new</code> and must manually invoke <code>free()</code> or <code>delete</code>. While delivering maximum performance, manual management carries severe risks of memory leaks, use-after-free corruptions, and double-free security exploits.- **Automated Garbage Collection (Java, Go, JavaScript, Python):** A runtime garbage collector (GC) periodically scans memory graphs to detect unreferenced objects and reclaim them. Advanced GCs employ generational hypotheses and concurrent mark-and-sweep algorithms, trading small CPU and latency pauses for programmer safety.- **Compile-Time Ownership and Borrowing (Rust):** Rust introduces memory safety without a garbage collector through a strict compiler ownership model: every value has a single owner variable, and the compiler statically verifies borrow lifespans, freeing memory deterministically when owners drop out of scope.

## 3. Operating System Level: Virtual Memory, Paging, and OOM Killer
Beneath application code, the operating system kernel coordinates physical RAM via hardware Memory Management Units (MMU):
- **Virtual Memory & Paging:** Each process operates within an isolated virtual address space divided into uniform 4 KB or 2 MB pages. The MMU maps virtual pages to physical hardware frames via page tables.- **Page Faults & Swap:** When a program addresses memory currently swapped out to disk storage, the OS triggers a page fault to retrieve the data back into RAM.- **Out of Memory (OOM) Killer:** When system memory is exhausted, the Linux kernel invokes the OOM Killer, scoring processes based on memory usage and terminating high-consumption processes (like runaway databases or web workers) to keep the core OS stable.

## Analogy
Stack memory is like a stack of plates on a dining table where you quickly place and remove items from the very top; heap memory is like a vast commercial warehouse where you rent storage space for arbitrary crates and need a cataloging system to remember where each parcel was placed.

## Frequently asked questions

**What is the difference between Stack and Heap memory?**  
Stack memory is automatic, extremely fast, and limited to local function execution scopes; Heap memory is dynamic, large, and requires explicit tracking or garbage collection.

**What is a memory leak?**  
A memory leak occurs when an application allocates heap memory but fails to release it after it is no longer needed, causing memory usage to climb until the system crashes.

**How does Rust achieve memory safety without a garbage collector?**  
Rust uses compile-time ownership, borrowing, and lifetime rules that ensure memory is freed deterministically as soon as its owner variable goes out of scope.

**What triggers the Linux Out of Memory (OOM) Killer?**  
When physical RAM and swap space are completely exhausted and the kernel cannot satisfy new allocation requests, it kills memory-heavy processes to prevent a total system freeze.

## Related terms
- [Runtime](/en/dictionary/runtime/)
- [State Management](/en/dictionary/state-management/)
- [Serialization](/en/dictionary/serialization/)
- [Network Stack](/en/dictionary/network-stack/)
- [Assembly](/en/dictionary/assembly/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/memory-management/
