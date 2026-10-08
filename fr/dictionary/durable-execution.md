# Qu'est-ce que Durable Execution ?

*Glossaire · Dev · Dernière mise à jour : 8 juin 2026*

Il s'agit d'un système qui permet à un processus de continuer en toute sécurité là où il s'est arrêté, même en cas d'erreur ou d'interruption.

## Définition

Normalement, si un programme informatique perd de l'alimentation ou tombe en panne pendant son exécution, tout est supprimé et vous devez recommencer. L'exécution durable enregistre chaque étape du programme, en se souvenant de l'endroit où elle s'est arrêtée au moment de l'interruption. De cette façon, les transactions qui prennent des heures peuvent être effectuées en toute sécurité.

***Analogie :** C'est comme mettre un marque-page en lisant un livre pour ne pas oublier la page ; Vous pouvez continuer là où vous vous êtes arrêté.*

## Comment ça marche

Le système sauvegarde constamment l'état du programme dans une base de données. Lorsqu'une erreur se produit, le système redémarre le processus à partir du dernier point sauvegardé.

## Où est-ce utilisé

Il est utilisé pour les virements bancaires, les longs processus de traitement de données et les flux de travail complexes d’intelligence artificielle.

## Souvent confondu avec

Cela peut être confondu avec la sauvegarde automatique, mais cela préserve la logique de fonctionnement de l'ensemble du programme, pas seulement le fichier.

## Questions fréquentes

**Chaque programme doit-il être durable ?**

Il n’est pas nécessaire pour les transactions courtes, mais il est essentiel pour les transactions critiques qui durent des heures.

**Pourquoi est-ce si important ?**

En cas d’erreur, recommencer tout le processus à partir de zéro est une perte de temps et d’argent.

## Termes liés

- [State Management](https://trescout.com/fr/dictionary/state-management/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [Pg Durable](https://trescout.com/fr/discover/pg-durable/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/durable-execution/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/durable-execution/
