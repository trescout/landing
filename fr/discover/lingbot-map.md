# Créez des scènes tridimensionnelles à partir de données en streaming

Lingbot-map est un modèle de base 3D à rétroaction conçu pour reconstruire des scènes à partir de données en streaming. Le projet optimise les processus de visualisation en traitant des données environnementales complexes, grâce à son architecture développée en langage Python.

- ★ 16 054
- Python
- GitHub Trending · 2026-06-29

## Ce que ça vous apporte
- Reconstruction 3D stable de longues séquences vidéo
- Prise en charge de l'inférence de streaming à faible latence
- Architecture d'intelligence artificielle capable de traiter des données environnementales complexes

## Installation
**Préparation de l'environnement et configuration de base**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Installation des bibliothèques requises**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```


## Exécution
**Démarrage de la scène exemple**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
```


## Si vous ne codez pas
Je souhaite créer une scène 3D à partir de données diffusées en continu à l'aide de LingBot-Map. J'ai terminé l'installation et mon fichier modèle est prêt. Comment puis-je lancer l'interface de visualisation dans mon navigateur local à l'aide de la commande requise pour exécuter l'instance Courthouse ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/lingbot-map/
