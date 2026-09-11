# Execute modelos de inteligência artificial massivos localmente

Colibri é um motor baseado na linguagem C que permite executar modelos de mistura de especialistas (Mixture of Experts) de grande escala em computadores locais com baixos requisitos de hardware. Ao processar camadas de especialistas via streaming a partir do disco, torna possível executar modelos de IA de alta capacidade em hardware limitado.

- ★ 27.610
- C
- GitHub Trending · 2026-09-11

## O que você ganha
- Executa modelos de alta capacidade em hardware limitado
- Gerencia VRAM, RAM e memória de disco como uma única camada
- Proporciona eficiência processando camadas de especialistas via streaming

## Instalação
**Compilando a partir do código-fonte**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
```


## Execução
**Iniciar interface de chat**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable  (+ make cuda-dsv4-dg-dll on RTX 50)
```


## Se você não programa
Quero executar modelos de IA de grande escala no meu computador local usando o motor Colibri. Configure-me para usar meus recursos de hardware (VRAM, RAM e disco NVMe) da maneira mais eficiente possível. Explique passo a passo como posso otimizar e executar modelos como GLM ou DeepSeek de acordo com a capacidade de memória do meu sistema.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/colibri/
