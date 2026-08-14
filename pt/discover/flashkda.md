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
Quero acelerar alguns cálculos de Delta Attention usando a ferramenta FlashKDA. Como posso otimizar o mecanismo de atenção do meu modelo usando a função chunk_kda em torch.inference_mode(), integrada à biblioteca flash-linear-attention? Crie um exemplo de aplicação, levando em consideração os parâmetros necessários e os requisitos de hardware aos quais preciso prestar atenção.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/flashkda/
