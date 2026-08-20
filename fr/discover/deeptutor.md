# Formation personnalisée basée sur l'intelligence artificielle

DeepTutor est un système de tutorat privé basé sur l'apprentissage tout au long de la vie qui propose des processus éducatifs personnalisés utilisant les données des étudiants. Le projet vise à optimiser l’expérience d’apprentissage grâce à des méthodes de tutorat individualisé basées sur l’intelligence artificielle.

- ★ 36 594
- Python
- GitHub Trending · 2026-07-16

## Ce que ça vous apporte
- Système de cours particuliers axé sur l'apprentissage tout au long de la vie
- Interaction avec des agents d'intelligence artificielle personnalisés
- Base de connaissances avancée et prise en charge de RAG

## Installation
**Installation rapide**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
```

**Exécuter avec Docker**

```
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```


## Exécution
**Initialisation du système**

```
deeptutor start    # starts backend + frontend; keep the terminal open
```


## Si vous ne codez pas
Comment puis-je personnaliser mon processus d'apprentissage à l'aide du système DeepTutor ? Expliquez les étapes de base que je dois suivre pour créer mes propres partenaires d'IA et optimiser mon expérience d'apprentissage tout au long de la vie en intégrant mes supports de formation personnalisés dans ce système.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deeptutor/
