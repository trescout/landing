# Serveur d'inférence pour agents d'intelligence artificielle

Développé par Superlinked, SIE est un serveur d'inférence open source et un cluster de production utilisé pour exécuter les modèles dont les agents d'IA ont besoin. Cette structure basée sur Python vise à gérer des déploiements de modèles complexes et à fournir une infrastructure évolutive.

- ★ 3 198
- Python
- GitHub Trending · 2026-09-03

## Ce que ça vous apporte
- Gère les modèles open source via un seul cluster
- Permet une intégration facile grâce à son interface compatible avec OpenAI
- Prend en charge des tâches telles que la recherche, l'extraction de données et la génération de texte

## Installation
**Installation du SDK**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```


## Exécution
**Premier essai de déploiement**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```


## Si vous ne codez pas
Je souhaite exécuter un modèle pour un agent d'IA via le serveur SIE. Comment puis-je gérer les tâches dont mon agent a besoin, telles que la recherche, l'extraction de données et la génération de texte, via une seule API ? Comment puis-je configurer les processus de création d'embeddings et de génération de texte en utilisant les points de terminaison compatibles avec OpenAI fournis par SIE ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sie/
