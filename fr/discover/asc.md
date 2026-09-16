# Analysez rapidement les applications Android

ASC est une interface de décompilation Android ultra-rapide conçue pour les chercheurs en applications mobiles et les agents d'intelligence artificielle. Écrit en Python, cet outil vise à accélérer le processus d'analyse de fichiers d'application complexes.

- ★ 1 336
- Python
- GitHub Trending · 2026-09-16

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
Agissez comme un chercheur en sécurité d'applications Android. Aidez-moi à utiliser l'outil Droid ASC pour trouver une classe spécifique dans un fichier APK, analyser le fichier AndroidManifest.xml ou rechercher des références dans le code. Lors de la création des commandes, utilisez les commandes getclass, getmanifest et findrefs de l'outil avec les paramètres appropriés et expliquez-moi comment interpréter les résultats.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/asc/
