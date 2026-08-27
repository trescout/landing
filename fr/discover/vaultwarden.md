# Gestion des mots de passe sur votre propre serveur

Un résumé pour cet article n'a pas pu être produit aujourd'hui · voir le lien source pour plus de détails.

- ★ 65 982
- Rust
- GitHub Trending · 2026-08-24

## Ce que ça vous apporte
- Entièrement compatible avec les clients Bitwarden officiels
- Peut être hébergé sur votre propre serveur avec une faible consommation de ressources
- Offre une authentification à deux facteurs et un accès d’urgence

## Installation
**Téléchargez et exécutez le conteneur**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```


## Si vous ne codez pas
Aidez-moi à installer Vaultwarden, un outil qui permet de gérer les mots de passe sur mon propre serveur. Cet outil est un logiciel serveur compatible avec les clients Bitwarden. Puisque je vais installer à l'aide de Docker, expliquez étape par étape comment configurer les commandes d'image à extraire et à exécuter, en montant un volume pour conserver mes données et en tenant compte des exigences HTTPS.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vaultwarden/
