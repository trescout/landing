# Computação matricial rápida para inteligência artificial

O DeepGEMM, desenvolvido pela DeepSeek, é uma biblioteca de subprogramas de álgebra linear básica (BLAS) de código aberto que acelera as operações de multiplicação de matrizes em unidades de processamento gráfico (GPUs). O software oferece kernels otimizados para modelos de inteligência artificial que exigem computação de alto desempenho.

- ★ 8.528
- Cuda
- GitHub Trending · 2026-10-06

## O que você ganha
- Reduz o tempo de execução de grandes modelos de linguagem ao acelerar as multiplicações de matrizes.
- Compila automaticamente os kernels em tempo de execução, sem esperar pela compilação CUDA durante a instalação.
- Reduz as perdas de comunicação da placa gráfica ao combinar diferentes modelos de especialistas em uma única operação.

## Instalação
**Clonagem do repositório e o ambiente de desenvolvimento p**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Instalação da biblioteca**

```
cat install.sh
./install.sh
```


## Se você não programa
Quero instalar a biblioteca DeepGEMM no meu hardware com arquitetura NVIDIA SM90 ou SM100. Primeiro, para clonar o repositório com seus submódulos e preparar o ambiente de desenvolvimento, execute os comandos '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh'. Em seguida, para concluir a instalação, execute o comando 'cat install.sh\n./install.sh' e disponibilize a biblioteca para uso no ambiente Python com o comando 'import deep_gemm'.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deepgemm/
