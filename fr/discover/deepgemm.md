# Calcul matriciel rapide pour l'intelligence artificielle

DeepGEMM, développé par DeepSeek, est une bibliothèque open-source de sous-programmes d'algèbre linéaire de base (BLAS) qui accélère les opérations de multiplication de matrices sur les processeurs graphiques (GPU). Le logiciel fournit des noyaux (kernels) optimisés pour les modèles d'intelligence artificielle nécessitant des calculs de haute performance.

- ★ 8 528
- Cuda
- GitHub Trending · 2026-10-06

## Ce que ça vous apporte
- Il réduit les temps d'exécution des grands modèles de langage en accélérant les multiplications de matrices.
- Il compile automatiquement les noyaux au moment de l'exécution sans attendre la compilation CUDA lors de l'installation.
- Il réduit les pertes de communication de la carte graphique en combinant différents modèles d'experts en une seule opération.

## Installation
**Clonage du dépôt et de l'environnement de développement h**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Installation de la bibliothèque**

```
cat install.sh
./install.sh
```


## Si vous ne codez pas
Je souhaite installer la bibliothèque DeepGEMM sur mon matériel doté de l'architecture NVIDIA SM90 ou SM100. Tout d'abord, pour cloner le dépôt avec ses sous-modules et préparer l'environnement de développement, exécutez les commandes '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh'. Ensuite, pour terminer l'installation, appliquez la commande 'cat install.sh\n./install.sh' et rendez la bibliothèque prête à l'emploi dans l'environnement Python avec la commande 'import deep_gemm'.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deepgemm/
