# Secure Netcat tunneling in Tailscale networks

Tailcat brings classic netcat functionality to the Tailscale VPN mesh layer, providing secure data transfer without requiring a control plane or open port.

- ★ 7,746
- Go
- GitHub Trending · 2026-08-28

## Updates

- **September 27, 2026:** Stars 2,435 → 7,746, latest release v0.7.0 (September 20, 2026).

## What you get

- Zero port forwarding (Port Forwarding): Direct communication between devices behind NAT or firewall restricted without opening open ports.
- End-to-end WireGuard encryption: Automatically encrypt all TCP and raw data transfers with Tailscale authentication and WireGuard.
- Embedded tsnet library: Working as a standalone Tailscale node without the need to install a Tailscale client at the operating system level.
- Fast file and pipeline transfer: Flow tar, gzip or dd commands between machines via standard input/output (stdin/stdout) pipes.
- Network debugging and diagnostics: Testing port accessibility between microservices and remote machines with practical commands like traditional netcat.

## Installation

**Direct installation with Go**

```
go install tailscale.com/cmd/tailcat@latest
```

## Running it

**Starting listening mode and connecting a client**

```
# Sunucu düğümde dinle:
tailcat -l 8080
# İstemci düğümden bağlan:
tailcat hedef-node 8080
```

## Technical architecture and working principle

- tsnet User Area Network: Creates a VPN session directly within the application without the need for root privileges or a virtual TUN device.
- MagicDNS Node Resolution: Ability to instantly connect with Tailscale machine names such as 'server-node' instead of IP addresses.
- DERP Relay Support: Resuming data transfer via Tailscale DERP relays in extremely restrictive networks where direct P2P connection is not possible.

## Secure network tunneling and end-to-end scenarios

- Fast Secure File Transfer: Zero-configuration transfer with `tailcat -l 9000 > backup.tar.gz` at the receiver and `tailcat destination 9000 \< backup.tar.gz` at the sender.
- Temporary HTTP Service Sharing: Opening the local web server under development to your colleagues on the tailnet network with a single command.
- Embedded Device and Raspberry Pi Access: Securely send data remotely to restricted IoT devices with dynamic IP and in the home network.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up an encrypted file transfer tunnel between two different servers over the Tailscale mesh network using the Tailcat tool. Can you explain how to start the listener on the server side, how to stream the tar archive from standard output on the client side, and how to manage tsnet authentication?

## Frequently asked questions

- Do I need a Tailscale client installed on my machine? No. Tailcat has the tsnet engine built into it; It launches its own Tailscale link as a standalone binary.
- Is traffic truly end-to-end encrypted? Yes. Tailcat uses the WireGuard protocol at the core of the Tailscale network; data is encrypted directly between devices.
- Does it support UDP traffic? Tailcat is primarily optimized for TCP streams and socket tunneling; It secures the TCP capabilities of classic netcat.
- How to authenticate for connection? When Tailcat first runs, it gives a Tailscale login link in the terminal or auto-authenticates with the TAILSCALE_AUTHKEY environment variable.

## Related dictionary terms

- [Root](https://trescout.com/en/dictionary/root/)
- [VPN](https://trescout.com/en/dictionary/vpn/)
- [Mesh](https://trescout.com/en/dictionary/mesh/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** System administrators, DevOps engineers, network experts and cloud architects.
- **License:** BSD 3-Clause (Esnek açık kaynak lisansı)
- **Framework:** Go & Tailscale tsnet Library
- **Platforms:** Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/tailscale/tailcat)
- [Read in Turkish →](https://trescout.com/discover/tailcat/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-28: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/tailcat/
