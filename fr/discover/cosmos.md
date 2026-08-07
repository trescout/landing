# Modèles d'intelligence artificielle pour les systèmes physiques

Développée par NVIDIA, Cosmos est une plateforme ouverte qui fournit des modèles mondiaux, des ensembles de données et des outils pour les systèmes physiques tels que les robots et les véhicules autonomes. Il fournit une infrastructure qui permet aux développeurs de créer plus facilement des applications physiques d'IA.

- ★ 11 343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Mise à jour
- 2 août 2026 : Étoile 9 173 → 11 343, dernière version Cosmos3 (1er juin 2026).

## Ce que ça vous apporte
- Il fournit des modèles mondiaux, des ensembles de données et des outils pour les applications physiques d'IA.
- Il peut traiter et produire des séquences textuelles, visuelles, audio et d’action dans une architecture unifiée.
- Fournit des capacités de prévision, de planification et de simulation pour les systèmes robotiques et autonomes.

## Installation
**Installation avec vLLM-Omni**

```
uv pip install --torch-backend=cu130 \
  "vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```


## Exécution
**Production vidéo**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
  --form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
  --form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
  -o cosmos3_t2v.mp4
```


## Si vous ne codez pas
Je souhaite développer des applications d'intelligence artificielle physique à l'aide de la plateforme NVIDIA Cosmos. Expliquez en détail technique les capacités offertes par la famille de modèles Cosmos 3, en particulier les différences dans l'utilisation des surfaces « Reasoner » et « Generator », et comment ces modèles peuvent être configurés dans des scénarios tels que la planification de mission ou la simulation du monde dans des systèmes robotiques et autonomes. Résumez également le processus de travail avec l'outil « uv » et la bibliothèque « vllm-omni » pendant la phase d'installation, étape par étape, en tenant compte des exigences du pilote CUDA.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/cosmos/
