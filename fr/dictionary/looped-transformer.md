# Qu'est-ce que Looped Transformer ?

Il s'agit d'une architecture d'intelligence artificielle qui réduit l'utilisation de la mémoire en utilisant les mêmes couches de traitement à plusieurs reprises.

## Définition
Alors que les modèles traditionnels nécessitent une unité de traitement distincte pour chaque couche, cette architecture utilise la même couche de manière répétée dans une boucle. Cela permet de réduire la taille du modèle et de consommer moins de mémoire. L'objectif est de faire fonctionner de grands modèles sur des appareils plus petits sans sacrifier les performances.

## Comment ça marche
Les données entrent dans le modèle et passent plusieurs fois par le même bloc de couches. À chaque passage, les données sont traitées un peu plus jusqu'à atteindre le résultat final.

## Où est-ce utilisé
Il est privilégié pour les appareils à faibles ressources ou les applications d'intelligence artificielle mobile.

## Souvent confondu avec
Il peut être confondu avec l'architecture transformer standard, mais ici, le nombre de couches est physiquement plus réduit.

## Questions fréquentes
**Est-ce qu'il fonctionne plus lentement ?**
Comme il réutilise les couches, il peut nécessiter un peu plus de temps de traitement, mais il permet d'économiser de la mémoire.

**Pourquoi tous les modèles ne sont-ils pas comme ça ?**
Pour certaines tâches complexes, il est préférable que chaque couche soit spécialisée pour obtenir de meilleurs résultats.


## Termes liés
- [Transformer](/fr/dictionary/transformer/)
- [Quantization](/fr/dictionary/quantization/)
- [SLM](/fr/dictionary/slm/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/looped-transformer/
