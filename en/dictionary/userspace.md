# What is Userspace?

A safe area where user applications run without interfering with the computer's kernel.

## Overview
Operating systems are divided into two main parts: kernel and userspace. Userspace is where the browser, music player or code editors you use run. An error here will not crash the entire computer, it will only affect that application.

*Analogy: It's like the difference between the place where a building's plumbing and electrical systems are located (the core) and the apartment where you live (userspace); A problem in your apartment does not bring down the building.*

## How it works
Applications request permission from the kernel to access the system's underlying resources. In this way, the rest of the system is protected.

## Where it is used
It is a fundamental concept in software development, security and system architecture.

## Commonly confused with
It is confused with kernel space; The kernel dominates the entire system, while userspace is limited.

## Frequently asked questions
**Why does this distinction exist?**
For security and stability; To prevent applications from corrupting the system.

**Where does the code I wrote run?**
Most applications and code run within userspace.


## Related terms
- [Runtime](/en/dictionary/runtime/)
- [Containers](/en/dictionary/containers/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/userspace/
