# Produção de vídeos com inteligência artificial no sistema local

Desenvolvido pela Lightricks, o LTX-2 oferece um pacote de treinamento de inferência Python e adaptação de baixa classificação (LoRA) para modelos de inteligência artificial que produzem áudio e vídeo. Este conjunto de ferramentas permite aos usuários treinar modelos LTX-2 com seus próprios dados e executar saídas de modelo em sistemas locais.

- ★ 9.567
- GitHub Trending · 2026-06-19

## Atualizações

- **2 de outubro de 2026:** Estrelas 9,562 → 9,567, versão mais recente v1.4.2 (2 de outubro de 2026).
- **1 de outubro de 2026:** Estrelas 9,552 → 9,562, versão mais recente v1.4.1 (30 de setembro de 2026).
- **29 de setembro de 2026:** Estrelas 9,267 → 9,552, versão mais recente v1.4.0 (29 de setembro de 2026).
- **27 de agosto de 2026:** Estrelas 8,587 → 9,267, versão mais recente v1.3.0 (26 de agosto de 2026).

## O que você ganha

- Fornece sincronização de áudio e vídeo
- Você pode treinar LoRA com seus próprios dados
- Produção de vídeo de alta qualidade em sistema local

## Instalação

**Clone o repositório do GitHub e entre no diretório**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Baixe os pesos do modelo (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```

## Execução

**execute pipeline de inferência com uv**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Crie um vídeo usando o modelo LTX-2 que descreva detalhadamente a cena que desejo e inclua sincronização de áudio e vídeo. Faça com que o modelo produza resultados especificando detalhes da cena, aparência do personagem, ângulo da câmera e texto de fala.

## Termos relacionados do glossário

- [LoRA](https://trescout.com/pt/dictionary/lora/)
- [Inference](https://trescout.com/pt/dictionary/inference/)
- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para usuários que desejam criar vídeos de IA de áudio e vídeo ou treinar modelos em seu próprio sistema local.

## Links

- [Repositório no GitHub →](https://github.com/Lightricks/LTX-2)
- [Ler em turco →](https://trescout.com/discover/ltx-2/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-19: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ltx-2/
