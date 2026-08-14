# Pesquisa aprofundada com inteligência artificial autônoma

Desenvolvido pela LangChain, o open-deep-research é um sistema autônomo que realiza pesquisas em várias etapas na internet para responder questões complexas. Facilita processos de pesquisa profunda, automatizando o processo de pesquisa por meio das etapas de planejamento, coleta de dados e síntese.

- ★ 12.307
- Python
- GitHub Trending · 2026-07-22

## O que você ganha
- Pesquisa autônoma em várias etapas para questões complexas
- Compatibilidade com diferentes fornecedores de modelos e ferramentas de pesquisa
- Processos de pesquisa visualizados via LangGraph

## Instalação
**Clonando o repositório e preparando o ambiente**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Instalando dependências**

```
uv sync
# or
uv pip install -r pyproject.toml
```


## Execução
**Iniciando o servidor**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```


## Se você não programa
Conduza uma análise aprofundada de [ESCREVA SEU TÓPICO DE PESQUISA AQUI] usando a ferramenta Open Deep Research. Planeje seu processo de pesquisa, colete dados on-line e sintetize suas descobertas para criar um relatório abrangente.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/open-deep-research/
