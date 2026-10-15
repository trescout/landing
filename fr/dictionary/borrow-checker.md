# Qu'est-ce que Borrow Checker ?

*Dev · Dernière mise à jour : 13 octobre 2026*

Le mécanisme qui empêche les programmes écrits en langage Rust de commettre des erreurs de mémoire et contrôle la manière dont les données sont utilisées.

## Définition

L'emprunteur est l'une des parties les plus importantes du compilateur Rust et garantit une utilisation sûre de la mémoire. Il examine méticuleusement si plusieurs endroits accèdent aux mêmes données en même temps dans le code que vous écrivez, et si la durée de vie des données est suffisante. Lorsqu'il détecte une situation qui ne respecte pas la règle de sécurité, il empêche le programme de s'exécuter et vous avertit.

***Analogie :** C'est un registre de suivi strict dans un laboratoire sensible, qui garantit qu'un seul chercheur à la fois peut emprunter un équipement spécial et le ramener lorsqu'il a terminé.*

## Comment ça marche

Il entre en action en arrière-plan lorsque vous essayez de compiler votre code. Il examine les règles de propriété des variables et les durées d'emprunt. S'il détecte un partage de données contraire aux règles, il arrête la compilation et indique où se trouve l'erreur.

## Où est-ce utilisé

En programmation système, il fonctionne activement lors de la phase de compilation pour les projets Rust qui souhaitent prévenir les fuites de mémoire et les plantages dès le départ.

## Souvent confondu avec

Il est différent des débogueurs normaux ; il fonctionne pendant que le code est écrit et compilé, et non pendant que le programme s'exécute.

## Questions fréquentes

**Pourquoi est-il si strict ?**

Il prend des mesures préventives à un stade précoce pour éliminer complètement les plantages de mémoire au moment de l'exécution.

**Est-ce que cela ralentit l'exécution ?**

Non, il fonctionne uniquement au stade de la compilation et n'entraîne aucun coût supplémentaire au moment de l'exécution.

## Termes liés

- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Compiler](https://trescout.com/fr/dictionary/compiler/)
- [Thread-safety](https://trescout.com/fr/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/fr/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/borrow-checker/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/borrow-checker/
