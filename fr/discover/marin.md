# Plateforme de développement ouverte pour la recherche sur les modèles fondamentaux

Plateforme et ensemble d'outils pour expérimenter les étapes allant du traitement des données à l'entraînement et à l'évaluation des modèles fondamentaux.

- ★ 3 089
- Python
- GitHub Trending · 2026-08-25

## Mises à jour

- **31 août 2026:** Étoiles 1,967 → 3,089.

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

1. Clonez le dépôt officiel et créez un environnement virtuel Python 3.12 ou supérieur
2. Synchronisez les dépendances avec uv
3. Configurez la variable d'environnement MARIN_PREFIX
4. Exécutez le test smoke TinyStories hors ligne sur le CPU

## Démarrage prudent

Le test smoke CPU sert uniquement à la validation initiale. Les dépendances CPU, GPU et TPU peuvent nécessiter des matériels additionnels distincts. WANDB_API_KEY et HF_TOKEN ne sont nécessaires que pour le suivi ou les workflows avec modèles fermés.

## Premier prompt

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Lancez comme première validation l'entraînement d'un petit modèle sur CPU avec le flux TinyStories hors ligne.

## Termes liés du glossaire

- [CPU](https://trescout.com/fr/dictionary/cpu/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)

## Liens

- [Dépôt GitHub →](https://github.com/marin-community/marin)
- [Documentation d’installation →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [Première expérience →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [README officiel →](https://github.com/marin-community/marin)
- [Lire en turc →](https://trescout.com/discover/marin/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/marin/
