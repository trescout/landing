# Qu'est-ce que Caching ?

*Glossaire · Data · Dernière mise à jour : 22 septembre 2026*

La mise en cache (caching) consiste à copier des données fréquemment utilisées vers une couche rapide.

## Définition et origine du mot

Le cache désigne une mémoire tampon. Au lieu de recalculer les mêmes données, le système les fournit à partir d'une copie. Le temps de réponse diminue et la charge est allégée. Il fonctionne à tous les niveaux, du navigateur au centre de données.

***Analogie :** C'est comme transporter son livre préféré dans son sac ; on ne va pas à la bibliothèque à chaque fois.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Navigateur :** Stockage de pages et d'images.
**Application :** Copie hors ligne.
**Présentateur:** Stockage des résultats de requête.

## Profondeur technique et architecture

Stratégies :

**LRU :** Supprime le moins récemment utilisé.
**TTL :** Ce qui expire est supprimé.
**Cache-aside :** L'application gère.

Directive du navigateur :

```
Cache-Control: public, max-age=3600
```

Cette ligne indique que la copie est valide pendant une heure. Il y a un coût de cohérence : lorsque la source change, la copie devient obsolète ; pour les données critiques, la durée est maintenue courte.

## Choses fréquemment mélangées

On pense à la base de données. La base de données est persistante et vaste, le cache est temporaire et rapide. L'un est un coffre-fort, l'autre est un portefeuille de poche.

## Utilisation dans différentes disciplines

**Sac :** Livre souvent utilisé à portée de main.
**Réfrigérateur :** Nourriture quotidienne devant.
**Garde-manger :** Stock global en arrière-plan.

## Foire aux questions

**Que se passe-t-il si le cache est plein ?**

L'ancien et le moins utilisé est supprimé, le nouveau est écrit. La politique gère cela.

**Quand est-ce nettoyé ?**

À l'expiration du délai, lorsque la capacité est dépassée ou manuellement. Les données critiques sont conservées à court terme.

**Y a-t-il un risque d'incohérence ?**

C'est possible. Lorsque la source change, la copie devient obsolète ; une discipline de version et de durée est nécessaire.

**Où est-ce conservé ?**

En mémoire, sur disque ou en périphérie CDN. Le choix dépend de l'équilibre entre vitesse et capacité.

## Termes liés

- [KV Cache](https://trescout.com/fr/dictionary/kv-cache/)
- [Prefix Cache](https://trescout.com/fr/dictionary/prefix-cache/)
- [Database](https://trescout.com/fr/dictionary/database/)

## Outils liés

- [Free for Dev](https://trescout.com/fr/discover/free-for-dev/)
- [OmniRoute](https://trescout.com/fr/discover/omniroute/)
- [Guava](https://trescout.com/fr/discover/guava/)
- [Omlx](https://trescout.com/fr/discover/omlx/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/caching/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/caching/
