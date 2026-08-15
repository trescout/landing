# Gestion des données persistantes dans les systèmes distribués

Développé par Deno, Celld propose une infrastructure d'objets durables auto-hébergée pour les systèmes distribués. Cette technologie, écrite en langage Rust, permet de répartir la gestion des états entre différents nœuds de manière évolutive.

- ★ 2 266
- Rust
- GitHub Trending · 2026-08-08

## Ce que ça vous apporte
- Fournit une gestion d’état évolutive dans votre propre infrastructure.
- Il stocke chaque objet en tant que base de données SQLite indépendante.
- Il établit une coordination inter-nœuds avec un stockage compatible S3.

## Installation
**Téléchargez l'outil sur votre ordinateur**

```
curl -fsSL https://celld.dev/install.sh | sh
```


## Exécution
**Nœud à ressources restreintes**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```


## Si vous ne codez pas
Je souhaite créer un système distribué en utilisant Celld. Après avoir créé un espace de stockage compatible S3, expliquez étape par étape comment les nœuds vont utiliser cet espace et comment distribuer les packages Wrangler. Résumez les détails techniques dans un langage simple, en particulier sur la façon dont les nœuds se découvrent et garantissent la cohérence des données sur S3.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/celld/
