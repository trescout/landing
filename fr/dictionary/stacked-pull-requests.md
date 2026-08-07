# Qu'est-ce que Stacked Pull Requests ?

Il s'agit d'une méthode permettant d'introduire séquentiellement des modifications logicielles majeures dans le système en petits éléments gérables et interconnectés.

## Définition
Lors du développement d'un logiciel, au lieu de soumettre un changement énorme d'un seul coup, vous divisez ce changement en parties logiques et les soumettez l'une après l'autre. Chaque pièce s’appuie sur la précédente. De cette façon, les personnes qui examinent votre code peuvent approuver plus rapidement des étapes petites et ciblées, au lieu d’essayer de comprendre une structure complexe d’un seul coup.

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
- [Code Review](/fr/dictionary/code-review/)
- [Git Push](/fr/dictionary/git-push/)
- [Checkout](/fr/dictionary/checkout/)

## Outils liés
- [Gh Stack](/fr/discover/gh-stack/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/stacked-pull-requests/
