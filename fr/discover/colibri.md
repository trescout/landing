# Exécutez des modèles d'IA massifs localement

Colibri est un moteur basé sur le langage C qui permet d'exécuter des modèles de mélange d'experts (Mixture of Experts) à grande échelle sur des ordinateurs locaux avec de faibles exigences matérielles. En traitant les couches d'experts par flux depuis le disque, il permet d'exécuter des modèles d'IA à haute capacité sur du matériel limité.

- ★ 40 157
- C
- GitHub Trending · 2026-09-11

## Mises à jour

- **7 octobre 2026:** Étoiles 39,698 → 40,157, dernière version v2.0.0 (6 octobre 2026).
- **5 octobre 2026:** Étoiles 37,791 → 39,698, dernière version v1.12.1 (24 septembre 2026).
- **27 septembre 2026:** Étoiles 36,260 → 37,791, dernière version v1.12.1 (24 septembre 2026).
- **19 septembre 2026:** Étoiles 34,474 → 36,260, dernière version v1.11.0 (13 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite exécuter des modèles d'IA à grande échelle sur mon ordinateur local en utilisant le moteur Colibri. Aidez-moi à configurer mes ressources matérielles (VRAM, RAM et disque NVMe) de la manière la plus efficace possible. Expliquez étape par étape comment optimiser et exécuter des modèles tels que GLM ou DeepSeek en fonction de la capacité mémoire de mon système.

## Termes liés du glossaire

- [Mixture of Experts](https://trescout.com/fr/dictionary/mixture-of-experts/)
- [VRAM](https://trescout.com/fr/dictionary/vram/)
- [RAM](https://trescout.com/fr/dictionary/ram/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux chercheurs et aux développeurs souhaitant exécuter des modèles de langage volumineux sur leur propre ordinateur avec des ressources matérielles limitées.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/JustVugg/colibri)
- [Lire en turc →](https://trescout.com/discover/colibri/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-11 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/colibri/
