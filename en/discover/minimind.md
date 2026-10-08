# A 64M parameter language model trained from scratch in two hours

MiniMind provides tokenization, pre-training, supervised fine-tuning (SFT), LoRA, and DPO stages with clean PyTorch code for developers who want to understand the working principles of large language models (LLMs).

- ★ 62,670
- Python
- GitHub Trending · 2026-08-31

## Updates

- **September 27, 2026:** Stars 55,708 → 62,670, latest release v2 (October 21, 2025).

## What you get

- Training in 2 hours on consumer hardware: A compact architecture that can be trained from scratch in about 2 hours on a single NVIDIA RTX 3090/4090 graphics card.
- Full LLM training lifecycle: BPE tokenization, pretraining, supervised fine-tuning (SFT), LoRA adaptation, and DPO alignment pipeline.
- Minimalist and readable codebase: Transparent Transformer blocks written in pure PyTorch without complex third-party abstractions.
- MoE (Mixture of Experts) support: The ability to train and run 8x MoE architecture from scratch alongside dense models.
- An exceptional educational and pedagogical resource: An ideal guide for researchers seeking to experimentally grasp the inner workings of large language models.

## Installation

**Cloning the repository and installing dependencies**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

## Running it

**Initiating pre-training and testing model output**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```

## Technical architecture and working principle

- RoPE and SwiGLU Activations: Modern architectural standards with Rotary Position Embeddings and SwiGLU activation functions.
- Stable Gradient Flow with RMSNorm: Using the RMSNorm layer normalization instead of the traditional LayerNorm, which is faster and more stable.
- Flash Attention Integration: Flash Attention v2 optimization to quickly compute large attention matrices in GPU memory.

## Training stages: Pre-training, SFT, and DPO

- Phase 1 - Pre-training (1-pretrain.py): It learns grammar and general world knowledge on raw texts with the logic of predicting the next token.
- Phase 2 - Supervised Fine-Tuning (2-sft.py): Transforms the model into an assistant that obeys user commands using question-answer and instruction datasets.
- Phase 3 - DPO Alignment (4-dpo.py): Directly optimizes the model based on user preferences using pairs of good and bad responses.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to train a 64M parameter language model from scratch with PyTorch using the MiniMind repository. Could you explain step-by-step how to prepare the tokenizer based on my own Turkish text dataset, how to run the 1-pretrain.py script, and then how to fine-tune it with LoRA?

## Frequently asked questions

- How much VRAM is required to train MiniMind? Depending on the batch size setting, the 64M parameter model can be comfortably trained within the 6GB to 12GB VRAM range; even an RTX 3060 or RTX 4060 is sufficient.
- Does it run on Apple Silicon (Mac M series)? Yes. Training and inference can also be performed on Mac computers with PyTorch MPS (Metal Performance Shaders) acceleration.
- Are the model's outputs sufficient for everyday conversation? 64M is a small model; it is optimized to demonstrate language structure, basic question-answering, and text-completion capabilities rather than complex logical reasoning.
- Which datasets come pre-loaded? The repository provides automated download commands for filtered open datasets for Chinese and English pre-training and SFT.

## Related dictionary terms

- [Tokenizer](https://trescout.com/en/dictionary/tokenizer/)
- [LoRA](https://trescout.com/en/dictionary/lora/)
- [VRAM](https://trescout.com/en/dictionary/vram/)
- [Attention](https://trescout.com/en/dictionary/attention/)
- [Transformer](https://trescout.com/en/dictionary/transformer/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)

- **Who it is for:** AI researchers, machine learning engineers, data scientists, and students.
- **License:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** PyTorch-Based Minimalist LLM Framework
- **Platforms:** Linux, macOS (Apple Silicon MPS), Windows

## Links

- [GitHub repository →](https://github.com/jingyaogong/minimind)
- [Read in Turkish →](https://trescout.com/discover/minimind/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/minimind/
