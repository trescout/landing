# Editable composition with AI in music production

YuE is a music generation system equipped with capabilities such as symbolic planning and zero-shot cover generation. This AI model, which automates music editing processes, allows you to manage complex compositions with agentic workflows.

- ★ 12,774
- Python
- GitHub Trending · 2026-09-13

## Updates

- **October 27, 2026:** Stars 11,751 → 12,774, latest release yue2-v0.1.6 (September 9, 2026).
- **October 12, 2026:** Stars 10,749 → 11,751, latest release yue2-v0.1.6 (September 9, 2026).
- **October 3, 2026:** Stars 9,749 → 10,749, latest release yue2-v0.1.6 (September 9, 2026).
- **September 19, 2026:** Stars 8,744 → 9,749, latest release yue2-v0.1.6 (September 9, 2026).

## What you get

- Generating melody and chord plans with lyrics and style input
- Ability to edit music notes before converting them into audio files
- Reinterpreting and arranging existing songs in different styles

## Installation

**Downloading and installing the project**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```

## Running it

**Creating songs with edited notes**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a song using YuE2. Please prepare an editable melody and chord plan based on the lyrics and the music style I want. Then, use this plan to produce a full song recording including vocals and instrumental accompaniment. If I have a notation file, allow me to make edits using this file.

Repository: https://github.com/multimodal-art-projection/YuE. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Zero-shot](https://trescout.com/en/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for musicians and content creators who want to plan their musical compositions with the help of artificial intelligence, make changes to notes, and produce original songs.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/multimodal-art-projection/YuE)
- [Read in Turkish →](https://trescout.com/discover/yue/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-09-13: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/yue/
