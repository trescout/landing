# Apporter des données intelligentes avec l'intelligence artificielle

Production-agentic-rag-course propose une formation pratique sur le développement de systèmes de production assistés par récupération basés sur des agents (agentic RAG) qui automatisent les processus de récupération d'informations à partir de sources de données complexes. Basée sur le langage Python, cette ressource enseigne l'architecture technique requise pour créer des applications d'intelligence artificielle évolutives et de niveau production.

- ★ 8 216
- GitHub Trending · 2026-06-03

## Ce que ça vous apporte
- Établir l'infrastructure nécessaire pour les systèmes RAG au niveau de la production.
- Application de méthodes de recherche hybride et de traitement de données intelligent.
- Développer des mécanismes de décision basés sur des agents avec LangGraph.

## Installation
**Clonage et installation du référentiel**

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


## Exécution
**Lire le contenu d'une semaine spécifique**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```


## Si vous ne codez pas
Je souhaite développer un assistant de recherche universitaire en utilisant le projet production-agentic-rag-course. Pour l'installation de base du projet, après avoir téléchargé le référentiel avec la commande git clone, je dois configurer le fichier .env et installer les dépendances avec uv sync. Ensuite, je souhaite vérifier que le système fonctionne sur http://localhost:8000/api/v1/health en démarrant tous les services avec la commande docker compose up --build -d. Pouvez-vous me guider sur les clés API et les configurations de service auxquelles je dois prêter attention dans ce processus ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/production-agentic-rag-course/
