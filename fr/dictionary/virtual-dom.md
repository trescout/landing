# Qu'est-ce que Virtual DOM ?

*Développement · Dernière mise à jour : 19 novembre 2026*

Technique qui gère les mises à jour via une copie légère de la structure de la vraie page Web conservée en mémoire.

## Définition

Le DOM virtuel est une optimisation des performances utilisée, lorsqu'un changement se produit sur une page Web, pour détecter uniquement la partie modifiée et la refléter sur la réalité au lieu de recharger toute la page. Grâce à cette copie légère fonctionnant en mémoire, le navigateur ne s'épuise pas et les pages fonctionnent de manière beaucoup plus fluide.

***Analogie :** C'est comme dessiner un brouillon au crayon dans un carnet avant d'écrire un livre. Vous faites les erreurs et les modifications sur le brouillon, et une fois nettoyé, vous les transférez dans le livre final en une seule fois.*

## Comment ça marche

Lorsqu'une donnée change dans l'application, le système crée d'abord un nouvel arbre sur le DOM virtuel. Il trouve la différence en comparant l'ancien arbre et le nouveau, et allège la charge de travail du navigateur en transférant uniquement cette petite différence sur le DOM réel.

## Où est-ce utilisé

Il sert d'outil fondamental dans les bibliothèques d'interface modernes et pour la gestion des performances des applications Web monopage.

## Souvent confondu avec

Il peut être confondu avec la structure DOM principale du navigateur. Le DOM virtuel est une couche d'optimisation entièrement temporaire qui réside en mémoire.

## Questions et réponses

**Y a-t-il un DOM virtuel sur chaque site Web ?**

Non, il se trouve généralement dans les projets utilisant des bibliothèques d'interface modernes et avancées comme React.

**Est-il plus rapide que le DOM réel ?**

Étant donné que la modification directe du DOM est coûteuse, effectuer une comparaison virtuelle accélère généralement le site Web.

## Termes liés

- [DOM](https://trescout.com/fr/dictionary/dom/)
- [Frontend](https://trescout.com/fr/dictionary/frontend/)
- [Framework](https://trescout.com/fr/dictionary/framework/)

## Outils liés

- [Solid](https://trescout.com/fr/discover/solid/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/virtual-dom/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/virtual-dom/
