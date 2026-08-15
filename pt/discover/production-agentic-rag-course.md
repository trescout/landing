# Trazendo dados inteligentes com inteligência artificial

O curso Production-agentic-rag oferece treinamento prático no desenvolvimento de sistemas de produção assistida por busca baseados em agentes (RAG agentic) que automatizam os processos de recuperação de informações de fontes de dados complexas. Baseado na linguagem Python, este recurso ensina a arquitetura técnica necessária para criar aplicativos de inteligência artificial escalonáveis ​​e em nível de produção.

- ★ 8.216
- GitHub Trending · 2026-06-03

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
Quero desenvolver um assistente de pesquisa acadêmica usando o projeto de curso de agente de produção. Para a instalação básica do projeto, após baixar o repositório com o comando git clone, preciso configurar o arquivo .env e instalar as dependências com uv sync. Então, quero verificar se o sistema está funcionando em http://localhost:8000/api/v1/health iniciando todos os serviços com o comando docker compose up --build -d. Você pode me orientar sobre as chaves de API e configurações de serviço às quais devo prestar atenção neste processo?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/production-agentic-rag-course/
