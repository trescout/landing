# Qu'est-ce que Working Memory ?

*Intelligence artificielle · Dernière mise à jour : 22 septembre 2026*

La mémoire de travail, ou çalışma belleği en turc, est l'information temporaire que le modèle conserve pour la tâche en cours.

## Définition et origine du mot

Une fois la tâche terminée ou le contexte modifié, le contenu est effacé. Le conteneur de la fenêtre de contexte est l'information active au sein de la mémoire de travail. L'historique des discussions et les résultats intermédiaires s'y trouvent.

***Analogie :** C'est comme des notes temporaires prises sur le côté lors de la résolution de maths ; une fois le problème résolu, elles n'ont plus d'importance.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Discussion :** Mémorisation des messages précédents.
**Raisonnement :** Conservation des étapes intermédiaires.
**Véhicule :** Mise en attente des résultats d'appel.

## Profondeur technique et architecture

Calcul du budget :

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

En cas de dépassement, le modèle dit adieu à l'ancien : un élagage, un résumé ou un défilement est appliqué. Différence RAG : Le RAG apporte des informations de l'extérieur, tandis que la mémoire de travail conserve l'information instantanée. Les deux fonctionnent ensemble.

## Choses fréquemment mélangées

On la prend à tort pour une mémoire à long terme. Celle-ci est le profil permanent, alors que celle-là est l'établi temporaire. Lorsque la session se ferme, cet espace se vide.

## Utilisation dans différentes disciplines

**Remarque :** Le brouillon jeté une fois le problème résolu.
**Rester:** L'outil rangé une fois le travail terminé.
**RAM :** La zone effacée lorsque l'alimentation est coupée.

## Foire aux questions

**Que se passe-t-il si elle est saturée ?**

Les anciennes informations sont oubliées, le contexte glisse. Géré par la synthèse et l'élagage.

**Comment l'agrandir ?**

On choisit un modèle à grande fenêtre ou on ajoute des informations externes avec le RAG.

**Quelle est la différence du RAG ?**

Le RAG apporte des éléments de l'extérieur, la mémoire retient le moment présent. Les deux sont complémentaires.

**Oublie-t-il ?**

Oui. C'est un espace temporaire, la persistance n'est pas attendue. Les informations permanentes sont écrites à l'extérieur.

## Termes liés

- [Memory](https://trescout.com/fr/dictionary/memory/)
- [Context Window](https://trescout.com/fr/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/fr/dictionary/long-term-memory/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/working-memory/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/working-memory/
