# Fast speech conversion on local systems

Transcribe.cpp is a speech-to-text inference library developed in C++ that supports more than 16 model families. Using the ggml infrastructure, this tool enables different audio processing models to run efficiently on local systems.

- ★ 1,673
- C++
- GitHub Trending · 2026-07-21

## Update
- August 2, 2026: Star 1,357 → 1,673, latest version v0.1.3 (July 12, 2026).

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
I want to convert a local audio file to text using the Transcribe.cpp tool. How can I process my 16 kHz mono WAV format audio file using the transcribe-cli tool compiled on my system and the GGUF format model file I downloaded? Please explain the command structure required for this process and the file paths I should pay attention to.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/transcribe-cpp/
