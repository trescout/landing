# Lightweight and open source strategy game

Unciv is an open source, minimalist and cross-platform desktop and Android adaptation of Civilization V. Developed with Kotlin and LibGDX infrastructure, the project offers original 4X strategy mechanics with zero hardware load and high mod support.

- ★ 11,458
- Kotlin
- GitHub Trending · 2026-06-18

## Updates

- **October 18, 2026:** Stars 11,452 → 11,458, latest release 4.22.11-patch1 (October 17, 2026).
- **October 17, 2026:** Stars 11,433 → 11,452, latest release 4.22.11 (October 16, 2026).
- **October 13, 2026:** Stars 11,429 → 11,433, latest release 4.22.10 (October 13, 2026).
- **October 12, 2026:** Stars 11,403 → 11,429, latest release 4.22.9 (October 12, 2026).

## What you get

- Low hardware and battery-friendly architecture: It works with zero heating even on the most basic mobile devices by using 2D vector and pixel graphics instead of heavy 3D rendering engines.
- Original Civilization V mechanics: City planning, technology tree, social policies, diplomacy and tactical hex combat system are fully preserved.
- Cross-platform save and multiplayer support: You can directly move save files between desktop and Android or play email/server-based round-robin multiplayer matches.
- Community-driven rich mod ecosystem: New civilizations, units, fantasy scenarios and graphic themes can be installed and activated with a single click from the in-game interface.
- Completely free and ad-free experience: Distributed under MPL-2.0 license; contains no in-app purchases, advertising, tracking or data collection.

## How to get started and installation options

To play the Unciv project on your device, you can choose the distribution channel suitable for your platform. On the mobile side, Android users can install via the Google Play Store or the privacy-focused F-Droid repository. On the desktop side, direct MSI or portable ZIP files for Windows, Flatpak package or itch.io distributions for Linux can be preferred.

- [Google Play Store Sayfası →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [F-Droid Açık Kaynak Deposu →](https://f-droid.org/packages/com.unciv.app/)
- [itch.io Masaüstü Sürümleri →](https://yairm210.itch.io/unciv)

## Technical architecture and working principle

- State-driven game engine: Every hex tile, unit, city, and diplomatic relationship on the game board is stored as pure JSON objects. This structure keeps log file sizes to only a few hundred kilobytes.
- Declarative modding engine: Civilization features, technology trees and building costs are defined via JSON files without touching the source code. In this way, mod developers do not need an external compiler.
- Deterministic round calculation: AI moves and battle results are calculated with predictable algorithms. This prevents synchronization breaks in asynchronous multiplayer games.
- Multi-platform compilation: Thanks to LibGDX, a single Kotlin codebase is packaged with native performance for desktop (JVM) and mobile (Android runtime).

## Gameplay strategies and 4X dynamics

- Map exploration in the first rounds: Distribute your warrior and scout units around the map early to collect ancient artifacts, make first contact with city-states and earn gold income.
- Happiness and food balance: When establishing new cities, be careful to be within range of luxury resources. When your happiness rate drops to negative, population growth and production slow down significantly.
- Technology roadmap: Focus on your civilization's strengths rather than random research; Follow the paths of blacksmithing and gunpowder for military victory, philosophy and education for cultural victory.
- Using terrain advantages: Repel large armies with a small number of units by creating riverside defense, hill advantage and narrow passes.

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to prepare a valid JSON mod structure for the game Unciv. Can you create a sample Unciv mod template that includes a special cavalry unit and a special library building that gives a bonus to science and culture production as a leader ability? Can you explain step by step which JSON files I should save in which folder structure and how I can test this from the in-game Mod Manager interface?

Repository: https://github.com/yairm210/Unciv. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Frequently asked questions

- How similar is Unciv to Civilization V? Game mechanics, unit statistics, technology tree and victory conditions are largely compatible with the Civilization V Gods and Kings and Brave New World add-ons. The difference is basically the use of plain 2D visual design instead of 3D graphics.
- Is an internet connection required to play? No. Unciv can be played completely offline. No network connection is required to play against AI opponents in single-player mode. Only mod downloads and multiplayer matches require a connection.
- How to install Unciv mods? By going to the Mods tab in the main menu, you can list hundreds of mods uploaded by the community and download them to your device with a single click. You can also install directly by adding a link to any mod repository on GitHub.
- Can recording files be transferred between desktop and phone? Yes. You can copy the save file to the clipboard from the in-game recording menu, send it to your other device via e-mail or message in text format and continue where you left off with the load from the clipboard option there.

## Related dictionary terms

- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For gamers and independent modders who want to experience classic 4X strategy games on a lightweight, ad-free and open source infrastructure.
- **License:** MPL-2.0 (Mozilla Public License 2.0)
- **Game Engine:** LibGDX (Kotlin-based cross-platform)
- **Platforms:** Android, Windows, Linux, macOS

## Links

- [GitHub repository →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-18: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/unciv/
