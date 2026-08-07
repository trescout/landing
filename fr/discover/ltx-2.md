# Production vidéo avec intelligence artificielle dans le système local

Développé par Lightricks, LTX-2 propose un package de formation Python d'inférence et d'adaptation de bas rang (LoRA) pour les modèles d'intelligence artificielle qui produisent de l'audio et de la vidéo. Cet ensemble d'outils permet aux utilisateurs de former des modèles LTX-2 avec leurs propres données et d'exécuter les sorties du modèle sur les systèmes locaux.

- ★ 7 550
- GitHub Trending · 2026-06-19

## Ce que ça vous apporte
- Fournit une synchronisation audio et vidéo
- Vous pouvez entraîner LoRA avec vos propres données
- Production vidéo de haute qualité sur système local

## Installation
**Clonez le référentiel depuis GitHub et entrez dans le répertoire**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Télécharger les poids des modèles (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```


## Exécution
**exécuter un pipeline d'inférence avec uv**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```


## Si vous ne codez pas
Veuillez créer une vidéo à l'aide du modèle LTX-2 qui décrit la scène que je souhaite en détail et inclut la synchronisation audio et vidéo. Demandez au modèle de produire une sortie en spécifiant les détails de la scène, l'apparence du personnage, l'angle de la caméra et le texte vocal.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ltx-2/
