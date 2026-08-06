# Transcribe sounds with artificial intelligence

Developed by OpenAI, Whisper is a speech recognition model trained by large-scale weak supervision learning method. It offers high accuracy rates in converting and translating multilingual audio data into text.

- ★ 106,452
- Python
- GitHub Trending · 2026-06-07

## Update
- August 2, 2026: Star 101,952 → 106,452, last version v20250625 (June 26, 2025).

## What you get
- Convert audio files to text with high accuracy.
- Translating conversations from different languages ​​into English.
- Language identification and speech activity detection in audio content.

## Installation
**System dependencies**

```
sudo apt update && sudo apt install ffmpeg
```

**Additional installation requirement**

```
pip install setuptools-rust
```


## Running it
**Convert audio file to text**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Transcription in a specific language**

```
whisper japanese.wav --language Japanese
```


## If you don't write code
I want to convert my audio file into text using the Whisper tool. I made the necessary installations on my system. What is the basic command structure I need to type in the terminal to translate the content of my audio file into text, and how should I use the language specification parameter for audio files in different languages?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/whisper/
