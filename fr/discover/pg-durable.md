# Gestion robuste des processus sur PostgreSQL

Développée par Microsoft, pg_durable est une bibliothèque conçue pour gérer les processus d'exécution durables sur PostgreSQL. Écrit en Rust, l'outil permet à des flux de travail complexes de s'exécuter dans la base de données de manière persistante et tolérante aux pannes.

- ★ 2 716
- Rust
- GitHub Trending · 2026-06-08

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
Je souhaite créer un workflow à l'aide du plugin pg_durable sur PostgreSQL. Comment dois-je configurer la fonction df.start() pour gérer un processus tolérant aux pannes et persistant au sein de la base de données ? Comment puis-je créer une structure qui traite les données et peut continuer là où elle s'est arrêtée en cas d'erreur, en utilisant les opérateurs ~> et |=> qui connectent les étapes SQL ? Veuillez expliquer ce processus en donnant des exemples avec des commandes SQL.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/pg-durable/
