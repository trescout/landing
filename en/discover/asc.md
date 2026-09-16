# Analyze Android applications quickly

ASC is a high-speed Android decompiler interface developed for mobile application researchers and AI agents. Written in Python, this tool aims to accelerate the process of analyzing complex application files.

- ★ 1,336
- Python
- GitHub Trending · 2026-09-16

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
Act as an Android application researcher. Help me find a specific class in an APK file, parse the AndroidManifest.xml file, or search for references within the code using the Droid ASC tool. When generating commands, use the tool's getclass, getmanifest, and findrefs commands with the correct parameters and explain how I should interpret the outputs.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/asc/
