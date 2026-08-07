# Qu'est-ce que Thread-safety ?

Fonction de sécurité d'un programme qui empêche la corruption des données lors de l'exécution de plusieurs opérations en même temps.

## Définition
Les ordinateurs font plusieurs choses à la fois. Si deux processus différents tentent de modifier les mêmes données en même temps, le chaos se produira. Cette fonctionnalité permet aux processus de s'attendre ou de s'exécuter de manière séquentielle.

## Comment ça marche
Les règles d'accès aux données sont déterminées lors de l'écriture du programme. Tandis qu'un processus utilise les données, les autres semblent avoir un statut « verrouillé ».

## Où est-ce utilisé
Il est obligatoire pour les applications bancaires, les serveurs web et tous les logiciels multitâches.

## Souvent confondu avec
Il ne s’agit pas seulement de sécurité (piratage), mais aussi de cohérence des données.

## Questions fréquentes
**Que se passe-t-il s’il n’est pas thread-safe ?**
Vos données sont perturbées, les applications plantent ou des erreurs de calcul se produisent.


## Termes liés
- [Concurrency](/fr/dictionary/concurrency/)
- [System Programming Language](/fr/dictionary/system-programming-language/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/thread-safety/
