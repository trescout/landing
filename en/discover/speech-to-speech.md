# Open source native voice agents

The speech-to-speech library developed by Hugging Face allows creating local voice agents using open source models. This Python-based tool allows developers to build real-time voice interaction systems that run on the device.

- ★ 12,310
- Python
- GitHub Trending · 2026-07-29

## Update
- August 12, 2026: Star 11,283 → 12,310, latest version v0.2.12 (August 5, 2026).
- 6 August 2026: Star 10,774 → 11,283, latest version v0.2.12 (5 August 2026).
- 4 August 2026: Star 10,402 → 10,774, latest version v0.2.11 (3 August 2026).
- August 2, 2026: Star 7,443 → 10,402, latest version v0.2.10 (June 11, 2026).

## What you get
- Low latency modular audio line
- OpenAI Realtime compatible WebSocket support
- Opportunity to work locally on different hardware

## Installation
**Basic setup**

```
pip install speech-to-speech
```

**Installation from source code**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```


## Running it
**Starting the server**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**Connecting with the client**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```


## If you don't write code
I want to setup my own local voice agent using this tool. What are the basic steps I need to follow to create a low latency audio pipeline using VAD, STT, LLM and TTS components? With what command can I stand up the server and connect with an OpenAI Realtime compatible client?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/speech-to-speech/
