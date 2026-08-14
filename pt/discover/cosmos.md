# Modelos de inteligência artificial para sistemas físicos

Desenvolvido pela NVIDIA, o Cosmos é uma plataforma aberta que fornece modelos mundiais, conjuntos de dados e ferramentas para sistemas físicos, como robôs e veículos autônomos. Ele fornece uma infraestrutura que facilita aos desenvolvedores a criação de aplicativos físicos de IA.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Atualizar
- 2 de agosto de 2026: Star 9.173 → 11.343, último lançamento Cosmos3 (1 de junho de 2026).

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
Quero desenvolver aplicações físicas de inteligência artificial usando a plataforma NVIDIA Cosmos. Explicar em detalhes técnicos as capacidades oferecidas pela família de modelos Cosmos 3, especialmente as diferenças no uso de superfícies ‘Reasoner’ e ‘Generator’, e como esses modelos podem ser configurados em cenários como planejamento de missão ou simulação de mundo em sistemas robóticos e autônomos. Além disso, resuma o processo de trabalho com a ferramenta 'uv' e a biblioteca 'vllm-omni' durante a fase de instalação, passo a passo, levando em consideração os requisitos do driver CUDA.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cosmos/
