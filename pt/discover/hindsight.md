# Camada de memória inteligente para agentes de inteligência artificial

O Hindsight oferece uma camada de memória (memory layer) de aprendizado para agentes de inteligência artificial. Fazendo inferências a partir de interações passadas para melhorar os processos de tomada de decisão dos agentes, esta biblioteca de código aberto permite que os sistemas produzam resultados mais consistentes ao longo do tempo.

- ★ 41.939
- GitHub Trending · 2026-09-25

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
Quero que meu agente de inteligência artificial aprenda com as interações passadas, não apenas lembrando o histórico de conversas, mas também tomando decisões mais consistentes ao longo do tempo. Ajude-me a configurar a instalação do servidor e as conexões do cliente necessárias para integrar esta camada de memória ao meu projeto.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/hindsight/
