# Qu'est-ce que Offline-first ?

Il s'agit d'une approche de conception logicielle qui continue d'exécuter toutes les fonctions de base de l'application sans interruption même si la connexion Internet est perdue.

## Définition
Dans cette approche, l'application stocke d'abord les données sur le propre appareil de l'utilisateur et effectue les opérations localement. Dès qu'une connexion Internet est établie, les données de l'appareil sont synchronisées silencieusement avec le serveur cloud en arrière-plan. En tant que TreScout, nous recommandons cette architecture pour maintenir l'expérience utilisateur au plus haut niveau et ne pas être affecté par les interruptions de connexion.

## Comment ça marche
Lorsque l'application est ouverte, elle lit les données de la base de données locale sur l'appareil au lieu de les extraire d'un serveur distant. Tous les nouveaux enregistrements et modifications apportées par l'utilisateur sont d'abord écrits dans cette base de données locale. Un mécanisme de synchronisation spécial exécuté en arrière-plan vérifie en permanence la connexion Internet et synchronise les données de manière bilatérale avec le serveur.

## Où est-ce utilisé
Il est fréquemment utilisé dans les applications de notes utilisées lors des déplacements dans le métro, dans les systèmes de suivi des tâches où les agents de terrain saisissent des données dans des endroits sans connexion Internet et dans les applications cartographiques.

## Souvent confondu avec
Il est confondu avec le mode de fonctionnement hors ligne : alors que le mode hors ligne vise uniquement à éviter les erreurs en l'absence d'Internet, l'approche hors ligne d'abord base le principe de fonctionnement principal de l'application entièrement sur les données locales.

## Questions fréquentes
**Que se passe-t-il si les modifications apportées hors ligne entrent en conflit avec les données d'autres utilisateurs lorsqu'ils sont en ligne ?**
Les algorithmes de résolution de conflits du logiciel entrent en jeu et fusionnent les données en toute sécurité, préservant ou invitant l'utilisateur à indiquer la dernière modification effectuée.

**Les applications hors ligne occupent-elles beaucoup d’espace sur l’appareil ?**
Non, puisque seules les données textuelles et les petits fichiers que l'utilisateur utilise activement sont stockés sur l'appareil, cela ne remplit pas inutilement l'espace de stockage.


## Termes liés
- [Local-first](/fr/dictionary/local-first/)
- [Offline](/fr/dictionary/offline/)
- [Database](/fr/dictionary/database/)
- [State Management](/fr/dictionary/state-management/)

## Outils liés
- [LAP](/fr/discover/lap/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/offline-first/
