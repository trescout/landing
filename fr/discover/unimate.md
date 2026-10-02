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
Comment puis-je animer mes modèles de personnages ayant des structures squelettiques différentes dans un format standard en utilisant le projet UniMate ? Expliquez étape par étape le processus de création d'animation en tirant parti du jeu de données UniML3D et des points de contrôle pré-entraînés fournis par le projet.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/unimate/
