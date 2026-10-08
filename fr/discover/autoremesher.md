# Quadrature automatique pour les modèles tridimensionnels

Autoremesher est un outil qui convertit automatiquement les structures de surface irrégulières dans les modèles tridimensionnels en remaillage quadruple. Développé en langage C++, ce logiciel est optimisé pour réaliser des géométries complexes adaptées aux processus d'animation et de modélisation.

- ★ 3 322
- C++
- GitHub Trending · 2026-07-09

## Mises à jour

- **24 août 2026:** Étoiles 3,225 → 3,322, dernière version 1.2.0 (23 août 2026).
- **17 août 2026:** Étoiles 3,087 → 3,225, dernière version 1.1.0 (16 août 2026).
- **2 août 2026:** Étoiles 2,123 → 3,087, dernière version 1.0.0 (6 juillet 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite convertir le fichier de modèle 3D dont je dispose en une structure maillée rectangulaire. Comment puis-je traiter mon fichier d'entrée avec un nombre cible spécifié de quadrilatères, une mise à l'échelle des bords et des paramètres d'arêtes vives à l'aide de l'outil Autoremesher ? Veuillez créer un exemple de configuration que je peux utiliser via la ligne de commande.

## Termes liés du glossaire

- [Quad Remeshing](https://trescout.com/fr/dictionary/quad-remeshing/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Pour les artistes et les développeurs qui ont besoin d'éditer la topologie dans les processus de modélisation et d'animation 3D.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/huxingyi/autoremesher)
- [Lire en turc →](https://trescout.com/discover/autoremesher/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-09 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/autoremesher/
