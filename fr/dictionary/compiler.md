# Qu'est-ce que Compiler ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Un compilateur est le programme qui convertit le code que vous écrivez en langage machine compréhensible par l'ordinateur.

## Définition et origine du mot

Compiler signifie compiler ou rassembler. Les ordinateurs ne comprennent que les suites de 0 et de 1. Les développeurs, quant à eux, écrivent dans un langage lisible. Le compilateur fait office de traducteur entre ces deux mondes : il analyse le code et, s'il ne contient aucune erreur, le convertit en fichier exécutable.

***Analogie :** C'est comme transformer une recette écrite en anglais en instructions écrites pour un chef qui ne parle pas anglais, dans une langue qu'il peut comprendre.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Installation d'application :** La version compilée du programme que vous avez téléchargé s'exécute.
**Messages d'erreur :** Le compilateur vous avertit lorsque vous oubliez un point-virgule.
**Moteurs de jeux :** Une sortie de compilation distincte pour chaque plateforme.

## Profondeur technique et architecture

La compilation passe par quatre étapes :

**Analyse lexicale et syntaxique :** Le code est découpé en morceaux, la structure de la phrase est extraite.
**Contrôle sémantique :** On recherche les variables non définies et les incompatibilités de types.
**Optimisation :** Un code équivalent mais plus rapide est généré.
**Génération de code :** Le code machine spécifique au processeur est écrit.

En langage C, la compilation s'effectue comme suit :

```
gcc merhaba.c -o merhaba
./merhaba
```

La première ligne traduit, la seconde exécute. L'interpréteur, quant à lui, exécute ligne par ligne et ne produit pas de fichier de sortie séparé.

## Utilisation dans différentes disciplines

**Interprétation :** La distinction entre traduction simultanée (interprète) et traduction écrite (compilateur).
**Imprimerie :** La conversion du brouillon en matrice d'impression.
**Cuisine :** La transformation de la recette en plat préparé.

## Foire aux questions

**Le compilateur de chaque langage est-il différent ?**

Oui. Chaque langage requiert un compilateur ou un interpréteur conforme à ses propres règles. Certains langages utilisent les deux conjointement.

**Quelle est la différence avec l'interpréteur ?**

Le compilateur traduit le code à l'avance et génère un fichier, le programme s'exécute ensuite rapidement. L'interpréteur traduit et exécute ligne par ligne, il est flexible mais généralement plus lent.

**Qu'est-ce que le JIT ?**

La compilation à la volée (just-in-time) traduit en code machine les sections fréquemment utilisées pendant l'exécution. C'est une approche intermédiaire, utilisée par Java et JavaScript.

**Qui a compilé le premier compilateur ?**

C'est un problème de la poule et de l'œuf. Les premiers compilateurs ont été écrits à la main en code machine, les suivants ont été compilés par le compilateur précédent (amorçage ou bootstrapping).

## Termes liés

- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Compile-time](https://trescout.com/fr/dictionary/compile-time/)

## Outils liés

- [Llvm Project](https://trescout.com/fr/discover/llvm-project/)
- [SWC](https://trescout.com/fr/discover/swc/)
- [FMT](https://trescout.com/fr/discover/fmt/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/compiler/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/compiler/
