# Noyaux hautes performances pour certains Delta Attention

Développé par Moonshot AI, FlashKDA propose des noyaux hautes performances pour le mécanisme Some Delta Attention. Cette technologie basée sur CUDA vise à accélérer les calculs d'attention dans les grands modèles de langage.

- ★ 1 043
- Cuda
- GitHub Trending · 2026-07-30

## Ce que ça vous apporte
- Calculs d'attention accélérés basés sur CUDA
- Travailler efficacement sur de grands modèles de langage
- Structure du noyau optimisée avec CUTLASS

## Installation
**Configuration de base**

```
git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda
cd flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation .
```

**Construire pour toutes les architectures**

```
FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation .
```


## Exécution
**Utiliser FLA comme back-end**

```
pip install -U flash-linear-attention
```


## Si vous ne codez pas
Je souhaite accélérer certains calculs Delta Attention à l'aide de l'outil FlashKDA. Comment puis-je optimiser le mécanisme d'attention de mon modèle en utilisant la fonction chunk_kda sous torch.inference_mode(), intégrée à la bibliothèque flash-linear-attention ? Veuillez créer un exemple d'application, en tenant compte des paramètres nécessaires et de la configuration matérielle requise auxquels je dois prêter attention.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/flashkda/
