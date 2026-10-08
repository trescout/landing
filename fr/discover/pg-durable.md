# Gestion robuste des processus sur PostgreSQL

Développée par Microsoft, pg_durable est une bibliothèque conçue pour gérer les processus d'exécution durables sur PostgreSQL. Écrit en Rust, l'outil permet à des flux de travail complexes de s'exécuter dans la base de données de manière persistante et tolérante aux pannes.

- ★ 2 831
- Rust
- GitHub Trending · 2026-06-08

## Mises à jour

- **7 octobre 2026:** Étoiles 2,811 → 2,831, dernière version v0.2.9 (7 octobre 2026).
- **12 septembre 2026:** Étoiles 2,800 → 2,811, dernière version v0.2.8 (11 septembre 2026).
- **2 septembre 2026:** Étoiles 2,781 → 2,800, dernière version v0.2.7 (1 septembre 2026).
- **24 août 2026:** Étoiles 2,716 → 2,781, dernière version v0.2.6 (24 août 2026).

## Ce que ça vous apporte

- Il gère les flux de travail au sein de la base de données de manière tolérante aux pannes et persistante.
- En cas de crash ou d'interruption, il continue ses opérations à partir du dernier point de contrôle.
- Il s'exécute directement sur PostgreSQL sans nécessiter d'infrastructure supplémentaire.

## Installation

**Activation du plugin**

```
CREATE EXTENSION pg_durable;
```

## Exécution

**Démarrage d'un flux de travail**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer un workflow à l'aide du plugin pg_durable sur PostgreSQL. Comment dois-je configurer la fonction df.start() pour gérer un processus tolérant aux pannes et persistant au sein de la base de données ? Comment puis-je créer une structure qui traite les données et peut continuer là où elle s'est arrêtée en cas d'erreur, en utilisant les opérateurs ~> et |=> qui connectent les étapes SQL ? Veuillez expliquer ce processus en donnant des exemples avec des commandes SQL.

## Termes liés du glossaire

- [Durable Execution](https://trescout.com/fr/dictionary/durable-execution/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs back-end, aux administrateurs de bases de données et aux ingénieurs de données qui souhaitent gérer les processus de traitement des données directement sur PostgreSQL de manière persistante et tolérante aux pannes.

## Liens

- [Dépôt GitHub →](https://github.com/microsoft/pg_durable)
- [Lire en turc →](https://trescout.com/discover/pg-durable/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-08 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/pg-durable/
