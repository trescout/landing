# Run giant AI models with 4GB VRAM

AirLLM is a groundbreaking open-source library that runs massive 70-billion and 405-billion parameter large language models (LLMs) on standard consumer graphics cards with as little as 4 GB of video memory (VRAM), without requiring enterprise servers or costly GPU clusters.

- ★ 33,755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Updates
- September 6, 2026: Stars 33,307 → 33,755, latest release v4.0.0 (September 5, 2026).
- August 31, 2026: Stars 31,598 → 33,307, latest release v3.3.0 (August 28, 2026).
- August 19, 2026: Stars 30,796 → 31,598, latest release v3.2.0 (August 18, 2026).
- August 12, 2026: Stars 29,265 → 30,796, latest release v3.1.0 (July 29, 2026).

## What you get
- Run 70B models on 4GB VRAM: Execute heavyweight models like Llama 3 70B, Qwen, or DeepSeek on entry-level GTX 1650 or RTX 3050 graphics cards.
- 405B Llama 3.1 support: Run flagship 405-billion parameter models that typically require multi-hundred-thousand-dollar GPU clusters on personal 8GB VRAM rigs.
- Layer-wise execution: Streams transformer layers sequentially from disk into memory and computes them one by one, shattering the VRAM bottleneck.
- Up to 3x speedup with block compression: Reads model weights from NVMe SSDs in optimized blocks to accelerate disk-to-GPU data pipelines.
- Full precision without quantization degradation: Eliminates the strict requirement to compress to 4-bit, enabling full 16-bit (bfloat16) precision if desired.

## Installation

**With pip (PyPI)**

```
pip install airllm
```

## Technical architecture and working principle

Traditional LLM inference engines (such as vLLM, Ollama, or standard HuggingFace) require all model weights to reside in GPU video memory (VRAM) simultaneously. A 70B parameter model demands ~140 GB in 16-bit precision and at least 35-40 GB even when 4-bit quantized. AirLLM overturns this fundamental limitation:
- Sequential nature of transformer layers: A transformer network consists of roughly 80 sequential layers. Each layer receives the tensor output of the previous layer as input. Storing all layers in VRAM at the exact same instant is mathematically unnecessary.
- Sequential layer offloading: AirLLM loads only the active layer into VRAM (~1.5 GB). Once that layer's forward pass completes, memory is immediately released and the subsequent layer is loaded from disk.
- Speed vs. memory trade-off: This architecture is not tailored for real-time interactive chats producing dozens of tokens per second; it is an invaluable cost-saving engine for batch evaluation, data analysis, deep reasoning, translation, and synthetic data generation.
- Memory-mapped file streaming (mmap): Binds PyTorch tensors directly to NVMe SSD storage via mmap, maximizing disk throughput without consuming excessive system RAM.

## Python usage example

AirLLM features a clean Python API very similar to the standard HuggingFace AutoModel interface:

**Running a 70B model with Python**

```python
from airllm import AutoModel

# Initialize a 70B model with just 4GB VRAM
model = AutoModel.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")

input_text = ["Summarize the future of open source AI agents."]
input_tokens = model.tokenizer(input_text, return_tensors="pt", padding=True)

# Generate output (layers are executed sequentially)
generation_output = model.generate(
    input_tokens['input_ids'].cuda(),
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

output = model.tokenizer.decode(generation_output.sequences[0])
print(output)
```

## If you do not code
🤖 If you do not code
I want to run a 70-billion parameter model (such as meta-llama/Llama-3-70B-Instruct) on my local PC with 4GB VRAM using the AirLLM library. I ran pip install airllm. Can you provide the Python code to load the model, generate text output, and avoid memory errors? Please outline the disk space requirements and the step-by-step procedure.

- **Who it is for:** Researchers and developers with constrained GPU hardware wanting to test 70B and 405B models locally for evals and data extraction.
- **License:** Apache-2.0 (Permissive open source license)
- **Hardware Requirements:** Minimum 4 GB VRAM GPU and high-speed NVMe SSD storage
- **Ecosystem:** Python, PyTorch, and HuggingFace Transformers

## Frequently asked questions
- How fast is AirLLM when running models? Because AirLLM continuously moves layers between disk and GPU, generation speed is bound by NVMe SSD read speeds. On a Gen4 SSD, a 70B model yields about 1-3 tokens per second. While slow for real-time chat, it allows running giant models at zero additional hardware cost.
- How much free disk space is required? A 70B model in 16-bit float requires ~140 GB of disk space (or 35-40 GB in 4-bit). A 405B model requires at least 800 GB of free NVMe storage.
- Can I use original unquantized model weights? Yes. One of AirLLM's strongest advantages is lifting the quantization mandate. Because memory limits are addressed per layer, you can run original 16-bit weights with zero degradation in accuracy.
- Does AirLLM work on Apple Silicon Macs or CPU only? AirLLM is primarily optimized for CUDA (NVIDIA GPUs). Experimental CPU execution and Apple Silicon MPS support exist, but the highest efficiency is achieved with an NVIDIA GPU and NVMe SSD.

## Links
- [GitHub →](https://github.com/lyogavin/airllm)

## Related dictionary terms
VRAM LLM Large Language Models Transformer Open Source

---
Source: TreScout Discover · https://trescout.com/en/discover/airllm/
