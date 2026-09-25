# Open-source phased array radar system

PLFM RADAR is an open-source phased array radar system operating at 10.5 GHz (X-band), featuring electronic beam steering and FPGA-based digital signal processing. It detects and tracks aerial and ground targets with high precision without relying on mechanical rotating parts.

- ★ 24,168
- C++
- GitHub Trending · 2026-08-18

## Updates
- August 18, 2026: Stars 24,168, stable release v2.0.2-p0-audit (FPGA signal filtering and range calibration update).

## What you get
- Electronic beam steering: Sweeps a 90-degree sector in milliseconds using digital phase shifters with zero moving mechanical parts.
- Dual range operational modes: 3 km tactical mode for anti-drone surveillance and 20 km long-range mode for wide perimeter monitoring.
- FPGA-powered real-time DSP: Hardware-accelerated FFT and CFAR target detection executed directly on FPGA silicon.
- Accessible low-cost hardware: Lowers the multi-hundred-thousand-dollar barrier of commercial military radars to under one thousand dollars.
- Python and SDR integration: Stream and visualize live target tracking data via open-source SDRs and clean Python PPI interfaces.

## Hardware components and radar architecture

The PLFM RADAR architecture is divided into RF front-end, planar antenna array, and digital processing layers:
- 10.5 GHz X-Band microstrip patch array: High-frequency antenna array fabricated on low-loss Rogers/FR4 substrate layers.
- Digitally controlled phase shifters: Delays the signal phase for each antenna element in 5.6-degree increments to steer the RF wavefront in space.
- FMCW frequency synthesizer: Highly stable local oscillator (VCO/PLL) producing linear frequency-modulated continuous waves.

## Signal processing and control software

Raw echoes are filtered at the hardware level to extract target distance, radial velocity, and azimuth:
- Range-Doppler 2D FFT: Computes range FFT followed by Doppler FFT to simultaneously resolve target distance and velocity.
- CFAR (Constant False Alarm Rate) detector: Dynamically adapts thresholding to isolate moving targets from ground clutter and thermal noise.
- Python GUI and PPI display: Renders real-time target vectors on a classic Plan Position Indicator (PPI) radar display over map layers.

## Technical working principle: FMCW and phased array

PLFM RADAR utilizes frequency-modulated continuous wave (FMCW) architecture rather than conventional high-power pulsed transmissions:
- Range extraction via beat frequency: Mixing the transmitted chirp with the received echo yields an intermediate beat frequency proportional to target distance.
- Beamforming via constructive interference: Controlling the relative phase across antenna elements forces constructive wave interference in the targeted azimuth.

## Use cases and field scenarios

Open-source phased array radar technology unlocks extensive experimental and commercial applications:
- Low-altitude anti-drone defense: Detects small rogue UAVs in foggy or nighttime conditions where optical sensors fail.
- Critical infrastructure perimeter security: Monitors unauthorized vehicle or human intrusions across 3 km perimeters around airports and datacenters.
- Meteorological and atmospheric sensing: Measures localized wind velocities, cloud formations, and micro-Doppler precipitation shifts.

## If you do not code
🤖 If you do not code
I want to explore the 10.5 GHz phased array hardware schematics and FPGA DSP blocks of the PLFM RADAR project. Could you write a Python simulation script that generates an FMCW chirp, applies Range-Doppler 2D FFT processing, and extracts distance and velocity for a simulated aerial drone target?

- **Who it is for:** Radar researchers, defense engineers, anti-drone developers, and RF/SDR enthusiasts.
- **License:** Open-source hardware and software license
- **Frequency Band:** 10.5 GHz (X-Band) FMCW
- **Operational Range:** 3 km (tactical drone tracking) to 20 km (wide area surveillance)

## Frequently asked questions
- Can this system be built in a lab or workshop? Yes. All PCB schematics, Gerber files, and FPGA Verilog/VHDL codebases are publicly available in the GitHub repository. Boards can be fabricated at standard PCB houses and hand-assembled.
- What is the primary advantage of phased arrays over rotating antennas? Phased arrays steer their beam in microseconds electronically rather than seconds. They feature zero mechanical friction, higher reliability, and instant multi-target interleaving.
- Are special RF transmission licenses required? The 10.5 GHz band is allocated for amateur radio and ISM in many jurisdictions. Low-power laboratory bench testing is generally unrestricted, but outdoor transmissions must comply with local RF regulations.
- Which FPGA development boards are supported? Xilinx Zynq-7000 and AMD UltraScale+ RFSoC platforms are directly supported via FMC connectors interfacing with the high-speed ADC/DAC boards.

## Links
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## Related dictionary terms
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/en/discover/plfm-radar/
