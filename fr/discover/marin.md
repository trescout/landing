# Plateforme de développement ouverte pour la recherche sur les modèles fondamentaux

Plateforme et ensemble d'outils pour expérimenter les étapes allant du traitement des données à l'entraînement et à l'évaluation des modèles fondamentaux.

- ★ 1 967
- Python
- GitHub Trending · 2026-08-25

## Que fait cet outil ?
Exécute les expériences comme une séquence d'étapes dépendantes dans un ordre topologique. L'exemple officiel montre la tokenisation de TinyStories et l'entraînement d'un petit modèle de langage; l'approche de développement ouverte documente aussi le code, les données, les décisions et les essais infructueux.

## Pour qui ?
Équipes menant des recherches sur la curation, la transformation et le filtrage de données, la tokenisation, l'entraînement de modèles et l'évaluation.

## À quoi ne faut-il pas s’attendre ?
Pas destiné au développement d'applications simples hors du périmètre de la recherche sur les modèles fondamentaux, ni aux utilisateurs qui ne veulent pas configurer Python et l'environnement de développement requis.

## Points forts
- Portée de recherche couvrant le traitement des données, le pré‑entraînement, le fine‑tuning et l'évaluation
- Flux d'expérimentation qui exécute les étapes dépendantes dans un ordre topologique
- Documentation ouverte couvrant également les expériences infructueuses et les décisions de développement

## Premiers pas
- Clonez le dépôt officiel et créez un environnement virtuel Python 3.12 ou supérieur
- Synchronisez les dépendances avec uv
- Configurez la variable d'environnement MARIN_PREFIX
- Exécutez le test smoke TinyStories hors ligne sur le CPU

## Démarrage prudent

## Premier prompt
Lancez comme première validation l'entraînement d'un petit modèle sur CPU avec le flux TinyStories hors ligne.

## Installation
**Cloner le dépôt officiel**

```
git clone https://github.com/marin-community/marin.git
```

**Créer l'environnement Python**

```
uv venv --python 3.12
```

**Installer les dépendances**

```
uv sync --all-packages
```


## Exécution
**Exécuter le test smoke CPU**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```


## Liens
- Dépôt GitHub →
- Documentation d’installation →
- Première expérience →
- README officiel →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/marin/
