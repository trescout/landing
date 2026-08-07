# Rechercher rapidement du Big Data

Développé avec Java, Elasticsearch est un moteur de recherche distribué et open source qui permet une recherche et une analyse rapides sur de grands ensembles de données. Grâce à son architecture RESTful, il prend en charge l'indexation et l'interrogation des données en temps réel.

- ★ 77 787
- Java
- GitHub Trending · 2026-07-04

## Mise à jour
- 6 août 2026 : Star 77 640 → 77 787, dernière version v9.5.0 (4 août 2026).
- 2 août 2026 : Star 77 374 → 77 640, dernière version v9.4.4 (21 juillet 2026).

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
Le moyen le plus simple de démarrer avec Elasticsearch consiste à créer un déploiement géré via Elastic Cloud. Alternativement, si vous souhaitez gérer votre propre installation, vous pouvez visiter la page de téléchargement sur le site officiel ou consulter les scripts de démarrage basés sur Docker disponibles pour les environnements de développement locaux.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/elasticsearch/
