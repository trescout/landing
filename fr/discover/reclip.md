# Téléchargez des vidéos Internet sur votre propre serveur

Développé par Averygan, Reclip est un outil léger et auto-hébergé permettant de télécharger des vidéos depuis presque tous les sites Internet. Il vous permet d'enregistrer des fichiers multimédias sur votre appareil local via une interface web simple.

- ★ 7 951
- HTML
- GitHub Trending · 2026-09-02

## Ce que ça vous apporte
- Télécharge des fichiers vidéo et audio depuis plus de 1000 sites tels que YouTube et Instagram.
- Enregistre les fichiers téléchargés au format vidéo MP4 ou audio MP3.
- Offre une interface simple et rapide fonctionnant via un navigateur web.

## Installation
**Installation standard**

```
brew install yt-dlp ffmpeg    # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Installation avec Docker**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```


## Exécution
**Accès à l'interface**

```
http://localhost:8899
```


## Si vous ne codez pas
Je souhaite utiliser l'outil Reclip pour télécharger des liens vidéo Internet sur mon appareil local au format MP4 ou MP3. Pour lancer le téléchargement, je dois coller les liens dans la zone de saisie, sélectionner le format, cliquer sur le bouton Fetch pour charger les informations de la vidéo, puis utiliser le bouton Download. Dans ce processus, je peux effectuer des téléchargements groupés et ajuster la résolution vidéo selon mes préférences.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/reclip/
