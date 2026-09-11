# Exécutez des modèles d'IA massifs localement

Colibri est un moteur basé sur le langage C qui permet d'exécuter des modèles de mélange d'experts (Mixture of Experts) à grande échelle sur des ordinateurs locaux avec de faibles exigences matérielles. En traitant les couches d'experts par flux depuis le disque, il permet d'exécuter des modèles d'IA à haute capacité sur du matériel limité.

- ★ 27 610
- C
- GitHub Trending · 2026-09-11

## Ce que ça vous apporte
- Exécute des modèles à haute capacité sur du matériel limité
- Gère la VRAM, la RAM et la mémoire disque comme une seule couche
- Assure l'efficacité en traitant les couches d'experts par flux

## Installation
**Compilation à partir du code source**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
```


## Exécution
**Lancer l'interface de chat**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable  (+ make cuda-dsv4-dg-dll on RTX 50)
```


## Si vous ne codez pas
Je souhaite exécuter des modèles d'IA à grande échelle sur mon ordinateur local en utilisant le moteur Colibri. Aidez-moi à configurer mes ressources matérielles (VRAM, RAM et disque NVMe) de la manière la plus efficace possible. Expliquez étape par étape comment optimiser et exécuter des modèles tels que GLM ou DeepSeek en fonction de la capacité mémoire de mon système.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/colibri/
