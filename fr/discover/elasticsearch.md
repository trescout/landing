# Moteur de recherche distribué et puissant

Elasticsearch est un moteur de recherche et d'analyse distribué et haute performance, basé sur une API RESTful.

- ★ 77 846
- GitHub Trending · 2026-07-04

## Que fait cet outil ?
Elasticsearch est un moteur de recherche et d'analyse distribué et haute performance, basé sur une API RESTful. Il fournit une infrastructure pour la recherche en temps réel, l'analyse de logs et la visualisation de données sur de grands volumes de données textuelles, numériques et géographiques.

## Pour qui ?
Pour ceux qui souhaitent effectuer des recherches complexes et des analyses de logs sur des millions de lignes de données en quelques millisecondes.

## À quoi ne faut-il pas s’attendre ?
Utilisateurs de bases de données traditionnelles ayant besoin de modèles de données relationnels et d'opérations SQL `JOIN` complexes.

## Points forts
- Offre une recherche plein texte haute vitesse sur de grands volumes de données.
- Grâce à son architecture distribuée, il est facilement évolutif horizontalement.
- Héberge un riche écosystème pour la gestion des logs et la surveillance du système.

## Premiers pas
- Installez Elasticsearch en suivant les instructions Docker ou du gestionnaire de paquets dans la documentation officielle.
- Configurez les paramètres de sécurité par défaut (mots de passe et certificats).
- Vérifiez l'état du cluster en envoyant une requête au point de terminaison principal avec un client REST.

## Démarrage prudent

## Premier prompt
Comment créer un nouvel index dans Elasticsearch ?

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


## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- README officiel d'Elasticsearch →
- Site officiel d'Elasticsearch →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/elasticsearch/
