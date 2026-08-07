# Modèles d'IA sur appareil local

Le projet de démonstration Bonsai fournit un ensemble d'outils conçu pour simplifier les processus de déploiement de modèles d'apprentissage automatique. Le logiciel aide les développeurs à optimiser leurs processus d'application en transformant des architectures de modèles complexes en flux de travail gérables.

- ★ 1 587
- Shell
- GitHub Trending · 2026-07-17

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
Je souhaite exécuter des modèles d'IA sur mon appareil local à l'aide du projet bonsai-demo. Après avoir cloné le référentiel git requis pour l'installation, je dois définir les informations de mon jeton HuggingFace et télécharger les dépendances et les modèles avec la commande ./setup.sh. Ensuite, en utilisant la commande ./scripts/start_llama_server.sh, je peux mettre en place le serveur local et interagir avec l'IA via le port 8080 via mon navigateur.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/bonsai-demo/
