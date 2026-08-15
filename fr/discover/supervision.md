# Outils pour les projets de vision par ordinateur

Développé par Roboflow, Supervision propose des outils et fonctions auxiliaires réutilisables pour les projets de vision par ordinateur. Cette bibliothèque basée sur Python accélère les flux de travail de développement en facilitant les opérations standard dans les processus tels que la détection et le suivi d'objets.

- ★ 49 033
- Python
- GitHub Trending · 2026-06-09

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
J'ai installé la bibliothèque avec la commande pip install supervision dans un environnement Python 3.9 ou supérieur. Je souhaite visualiser les résultats de la détection d'objets et gérer mon ensemble de données dans mon projet de vision par ordinateur. Comment marquer les résultats de détection d'objets sur une image à l'aide de la bibliothèque Supervision et comment charger et convertir des jeux de données dans différents formats (COCO, YOLO, etc.) ? S'il vous plaît, aidez-moi à créer un exemple de flux de travail à l'aide des outils d'annotation et d'assistance aux ensembles de données fournis par la bibliothèque.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/supervision/
