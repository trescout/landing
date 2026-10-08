# Outils pour les projets de vision par ordinateur

Développé par Roboflow, Supervision propose des outils et fonctions auxiliaires réutilisables pour les projets de vision par ordinateur. Cette bibliothèque basée sur Python accélère les flux de travail de développement en facilitant les opérations standard dans les processus tels que la détection et le suivi d'objets.

- ★ 51 154
- Python
- GitHub Trending · 2026-06-09

## Mises à jour

- **8 octobre 2026:** Étoiles 51,146 → 51,154, dernière version 0.30.9 (8 octobre 2026).
- **7 octobre 2026:** Étoiles 51,118 → 51,146, dernière version 0.30.8 (6 octobre 2026).
- **4 octobre 2026:** Étoiles 51,075 → 51,118, dernière version 0.30.7 (4 octobre 2026).
- **29 septembre 2026:** Étoiles 51,054 → 51,075, dernière version 0.30.6 (29 septembre 2026).

## Ce que ça vous apporte

- Il accélère les processus de chargement et de traitement des données dans les projets de vision par ordinateur.
- Il simplifie le développement d'applications en standardisant les opérations telles que la détection et le suivi d'objets.
- Il permet la visualisation et la gestion des ensembles de données en fonctionnant de manière compatible avec différentes bibliothèques de modèles.

## Installation

**Installation du paquet**

```
pip install supervision
```

## Exécution

**Marquage d'un objet sur l'image**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

J'ai installé la bibliothèque avec la commande pip install supervision dans un environnement Python 3.9 ou supérieur. Je souhaite visualiser les résultats de la détection d'objets et gérer mon ensemble de données dans mon projet de vision par ordinateur. Comment marquer les résultats de détection d'objets sur une image à l'aide de la bibliothèque Supervision et comment charger et convertir des jeux de données dans différents formats (COCO, YOLO, etc.) ? S'il vous plaît, aidez-moi à créer un exemple de flux de travail à l'aide des outils d'annotation et d'assistance aux ensembles de données fournis par la bibliothèque.

## Termes liés du glossaire

- [Computer Vision](https://trescout.com/fr/dictionary/computer-vision/)
- [Computer Vision](https://trescout.com/fr/dictionary/cv/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs Python qui souhaitent normaliser les processus de détection et de suivi d'objets dans les projets de vision par ordinateur.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/roboflow/supervision)
- [Lire en turc →](https://trescout.com/discover/supervision/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-09 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/supervision/
