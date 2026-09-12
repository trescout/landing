# TCP tunneling for network traffic

Developed in the Go language, OpenFlux is a TCP tunneling tool designed for network stack research. It offers flexible analysis and management capabilities for network traffic through support for pluggable transports.

- ★ 1,241
- Go
- GitHub Trending · 2026-09-12

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
I want to create a TCP tunnel using the OpenFlux tool. Explain step-by-step the build steps required to run the client on my desktop computer and how to configure SOCKS5 proxy settings in the browser. Additionally, explain with technical details why it is necessary to block RST packets using iptables when setting up an exit node on a Linux server, and the impact of this process on network security.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/openflux/
