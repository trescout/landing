# Modèle de langage de 64 millions de paramètres formé à partir de zéro en deux heures

MiniMind propose des étapes de tokenisation, de pré-formation, de réglage fin supervisé (SFT), LoRA et DPO avec des codes PyTorch nus pour les développeurs qui souhaitent comprendre les principes de fonctionnement des grands modèles de langage (LLM).

- ★ 62 670
- Python
- GitHub Trending · 2026-08-31

## Mises à jour

- **27 septembre 2026:** Étoiles 55,708 → 62,670, dernière version v2 (21 octobre 2025).

## Ce que ça vous apporte

- Formation de 2 heures sur le matériel grand public : Architecture compacte pouvant être formée à partir de zéro en 2 heures environ sur une seule carte graphique NVIDIA RTX 3090/4090.
- Cycle de vie complet de la formation LLM : tokenisation BPE, pré-formation, réglage fin supervisé (SFT), adaptation LoRA et pipeline d'alignement DPO.
- Base de code minimaliste et lisible : blocs Transparent Transformer écrits en pur PyTorch, sans abstractions tierces complexes.
- Prise en charge de MoE (Expert Mix) : possibilité d'essayer d'exécuter une architecture MoE 8x à partir de zéro ainsi que des modèles Dense.
- Excellente ressource éducative et pédagogique : le guide idéal pour les chercheurs qui souhaitent acquérir un aperçu empirique du fonctionnement interne des grands modèles de langage.

## Installation

**Clonage du référentiel et installation des dépendances**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

## Exécution

**Démarrer le pré-entraînement et tester la sortie du modèle**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```

## Architecture technique et principe de fonctionnement

- Activations RoPE et SwiGLU : normes architecturales modernes avec intégrations de positions rotatives et fonctions d'activation SwiGLU.
- Flux de gradient stable avec RMSNorm : utilisation d'une normalisation de couche RMSNorm plus rapide et plus stable au lieu du LayerNorm traditionnel.
- Intégration de Flash Attention : optimisation de Flash Attention v2 pour calculer rapidement de grandes matrices d'attention dans la mémoire GPU.

## Étapes de formation : Pré-formation, PFT et DPO

- Étape 1 - Pré-entraînement (1-pretrain.py) : Apprend la grammaire et les connaissances générales du monde avec la logique de prédire le prochain jeton sur des textes bruts.
- Phase 2 - Réglage fin supervisé (2-sft.py) : transforme le modèle en un assistant qui obéit aux commandes de l'utilisateur avec des ensembles de données de questions-réponses et d'instructions.
- Étape 3 - Alignement DPO (4-dpo.py) : optimise directement le modèle en fonction des préférences de l'utilisateur via des paires de réponses bonnes et mauvaises.

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite entraîner un modèle de langage de 64 millions de paramètres à partir de zéro avec PyTorch à l'aide du référentiel MiniMind. Pouvez-vous expliquer étape par étape comment préparer le tokenizer basé sur mon propre ensemble de données de texte turc, exécuter le script 1-pretrain.py, puis l'affiner avec LoRA ?

## Questions fréquemment posées

- Quelle quantité de VRAM est nécessaire pour entraîner MiniMind ? Le modèle de paramètres 64M peut être confortablement entraîné sur 6 Go à 12 Go de VRAM en fonction du paramètre de taille du lot ; Même RTX 3060 ou RTX 4060 suffisent.
- Est-ce que ça marche sur Apple Silicon (série Mac M) ? Oui. La formation et l'inférence peuvent également être effectuées sur des ordinateurs Mac avec l'accélération PyTorch MPS (Metal Performance Shaders).
- Les résultats du modèle sont-ils suffisants pour la conversation quotidienne ? Le 64M est un petit modèle ; Il est optimisé pour présenter la structure du langage, la capacité à répondre à des questions de base et à compléter un texte plutôt qu'un raisonnement logique complexe.
- Quels ensembles de données sont prêts à l'emploi ? Le référentiel propose des commandes pour télécharger automatiquement des ensembles de données ouverts filtrés pour la pré-formation en chinois et en anglais et SFT.

## Termes liés du glossaire

- [Tokenizer](https://trescout.com/fr/dictionary/tokenizer/)
- [LoRA](https://trescout.com/fr/dictionary/lora/)
- [VRAM](https://trescout.com/fr/dictionary/vram/)
- [Attention](https://trescout.com/fr/dictionary/attention/)
- [Transformer](https://trescout.com/fr/dictionary/transformer/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)

- **Pour qui:** Chercheurs en IA, ingénieurs en apprentissage automatique, data scientists et étudiants.
- **Licence:** Apache-2.0 (Açık kaynak lisansı)
- **Toit:** Framework LLM minimaliste basé sur PyTorch
- **Plateformes:** Linux, macOS (Apple Silicon MPS), Windows

## Liens

- [Dépôt GitHub →](https://github.com/jingyaogong/minimind)
- [Lire en turc →](https://trescout.com/discover/minimind/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-31 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/minimind/
