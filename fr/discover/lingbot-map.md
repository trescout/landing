# Créez des scènes tridimensionnelles à partir de données en streaming

Lingbot-map est un modèle de base 3D à rétroaction conçu pour reconstruire des scènes à partir de données en streaming. Le projet optimise les processus de visualisation en traitant des données environnementales complexes, grâce à son architecture développée en langage Python.

- ★ 17 060
- Python
- GitHub Trending · 2026-06-29

## Mises à jour

- **16 septembre 2026:** Étoiles 16,054 → 17,060.
- **2 août 2026:** Étoiles 8,439 → 16,054.

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer une scène 3D à partir de données diffusées en continu à l'aide de LingBot-Map. J'ai terminé l'installation et mon fichier modèle est prêt. Comment puis-je lancer l'interface de visualisation dans mon navigateur local à l'aide de la commande requise pour exécuter l'instance Courthouse ?

## Termes liés du glossaire

- [Foundation Model](https://trescout.com/fr/dictionary/foundation-model/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux chercheurs et développeurs intéressés par la vision par ordinateur 3D et le traitement des données en streaming.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/Robbyant/lingbot-map)
- [Lire en turc →](https://trescout.com/discover/lingbot-map/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-29 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/lingbot-map/
