# Qu'est-ce que Error Tracking ?

*Glossaire · Dev · Dernière mise à jour : 3 octobre 2026*

Processus de suivi qui capture, regroupe et notifie en temps réel aux développeurs les erreurs d'exécution survenant dans les applications.

## Définition

Le suivi des erreurs (error tracking) est une approche de surveillance qui enregistre automatiquement les plantages et les situations inattendues rencontrées par les utilisateurs dans les logiciels en production. Le système documente étape par étape la source de l'erreur, les détails du système d'exploitation et les actions des utilisateurs ayant déclenché l'erreur. Ainsi, les équipes logicielles ont la possibilité d'intervenir avant que les problèmes ne soient signalés par les utilisateurs.

***Analogie :** C'est semblable au fait qu'un alarme incendie dans un bâtiment ne se contente pas de détecter la fumée, mais indique également aux pompiers le numéro exact de la pièce et la cause de l'incendie.*

## Comment ça marche

Une petite bibliothèque de surveillance intégrée à l'application écoute toutes les exceptions logicielles non interceptées. En cas de dysfonctionnement, la trace de la pile (stack trace) et les données environnementales sont regroupées et envoyées au serveur d'analyse. Le serveur rassemble les erreurs similaires sous un même toit et envoie des notifications aux développeurs par e-mail ou par messagerie instantanée.

## Où est-ce utilisé

Il est activement privilégié dans les applications mobiles où l'expérience utilisateur est critique, les projets web à page unique (SPA) et les architectures de microservices fonctionnant en arrière-plan.

## Souvent confondu avec

Il est différent du concept de journalisation (logging) qui stocke tous les événements du système de manière chronologique : le suivi des erreurs se concentre directement sur les exceptions et analyse et regroupe automatiquement ces problèmes.

## Questions fréquentes

**Les outils de suivi des erreurs enregistrent-ils les données personnelles des utilisateurs ?**

Les systèmes correctement configurés filtrent et masquent automatiquement les données personnelles telles que les mots de passe ou les cartes de crédit avant de les envoyer au serveur.

**Le rapport d'erreur disparaît-il lorsque l'application se ferme soudainement ?**

Non, les informations collectées au moment du plantage sont enregistrées dans la mémoire locale de l'appareil et transmises au centre lors de la réouverture de l'application.

## Termes liés

- [Logging](https://trescout.com/fr/dictionary/logging/)
- [Observability](https://trescout.com/fr/dictionary/observability/)
- [Traces](https://trescout.com/fr/dictionary/traces/)
- [QA](https://trescout.com/fr/dictionary/qa/)
- [Session Replay](https://trescout.com/fr/dictionary/session-replay/)

## Outils liés

- [Sentry](https://trescout.com/fr/discover/sentry/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/error-tracking/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/error-tracking/
