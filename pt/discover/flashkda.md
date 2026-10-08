# Núcleos de alto desempenho para alguns Delta Attention

Desenvolvido pela Moonshot AI, FlashKDA oferece kernels de alto desempenho para o mecanismo Some Delta Attention. Esta tecnologia baseada em CUDA visa acelerar cálculos de atenção em grandes modelos de linguagem.

- ★ 1.043
- Cuda
- GitHub Trending · 2026-07-30

## O que você ganha

- Cálculos de atenção acelerada baseados em CUDA
- Trabalhando com eficiência em grandes modelos de linguagem
- Estrutura do kernel otimizada com CUTLASS

## Instalação

**Configuração básica**

```
git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda
cd flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation .
```

**Construa para todas as arquiteturas**

```
FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation .
```

## Execução

**Usando FLA como back-end**

```
pip install -U flash-linear-attention
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero acelerar alguns cálculos de Delta Attention usando a ferramenta FlashKDA. Como posso otimizar o mecanismo de atenção do meu modelo usando a função chunk_kda em torch.inference_mode(), integrada à biblioteca flash-linear-attention? Crie um exemplo de aplicação, levando em consideração os parâmetros necessários e os requisitos de hardware aos quais preciso prestar atenção.

## Termos relacionados do glossário

- [Kernels](https://trescout.com/pt/dictionary/kernels/)
- [Attention](https://trescout.com/pt/dictionary/attention/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores que desejam acelerar cálculos de atenção em grandes modelos de linguagem em CUDA.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/MoonshotAI/FlashKDA)
- [Ler em turco →](https://trescout.com/discover/flashkda/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-30: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/flashkda/
