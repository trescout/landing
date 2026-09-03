# Servidor de inferência para agentes de inteligência artificial

O SIE, desenvolvido pela Superlinked, é um servidor de inferência de código aberto e um cluster de produção usado para executar os modelos necessários para agentes de IA. Esta estrutura baseada em Python visa gerenciar implantações complexas de modelos e oferecer uma infraestrutura escalável.

- ★ 3.157
- Python
- GitHub Trending · 2026-09-03

## O que você ganha
- Gerencia modelos de código aberto através de um único cluster
- Proporciona fácil integração graças à sua interface compatível com OpenAI
- Suporta tarefas como busca, extração de dados e geração de texto

## Instalação
**Instalação do SDK**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```


## Execução
**Primeira tentativa de implantação**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```


## Se você não programa
Quero executar um modelo para um agente de IA através do servidor SIE. Como posso gerenciar as tarefas que meu agente precisa, como busca, extração de dados e geração de texto, através de uma única API? Como posso configurar os processos de criação de embeddings e geração de texto usando os endpoints compatíveis com OpenAI oferecidos pelo SIE?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sie/
