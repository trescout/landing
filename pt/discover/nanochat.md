# Ferramenta de treinamento de modelos de inteligência artificial

karpathy/nanochat é um framework de software experimental desenvolvido para treinar grandes modelos de linguagem (LLMs), capaz de rodar em uma única unidade de processamento gráfico (GPU). Abrangendo os processos de tokenização, pré-treinamento, ajuste fino (fine-tuning), avaliação e inferência, este projeto oferece aos desenvolvedores uma estrutura mínima e altamente customizável.

- ★ 59.998
- Python
- GitHub Trending · 2026-11-03

## O que você ganha

- Permite treinar um modelo de inteligência artificial em uma única unidade de processamento gráfico.
- Permite gerenciar as etapas de geração de texto através da linha de comando.
- Oferece opções de instalação flexíveis para diferentes tipos de hardware.

## Instalação

**Instalando dependências**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Execução

**Iniciar o processo de treinamento**

```
bash runs/speedrun.sh
```

**Conversar com o modelo**

```
python -m scripts.chat_cli
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar e executar a ferramenta de inteligência artificial chamada nanochat. Primeiro, instale as dependências e ative o ambiente virtual usando os comandos uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate. Em seguida, inicie o processo com o comando bash runs/speedrun.sh e, quando terminar, interaja com o modelo executando python -m scripts.chat_cli.

Repositório: https://github.com/karpathy/nanochat. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Fine-tuning](https://trescout.com/pt/dictionary/fine-tuning/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)
- [LLM](https://trescout.com/pt/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destinado a desenvolvedores que desejam treinar e testar grandes modelos de linguagem do zero.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/karpathy/nanochat)
- [Ler em turco →](https://trescout.com/discover/nanochat/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-03: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/nanochat/
