# Editable composition with AI in music production

YuE is a music generation system equipped with capabilities such as symbolic planning and zero-shot cover generation. This AI model, which automates music editing processes, allows you to manage complex compositions with agentic workflows.

- ★ 7,463
- Python
- GitHub Trending · 2026-09-13

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
I want to create a song using YuE2. Please prepare an editable melody and chord plan based on the lyrics and the music style I want. Then, use this plan to produce a full song recording including vocals and instrumental accompaniment. If I have a notation file, allow me to make edits using this file.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/yue/
