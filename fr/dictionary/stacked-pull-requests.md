# Qu'est-ce que Stacked Pull Requests ?

*Glossaire · Dev · Dernière mise à jour : 2 août 2026*

Il s'agit d'une méthode permettant d'introduire séquentiellement des modifications logicielles majeures dans le système en petits éléments gérables et interconnectés.

## Définition

Lors du développement d'un logiciel, au lieu de soumettre un changement énorme d'un seul coup, vous divisez ce changement en parties logiques et les soumettez l'une après l'autre. Chaque pièce s’appuie sur la précédente. De cette façon, les personnes qui examinent votre code peuvent approuver plus rapidement des étapes petites et ciblées, au lieu d’essayer de comprendre une structure complexe d’un seul coup.

***Analogie :** C'est comme avancer en envoyant chaque chapitre à l'éditeur dès qu'il est terminé et en obtenant l'approbation, au lieu d'écrire un livre d'un seul coup et de l'envoyer à l'éditeur. De cette façon, si vous faites une erreur, vous n’aurez qu’à corriger cette section, pas tout le livre.*

## Comment ça marche

Divisez vos modifications en blocs logiques. Soumettez le premier bloc et commencez à construire le suivant par-dessus avant qu'il ne soit approuvé. Ce processus garantit que le code reste plus propre et que les erreurs sont détectées plus tôt.

## Où est-ce utilisé

Il est utilisé dans les processus internes de révision du code des équipes sur des plateformes telles que GitHub ou GitLab, en particulier lors du développement de fonctionnalités volumineuses.

## Souvent confondu avec

Elle peut être confondue avec une seule grande « Pull Request » ; cependant, cette méthode propose une approche fragmentée et séquentielle.

## Questions fréquentes

**Pourquoi ne pas tout envoyer en même temps ?**

Les changements importants sont plus sujets aux erreurs et rendent plus difficile la révision du code par les autres.

**Si tout est connecté, que se passe-t-il si une pièce se brise ?**

Puisqu’il est séquentiel, vous devez gérer vos modifications avec soin pour éviter de briser la chaîne.

## Termes liés

- [Code Review](https://trescout.com/fr/dictionary/code-review/)
- [Git Push](https://trescout.com/fr/dictionary/git-push/)
- [Checkout](https://trescout.com/fr/dictionary/checkout/)

## Outils liés

- [Gh Stack](https://trescout.com/fr/discover/gh-stack/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/stacked-pull-requests/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/stacked-pull-requests/
