# Qu'est-ce que Userspace ?

Une zone sûre où les applications utilisateur s'exécutent sans interférer avec le noyau de l'ordinateur.

## Définition
Les systèmes d'exploitation sont divisés en deux parties principales : le noyau et l'espace utilisateur. L'espace utilisateur est l'endroit où s'exécutent le navigateur, le lecteur de musique ou les éditeurs de code que vous utilisez. Une erreur ici ne fera pas planter l’ensemble de l’ordinateur, elle n’affectera que cette application.

## Comment ça marche
Les applications demandent l'autorisation au noyau pour accéder aux ressources sous-jacentes du système. De cette façon, le reste du système est protégé.

## Où est-ce utilisé
Il s'agit d'un concept fondamental dans le développement de logiciels, la sécurité et l'architecture système.

## Souvent confondu avec
Il est confondu avec l'espace noyau ; Le noyau domine l'ensemble du système, tandis que l'espace utilisateur est limité.

## Questions fréquentes
**Pourquoi cette distinction existe-t-elle ?**
Pour la sécurité et la stabilité ; Pour empêcher les applications de corrompre le système.

**Où s'exécute le code que j'ai écrit ?**
La plupart des applications et du code s'exécutent dans l'espace utilisateur.


## Termes liés
- [Runtime](/fr/dictionary/runtime/)
- [Containers](/fr/dictionary/containers/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/userspace/
