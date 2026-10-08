# Recherche approfondie avec intelligence artificielle autonome

Développé par LangChain, open-deep-research est un système autonome qui effectue des recherches en plusieurs étapes sur Internet pour répondre à des questions complexes. Il facilite les processus de recherche approfondis en automatisant le processus de recherche à travers les étapes de planification, de collecte de données et de synthèse.

- ★ 12 655
- Python
- GitHub Trending · 2026-07-22

## Mises à jour

- **22 août 2026:** Étoiles 12,307 → 12,655, dépôt archivé, développement arrêté.

## Ce que ça vous apporte

- Recherche autonome en plusieurs étapes pour des questions complexes
- Compatibilité avec différents fournisseurs de modèles et outils de recherche
- Processus de recherche visualisés via LangGraph

## Installation

**Clonage du référentiel et préparation de l'environnement**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Installation des dépendances**

```
uv sync
# or
uv pip install -r pyproject.toml
```

## Exécution

**Démarrage du serveur**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Réalisez une analyse approfondie de [ÉCRIVEZ VOTRE SUJET DE RECHERCHE ICI] à l’aide de l’outil Open Deep Research. Planifiez votre processus de recherche, collectez des données en ligne et synthétisez vos résultats pour créer un rapport complet.

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs et aux chercheurs qui souhaitent automatiser des processus de recherche autonomes sur des sujets complexes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/langchain-ai/open_deep_research)
- [Lire en turc →](https://trescout.com/discover/open-deep-research/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-22 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/open-deep-research/
