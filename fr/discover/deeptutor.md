# Formation personnalisée basée sur l'intelligence artificielle

DeepTutor est un système de tutorat privé basé sur l'apprentissage tout au long de la vie qui propose des processus éducatifs personnalisés utilisant les données des étudiants. Le projet vise à optimiser l’expérience d’apprentissage grâce à des méthodes de tutorat individualisé basées sur l’intelligence artificielle.

- ★ 40 808
- Python
- GitHub Trending · 2026-07-16

## Mises à jour

- **5 octobre 2026:** Étoiles 40,358 → 40,808, dernière version v1.6.13 (4 octobre 2026).
- **27 septembre 2026:** Étoiles 40,334 → 40,358, dernière version v1.6.12 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 39,561 → 40,334, dernière version v1.6.11 (24 septembre 2026).
- **14 septembre 2026:** Étoiles 39,283 → 39,561, dernière version v1.6.8 (14 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Comment puis-je personnaliser mon processus d'apprentissage à l'aide du système DeepTutor ? Expliquez les étapes de base que je dois suivre pour créer mes propres partenaires d'IA et optimiser mon expérience d'apprentissage tout au long de la vie en intégrant mes supports de formation personnalisés dans ce système.

## Termes liés du glossaire

- [Lifelong Learning](https://trescout.com/fr/dictionary/lifelong-learning/)
- [Personalized Tutoring](https://trescout.com/fr/dictionary/personalized-tutoring/)
- [Tutoring](https://trescout.com/fr/dictionary/tutoring/)
- [RAG](https://trescout.com/fr/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux étudiants et aux professeurs qui souhaitent créer leur propre assistant pédagogique privé et établir un environnement d'apprentissage personnalisé.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/HKUDS/DeepTutor)
- [Lire en turc →](https://trescout.com/discover/deeptutor/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-16 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deeptutor/
