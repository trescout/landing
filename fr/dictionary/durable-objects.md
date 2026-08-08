# Qu'est-ce que Durable Objects ?

Ce sont de petites unités logicielles qui fonctionnent en permanence sur Internet et peuvent stocker des données sans perdre leur état.

## Définition
Normalement, les programmes sur Internet sont temporaires, mais ces structures fonctionnent sans interruption en gardant les données en elles-mêmes. Ils n'oublient pas les données même à la fin d'une interaction utilisateur. Idéal pour maintenir la cohérence dans les systèmes distribués.

## Comment ça marche
Ils vivent sur le serveur avec une identité spécifique et traitent chaque demande entrante avec l'état actuel dans leur mémoire.

## Où est-ce utilisé
Il est utilisé dans les jeux en temps réel, les applications de chat et les services Web dont l'état doit être maintenu.

## Souvent confondu avec
A ne pas confondre avec les fonctions de serveur temporaires (sans serveur) ; parce qu'ils repartent de zéro à chaque fois.

## Questions fréquentes
**Où sont stockées les données ?**
Il est stocké dans le volume lui-même, c'est-à-dire directement dans le cadre de l'environnement d'exploitation.


## Termes liés
- [Runtime](/fr/dictionary/runtime/)
- [State Management](/fr/dictionary/state-management/)
- [Distributed](/fr/dictionary/distributed/)

## Outils liés
- [Celld](/fr/discover/celld/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/durable-objects/
