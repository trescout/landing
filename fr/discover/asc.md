# Analysez rapidement les applications Android

ASC est une interface de décompilation Android ultra-rapide conçue pour les chercheurs en applications mobiles et les agents d'intelligence artificielle. Écrit en Python, cet outil vise à accélérer le processus d'analyse de fichiers d'application complexes.

- ★ 2 236
- Python
- GitHub Trending · 2026-09-16

## Mises à jour

- **10 octobre 2026:** Étoiles 1,980 → 2,236, dernière version dev-0.1.1-post4 (10 octobre 2026).
- **27 septembre 2026:** Étoiles 1,336 → 1,980, dernière version dev-0.1.1-post2 (21 septembre 2026).

## Ce que ça vous apporte

- Analyse les gros fichiers d'application en quelques secondes
- Effectue des requêtes directement sur le code sans surcharger la mémoire
- Produit des résultats rapides sans prétraitement inutile

## Installation

**Installation avec le gestionnaire de paquets**

```
pip install droidasc
```

**Installation à partir du code source**

```
pip install .
```

## Exécution

**Ouvrir un fichier d'application avec une interface visuelle**

```
droidasc app.apk --gui
```

**Exporter une classe spécifique**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Agissez comme un chercheur en sécurité d'applications Android. Aidez-moi à utiliser l'outil Droid ASC pour trouver une classe spécifique dans un fichier APK, analyser le fichier AndroidManifest.xml ou rechercher des références dans le code. Lors de la création des commandes, utilisez les commandes getclass, getmanifest et findrefs de l'outil avec les paramètres appropriés et expliquez-moi comment interpréter les résultats.

## Termes liés du glossaire

- [Decompiler](https://trescout.com/fr/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Convient aux chercheurs en sécurité des applications mobiles et aux développeurs de logiciels Android.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/MG1937/ASC)
- [Lire en turc →](https://trescout.com/discover/asc/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-16 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/asc/
