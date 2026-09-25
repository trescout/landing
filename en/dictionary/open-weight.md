# What is Open Weight?

> Publicly Accessible Model Weights

**Category:** AI  
**Last updated:** 2026-09-22

Open weight refers to AI foundation models whose trained parameter weights are publicly downloadable, allowing anyone to run, quantize, and fine-tune the model on private hardware.

## Definition and Etymology
In contrast to closed API providers that only expose a pay-per-token web endpoint, open-weight models allow developers to download raw neural network tensors. This enables complete control over deployment infrastructure, zero data leakage, and community-driven quantization.

## Everyday Context and Practical Usage
- **Edge AI Execution:** Running quantized models on laptops, workstations, or embedded devices with zero network connectivity.
- **Enterprise Data Privacy:** Guaranteeing that sensitive customer records remain inside internal firewalls during inference.
- **Cost Optimization:** Eliminating recurring API subscription fees by amortizing hardware costs over millions of tokens.

## Technical Depth and Architecture
Architectural Anatomy of Open Weights:- **Tensor Formats:** Distributed as Safetensors or GGUF files preserving precision in FP16, BF16, or 4-bit/8-bit integer formats.
- **Local Inference Engines:** Executed through high-throughput serving runtimes such as vLLM, Ollama, llama.cpp, and TGI.
- **Parameter-Efficient Fine-Tuning (PEFT):** Modifying model behavior using LoRA (Low-Rank Adaptation) adapters without retraining base weights.

## Commonly Confused With
Often conflated with full open-source AI. Full open source requires sharing raw training code and source datasets; open weight primarily provides the final pre-trained numerical parameters, sometimes accompanied by custom commercial usage licenses.

## Cross-Disciplinary Perspectives
- **Bakery:** Buying pre-mixed artisan flour and baking it in your own oven vs buying a factory-sealed loaf of bread.
- **Software:** Downloading an executable binary vs accessing a cloud SaaS website.
- **Music:** Having the master recording tracks to remix at home vs streaming a song from an online platform.

## Analogy
It is like sharing the ingredients and cooking instructions so anyone can prepare and customize the meal in their own home kitchen.

## Frequently Asked Questions

**What can you do with open weights?**  
You can host models on your own servers, convert them to quantized formats (GGUF), create LoRA fine-tunes, and run them offline.

**How do open-weight models differ from closed APIs?**  
Closed APIs charge per token and keep models hosted remotely; open weights let you run inference on your own hardware with no external oversight.

**What hardware is required to run open-weight models?**  
A 7B or 8B parameter model quantized to 4-bit can run smoothly on consumer GPUs or laptops with 8 GB to 16 GB of unified memory.

**Are open-weight models permitted for commercial applications?**  
Most modern open-weight models (like Llama, Mistral, and Qwen) permit commercial deployment, subject to license thresholds.

## Related terms
- [Open Source AI](/en/dictionary/open-source-ai/)
- [Foundation Model](/en/dictionary/foundation-model/)
- [SLM](/en/dictionary/slm/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/open-weight/
