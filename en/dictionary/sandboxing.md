# What is Sandboxing?

The technique of running software or suspicious code in an isolated environment to prevent it from harming the main system and environment.

## Overview
Sandboxing is the practice of running untrusted or testing-stage code snippets in a controlled area by segregating them from system resources. This mechanism limits the application's direct access to the file system, local network, or operating system kernel. It is an indispensable security layer to prevent vulnerabilities from spreading to the system and to minimize the impact of malware.

*Analogy: It is similar to conducting a potentially dangerous chemical experiment not in the middle of the room, but inside a blast-resistant glass chamber.*

## How it works
A protected barrier is established using operating system-level restrictions or virtualization tools. When the code is executed, it can only use the limited memory and disk space permitted to it. System calls are continuously monitored; when an unauthorized operation attempt is detected, the software is stopped immediately.

## Where it is used
It is used in running third-party scripts in web browsers, security software examining suspicious files in email attachments, and development environments where AI agents execute code.

## Commonly confused with
While the term sandbox defines the isolated area itself, sandboxing refers to the process of creating, managing, and restricting this secure environment.

## Frequently asked questions
**Does sandboxing significantly reduce system performance?**
Although monitoring system calls introduces a small processing overhead, in modern operating systems this loss is usually negligible.

**Why is sandboxing necessary in AI tools?**
Since the code generated and executed by AI models carries the risk of deleting critical files on the operating system, these operations are carried out in a secure isolation layer.


## Related terms
- [Sandbox](/en/dictionary/sandbox/)
- [Runtime](/en/dictionary/runtime/)
- [Virtual Machines](/en/dictionary/virtual-machines/)
- [Security Scanner](/en/dictionary/security-scanner/)

## Related tools
- [Agent Governance Toolkit](/en/discover/agent-governance-toolkit/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/sandboxing/
