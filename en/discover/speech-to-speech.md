# Open source native voice agents

The speech-to-speech library developed by Hugging Face allows creating local voice agents using open source models. This Python-based tool allows developers to build real-time voice interaction systems that run on the device.

- ★ 13,549
- Python
- GitHub Trending · 2026-07-29

## Updates

- **October 25, 2026:** Stars 13,072 → 13,549, latest release v1.1.0 (October 24, 2026).
- **September 7, 2026:** Stars 12,310 → 13,072, latest release v1.0.0 (September 6, 2026).
- **August 12, 2026:** Stars 11,283 → 12,310, latest release v0.2.12 (August 5, 2026).
- **August 6, 2026:** Stars 10,774 → 11,283, latest release v0.2.12 (August 5, 2026).

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

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to setup my own local voice agent using this tool. What are the basic steps I need to follow to create a low latency audio pipeline using VAD, STT, LLM and TTS components? With what command can I stand up the server and connect with an OpenAI Realtime compatible client?

Repository: https://github.com/huggingface/speech-to-speech. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Voice Agents](https://trescout.com/en/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/en/dictionary/speech-to-speech/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to develop native and customizable voice interaction systems on their own hardware.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/huggingface/speech-to-speech)
- [Read in Turkish →](https://trescout.com/discover/speech-to-speech/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-29: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/speech-to-speech/
