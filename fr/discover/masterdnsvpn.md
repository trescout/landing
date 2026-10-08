# Contourner les blocages de censure grâce au tunneling DNS

MasterDnsVPN est une solution de réseau privé virtuel (VPN) de tunneling de système de noms de domaine à faible charge (tunneling DNS) développée pour contourner les barrières de censure. Écrit en langage Go, l'outil offre une stabilité élevée en matière de perte de paquets et des fonctionnalités d'équilibrage de charge du résolveur dans la transmission de données.

- ★ 6 870
- Go
- GitHub Trending · 2026-06-11

## Mises à jour

- **2 août 2026:** Étoiles 5,411 → 6,870, dernière version v2026.06.13.234407-7de2476 (13 juin 2026).

## Ce que ça vous apporte

- Il assure la transmission de données dans des réseaux censurés via la méthode de tunneling DNS.
- Il offre le multipathing et l'équilibrage de charge pour une faible perte de paquets et une vitesse élevée.
- Optimisé pour une connexion stable même dans des conditions de réseau restreintes.

## Installation

**Configuration automatique du serveur**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Exécuter avec Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite établir une connexion sécurisée via un tunneling DNS dans un réseau censuré à l'aide de l'outil MasterDnsVPN. Comment puis-je configurer le côté serveur à l’aide du script d’installation automatique partagé et quelles étapes de base dois-je suivre pour garantir la connexion côté client ? Veuillez détailler les exigences réseau auxquelles je dois prêter attention pendant le processus d'installation et la méthode d'exécution via Docker.

## Termes liés du glossaire

- [DNS Tunneling](https://trescout.com/fr/dictionary/dns-tunneling/)
- [Resolver Load Balancing](https://trescout.com/fr/dictionary/resolver-load-balancing/)
- [VPN](https://trescout.com/fr/dictionary/vpn/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux chercheurs et aux utilisateurs avancés qui souhaitent fournir un accès Internet de haute stabilité dans des conditions de réseau restreintes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/masterking32/MasterDnsVPN)
- [Lire en turc →](https://trescout.com/discover/masterdnsvpn/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-11 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/masterdnsvpn/
