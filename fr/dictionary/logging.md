# Qu'est-ce que Logging ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

La journalisation (ou logging) consiste à enregistrer les événements d'un programme de manière chronologique.

## Définition et origine du mot

Un journal (log) est un registre d'événements. Lorsqu'un programme rencontre une erreur silencieuse, il est possible de consulter ce registre pour comprendre ce qu'il a fait jusqu'à ce moment-là. C'est comme la boîte noire d'un avion : c'est le premier endroit que l'on examine après un incident.

***Analogie :** C'est comme la boîte noire d'un avion qui enregistre les données de vol ; les actions du programme sont consignées dans un journal.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Présentateur:** Débogage.
**Produit:** Suivi d'utilisation.
**Sécurité :** Journalisation des événements.

## Profondeur technique et architecture

Niveaux :

**DEBUG :** Détail pour le développeur.
**INFO :** Flux normal.
**ATTENTION :** Situation suspecte.
**ERREUR :** Tâche échouée.

Règles :

**Journal structuré :** Format JSON, interrogeable.
**Interdiction des PII :** Les mots de passe et les identifiants ne sont pas enregistrés.
**Rotation :** Le fichier est archivé lorsqu'il devient trop volumineux.

Exemple :

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Ödeme alındı: sipariş=%s", siparis_id)
```

Trop de journaux ralentissent le système, trop peu rendent aveugle. INFO est activé en production, DEBUG en cas de problème.

## Choses fréquemment mélangées

On pense qu'il s'agit d'observabilité. Pourtant, la journalisation en est la pierre angulaire : le journal est la matière première, la capacité d'observation est le produit.

## Utilisation dans différentes disciplines

**Boîte noire :** Enregistrement des données de vol.
**Journal :** Notes par ordre chronologique.
**Enregistrement de la caméra :** Archive des événements.

## Foire aux questions

**Est-ce bien de tout sauvegarder ?**

Non. Un excès ralentit le système et masque l'essentiel ; un enregistrement équilibré est maintenu.

**Qu'est-ce qu'un niveau ?**

C'est l'étiquette d'urgence de l'enregistrement. Il sert de filtre lors de la recherche.

**Où les enregistrements sont-ils écrits ?**

Dans un fichier, un système central ou un service cloud. En production, une collecte centralisée est recommandée.

**Combien de temps sont-ils conservés ?**

Cela dépend de la politique. Le débogage nécessite des semaines, l'audit nécessite des années.

## Termes liés

- [Observability](https://trescout.com/fr/dictionary/observability/)
- [Traces](https://trescout.com/fr/dictionary/traces/)
- [Logs](https://trescout.com/fr/dictionary/logs/)

## Outils liés

- [OmniRoute](https://trescout.com/fr/discover/omniroute/)
- [Spdlog](https://trescout.com/fr/discover/spdlog/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/logging/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/logging/
