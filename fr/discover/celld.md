# Gestion des données persistantes dans les systèmes distribués

Développé par Deno, Celld propose une infrastructure d'objets durables auto-hébergée pour les systèmes distribués. Cette technologie, écrite en langage Rust, permet de répartir la gestion des états entre différents nœuds de manière évolutive.

- ★ 4 937
- Rust
- GitHub Trending · 2026-08-08

## Mises à jour

- **2 octobre 2026:** Étoiles 4,817 → 4,937, dernière version v0.6.1 (1 octobre 2026).
- **27 septembre 2026:** Étoiles 4,630 → 4,817, dernière version v0.6.0 (26 septembre 2026).
- **15 septembre 2026:** Étoiles 4,521 → 4,630, dernière version v0.5.0 (15 septembre 2026).
- **6 septembre 2026:** Étoiles 4,405 → 4,521, dernière version v0.4.1 (5 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer un système distribué en utilisant Celld. Après avoir créé un espace de stockage compatible S3, expliquez étape par étape comment les nœuds vont utiliser cet espace et comment distribuer les packages Wrangler. Résumez les détails techniques dans un langage simple, en particulier sur la façon dont les nœuds se découvrent et garantissent la cohérence des données sur S3.

## Termes liés du glossaire

- [State Management](https://trescout.com/fr/dictionary/state-management/)
- [Durable Objects](https://trescout.com/fr/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs qui travaillent sur des systèmes distribués et souhaitent établir une gestion d'état évolutive sur leurs propres serveurs.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/denoland/celld)
- [Lire en turc →](https://trescout.com/discover/celld/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-08 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/celld/
