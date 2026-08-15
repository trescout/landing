# Contourner les blocages de censure grâce au tunneling DNS

MasterDnsVPN est une solution de réseau privé virtuel (VPN) de tunneling de système de noms de domaine à faible charge (tunneling DNS) développée pour contourner les barrières de censure. Écrit en langage Go, l'outil offre une stabilité élevée en matière de perte de paquets et des fonctionnalités d'équilibrage de charge du résolveur dans la transmission de données.

- ★ 6 870
- Go
- GitHub Trending · 2026-06-11

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
Je souhaite établir une connexion sécurisée via un tunneling DNS dans un réseau censuré à l'aide de l'outil MasterDnsVPN. Comment puis-je configurer le côté serveur à l’aide du script d’installation automatique partagé et quelles étapes de base dois-je suivre pour garantir la connexion côté client ? Veuillez détailler les exigences réseau auxquelles je dois prêter attention pendant le processus d'installation et la méthode d'exécution via Docker.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/masterdnsvpn/
