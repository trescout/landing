# Production vidéo avec intelligence artificielle dans le système local

Développé par Lightricks, LTX-2 propose un package de formation Python d'inférence et d'adaptation de bas rang (LoRA) pour les modèles d'intelligence artificielle qui produisent de l'audio et de la vidéo. Cet ensemble d'outils permet aux utilisateurs de former des modèles LTX-2 avec leurs propres données et d'exécuter les sorties du modèle sur les systèmes locaux.

- ★ 9 567
- GitHub Trending · 2026-06-19

## Mises à jour

- **2 octobre 2026:** Étoiles 9,562 → 9,567, dernière version v1.4.2 (2 octobre 2026).
- **1 octobre 2026:** Étoiles 9,552 → 9,562, dernière version v1.4.1 (30 septembre 2026).
- **29 septembre 2026:** Étoiles 9,267 → 9,552, dernière version v1.4.0 (29 septembre 2026).
- **27 août 2026:** Étoiles 8,587 → 9,267, dernière version v1.3.0 (26 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Veuillez créer une vidéo à l'aide du modèle LTX-2 qui décrit la scène que je souhaite en détail et inclut la synchronisation audio et vidéo. Demandez au modèle de produire une sortie en spécifiant les détails de la scène, l'apparence du personnage, l'angle de la caméra et le texte vocal.

## Termes liés du glossaire

- [LoRA](https://trescout.com/fr/dictionary/lora/)
- [Inference](https://trescout.com/fr/dictionary/inference/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Pour les utilisateurs qui souhaitent créer des vidéos IA audio et vidéo ou former des modèles sur leur propre système local.

## Liens

- [Dépôt GitHub →](https://github.com/Lightricks/LTX-2)
- [Lire en turc →](https://trescout.com/discover/ltx-2/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-19 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ltx-2/
