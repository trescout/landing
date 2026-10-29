# Pesquisa aprofundada com inteligência artificial autônoma

Desenvolvido pela LangChain, o open-deep-research é um sistema autônomo que realiza pesquisas em várias etapas na internet para responder questões complexas. Facilita processos de pesquisa profunda, automatizando o processo de pesquisa por meio das etapas de planejamento, coleta de dados e síntese.

- ★ 12.655
- Python
- GitHub Trending · 2026-07-22

## Atualizações

- **22 de agosto de 2026:** Estrelas 12,307 → 12,655, repositório arquivado, desenvolvimento encerrado.

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Conduza uma análise aprofundada de [ESCREVA SEU TÓPICO DE PESQUISA AQUI] usando a ferramenta Open Deep Research. Planeje seu processo de pesquisa, colete dados on-line e sintetize suas descobertas para criar um relatório abrangente.

Repositório: https://github.com/langchain-ai/open_deep_research. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores e pesquisadores que desejam automatizar processos de pesquisa autônomos sobre temas complexos.
- **Licença:** MIT

## Nota editorial

Maintenance note: The GitHub source repository is archived. Treat this as an educational reference and verify an active successor/fork for current dependencies and security.

## Links

- [Repositório no GitHub →](https://github.com/langchain-ai/open_deep_research)
- [Ler em turco →](https://trescout.com/discover/open-deep-research/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-22: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/open-deep-research/
