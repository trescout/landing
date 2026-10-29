# TCP tunneling for network traffic

Developed in the Go language, OpenFlux is a TCP tunneling tool designed for network stack research. It offers flexible analysis and management capabilities for network traffic through support for pluggable transports.

- ★ 2,299
- Go
- GitHub Trending · 2026-09-12

## Updates

- **October 29, 2026:** Stars 2,184 → 2,299, latest release v0.17.1 (October 28, 2026).
- **October 16, 2026:** Stars 2,120 → 2,184, latest release v0.13.0 (October 16, 2026).
- **October 14, 2026:** Stars 2,107 → 2,120, latest release v0.7.3 (October 14, 2026).
- **October 13, 2026:** Stars 2,092 → 2,107, latest release v0.7.2 (October 13, 2026).

## What you get

- Flexible network management with pluggable transports
- Local network traffic routing with SOCKS5 proxy support
- Data transmission via Yandex Docs and WebRTC

## Installation

**Building the desktop client and exit node**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Building the Android client**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```

## Running it

**Starting the desktop client**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a TCP tunnel using the OpenFlux tool. Explain step-by-step the build steps required to run the client on my desktop computer and how to configure SOCKS5 proxy settings in the browser. Additionally, explain with technical details why it is necessary to block RST packets using iptables when setting up an exit node on a Linux server, and the impact of this process on network security.

Repository: https://github.com/p1neappleXpress/OpenFlux. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Pluggable Transports](https://trescout.com/en/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Proxy](https://trescout.com/en/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For users who conduct network stack research and want to tunnel TCP traffic over different transport protocols.
- **License:** GPL-3.0

## Links

- [GitHub repository →](https://github.com/p1neappleXpress/OpenFlux)
- [Read in Turkish →](https://trescout.com/discover/openflux/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openflux/
