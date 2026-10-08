# Modelos de inteligência artificial para sistemas físicos

Desenvolvido pela NVIDIA, o Cosmos é uma plataforma aberta que fornece modelos mundiais, conjuntos de dados e ferramentas para sistemas físicos, como robôs e veículos autônomos. Ele fornece uma infraestrutura que facilita aos desenvolvedores a criação de aplicativos físicos de IA.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Atualizações

- **2 de agosto de 2026:** Estrelas 9,173 → 11,343, versão mais recente Cosmos3 (1 de junho de 2026).

## O que você ganha

- Ele fornece modelos mundiais, conjuntos de dados e ferramentas para aplicações físicas de IA.
- Ele pode processar e produzir sequências de texto, visuais, de áudio e de ação em uma arquitetura unificada.
- Fornece recursos de previsão, planejamento e simulação para sistemas robóticos e autônomos.

## Instalação

**Instalação com vLLM-Omni**

```
uv pip install --torch-backend=cu130 \
  "vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```

## Execução

**Produção de Vídeo**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
  --form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
  --form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
  -o cosmos3_t2v.mp4
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero desenvolver aplicações físicas de inteligência artificial usando a plataforma NVIDIA Cosmos. Explicar em detalhes técnicos as capacidades oferecidas pela família de modelos Cosmos 3, especialmente as diferenças no uso de superfícies ‘Reasoner’ e ‘Generator’, e como esses modelos podem ser configurados em cenários como planejamento de missão ou simulação de mundo em sistemas robóticos e autônomos. Além disso, resuma o processo de trabalho com a ferramenta 'uv' e a biblioteca 'vllm-omni' durante a fase de instalação, passo a passo, levando em consideração os requisitos do driver CUDA.

## Termos relacionados do glossário

- [Physical AI](https://trescout.com/pt/dictionary/physical-ai/)
- [Jupyter Notebooks](https://trescout.com/pt/dictionary/jupyter-notebooks/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para desenvolvedores que trabalham em IA física, sistemas robóticos e veículos autônomos, interessados ​​em modelos mundiais e processamento de dados multimodais.

## Links

- [Repositório no GitHub →](https://github.com/NVIDIA/cosmos)
- [Ler em turco →](https://trescout.com/discover/cosmos/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-05: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cosmos/
