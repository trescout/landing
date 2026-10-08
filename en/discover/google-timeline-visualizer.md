# Turn your location history into motion video

Google Timeline Visualizer visualizes a year's worth of your travels with your Google Location History data.

- ★ 3,030
- Kotlin
- GitHub Trending · 2026-08-20

## Updates

- **October 5, 2026:** Stars 2,990 → 3,030, latest release v3.1.0 (October 5, 2026).
- **September 13, 2026:** Stars 2,980 → 2,990, latest release v3.0.18 (September 12, 2026).
- **September 9, 2026:** Stars 2,972 → 2,980, latest release v3.0.17 (September 9, 2026).
- **September 7, 2026:** Stars 2,969 → 2,972, latest release v3.0.16 (September 6, 2026).

## What you get

- Converts Google Maps history data to MP4 video
- Animates travel routes on the map
- Protects privacy by processing personal data on device

## Installation

**Install and run the necessary dependencies**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configure development tools**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a video showing my travels using the Timeline.json file I have. After installing the necessary dependencies in the Python environment, what command should I use to convert my 2025 data into a file named 'my_trip_2025.mp4' with 'steady' camera motion and 'balanced' compression settings?

## Related dictionary terms

- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for anyone who wants to visualize location history on Google Maps and save travel memories in video format.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/mahlernim/google-timeline-visualizer)
- [Read in Turkish →](https://trescout.com/discover/google-timeline-visualizer/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-20: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/google-timeline-visualizer/
