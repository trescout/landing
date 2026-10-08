# TCP tunneling for network traffic

Developed in the Go language, OpenFlux is a TCP tunneling tool designed for network stack research. It offers flexible analysis and management capabilities for network traffic through support for pluggable transports.

- ★ 2,027
- Go
- GitHub Trending · 2026-09-12

## Updates

- **October 8, 2026:** Stars 2,019 → 2,027, latest release v0.4.2 (October 7, 2026).
- **October 7, 2026:** Stars 1,910 → 2,019, latest release v0.4.1 (October 7, 2026).
- **October 1, 2026:** Stars 1,896 → 1,910, latest release v0.3.0 (September 30, 2026).
- **September 29, 2026:** Stars 1,884 → 1,896, latest release v0.2.0 (September 28, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a TCP tunnel using the OpenFlux tool. Explain step-by-step the build steps required to run the client on my desktop computer and how to configure SOCKS5 proxy settings in the browser. Additionally, explain with technical details why it is necessary to block RST packets using iptables when setting up an exit node on a Linux server, and the impact of this process on network security.

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

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openflux/
