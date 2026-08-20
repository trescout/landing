# Pesquise big data rapidamente

Desenvolvido em Java, o Elasticsearch é um mecanismo de busca distribuído e de código aberto que permite busca e análise rápidas em grandes conjuntos de dados. Graças à sua arquitetura RESTful, suporta indexação e consulta de dados em tempo real.

- ★ 77.846
- Java
- GitHub Trending · 2026-07-04

## O que você ganha
- Pesquisa e análise rápidas de grandes conjuntos de dados
- Integração com pesquisa vetorial e aplicativos de IA
- Indexação e consulta de dados em tempo real

## Instalação
**Extraia a imagem do Docker**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (homebrew)**

```
brew install elastic/tap/elasticsearch-full
```


## Execução
**Inicie com Docker no modo de nó único**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Como começar
- Fonte oficial →

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/elasticsearch/
