# Gestion des mots de passe sur votre propre serveur

Vaultwarden est un logiciel de serveur open source développé en langage Rust, compatible avec l'outil de gestion de mots de passe Bitwarden.

- ★ 68 594
- Rust
- GitHub Trending · 2026-08-24

## Mises à jour

- **6 octobre 2026:** Étoiles 67,398 → 68,594, dernière version 1.37.4 (5 octobre 2026).
- **14 septembre 2026:** Étoiles 65,982 → 67,398, dernière version 1.37.3 (13 septembre 2026).
- **24 août 2026:** Étoiles 65,983 → 65,982, dernière version 1.37.2 (22 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Aidez-moi à installer Vaultwarden, un outil qui permet de gérer les mots de passe sur mon propre serveur. Cet outil est un logiciel serveur compatible avec les clients Bitwarden. Puisque je vais installer à l'aide de Docker, expliquez étape par étape comment configurer les commandes d'image à extraire et à exécuter, en montant un volume pour conserver mes données et en tenant compte des exigences HTTPS.

## Termes liés du glossaire

- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux utilisateurs qui souhaitent héberger leurs propres mots de passe et données sensibles sur leur propre serveur plutôt que de recourir à des services cloud tiers.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/dani-garcia/vaultwarden)
- [Lire en turc →](https://trescout.com/discover/vaultwarden/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-24 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vaultwarden/
