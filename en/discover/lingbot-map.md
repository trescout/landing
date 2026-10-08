# Create three-dimensional scenes from streaming data

Lingbot-map is a feed-forward 3D foundation model designed to reconstruct scenes from streaming data. The project optimizes visualization processes by processing complex environmental data, thanks to its architecture developed in Python language.

- ★ 17,060
- Python
- GitHub Trending · 2026-06-29

## Updates

- **September 16, 2026:** Stars 16,054 → 17,060.
- **August 2, 2026:** Stars 8,439 → 16,054.

## What you get

- Stable 3D reconstruction of long video sequences
- Low latency streaming inference support
- Artificial intelligence architecture that can process complex environmental data

## Installation

**Environment preparation and basic setup**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Installing the required libraries**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

## Running it

**Starting the sample scene**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to create a 3D scene from streaming data using LingBot-Map. I completed the installation and my model file is ready. How can I launch the visualization interface in my local browser using the command required to run the Courthouse instance?

## Related dictionary terms

- [Foundation Model](https://trescout.com/en/dictionary/foundation-model/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for researchers and developers interested in 3D computer vision and streaming data processing.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/Robbyant/lingbot-map)
- [Read in Turkish →](https://trescout.com/discover/lingbot-map/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-29: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/lingbot-map/
