# Conversion rapide de la parole sur les systèmes locaux

Transcribe.cpp est une bibliothèque d'inférence parole-texte développée en C++ qui prend en charge plus de 16 familles de modèles. Utilisant l'infrastructure ggml, cet outil permet à différents modèles de traitement audio de s'exécuter efficacement sur les systèmes locaux.

- ★ 1 982
- C++
- GitHub Trending · 2026-07-21

## Mises à jour

- **4 octobre 2026:** Étoiles 1,981 → 1,982, dernière version v0.3.1 (4 octobre 2026).
- **3 octobre 2026:** Étoiles 1,963 → 1,981, dernière version v0.3.0 (3 octobre 2026).
- **27 septembre 2026:** Étoiles 1,865 → 1,963, dernière version v0.2.4 (25 septembre 2026).
- **31 août 2026:** Étoiles 1,825 → 1,865, dernière version v0.2.3 (30 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite convertir un fichier audio local en texte à l'aide de l'outil Transcribe.cpp. Comment puis-je traiter mon fichier audio au format WAV mono 16 kHz à l'aide de l'outil transcribe-cli compilé sur mon système et du fichier modèle au format GGUF que j'ai téléchargé ? Veuillez expliquer la structure de commande requise pour ce processus et les chemins de fichiers auxquels je dois prêter attention.

## Termes liés du glossaire

- [Speech-to-Text](https://trescout.com/fr/dictionary/speech-to-text/)
- [STT](https://trescout.com/fr/dictionary/stt/)
- [GGUF](https://trescout.com/fr/dictionary/gguf/)
- [Inference](https://trescout.com/fr/dictionary/inference/)
- [CPU](https://trescout.com/fr/dictionary/cpu/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent exécuter des systèmes de reconnaissance vocale rapides et axés sur la confidentialité sur leur propre matériel.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/handy-computer/transcribe.cpp)
- [Lire en turc →](https://trescout.com/discover/transcribe-cpp/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-21 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/transcribe-cpp/
