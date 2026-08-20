# Rechercher rapidement du Big Data

Développé avec Java, Elasticsearch est un moteur de recherche distribué et open source qui permet une recherche et une analyse rapides sur de grands ensembles de données. Grâce à son architecture RESTful, il prend en charge l'indexation et l'interrogation des données en temps réel.

- ★ 77 846
- Java
- GitHub Trending · 2026-07-04

## Ce que ça vous apporte
- Recherche et analyse rapides de grands ensembles de données
- Intégration avec les applications de recherche vectorielle et d'IA
- Indexation et interrogation des données en temps réel

## Installation
**Extraire l'image Docker**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (Homebrew)**

```
brew install elastic/tap/elasticsearch-full
```


## Exécution
**Lancer avec Docker en mode nœud unique**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Pour commencer
- Source officielle →

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/elasticsearch/
