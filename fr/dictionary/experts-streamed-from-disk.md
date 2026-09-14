# Qu'est-ce que Experts Streamed from Disk ?

Il s'agit d'une méthode consistant à charger instantanément des parties de modèles d'intelligence artificielle massifs depuis le disque lorsqu'elles ne tiennent pas dans la mémoire.

## Définition
Les modèles d'intelligence artificielle sont parfois si volumineux qu'ils ne tiennent pas dans la capacité RAM de l'ordinateur. Avec cette technique, seules les parties du modèle nécessaires à un instant T (les experts) sont rapidement lues depuis le disque et chargées en mémoire. Ainsi, des modèles très volumineux peuvent fonctionner même sur du matériel limité.

## Comment ça marche
Le système divise les poids du modèle en petits morceaux et les stocke sur le disque. Lorsqu'un utilisateur pose une question, les parties pertinentes du modèle sont transférées très rapidement du disque vers la mémoire, le traitement est effectué, puis la mémoire est libérée.

## Où est-ce utilisé
Il est particulièrement utilisé par les développeurs souhaitant exécuter de très grands modèles de langage sur des ordinateurs domestiques et sur des serveurs ayant des contraintes matérielles.

## Souvent confondu avec
Cela peut être confondu avec le chargement de l'intégralité du modèle en mémoire ; ici, il s'agit uniquement d'un chargement au moment du besoin.

## Questions fréquentes
**Cette méthode réduit-elle la vitesse ?**
Oui, comme l'opération de lecture depuis le disque est plus lente que celle depuis la RAM, un certain délai peut être ressenti dans le temps de réponse du modèle.

**Chaque modèle peut-il fonctionner de cette manière ?**
Le modèle doit avoir été conçu avec cette architecture ; c'est-à-dire qu'il est impératif qu'il possède une structure fragmentée (Mixture of Experts).


## Termes liés
- [Mixture of Experts](/fr/dictionary/mixture-of-experts/)
- [RAM](/fr/dictionary/ram/)
- [Inference Engine](/fr/dictionary/inference-engine/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/experts-streamed-from-disk/
