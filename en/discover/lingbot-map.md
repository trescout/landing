# Create three-dimensional scenes from streaming data

Lingbot-map is a feed-forward 3D foundation model designed to reconstruct scenes from streaming data. The project optimizes visualization processes by processing complex environmental data, thanks to its architecture developed in Python language.

- ★ 16,054
- Python
- GitHub Trending · 2026-06-29

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
I want to create a 3D scene from streaming data using LingBot-Map. I completed the installation and my model file is ready. How can I launch the visualization interface in my local browser using the command required to run the Courthouse instance?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/lingbot-map/
