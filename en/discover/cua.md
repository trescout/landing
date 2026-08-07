# Computer control for artificial intelligence agents

CUA provides an open source infrastructure for computer-capable artificial intelligence agents. It brings together sandbox, software development kit (SDK) and benchmark tools under one roof for the purpose of training and evaluating agents that can control desktop operating systems.

- ★ 20,990
- HTML
- GitHub Trending · 2026-06-16

## Update
- 7 August 2026: Star 20,962 → 20,990, latest version fleet-v0.1.7 (7 August 2026).
- August 6, 2026: Star 20,909 → 20,962, latest release sandbox-v0.1.27 (August 5, 2026).
- 4 August 2026: Star 20,874 → 20,909, latest release sandbox-v0.1.24 (3 August 2026).
- August 3, 2026: Star 20,856 → 20,874, latest release sandbox-v0.1.23 (August 3, 2026).

## What you get
- Control desktop apps in the background
- Isolated sandboxes for different operating systems
- Benchmarking tools to measure agent performance

## Installation
**Driver installation (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Sandbox SDK installation**

```
pip install cua
```


## Running it
**macOS virtual machine startup**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```


## If you don't write code
I want to develop a computer usage agent using the CUA infrastructure. Help me set up the basic Python structure that will allow my agent to interact with desktop applications in the background, make mouse clicks, and send keyboard input. Create a sample code sketch that runs commands and takes screenshots in a Linux environment using the CUA Sandbox SDK.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/cua/
