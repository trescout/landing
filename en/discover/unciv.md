# Lightweight and open source strategy game

Unciv is an open source, minimalist and cross-platform desktop and Android adaptation of Civilization V. Developed with Kotlin and LibGDX infrastructure, the project offers original 4X strategy mechanics with zero hardware load and high mod support.

- ★ 11,379
- Kotlin
- GitHub Trending · 2026-06-18

## What you get
- Low hardware and battery-friendly architecture: It works with zero heating even on the most basic mobile devices by using 2D vector and pixel graphics instead of heavy 3D rendering engines.
- Original Civilization V mechanics: City planning, technology tree, social policies, diplomacy and tactical hex combat system are fully preserved.
- Cross-platform save and multiplayer support: You can directly move save files between desktop and Android or play email/server-based round-robin multiplayer matches.
- Community-driven rich mod ecosystem: New civilizations, units, fantasy scenarios and graphic themes can be installed and activated with a single click from the in-game interface.
- Completely free and ad-free experience: Distributed under MPL-2.0 license; contains no in-app purchases, advertising, tracking or data collection.

## How to get started and installation options
- Google Play Store Page →
- F-Droid Open Source Repository →
- itch.io Desktop Versions →

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
I want to prepare a valid JSON mod structure for the game Unciv. Can you create a sample Unciv mod template that includes a special cavalry unit and a special library building that gives a bonus to science and culture production as a leader ability? Can you explain step by step which JSON files I should save in which folder structure and how I can test this from the in-game Mod Manager interface?

## Frequently asked questions
- How similar is Unciv to Civilization V? Game mechanics, unit statistics, technology tree and victory conditions are largely compatible with the Civilization V Gods and Kings and Brave New World add-ons. The difference is basically the use of plain 2D visual design instead of 3D graphics.
- Is an internet connection required to play? No. Unciv can be played completely offline. No network connection is required to play against AI opponents in single-player mode. Only mod downloads and multiplayer matches require a connection.
- How to install Unciv mods? By going to the Mods tab in the main menu, you can list hundreds of mods uploaded by the community and download them to your device with a single click. You can also install directly by adding a link to any mod repository on GitHub.
- Can recording files be transferred between desktop and phone? Yes. You can copy the save file to the clipboard from the in-game recording menu, send it to your other device via e-mail or message in text format and continue where you left off with the load from the clipboard option there.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/unciv/
