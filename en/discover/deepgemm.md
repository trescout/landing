# Fast matrix computation for artificial intelligence

DeepGEMM, developed by DeepSeek, is an open-source basic linear algebra subprograms (BLAS) library that accelerates matrix multiplication operations on graphics processing units (GPUs). The software provides optimized kernels for artificial intelligence models requiring high-performance computing.

- ★ 8,528
- Cuda
- GitHub Trending · 2026-10-06

## Updates

- **October 6, 2026:** Stars 8,522 → 8,528, latest release v2.1.1.post3 (October 15, 2025).

## What you get

- It shortens the execution times of large language models by accelerating matrix multiplications.
- It automatically compiles kernels at runtime without waiting for CUDA compilation during installation.
- It reduces graphics card communication losses by combining different expert models in a single operation.

## Installation

**Cloning the repository and the development environment h**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Installing the library**

```
cat install.sh
./install.sh
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install the DeepGEMM library on my hardware with NVIDIA SM90 or SM100 architecture. First, run the commands '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh' to clone the repository with its submodules and prepare the development environment. Then, execute the command 'cat install.sh\n./install.sh' to complete the installation, and make the library ready for use in the Python environment with the 'import deep_gemm' command.

## Related dictionary terms

- [BLAS](https://trescout.com/en/dictionary/blas/)
- [Kernels](https://trescout.com/en/dictionary/kernels/)
- [Clone](https://trescout.com/en/dictionary/clone/)
- [GPU](https://trescout.com/en/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers and researchers who want to run large artificial intelligence models with the highest performance on modern NVIDIA graphics processing units.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/deepseek-ai/DeepGEMM)
- [Read in Turkish →](https://trescout.com/discover/deepgemm/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-06: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/deepgemm/
