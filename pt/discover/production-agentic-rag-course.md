# Trazendo dados inteligentes com inteligência artificial

O curso Production-agentic-rag oferece treinamento prático no desenvolvimento de sistemas de produção assistida por busca baseados em agentes (RAG agentic) que automatizam os processos de recuperação de informações de fontes de dados complexas. Baseado na linguagem Python, este recurso ensina a arquitetura técnica necessária para criar aplicativos de inteligência artificial escalonáveis ​​e em nível de produção.

- ★ 9.265
- GitHub Trending · 2026-06-03

## Atualizações

- **3 de outubro de 2026:** Estrelas 8,216 → 9,265, versão mais recente week7.0 (26 de novembro de 2025).
- **2 de agosto de 2026:** Estrelas 6,536 → 8,216, versão mais recente week7.0 (26 de novembro de 2025).

## O que você ganha

- Estabelecer a infraestrutura necessária para sistemas RAG no nível de produção.
- Aplicação de pesquisa híbrida e métodos inteligentes de processamento de dados.
- Desenvolvendo mecanismos de decisão baseados em agentes com LangGraph.

## Instalação

**Clonando e instalando o repositório**

```
git clone <repository-url>
cd arxiv-paper-curator

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch, 
# arXiv API, and service connections. Defaults work out of the box.
# You need to add Jina embeddings free api key and langfuse keys (check the blogs)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Verify everything works
curl http://localhost:8000/api/v1/health
```

## Execução

**Reproduzir conteúdo de uma semana específica**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero desenvolver um assistente de pesquisa acadêmica usando o projeto de curso de agente de produção. Para a instalação básica do projeto, após baixar o repositório com o comando git clone, preciso configurar o arquivo .env e instalar as dependências com uv sync. Então, quero verificar se o sistema está funcionando em http://localhost:8000/api/v1/health iniciando todos os serviços com o comando docker compose up --build -d. Você pode me orientar sobre as chaves de API e configurações de serviço às quais devo prestar atenção neste processo?

## Termos relacionados do glossário

- [Clone](https://trescout.com/pt/dictionary/clone/)
- [Agentic](https://trescout.com/pt/dictionary/agentic/)
- [Localhost](https://trescout.com/pt/dictionary/localhost/)
- [RAG](https://trescout.com/pt/dictionary/rag/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para engenheiros e desenvolvedores de IA que desejam desenvolver sistemas RAG de nível de produção, escaláveis ​​e baseados em agentes.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/jamwithai/production-agentic-rag-course)
- [Ler em turco →](https://trescout.com/discover/production-agentic-rag-course/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-03: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/production-agentic-rag-course/
