# Transcrire les sons avec l'intelligence artificielle

Développé par OpenAI, Whisper est un modèle de reconnaissance vocale formé par une méthode d'apprentissage par supervision faible à grande échelle. Il offre des taux de précision élevés dans la conversion et la traduction de données audio multilingues en texte.

- ★ 106 452
- Python
- GitHub Trending · 2026-06-07

## Ce que ça vous apporte
- Convertissez des fichiers audio en texte avec une grande précision.
- Traduire des conversations de différentes langues vers l'anglais.
- Identification de la langue et détection de l'activité vocale dans le contenu audio.

## Installation
**Dépendances du système**

```
sudo apt update && sudo apt install ffmpeg
```

**Exigence d'installation supplémentaire**

```
pip install setuptools-rust
```


## Exécution
**Convertir un fichier audio en texte**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Transcription dans une langue spécifique**

```
whisper japanese.wav --language Japanese
```


## Si vous ne codez pas
Je souhaite convertir mon fichier audio en texte à l'aide de l'outil Whisper. J'ai effectué les installations nécessaires sur mon système. Quelle est la structure de commande de base que je dois saisir dans le terminal pour traduire le contenu de mon fichier audio en texte, et comment dois-je utiliser le paramètre de spécification de langue pour les fichiers audio dans différentes langues ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/whisper/
