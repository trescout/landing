# Outil d'entraînement de modèles d'intelligence artificielle

karpathy/nanochat est un framework logiciel expérimental développé pour entraîner des grands modèles de langage (LLM) et capable de s'exécuter sur une seule unité de traitement graphique (GPU). Couvrant les processus de tokenisation, de pré-entraînement, de réglage fin (fine-tuning), d'évaluation et d'inférence, ce projet offre aux développeurs une structure minimale et modifiable.

- ★ 59 998
- Python
- GitHub Trending · 2026-11-03

## Ce que ça vous apporte

- Vous permet d'entraîner un modèle d'intelligence artificielle sur une seule unité de traitement graphique.
- Vous permet de gérer les étapes de génération de texte via la ligne de commande.
- Offre des options d'installation flexibles pour différents types de matériel.

## Installation

**Installation des dépendances**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Exécution

**Démarrer le processus d'entraînement**

```
bash runs/speedrun.sh
```

**Discuter avec le modèle**

```
python -m scripts.chat_cli
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer et exécuter l'outil d'intelligence artificielle nommé nanochat. Tout d'abord, installez les dépendances et activez l'environnement virtuel en utilisant la commande uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate. Ensuite, lancez le processus avec la commande bash runs/speedrun.sh et, une fois terminé, interagissez avec le modèle en exécutant python -m scripts.chat_cli.

Dépôt : https://github.com/karpathy/nanochat. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Fine-tuning](https://trescout.com/fr/dictionary/fine-tuning/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux développeurs qui souhaitent entraîner et tester de grands modèles de langage à partir de zéro.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/karpathy/nanochat)
- [Lire en turc →](https://trescout.com/discover/nanochat/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/nanochat/
