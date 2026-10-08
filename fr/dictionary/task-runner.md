# Qu'est-ce que Task Runner ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Task Runner est un outil qui exécute des tâches répétitives de manière séquentielle.

## Définition et origine du mot

Les tâches telles que les tests, la compression et le déploiement sont liées à une seule commande. La liste est suivie, le processus s'accélère, les erreurs diminuent.

***Analogie :** C'est comme un robot qui fait les tâches de cuisine dans l'ordre ; La liste est donnée, le processus fonctionne.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Web :** Compilation et compression.
**CI :** Étapes de ligne.
**Publication :** Déploiement avec une seule commande.

## Profondeur technique et architecture

Scripts NPM :

```
"scripts": {
  "test": "pytest",
  "build": "vite build"
}
```

L'exécution se présente sous la forme npm run test. Makefile et Just sont des alternatives. Règle : Trois tâches manuelles sont écrites dans le script.

## Choses fréquemment mélangées

Il est considéré comme un terminal. Le terminal l'exécute, le runner le gère. L'un est la scène, l'autre est le metteur en scène.

## Utilisation dans différentes disciplines

**Robot:** Tâches de cuisine séquentielles.
**Machine à laver:** Lavage programmé.
**Pilote automatique :** Suivi d'itinéraire.

## Foire aux questions

**Dans quels métiers est-il utilisé ?**

En tests, compilation et déploiement. Tout emploi récurrent est un candidat.

**Lequel faut-il choisir ?**

L'écosystème détermine : npm est commun du côté JS, Make est commun sur le système.

**Quelle est la différence entre les IC ?**

Runner s'exécute localement, CI s'exécute dans le cloud. Les deux sont utilisés ensemble.

**Quand faut-il l'écrire ?**

À la troisième répétition. Le premier est réalisé à la main, le second par annotation, le troisième par script.

## Termes liés

- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Continuous Integration](https://trescout.com/fr/dictionary/continuous-integration/)
- [Script](https://trescout.com/fr/dictionary/script/)

## Outils liés

- [Mise](https://trescout.com/fr/discover/mise/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/task-runner/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/task-runner/
