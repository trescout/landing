# Quadrature automatique pour les modèles tridimensionnels

Autoremesher est un outil qui convertit automatiquement les structures de surface irrégulières dans les modèles tridimensionnels en remaillage quadruple. Développé en langage C++, ce logiciel est optimisé pour réaliser des géométries complexes adaptées aux processus d'animation et de modélisation.

- ★ 3 087
- C++
- GitHub Trending · 2026-07-09

## Mise à jour
- 2 août 2026 : Étoile 2 123 → 3 087, dernière version 1.0.0 (6 juillet 2026).

## Ce que ça vous apporte
- Transforme les modèles complexes en maillages rectangulaires épurés
- Fournit une topologie optimisée pour les processus d'animation
- Offre une prise en charge du traitement par lots via la ligne de commande

## Installation
**Compilation sous Linux**

```
# Install Qt and build tools
sudo apt install build-essential qt5-qmake qtbase5-dev qttools5-dev-tools libqt5svg5-dev libqt5multimedia5-dev

# Install TBB and OpenGL
sudo apt install libtbb-dev libgl1-mesa-dev

# Clone and build
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake
make -j$(nproc)
```

**Construire sur macOS**

```
# Install Xcode Command Line Tools
xcode-select --install

# Install dependencies via Homebrew
brew install qt@5 tbb cmake

# Build
export PATH="/usr/local/opt/qt@5/bin:$PATH"
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake CONFIG+=sdk_no_version_check
make -j$(sysctl -n hw.logicalcpu)
```


## Si vous ne codez pas
Je souhaite convertir le fichier de modèle 3D dont je dispose en une structure maillée rectangulaire. Comment puis-je traiter mon fichier d'entrée avec un nombre cible spécifié de quadrilatères, une mise à l'échelle des bords et des paramètres d'arêtes vives à l'aide de l'outil Autoremesher ? Veuillez créer un exemple de configuration que je peux utiliser via la ligne de commande.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/autoremesher/
