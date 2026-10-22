# Système de stockage d'objets haute performance

RustFS a été développé comme un système de stockage d'objets haute performance compatible S3. Il offre une interopérabilité et un support de migration de données avec d'autres plateformes compatibles S3 telles que MinIO et Ceph.

- ★ 35 063
- Rust
- GitHub Trending · 2026-09-19

## Mises à jour

- **18 octobre 2026:** Étoiles 35,038 → 35,063, dernière version 1.0.3 (17 octobre 2026).
- **17 octobre 2026:** Étoiles 34,330 → 35,038, dernière version 1.0.2 (16 octobre 2026).
- **3 octobre 2026:** Étoiles 33,264 → 34,330, dernière version 1.0.1 (3 octobre 2026).
- **19 septembre 2026:** Étoiles 33,264 → 33,264, dernière version 1.0.0 (16 septembre 2026).

## Ce que ça vous apporte

- Assure une vitesse élevée et une sécurité mémoire grâce au langage Rust
- Fonctionne parfaitement avec les outils existants grâce à sa structure compatible S3
- Offre une utilisation commerciale sans restriction sous licence Apache 2.0

## Installation

**Démarrage avec le script d'installation**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Exécuter la dernière version avec Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```

## Exécution

**Démarrer le système en utilisant Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite mettre en place un environnement de stockage d'objets haute performance en utilisant RustFS. Comment puis-je gérer mes données en tirant parti de la compatibilité S3 du système, et à quoi dois-je faire attention lors de la mise à l'échelle sur une architecture distribuée ? Guidez-moi étape par étape sur l'installation et les paramètres de configuration de base de ce système sous licence Apache 2.0.

Dépôt : https://github.com/rustfs/rustfs. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Object Storage System](https://trescout.com/fr/dictionary/object-storage-system/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux administrateurs système et aux développeurs à la recherche d'une solution de stockage rapide, sécurisée et compatible S3 pour les charges de travail Big Data, les projets d'intelligence artificielle et les lacs de données.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/rustfs/rustfs)
- [Lire en turc →](https://trescout.com/discover/rustfs/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-19 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rustfs/
