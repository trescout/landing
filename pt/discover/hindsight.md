# Camada de memória inteligente para agentes de inteligência artificial

O Hindsight oferece uma camada de memória (memory layer) de aprendizado para agentes de inteligência artificial. Fazendo inferências a partir de interações passadas para melhorar os processos de tomada de decisão dos agentes, esta biblioteca de código aberto permite que os sistemas produzam resultados mais consistentes ao longo do tempo.

- ★ 47.195
- GitHub Trending · 2026-09-25

## Atualizações

- **8 de outubro de 2026:** Estrelas 46,537 → 47,195, versão mais recente v0.10.3 (8 de outubro de 2026).
- **7 de outubro de 2026:** Estrelas 44,051 → 46,537, versão mais recente v0.10.2 (29 de setembro de 2026).
- **1 de outubro de 2026:** Estrelas 41,939 → 44,051, versão mais recente v0.10.2 (29 de setembro de 2026).
- **29 de setembro de 2026:** Estrelas 39,425 → 41,939, versão mais recente v0.10.2 (29 de setembro de 2026).

## O que você ganha

- Oferece uma arquitetura de memória que aprende com interações passadas e produz resultados mais consistentes ao longo do tempo.
- Vai além da simples recordação de informações, melhorando os processos de tomada de decisão dos agentes.
- Contém bibliotecas de cliente para diferentes linguagens, como Python, Node.js e Go.

## Instalação

**Iniciando o servidor com Docker**

```
export OPENAI_API_KEY=sk-xxx

docker run -it --pull always --name hindsight --restart unless-stopped -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
  -v hindsight-data:/home/hindsight/.pg0 \
  ghcr.io/vectorize-io/hindsight:latest
```

## Execução

**Configurando o cliente com Python**

```
pip install hindsight-client -U                                  # Python
npm install @vectorize-io/hindsight-client                        # Node.js / TypeScript
go get github.com/vectorize-io/hindsight/hindsight-clients/go     # Go
curl -fsSL https://hindsight.vectorize.io/get-cli | bash          # CLI
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero que meu agente de inteligência artificial aprenda com as interações passadas, não apenas lembrando o histórico de conversas, mas também tomando decisões mais consistentes ao longo do tempo. Ajude-me a configurar a instalação do servidor e as conexões do cliente necessárias para integrar esta camada de memória ao meu projeto.

## Termos relacionados do glossário

- [Memory Layer](https://trescout.com/pt/dictionary/memory-layer/)
- [Memory](https://trescout.com/pt/dictionary/memory/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Desenvolvedores que desejam que os agentes de inteligência artificial aprendam com o tempo e tomem decisões mais consistentes.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/vectorize-io/hindsight)
- [Ler em turco →](https://trescout.com/discover/hindsight/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-25: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/hindsight/
