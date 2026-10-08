# Modèles d'IA sur appareil local

Le projet de démonstration Bonsai fournit un ensemble d'outils conçu pour simplifier les processus de déploiement de modèles d'apprentissage automatique. Le logiciel aide les développeurs à optimiser leurs processus d'application en transformant des architectures de modèles complexes en flux de travail gérables.

- ★ 2 706
- Shell
- GitHub Trending · 2026-07-17

## Mises à jour

- **19 septembre 2026:** Étoiles 1,587 → 2,706.

## Ce que ça vous apporte

- Exécute des modèles hautes performances localement avec une faible utilisation de la mémoire.
- Il offre des fonctionnalités avancées telles que le traitement visuel et le covoiturage.
- Offre une large compatibilité avec différentes architectures matérielles.

## Installation

**Installation MacOS et Linux**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Exécution

**Démarrage du serveur local**

```
./scripts/start_llama_server.sh    # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite exécuter des modèles d'IA sur mon appareil local à l'aide du projet bonsai-demo. Après avoir cloné le référentiel git requis pour l'installation, je dois définir les informations de mon jeton HuggingFace et télécharger les dépendances et les modèles avec la commande ./setup.sh. Ensuite, en utilisant la commande ./scripts/start_llama_server.sh, je peux mettre en place le serveur local et interagir avec l'IA via le port 8080 via mon navigateur.

## Termes liés du glossaire

- [Machine Learning](https://trescout.com/fr/dictionary/machine-learning/)
- [Shell](https://trescout.com/fr/dictionary/shell/)
- [Token](https://trescout.com/fr/dictionary/token/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs qui souhaitent exécuter des modèles d’IA à haut débit sur leur matériel natif.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/PrismML-Eng/Bonsai-demo)
- [Lire en turc →](https://trescout.com/discover/bonsai-demo/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-17 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/bonsai-demo/
