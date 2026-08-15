# PostgreSQL réécrit avec Rust

Le projet pgrust, dans lequel le système de gestion de base de données PostgreSQL a été réécrit avec le langage de programmation Rust, réussit tous les tests de régression. Ce travail vise à moderniser l’architecture des bases de données avec un langage axé sur la sécurité de la mémoire.

- ★ 3 957
- Rust
- GitHub Trending · 2026-07-12

## Ce que ça vous apporte
- Compatibilité des disques avec Postgres 18.3
- Plus de 46 000 réussites aux tests de régression
- Architecture moderne axée sur la sécurité de la mémoire

## Installation
**Essai rapide avec Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```


## Si vous ne codez pas
Quel est l'objectif principal du projet Pgrust, comment la compatibilité des disques avec PostgreSQL existant est-elle assurée et comment la programmation basée sur l'intelligence artificielle est-elle utilisée dans le développement du projet ? Parlez-nous de la compatibilité de la version actuelle de Pgrust avec Postgres 18.3 et de son succès dans les tests de régression.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/pgrust/
