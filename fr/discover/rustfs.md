# Système de stockage d'objets haute performance

RustFS a été développé comme un système de stockage d'objets haute performance compatible S3. Il offre une interopérabilité et un support de migration de données avec d'autres plateformes compatibles S3 telles que MinIO et Ceph.

- ★ 33 264
- Rust
- GitHub Trending · 2026-09-19

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
Je souhaite mettre en place un environnement de stockage d'objets haute performance en utilisant RustFS. Comment puis-je gérer mes données en tirant parti de la compatibilité S3 du système, et à quoi dois-je faire attention lors de la mise à l'échelle sur une architecture distribuée ? Guidez-moi étape par étape sur l'installation et les paramètres de configuration de base de ce système sous licence Apache 2.0.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rustfs/
