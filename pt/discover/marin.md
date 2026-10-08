# Plataforma Aberta de Desenvolvimento para Pesquisa de Modelos de Base

Programa de pesquisa, plataforma de software e comunidade para investigar e desenvolver modelos de base. Documenta o escopo desde o processamento de dados até pré-treinamento, fine-tuning e avaliação.

- ★ 3.089
- Python
- GitHub Trending · 2026-08-25

## Atualizações

- **31 de agosto de 2026:** Estrelas 1,967 → 3,089.

## Instalação

**Clonar repositório oficial**

```
git clone https://github.com/marin-community/marin.git
```

**Criar ambiente Python**

```
uv venv --python 3.12
```

**Instalar dependências**

```
uv sync --all-packages
```

## Execução

**Executar smoke test na CPU**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```

## O que esta ferramenta faz?

Executa experimentos como passos dependentes em ordem topológica. O experimento inicial oficial demonstra tokenização do TinyStories e o treinamento de um pequeno modelo de linguagem; a abordagem de desenvolvimento aberto documenta código, dados, decisões e experimentos malsucedidos.

## Para quem é?

Equipes que pesquisam curadoria, transformação, filtragem de dados, tokenização, treinamento de modelos e avaliação.

## O que não esperar

Trabalhos de desenvolvimento de aplicações simples que não fazem parte de pesquisa de modelos de base ou para quem não quer configurar o ambiente Python e de desenvolvimento necessário.

## Destaques

- Cobertura de pesquisa do processamento de dados ao pré-treinamento, fine-tuning e avaliação
- Fluxo de trabalho de experimentos que executa passos dependentes em ordem topológica
- Documentação aberta que inclui experimentos fracassados e decisões de desenvolvimento

## Primeiro fluxo de uso

1. Clone o repositório oficial e crie um ambiente virtual Python 3.12 ou superior
2. Sincronize dependências com uv
3. Configure a variável de ambiente MARIN_PREFIX
4. Execute o teste rápido (smoke test) offline do TinyStories na CPU

## Início seguro

O teste rápido na CPU é apenas para verificação inicial. Dependências para CPU, GPU e TPU podem exigir anexos de hardware separados. WANDB_API_KEY e HF_TOKEN são necessários somente para fluxos de monitoramento ou modelos fechados correspondentes.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Execute como verificação inicial o fluxo TinyStories offline treinando um pequeno modelo na CPU.

## Termos relacionados do glossário

- [CPU](https://trescout.com/pt/dictionary/cpu/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)

## Links

- [Repositório no GitHub →](https://github.com/marin-community/marin)
- [Documentação de instalação →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [Primeiro experimento →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [README oficial →](https://github.com/marin-community/marin)
- [Ler em turco →](https://trescout.com/discover/marin/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-25: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/marin/
