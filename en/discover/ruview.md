# Wireless Sensing with WiFi Signals

RuView is a sensing platform that uses WiFi Channel State Information (CSI) to study environmental changes. It can run with ESP32 or research NIC hardware, while simulated data is available for evaluation without hardware.

- ★ 96,773
- GitHub Trending · 2026-05-30

## Updates

- **October 7, 2026:** Stars 96,651 → 96,773, latest release v3067 (October 6, 2026).
- **October 6, 2026:** Stars 96,464 → 96,651, latest release v3060 (October 5, 2026).
- **October 5, 2026:** Stars 95,926 → 96,464, latest release v3037 (October 4, 2026).
- **October 2, 2026:** Stars 95,751 → 95,926, latest release v2975 (October 2, 2026).

## Installation

**Pull the Docker image**

```
docker pull ruvnet/wifi-densepose:latest
```

**Clone the source code**

```
git clone https://github.com/ruvnet/RuView.git
```

## Running it

**Demo server without hardware**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Deterministic verification**

```
./verify
```

## What does this tool do?

RuView is an MIT-licensed platform for sensing experiments with WiFi Channel State Information. It can be installed with Docker or from source, and it can be evaluated with simulated data without hardware. Capabilities depend on the hardware mode: laptop RSSI-only sensing is for coarse presence and motion, while advanced sensing requires full CSI hardware.

## Who it is for

Researchers and developers who want to experiment with presence, motion or environmental sensing from WiFi signals.

## What not to expect

Medical monitoring claims or pose estimation expectations from a standard laptop in RSSI-only mode.

## Highlights

- Offers CSI-based sensing paths with ESP32 and research NIC hardware.
- Can be evaluated with simulated data without hardware.
- Documents a deterministic reference-signal check with `./verify`.
- Separates the capabilities of laptop RSSI-only mode from full CSI hardware.

## First-use flow

1. Prepare your environment with the Docker or source path in the official installation guides.
2. If you have no hardware, start by examining the simulated-data evaluation path.
3. Run the deterministic reference-signal check described in the build guide with `./verify`.
4. Choose the RSSI-only or full-CSI path according to your hardware.

## Safe start

Laptop RSSI-only mode is intended for coarse presence and motion detection and does not provide pose support. Pose and some benchmark capabilities are documented as experimental, first-cut or limited; evaluate results according to the hardware mode you use.

## First task prompt

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

How can I evaluate a simple motion-detection scenario from WiFi CSI data using simulated data?

## Related dictionary terms

- [WiFi](https://trescout.com/en/dictionary/wifi/)
- [Benchmark](https://trescout.com/en/dictionary/benchmark/)

## Links

- [GitHub repository →](https://github.com/ruvnet/RuView)
- [Official RuView GitHub repository →](https://github.com/ruvnet/RuView)
- [RuView user guide →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [RuView build guide →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)
- [Read in Turkish →](https://trescout.com/discover/ruview/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-05-30: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ruview/
