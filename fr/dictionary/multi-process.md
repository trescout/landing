# Qu'est-ce que Multi-process ?

*Glossaire · Dev · Dernière mise à jour : 7 octobre 2026*

C'est une méthode qui consiste, pour un programme informatique, à exécuter simultanément ses tâches en les divisant en plusieurs sous-processus totalement indépendants dotés de leur propre espace mémoire.

## Définition

Dans la programmation traditionnelle, une application s'exécute généralement de manière séquentielle sur un fil d'exécution unique. Avec l'approche multi-processus, le système d'exploitation crée en revanche un espace de travail distinct pour chaque tâche. Grâce à cette méthode, que vous rencontrerez souvent dans le dictionnaire TreScout, si l'un des processus rencontre une erreur et plante, les autres continuent de fonctionner sans être affectés par cette situation.

***Analogie :** Vous pouvez comparer cela à des cuisiniers indépendants travaillant dans la même cuisine mais disposant de leurs propres plans de travail, de leurs propres couteaux et de leurs propres ingrédients. Même si l'un des cuisiniers se coupe et arrête de travailler, les autres peuvent continuer à cuisiner en toute sécurité sur leurs propres plans de travail.*

## Comment ça marche

Au niveau du système d'exploitation, une adresse mémoire distincte est allouée à chaque processus. Le programme génère de nouveaux sous-processus à partir d'un processus principal, et ces processus se partagent les tâches en communiquant entre eux via des canaux de communication dédiés.

## Où est-ce utilisé

Il est fréquemment utilisé, notamment pour exécuter chaque onglet comme un processus distinct dans les navigateurs web, dans les systèmes de traitement de données massives (Big Data) et dans les applications de serveur effectuant des calculs lourds en arrière-plan.

## Souvent confondu avec

Il est souvent confondu avec le concept de multi-threading. Alors que dans la méthode multi-threading les tâches sont exécutées par des threads légers qui partagent le même espace mémoire, dans la méthode multi-processus chaque tâche possède son propre espace mémoire totalement isolé.

## Questions fréquentes

**L'utilisation du multi-processus sollicite-t-elle beaucoup l'ordinateur ?**

Oui, étant donné qu'une mémoire et des ressources distinctes sont allouées à chaque processus, il peut consommer davantage de ressources informatiques par rapport à d'autres méthodes.

**Dans quelles situations faut-il privilégier le multi-processus ?**

Il doit être privilégié pour les tâches lourdes où la sécurité et la stabilité sont primordiales, et où l'on ne souhaite pas qu'elles soient affectées par le plantage d'autres éléments.

## Termes liés

- [Concurrency](https://trescout.com/fr/dictionary/concurrency/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Thread-safety](https://trescout.com/fr/dictionary/thread-safety/)
- [Distributed](https://trescout.com/fr/dictionary/distributed/)

## Outils liés

- [Raddebugger](https://trescout.com/fr/discover/raddebugger/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/multi-process/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/multi-process/
