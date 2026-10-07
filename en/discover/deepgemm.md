# Fast matrix computation for artificial intelligence

DeepGEMM, developed by DeepSeek, is an open-source basic linear algebra subprograms (BLAS) library that accelerates matrix multiplication operations on graphics processing units (GPUs). The software provides optimized kernels for artificial intelligence models requiring high-performance computing.

- ★ 8,528
- Cuda
- GitHub Trending · 2026-10-06

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
I want to install the DeepGEMM library on my hardware with NVIDIA SM90 or SM100 architecture. First, run the commands '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh' to clone the repository with its submodules and prepare the development environment. Then, execute the command 'cat install.sh\n./install.sh' to complete the installation, and make the library ready for use in the Python environment with the 'import deep_gemm' command.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/deepgemm/
