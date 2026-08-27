# Motor de Busca Distribuído e Poderoso

O Elasticsearch é um motor de busca e análise distribuído e de alto desempenho, baseado em API RESTful.

- ★ 77.846
- GitHub Trending · 2026-07-04

## O que esta ferramenta faz?
O Elasticsearch é um motor de busca e análise distribuído e de alto desempenho, baseado em API RESTful. Ele fornece uma infraestrutura para busca em tempo real, análise de logs e visualização de dados sobre grandes volumes de dados textuais, numéricos e geográficos.

## Para quem é?
Para aqueles que desejam realizar buscas complexas e análises de logs em milhões de linhas de dados em milissegundos.

## O que não esperar
Usuários de bancos de dados tradicionais que precisam de modelos de dados relacionais e operações complexas de `JOIN` em SQL.

## Destaques
- Oferece busca de texto completo de alta velocidade em grandes volumes de dados.
- Graças à sua arquitetura distribuída, pode ser facilmente escalado horizontalmente.
- Possui um ecossistema rico para gerenciamento de logs e monitoramento de sistemas.

## Primeiro fluxo de uso
- Instale o Elasticsearch seguindo as instruções do Docker ou do gerenciador de pacotes na documentação oficial.
- Configure as definições de segurança padrão (senhas e certificados).
- Verifique o status do cluster enviando uma solicitação ao endpoint principal com um cliente REST.

## Início seguro

## Primeiro prompt
Como criar um novo índice no Elasticsearch?

## Instalação
**Extraia a imagem do Docker**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (Homebrew)**

```
brew install elastic/tap/elasticsearch-full
```


## Execução
**Inicie com Docker no modo de nó único**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- README oficial do Elasticsearch →
- Site oficial do Elasticsearch →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/elasticsearch/
