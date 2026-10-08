# Open source phased array radar

PLFM RADAR is an open-source phased array radar system operating at a 10.5 GHz (X-band) frequency, featuring electronic beam steering and FPGA-based digital signal processing capabilities. It detects and tracks air and ground targets with high precision without using any mechanically moving parts.

- ★ 26,713
- C++
- GitHub Trending · 2026-08-18

## Updates

- **October 6, 2026:** Stars 25,440 → 26,713, latest release v2.0.2-p0-audit (April 20, 2026).
- **September 27, 2026:** Stars 24,168 → 25,440, latest release v2.0.2-p0-audit (April 20, 2026).
- **August 18, 2026:** Stars 24,163 → 24,168, latest release v2.0.2-p0-audit (April 20, 2026).

## What you get

- Electronic beam steering: Scanning a 90-degree sector within milliseconds using phase shifters, without the need for mechanical motors or rotating antennas.
- Dual-range operating mode: 3 km short-range (UAV/drone detection) and 20 km long-range (perimeter surveillance and aircraft tracking) operational capability.
- FPGA-based real-time signal processing: Hardware-level processing of raw radar echoes on FPGAs using high-speed FFT and CFAR algorithms.
- Low-cost accessible hardware: Reducing the cost of commercial and military radars from hundreds of thousands of dollars to under a thousand dollars using open-source PCB designs.
- Python and SDR integration: Live monitoring of digital radar data via open-source SDR hardware and a Python interface.

## Hardware components and radar architecture

- 10.5 GHz X-Band microstrip antenna array: Multiple patch antenna elements designed on low-loss Rogers/FR4 substrates.
- Digitally controlled phase shifters: RF integrated circuits that steer the beam in space by delaying the signal phase of each antenna element with a precision of 5.6 degrees.
- FMCW frequency synthesizer: A high-stability local oscillator (VCO/PLL) that generates linear frequency-modulated continuous waves.

## Signal processing and control software

- Range-Doppler FFT (2D FFT): Calculating the target's distance and radial velocity simultaneously by applying Range FFT followed by Doppler FFT to the incoming signal.
- CFAR (Constant False Alarm Rate) detector: Distinguishing real moving targets from background noise and ground clutter using a dynamic threshold.
- Python GUI and PPI display: Visualizing target tracks on a live map using a traditional circular radar display (PPI).

## Technical operating principle: FMCW and phased array

- Distance measurement via frequency difference: The beat frequency is obtained by mixing the transmitted chirp signal with the signal reflected from the target. This frequency is directly proportional to the distance.
- Beamforming with constructive interference: By applying a specific phase delay to each antenna element in the array, the signal is made to interfere constructively in the desired direction and destructively in other directions.

## Use cases and field tests

- Low-altitude UAV and drone defense: Detecting small unmanned aerial vehicles in foggy or nighttime conditions where optical cameras are insufficient.
- Critical facility perimeter security: Monitoring unauthorized human or vehicle approaches within a 3 km radius at airports, data centers, and industrial sites.
- Meteorological and atmospheric research: Analyzing cloud movements and precipitation intensity on a local scale using micro-Doppler methods.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I would like to examine the 10.5 GHz phased array hardware schematics and FPGA signal processing blocks of the PLFM RADAR project. Could you prepare a simulation Python script that explains FMCW chirp signal generation, Range-Doppler 2D FFT calculation, and data transmission to a Python-based PPI radar display? Could you show the distance and velocity detection algorithm for an artificial target step-by-step?

## Frequently asked questions

- Is it possible to build the system at home or in a laboratory? Yes. All PCB schematics, Gerber production files, and FPGA Verilog/VHDL codes for the project are available as open source in the GitHub repository. Boards can be ordered from standard PCB manufacturers and soldered in a laboratory environment.
- What is the advantage of electronic beam steering over mechanical radars? While mechanical radars rotate at 1-2 turns per second, phased array radars can change the direction of the beam within microseconds. There are no mechanical parts subject to wear, and they can lock onto multiple targets instantaneously.
- Is a special radio frequency license required to operate it? The 10.5 GHz band is subject to amateur radio or industrial/scientific (ISM) frequency allocations in many countries. While in-lab testing at low output power is permitted, local regulations must be followed for long-range outdoor transmissions.
- Which FPGA development boards is it compatible with? Xilinx Zynq-7000 series or modern AMD UltraScale+ RFSoC boards are directly supported; high-speed ADC/DAC interfaces are connected via the FMC connector.

## Related dictionary terms

- [Patch](https://trescout.com/en/dictionary/patch/)
- [GUI](https://trescout.com/en/dictionary/gui/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Radar researchers, defense industry engineers, drone developers, and RF/SDR enthusiasts.
- **License:** Açık kaynak donanım ve yazılım lisansı
- **Frequency Band:** 10.5 GHz (X-Band) FMCW
- **Target Range:** 3 km (Drone/Tactical) - 20 km (Wide area surveillance)

## Links

- [GitHub repository →](https://github.com/NawfalMotii79/PLFM_RADAR)
- [Read in Turkish →](https://trescout.com/discover/plfm-radar/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-18: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/plfm-radar/
