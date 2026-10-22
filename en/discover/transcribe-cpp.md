# Fast speech conversion on local systems

Transcribe.cpp is a speech-to-text inference library developed in C++ that supports more than 16 model families. Using the ggml infrastructure, this tool enables different audio processing models to run efficiently on local systems.

- ★ 2,003
- C++
- GitHub Trending · 2026-07-21

## Updates

- **October 12, 2026:** Stars 1,982 → 2,003, latest release v0.4.0 (October 12, 2026).
- **October 4, 2026:** Stars 1,981 → 1,982, latest release v0.3.1 (October 4, 2026).
- **October 3, 2026:** Stars 1,963 → 1,981, latest release v0.3.0 (October 3, 2026).
- **September 27, 2026:** Stars 1,865 → 1,963, latest release v0.2.4 (September 25, 2026).

## What you get

- Support for 16 different model families
- High performance on GPU and CPU
- Efficient inference with GGUF format

## Installation

**Vulkan supported Linux installation**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to convert a local audio file to text using the Transcribe.cpp tool. How can I process my 16 kHz mono WAV format audio file using the transcribe-cli tool compiled on my system and the GGUF format model file I downloaded? Please explain the command structure required for this process and the file paths I should pay attention to.

Repository: https://github.com/handy-computer/transcribe.cpp. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Speech-to-Text](https://trescout.com/en/dictionary/speech-to-text/)
- [GGUF](https://trescout.com/en/dictionary/gguf/)
- [Inference](https://trescout.com/en/dictionary/inference/)
- [CPU](https://trescout.com/en/dictionary/cpu/)
- [GPU](https://trescout.com/en/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to run privacy-focused and fast speech recognition systems on their own hardware.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/handy-computer/transcribe.cpp)
- [Read in Turkish →](https://trescout.com/discover/transcribe-cpp/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-21: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/transcribe-cpp/
