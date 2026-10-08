# Générez des vidéos longues de manière cohérente

Développé par Meituan, LongCat-Video est un framework de génération vidéo utilisé pour créer des vidéos longues de manière cohérente. Cet outil permet de produire des contenus vidéo de plus longue durée et de haute qualité tout en préservant la cohérence visuelle.

- ★ 8 892
- Python
- GitHub Trending · 2026-10-04

## Ce que ça vous apporte

- Vous pouvez générer de nouveaux contenus de longue durée à partir de textes, d'images ou de vidéos existantes.
- Vous pouvez obtenir des résultats sans dérive des couleurs ni baisse de qualité dans des vidéos de plusieurs minutes.
- Vous pouvez créer des animations de personnages synchronisées avec le son en utilisant des fichiers audio.

## Installation

**Téléchargement du dépôt de code sur l'ordinateur**

```
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

**Téléchargement des poids du modèle**

```
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer le projet LongCat-Video sur mon système. Veuillez me guider étape par étape pour télécharger le code source avec les commandes 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' et 'cd LongCat-Video', puis pour exécuter les commandes de téléchargement avec 'pip install "huggingface_hub[cli]"' afin d'accéder aux fichiers requis via la bibliothèque de modèles Hugging Face.

## Termes liés du glossaire

- [Clone](https://trescout.com/fr/dictionary/clone/)
- [Framework](https://trescout.com/fr/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il est destiné aux développeurs et aux créateurs de contenu qui souhaitent générer des vidéos de haute qualité et de longue durée à partir d'entrées textuelles, visuelles ou audio à l'aide de l'intelligence artificielle.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/meituan-longcat/LongCat-Video)
- [Lire en turc →](https://trescout.com/discover/longcat-video/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-04 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/longcat-video/
