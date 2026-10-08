# Animez différents squelettes de personnages avec un seul modèle

UniMate est une technologie d'animation qui permet d'animer différentes structures squelettiques via un modèle unique. Présentés lors de SIGGRAPH Asia 2026, ces travaux visent à standardiser les processus d'animation de personnages.

- ★ 1 166
- Python
- GitHub Trending · 2026-10-02

## Ce que ça vous apporte

- Anime des structures squelettiques variées, telles que des humains, des animaux et des objets, avec un seul modèle d'intelligence artificielle.
- Offre un support d'animation complet grâce au jeu de données à grande échelle UniML3D.
- Accélère le flux de travail en standardisant les processus d'animation de personnages.

## Installation

**Préparation de l'environnement**

```
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools<81"
pip install -r requirements.txt --no-build-isolation
```

## Exécution

**Création d'une animation exemple**

```
python -m unimate.inference.sample \
    --exp_dir outputs/uniml3d_60frames_graph_adaln \
    --test_cases_json test_cases.json \
    --num_repetitions 3
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Comment puis-je animer mes modèles de personnages ayant des structures squelettiques différentes dans un format standard en utilisant le projet UniMate ? Expliquez étape par étape le processus de création d'animation en tirant parti du jeu de données UniML3D et des points de contrôle pré-entraînés fournis par le projet.

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux artistes 3D et aux développeurs souhaitant automatiser les processus d'animation de personnages et effectuer des transitions entre différentes structures squelettiques.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/Friedrich-M/UniMate)
- [Lire en turc →](https://trescout.com/discover/unimate/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-02 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/unimate/
