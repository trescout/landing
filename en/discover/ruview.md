# Wireless Sensing with WiFi Signals

RuView is a sensing platform that uses WiFi Channel State Information (CSI) to study environmental changes. It can run with ESP32 or research NIC hardware, while simulated data is available for evaluation without hardware.

- ★ 91,805
- GitHub Trending · 2026-05-30

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
- Prepare your environment with the Docker or source path in the official installation guides.
- If you have no hardware, start by examining the simulated-data evaluation path.
- Run the deterministic reference-signal check described in the build guide with `./verify`.
- Choose the RSSI-only or full-CSI path according to your hardware.

## Safe start

## First task prompt
How can I evaluate a simple motion-detection scenario from WiFi CSI data using simulated data?

## Related dictionary terms

## Links
- GitHub repository →
- Official RuView GitHub repository →
- RuView user guide →
- RuView build guide →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ruview/
