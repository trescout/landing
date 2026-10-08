# Computação matricial rápida para inteligência artificial

O DeepGEMM, desenvolvido pela DeepSeek, é uma biblioteca de subprogramas de álgebra linear básica (BLAS) de código aberto que acelera as operações de multiplicação de matrizes em unidades de processamento gráfico (GPUs). O software oferece kernels otimizados para modelos de inteligência artificial que exigem computação de alto desempenho.

- ★ 8.528
- Cuda
- GitHub Trending · 2026-10-06

## Atualizações

- **6 de outubro de 2026:** Estrelas 8,522 → 8,528, versão mais recente v2.1.1.post3 (15 de outubro de 2025).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar a biblioteca DeepGEMM no meu hardware com arquitetura NVIDIA SM90 ou SM100. Primeiro, para clonar o repositório com seus submódulos e preparar o ambiente de desenvolvimento, execute os comandos '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh'. Em seguida, para concluir a instalação, execute o comando 'cat install.sh\n./install.sh' e disponibilize a biblioteca para uso no ambiente Python com o comando 'import deep_gemm'.

## Termos relacionados do glossário

- [BLAS](https://trescout.com/pt/dictionary/blas/)
- [Kernels](https://trescout.com/pt/dictionary/kernels/)
- [Clone](https://trescout.com/pt/dictionary/clone/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É destinado a desenvolvedores e pesquisadores que desejam executar grandes modelos de inteligência artificial com o máximo desempenho em unidades de processamento gráfico (GPUs) modernas da NVIDIA.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/deepseek-ai/DeepGEMM)
- [Ler em turco →](https://trescout.com/discover/deepgemm/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-06: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deepgemm/
