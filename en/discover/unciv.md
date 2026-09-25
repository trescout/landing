# Lightweight and open source strategy game

Unciv is an open-source, minimalist, and cross-platform desktop and Android remake of Civilization V. Developed using Kotlin and LibGDX, the project delivers original 4X strategy mechanics with zero hardware overhead and extensive mod support.

- ★ 11,285
- Kotlin
- GitHub Trending · 2026-06-18

## Updates
- September 18, 2026: Stars 11,276 → 11,285, latest release 4.22.1 (September 17, 2026).
- September 15, 2026: Stars 11,257 → 11,276, latest release 4.22.0 (September 14, 2026).
- September 10, 2026: Stars 11,241 → 11,257, latest release 4.21.19 (September 9, 2026).
- September 8, 2026: Stars 11,223 → 11,241, latest release 4.21.18 (September 7, 2026).

## What you get
- Low hardware and battery-friendly architecture: Uses 2D vector and pixel graphics instead of heavy 3D rendering engines to run smoothly without device overheating.
- Original Civilization V mechanics: Faithfully preserves city planning, technology tree, social policies, diplomacy, and tactical hexagonal combat.
- Cross-platform save and multiplayer: Easily transfer saves between Android and desktop, or compete in turn-based multiplayer matches.
- Community-driven mod ecosystem: Install civilizations, units, scenarios, and visual skins with a single click in the game menu.
- Completely free and ad-free experience: Distributed under MPL-2.0 with zero in-app purchases, ads, tracking, or telemetry.

## Getting started and installation options

Unciv is available across multiple platforms. Android users can install via Google Play Store or privacy-focused F-Droid. Desktop players on Windows, Linux, and macOS can choose standalone ZIP files, Flatpak, or itch.io builds.
- [Google Play Store Page →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [F-Droid Open Source Repository →](https://f-droid.org/packages/com.unciv.app/)
- [itch.io Desktop Releases →](https://yairm210.itch.io/unciv)

## Technical architecture and inner workings

Unciv is built on LibGDX and Kotlin, abstracting graphical complexity to focus on deterministic, lightweight game state logic:
- State-driven game engine: Hexagonal tiles, units, cities, and diplomacy are serialized as pure JSON objects, keeping save files under a few hundred kilobytes.
- Declarative modding engine: Civilization stats, tech trees, and building rules are defined via JSON without recompiling source code.
- Deterministic turn resolution: AI decisions and combat outcomes are computed predictably to prevent desyncs in asynchronous multiplayer.
- Cross-platform compilation: Single codebase targets both JVM desktop and Android runtime with native performance.

## Gameplay strategies and 4X dynamics

Unciv delivers the core 4X loop: eXplore, eXpand, eXploit, and eXterminate:
- Early map exploration: Scout ancient ruins and establish early contact with city-states for vital gold bonuses.
- Happiness and food balance: Settle near luxury resources to prevent growth stagnation caused by negative happiness.
- Strategic tech roadmaps: Align scientific research with your civilization strengths rather than picking random technologies.
- Terrain-based warfare: Defend behind rivers and on hills to defeat superior armies using tactical positioning.

## If you do not code
🤖 If you do not code
I want to create a valid JSON mod for Unciv. Can you generate an example mod template that includes a leader with bonuses to science and culture, a custom mounted unit, and a unique library building? Please explain the required folder structure and how to test it via the in-game Mod Manager.

- **Who it is for:** Players and independent modders who want a lightweight, ad-free, open-source 4X strategy experience.
- **License:** MPL-2.0 (Mozilla Public License 2.0)
- **Game Engine:** LibGDX (Kotlin-based cross-platform)
- **Platforms:** Android, Windows, Linux, macOS

## Frequently asked questions
- How similar is Unciv to Civilization V? Mechanics, unit stats, tech trees, and victory conditions mirror Civilization V Gods & Kings and Brave New World expansions, using clean 2D graphics instead of 3D.
- Does playing require an internet connection? No. Unciv is fully playable offline against AI opponents. Internet is only required for downloading mods or multiplayer matches.
- How are mods installed? Browse hundreds of community mods directly in the in-game Mods menu and download with one click, or import custom repository URLs.
- Can save files be transferred between desktop and mobile? Yes. Copy the save string to clipboard from the save menu and import it on any device via clipboard.

## Links
- [GitHub →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

## Related dictionary terms
Open Source Offline

---
Source: TreScout Discover · https://trescout.com/en/discover/unciv/
