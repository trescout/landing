# Qu'est-ce que Object Storage System ?

Il s'agit d'une méthode de stockage à grande échelle qui conserve les données avec des identifiants uniques au lieu de dossiers de fichiers.

## Définition
Le système de fichiers de votre ordinateur traditionnel ressemble à une structure en arbre ; il progresse sous forme de dossiers dans des dossiers. Le stockage d'objets, quant à lui, traite la donnée comme un objet et lui attribue une identité spécifique. Ainsi, au lieu de suivre des chemins de dossiers pour accéder aux données, vous pouvez y accéder rapidement en utilisant directement cet identifiant.

## Comment ça marche
Lorsque la donnée est chargée dans le système, elle devient un objet et des descriptions (métadonnées) y sont ajoutées. Lorsque vous en avez besoin, vous appelez cet objet via son identifiant.

## Où est-ce utilisé
Il est utilisé dans les services de stockage cloud, les sauvegardes de données volumineuses et la diffusion de contenus multimédias.

## Souvent confondu avec
Il peut être confondu avec les systèmes de fichiers des disques durs classiques ; cependant, ce système est conçu pour des données beaucoup plus volumineuses.

## Questions fréquentes
**Pourquoi n'utilise-t-il pas de dossiers ?**
Parce que gérer des milliards de données dans une structure de dossiers est très lent, alors que le système d'objets est beaucoup plus rapide.


## Termes liés
- [Database](/fr/dictionary/database/)
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [Data Layer](/fr/dictionary/data-layer/)

## Outils liés
- [Rustfs](/fr/discover/rustfs/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/object-storage-system/
