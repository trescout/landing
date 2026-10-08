# Artificial intelligence models for physical systems

Developed by NVIDIA, Cosmos is an open platform that provides world models, datasets and tools for physical systems such as robots and autonomous vehicles. It provides an infrastructure that makes it easier for developers to create physical AI applications.

- ★ 11,343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Updates

- **August 2, 2026:** Stars 9,173 → 11,343, latest release Cosmos3 (June 1, 2026).

## What you get

- It provides world models, datasets, and tools for physical AI applications.
- It can process and produce text, visual, audio and action sequences in a unified architecture.
- Provides forecasting, planning and simulation capabilities for robotic and autonomous systems.

## Installation

**Installation with vLLM-Omni**

```
uv pip install --torch-backend=cu130 \
  "vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```

## Running it

**Video Production**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
  --form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
  --form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
  -o cosmos3_t2v.mp4
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to develop physical artificial intelligence applications using the NVIDIA Cosmos platform. Explain in technical detail the capabilities offered by the Cosmos 3 model family, especially the differences in the use of 'Reasoner' and 'Generator' surfaces, and how these models can be configured in scenarios such as mission planning or world simulation in robotic and autonomous systems. Also, summarize the process of working with the 'uv' tool and the 'vllm-omni' library during the installation phase, step by step, taking into account the CUDA driver requirements.

## Related dictionary terms

- [Physical AI](https://trescout.com/en/dictionary/physical-ai/)
- [Jupyter Notebooks](https://trescout.com/en/dictionary/jupyter-notebooks/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** For developers working on physical AI, robotic systems, and autonomous vehicles who are interested in world models and multimodal data processing.

## Links

- [GitHub repository →](https://github.com/NVIDIA/cosmos)
- [Read in Turkish →](https://trescout.com/discover/cosmos/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-05: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/cosmos/
