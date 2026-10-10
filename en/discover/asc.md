# Analyze Android applications quickly

ASC is a high-speed Android decompiler interface developed for mobile application researchers and AI agents. Written in Python, this tool aims to accelerate the process of analyzing complex application files.

- ★ 2,236
- Python
- GitHub Trending · 2026-09-16

## Updates

- **October 10, 2026:** Stars 1,980 → 2,236, latest release dev-0.1.1-post4 (October 10, 2026).
- **September 27, 2026:** Stars 1,336 → 1,980, latest release dev-0.1.1-post2 (September 21, 2026).

## What you get

- Scans large application files in seconds
- Queries directly on the code without straining memory
- Produces fast results without unnecessary preprocessing

## Installation

**Installation with package manager**

```
pip install droidasc
```

**Installation from source code**

```
pip install .
```

## Running it

**Opening an application file with a visual interface**

```
droidasc app.apk --gui
```

**Exporting a specific class**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Act as an Android application researcher. Help me find a specific class in an APK file, parse the AndroidManifest.xml file, or search for references within the code using the Droid ASC tool. When generating commands, use the tool's getclass, getmanifest, and findrefs commands with the correct parameters and explain how I should interpret the outputs.

## Related dictionary terms

- [Decompiler](https://trescout.com/en/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Suitable for mobile application security researchers and Android software developers.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/MG1937/ASC)
- [Read in Turkish →](https://trescout.com/discover/asc/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-16: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/asc/
