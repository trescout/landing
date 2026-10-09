# Analysis framework for software reverse engineering

Ghidra is a comprehensive software reverse engineering (SRE) framework developed by the National Security Agency (NSA) and released as open source. Developed with Java and a C++ core, the platform converts compiled binary files into source code, offering advanced decompilers, symbolic analysis, and multi-architecture support to security researchers.

- ★ 79,733
- Java
- GitHub Trending · 2026-08-28

## Updates

- **September 27, 2026:** Stars 78,142 → 79,733, latest release Ghidra_12.1.4_build (September 21, 2026).
- **September 17, 2026:** Stars 74,145 → 78,142, latest release Ghidra_12.1.3_build (August 18, 2026).
- **August 31, 2026:** Stars 73,203 → 74,145, latest release Ghidra_12.1.3_build (August 18, 2026).

## What you get

- Built-in powerful C decompiler: Translates machine code and assembly instructions into readable, high-level C-like syntax.
- Broad processor and architecture range: Support for x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC, and hundreds of embedded microcontroller architectures.
- Collaborative multi-user analysis: Simultaneous annotation, function naming, and version control on the same binary file powered by the Ghidra Server infrastructure.
- Automation and Headless analysis: Automatically scanning thousands of malwares from the command line on the server without entering the graphical interface.
- Extensibility with Java and Python: Personalizing analysis with custom scripts, plugins, and data type libraries.

## Installation and system requirements

**JDK 21 and Ghidra installation**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Execution and headless command line analysis

**Launching the graphical user interface**

```
./ghidraRun
```

**Running headless automated analysis**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```

## Technical architecture: Sleigh and decompiler engine

- Sleigh processor modeling language: A declarative specification language used to introduce a new processor or instruction set architecture (ISA) to Ghidra.
- P-Code intermediate representation (IR): Translating all processor instructions into a common intermediate language (P-Code) to perform architecture-independent data flow and control flow analysis.
- C++-based decompiler engine: A high-performance native engine that simplifies control flow graphs, infers variable types, and reduces complex loops into C code.

## Reverse engineering and vulnerability analysis workflows

- Malware Triage: Opening suspicious executables in an isolated environment to uncover hidden API calls, C2 domain names, and encryption keys.
- Binary file comparison (Program Diff): Visualizing the differences between two files before and after a security patch to detect the closed vulnerability.
- Embedded firmware analysis: Mapping raw flash memory dumps obtained from IoT devices to a memory map and analyzing bootloader and kernel functions.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to inspect a suspicious binary file using Ghidra. Could you explain step by step the steps for opening a new project in Ghidra, importing the file, running Auto Analysis, inspecting functions in the Decompiler window, and detecting suspicious externally called API functions?

## Frequently asked questions

- What are the main differences between Ghidra and IDA Pro? While IDA Pro has commercial and high licensing fees, Ghidra is completely free and open source. Ghidra offers a built-in decompiler for all architectures and includes a multi-user collaboration server.
- Is Ghidra safe when performing malware analysis? Yes, during static analysis, the file is not executed, only its code is disassembled. However, conducting the analysis in an isolated virtual machine (VM) is essential for security.
- How to set up Ghidra Server? Using the svrAdmin script located in the server directory within the Ghidra package, a team server can be set up on a local network in a few minutes and user permissions can be assigned.
- Can Python 3 scripts be run inside Ghidra? Although Ghidra comes with Jython (Python 2.7) by default, modern Python 3 environments and external libraries (NumPy, Capstone) can be used directly thanks to the PyGhidra plugin.

## Related dictionary terms

- [NSA](https://trescout.com/en/dictionary/nsa/)
- [Assembly](https://trescout.com/en/dictionary/assembly/)
- [Decompiler](https://trescout.com/en/dictionary/decompiler/)
- [IoT](https://trescout.com/en/dictionary/iot/)
- [Binary](https://trescout.com/en/dictionary/binary/)
- [API](https://trescout.com/en/dictionary/api/)

- **Who it is for:** Malware researchers, vulnerability hunters, reverse engineering experts, and embedded system developers.
- **License:** Apache-2.0 (Açık kaynak lisansı)
- **Developer:** National Security Agency (NSA) and Open Source Community
- **Requirement:** Java Development Kit (JDK) 21 64-bit

## Links

- [GitHub repository →](https://github.com/NationalSecurityAgency/ghidra)
- [Read in Turkish →](https://trescout.com/discover/ghidra/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-28: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ghidra/
