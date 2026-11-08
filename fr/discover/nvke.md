# Gestion de Kubernetes pour les cartes graphiques Nvidia

NVIDIA Kubernetes Engine (NVKE) propose un plan de contrôle (management plane) qui permet la gestion de clusters Kubernetes compatibles GPU sur des serveurs bare metal. Développé en langage Go, cet outil fonctionne sur une infrastructure Docker avec la prise en charge de TPM virtuel, simplifiant ainsi les processus de déploiement de clusters et de création de charges de travail.

- ★ 603
- Go
- GitHub Trending · 2026-11-08

## Mises à jour

- **8 novembre 2026:** Étoiles 600 → 603, dernière version v0.23.1 (3 novembre 2026).

## Ce que ça vous apporte

- Configurez des clusters gérés sur votre propre matériel.
- Créez des clusters de charges de travail indépendants.
- Compilez des fichiers binaires à partir du code source.

## Installation

**Compilation à partir du code source**

```
git clone https://github.com/dsx-ai-factory/nvke.git
cd nvke
make build
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite que vous compiliez l'outil NVIDIA Kubernetes Engine à partir du code source en clonant le projet, en accédant au répertoire, puis en exécutant les commandes git clone https://github.com/dsx-ai-factory/nvke.git, cd nvke et make build.

Dépôt : https://github.com/dsx-ai-factory/nvke. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Bare Metal](https://trescout.com/fr/dictionary/bare-metal/)
- [NVKE](https://trescout.com/fr/dictionary/nvke/)
- [Clone](https://trescout.com/fr/dictionary/clone/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux équipes de plateforme qui souhaitent gérer des clusters Kubernetes sur leur propre infrastructure GPU.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/dsx-ai-factory/nvke)
- [Lire en turc →](https://trescout.com/discover/nvke/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-08 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/nvke/
