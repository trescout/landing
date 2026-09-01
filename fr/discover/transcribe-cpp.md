# Conversion rapide de la parole sur les systèmes locaux

Transcribe.cpp est une bibliothèque d'inférence parole-texte développée en C++ qui prend en charge plus de 16 familles de modèles. Utilisant l'infrastructure ggml, cet outil permet à différents modèles de traitement audio de s'exécuter efficacement sur les systèmes locaux.

- ★ 1 865
- C++
- GitHub Trending · 2026-07-21

## Ce que ça vous apporte
- Prise en charge de 16 familles de modèles différentes
- Hautes performances sur GPU et CPU
- Inférence efficace avec le format GGUF

## Installation
**Installation Linux prise en charge par Vulkan**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```


## Si vous ne codez pas
Je souhaite convertir un fichier audio local en texte à l'aide de l'outil Transcribe.cpp. Comment puis-je traiter mon fichier audio au format WAV mono 16 kHz à l'aide de l'outil transcribe-cli compilé sur mon système et du fichier modèle au format GGUF que j'ai téléchargé ? Veuillez expliquer la structure de commande requise pour ce processus et les chemins de fichiers auxquels je dois prêter attention.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/transcribe-cpp/
