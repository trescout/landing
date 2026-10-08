# Run giant AI models with 4GB VRAM

AirLLM is a groundbreaking open-source library that runs massive large language models (LLMs) with 70 billion and 405 billion parameters on standard consumer-grade graphics cards with only 4 GB of video memory (VRAM), without the need for enterprise servers or expensive GPU clusters.

- ★ 35,481
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## What you get
- Running 70B models with 4GB VRAM: The power to run high-parameter models like Llama 3 70B, Qwen, or DeepSeek even on entry-level GTX 1650 or RTX 3050 graphics cards.
- 405B Llama 3.1 support: The ability to run 405-billion parameter models, which require hundreds of thousands of dollars worth of GPU clusters in data centers, on personal computers with 8GB VRAM.
- Layer-wise Execution: Instead of fitting the entire model into VRAM, it overcomes the VRAM bottleneck by loading and processing layers sequentially from the disk into memory.
- Up to 3x speedup with block-based compression: accelerates data transfer from disk to GPU by reading model weights on the NVMe SSD in optimized blocks.
- Full precision without quantization quality loss: It enables inference even at the original 16-bit (bfloat16) precision if desired, without the necessity of compressing weights to 4-bit.

## Installation
**Using pip (PyPI)**

```
pip install airllm
```


## Technical architecture and working principle
- The sequential nature of Transformer layers: A Transformer network consists of 80 independent layers. Each layer takes the tensor output of the previous layer as input. It is not theoretically mandatory for the entire model to reside in memory.
- Sequential Offloading: AirLLM only loads a single layer currently being computed into the VRAM (approximately 1.5 GB). Once the forward pass calculation for that layer is complete, the memory is cleared and the next layer is fetched from the disk.
- Speed and memory trade-off: This architecture is not meant for interactive chats generating dozens of tokens per second; rather, it is an unparalleled cost-saving tool for batch data analysis, deep reasoning, translation, synthetic data generation, and model evaluation (evals) processes.
- Memory-mapped file reading (mmap): Connects PyTorch tensors directly to disk using the mmap method, utilizing NVMe SSD bandwidth directly without unnecessarily bloating system RAM.

## Example Python usage
AirLLM has an extremely simple Python syntax, very similar to the HuggingFace AutoModel API:

## If you don't write code
I want to run a 70 billion parameter model (for example, meta-llama/Llama-3-70B-Instruct) on my local graphics card with 4GB VRAM capacity using the AirLLM library. I used the pip install airllm command for installation. Could you explain the Python code required to load my model, get output with text input, and prevent out-of-memory errors? I know I need to make sure my disk space is sufficient in the process, could you detail the steps I need to follow?

## Frequently asked questions
- How fast is it to run a model with AirLLM? Since AirLLM continuously transfers layers between the disk and GPU, token generation speed depends directly on the read speed of your NVMe SSD. On a typical Gen4 SSD, a 70B model runs at a speed of 1-3 tokens per second. While this speed is slow for interactive chat, it is unique for running massive models locally with zero hardware cost.
- How much free disk space is required for AirLLM? A 70B parameter model requires approximately 140 GB of disk space in 16-bit float format. In 4-bit quantized versions, this space drops to around 35-40 GB. For the 405B model, at least 800 GB of free NVMe disk space should be allocated.
- Can I use the original model weights without quantization? Yes. One of the biggest advantages of AirLLM is that it eliminates the need for quantization. Since VRAM constraints are resolved on a layer-by-layer basis, you can run the original 16-bit weights without experiencing any loss in reasoning or accuracy.
- Does AirLLM run on Apple Silicon Macs or just CPU? AirLLM is primarily optimized for CUDA (NVIDIA GPU) acceleration. However, it also experimentally supports CPU execution and MPS (Apple Silicon Metal) layers. The highest throughput is achieved with a fast NVMe SSD and an NVIDIA graphics card.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/airllm/
