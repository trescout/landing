# Execute modelos de inteligência artificial massivos localmente

Colibri é um motor baseado na linguagem C que permite executar modelos de mistura de especialistas (Mixture of Experts) de grande escala em computadores locais com baixos requisitos de hardware. Ao processar camadas de especialistas via streaming a partir do disco, torna possível executar modelos de IA de alta capacidade em hardware limitado.

- ★ 40.157
- C
- GitHub Trending · 2026-09-11

## Atualizações

- **7 de outubro de 2026:** Estrelas 39,698 → 40,157, versão mais recente v2.0.0 (6 de outubro de 2026).
- **5 de outubro de 2026:** Estrelas 37,791 → 39,698, versão mais recente v1.12.1 (24 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 36,260 → 37,791, versão mais recente v1.12.1 (24 de setembro de 2026).
- **19 de setembro de 2026:** Estrelas 34,474 → 36,260, versão mais recente v1.11.0 (13 de setembro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero executar modelos de IA de grande escala no meu computador local usando o motor Colibri. Configure-me para usar meus recursos de hardware (VRAM, RAM e disco NVMe) da maneira mais eficiente possível. Explique passo a passo como posso otimizar e executar modelos como GLM ou DeepSeek de acordo com a capacidade de memória do meu sistema.

## Termos relacionados do glossário

- [Mixture of Experts](https://trescout.com/pt/dictionary/mixture-of-experts/)
- [VRAM](https://trescout.com/pt/dictionary/vram/)
- [RAM](https://trescout.com/pt/dictionary/ram/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destinado a pesquisadores e desenvolvedores que desejam executar grandes modelos de linguagem em seus próprios computadores com recursos de hardware limitados.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/JustVugg/colibri)
- [Ler em turco →](https://trescout.com/discover/colibri/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-11: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/colibri/
