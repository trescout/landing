# PostgreSQL réécrit avec Rust

Le projet pgrust, dans lequel le système de gestion de base de données PostgreSQL a été réécrit avec le langage de programmation Rust, réussit tous les tests de régression. Ce travail vise à moderniser l’architecture des bases de données avec un langage axé sur la sécurité de la mémoire.

- ★ 5 030
- Rust
- GitHub Trending · 2026-07-12

## Mises à jour

- **16 septembre 2026:** Étoiles 4,964 → 5,030, dernière version v0.3 (15 septembre 2026).
- **10 septembre 2026:** Étoiles 3,957 → 4,964, dernière version v0.2-release (30 juillet 2026).
- **2 août 2026:** Étoiles 2,171 → 3,957, dernière version v0.2-release (30 juillet 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Quel est l'objectif principal du projet Pgrust, comment la compatibilité des disques avec PostgreSQL existant est-elle assurée et comment la programmation basée sur l'intelligence artificielle est-elle utilisée dans le développement du projet ? Parlez-nous de la compatibilité de la version actuelle de Pgrust avec Postgres 18.3 et de son succès dans les tests de régression.

## Termes liés du glossaire

- [Memory](https://trescout.com/fr/dictionary/memory/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs et chercheurs en bases de données qui souhaitent moderniser l'architecture PostgreSQL avec le langage Rust.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/malisper/pgrust)
- [Lire en turc →](https://trescout.com/discover/pgrust/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-12 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/pgrust/
