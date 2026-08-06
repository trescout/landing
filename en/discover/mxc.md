# Policy-based layered system isolation with Rust

Developed by Microsoft, MXC is a policy-based, layered isolation and containment solution written in Rust language. It is designed to safely limit system resources and increase application security.

- ★ 641
- Rust
- GitHub Trending · 2026-06-07

## What you get
- Runs untrusted code safely in isolated environments.
- Controls file, network and interface access with JSON-based policies.
- It offers multiple isolation backends on Windows, Linux, and macOS.

## Installation
**Compiling on Linux**

```
./build.sh
```

**Build on macOS**

```
./build-mac.sh
```


## Running it
**Running with native binary**

```
wxc-exec.exe config.json
```


## If you don't write code
I want to run an untrusted code snippet in an isolated container using the MXC tool developed by Microsoft. According to the documentation in the project's GitHub repository, I need to prepare a JSON-based configuration file and use the binary appropriate for my platform. Can you create a sample JSON configuration file for me that will allow me to run a Python script with restricted file system and network access, and explain step by step how to run this configuration with wxc-exec.exe?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/mxc/
