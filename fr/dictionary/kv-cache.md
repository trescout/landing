# Qu'est-ce que KV Cache ?

> Key-Value Cache

Il s’agit d’une méthode d’accélération qui évite à l’intelligence artificielle de répéter les mêmes opérations en gardant dans sa mémoire les mots qu’elle a préalablement traités.

## Définition
Lors de la production d'un texte, au lieu de repenser chaque mot à partir de zéro, l'intelligence artificielle stocke les informations précédemment traitées dans un cache sous forme de valeurs « Clé » et « Valeur ». Ce système permet au modèle de rappeler rapidement le passé sans avoir à le recalculer lors de la prédiction du mot suivant. Ainsi, la charge de traitement est réduite et les temps de réponse sont considérablement raccourcis.

## Comment ça marche
Pendant l'exécution du modèle, il est automatiquement créé en arrière-plan et conservé en mémoire. Ce cache commence à se remplir lorsque l'utilisateur démarre une longue conversation. Lorsque la mémoire est pleine, le système développe des stratégies pour effacer les anciennes informations ou faire de la place pour de nouvelles données.

## Où est-ce utilisé
Il est utilisé dans les processus de travail des LLM et notamment dans les interfaces de chat où sont produits des textes longs.

## Souvent confondu avec
Il peut être confondu avec Context Window, mais il ne s'agit pas d'une limite de capacité, mais d'une méthode permettant d'utiliser efficacement cette capacité.

## Questions fréquentes
**Pourquoi le cache KV est-il important ?**
En empêchant l’intelligence artificielle de calculer encore et encore la même phrase, elle réduit la charge du processeur et accélère la réponse.

**Que se passe-t-il si la mémoire est pleine ?**
Le système peut devenir incapable de traiter de nouvelles données ou commencer à oublier d'anciennes informations.


## Termes liés
- [LLM](/fr/dictionary/llm/)
- [Context Window](/fr/dictionary/context-window/)
- [Inference](/fr/dictionary/inference/)
- [Memory Management](/fr/dictionary/memory-management/)

## Outils liés
- [LMCache](/fr/discover/lmcache/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/kv-cache/
