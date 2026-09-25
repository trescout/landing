# Software reverse engineering and analysis suite

Ghidra is a comprehensive open-source software reverse engineering (SRE) suite developed and released by the National Security Agency (NSA). Built with Java and a high-performance C++ decompiler, it decompiles compiled binaries into readable code and provides advanced symbolic analysis across dozens of processor architectures.

- ★ 78,142
- Java
- GitHub Trending · 2026-08-28

## Updates
- September 17, 2026: Stars 78,142, latest release Ghidra_12.1.3_build (Java 21 support, RISC-V and ARM64 decompiler enhancements).

## What you get
- Built-in robust C decompiler: Translates raw machine instructions and assembly directly into clean, high-level C-like pseudocode.
- Extensive multi-architecture support: Covers x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC, and hundreds of microcontroller targets.
- Collaborative multi-user analysis: Team members can simultaneously annotate, rename functions, and version-control projects via Ghidra Server.
- Automated headless analysis: Run scalable vulnerability and malware triage scripts from the command line without launching the GUI.
- Extensible Java and Python scripting: Write custom plugins, automated unpackers, and custom data type parsers.

## Installation and system requirements

**JDK 21 and Ghidra installation**

```
# macOS via Homebrew:
brew install --cask ghidra

# Linux / Windows (Manual launch from release archive):
# Requires 64-bit JDK 21.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Running it and headless command-line analysis

**Launch Graphical User Interface**

```
./ghidraRun
```

**Run headless automated analysis**

```
analyzeHeadless /project/dir ProjectName -import target_binary.bin -postScript SecurityAudit.py
```

## Technical architecture: Sleigh and decompiler engine

The foundational components making Ghidra an industry standard include:
- Sleigh processor specification language: A declarative domain-specific language used to specify instruction sets and register spaces for new CPU architectures.
- P-Code intermediate representation (IR): Normalizes diverse assembly instructions into an intermediate language, allowing architecture-neutral data-flow and control-flow analysis.
- Native C++ decompiler engine: A fast standalone engine that performs aggressive dead-code elimination, control-flow structuring, and variable type recovery.

## Reverse engineering and vulnerability analysis workflows

Ghidra serves as a primary workstation across defensive and offensive cybersecurity engagements:
- Malware triage and analysis: Unpacks unknown suspicious binaries to uncover encrypted strings, C2 domains, and imported system APIs.
- Binary diffing (Program Diff): Compares pre-patch and post-patch binaries to pinpoint vulnerability fixes and exploit vectors.
- Firmware extraction and reversing: Maps raw hardware flash dumps into memory spaces to audit bootloaders, IoT device logic, and kernel routines.

## If you do not code
🤖 If you do not code
I want to inspect a suspicious binary using Ghidra. Can you explain step by step how to create a new project, import the executable, run Auto Analysis, navigate the Decompiler view to read functions, and identify sensitive imported API calls?

- **Who it is for:** Malware analysts, vulnerability researchers, reverse engineers, and embedded firmware developers.
- **License:** Apache-2.0 (Permissive open source license)
- **Developer:** National Security Agency (NSA) and Open Source Community
- **Requirements:** Java Development Kit (JDK) 21 64-bit

## Frequently asked questions
- What are the key differences between Ghidra and IDA Pro? While IDA Pro is a commercial product with expensive per-architecture licensing, Ghidra is free, open source, includes full decompilers for all supported architectures, and features built-in multi-user collaboration.
- Is Ghidra safe when analyzing malicious code? Yes, static analysis merely disassembles instructions without executing the binary. However, performing all malware analysis inside an isolated virtual machine remains standard security hygiene.
- How does Ghidra Server work? Ghidra Server runs on any networked host via the included svrAdmin script, providing versioned multi-user collaboration and user access control in minutes.
- Can I run Python 3 scripts inside Ghidra? While Ghidra historically bundled Jython (Python 2.7), modern installations can leverage PyGhidra to execute native Python 3 with access to external libraries like NumPy and Capstone.

## Links
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## Related dictionary terms
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/en/discover/ghidra/
