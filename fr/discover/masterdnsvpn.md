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

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite établir une connexion sécurisée via un tunneling DNS dans un réseau censuré à l'aide de l'outil MasterDnsVPN. Comment puis-je configurer le côté serveur à l’aide du script d’installation automatique partagé et quelles étapes de base dois-je suivre pour garantir la connexion côté client ? Veuillez détailler les exigences réseau auxquelles je dois prêter attention pendant le processus d'installation et la méthode d'exécution via Docker.

Dépôt : https://github.com/masterking32/MasterDnsVPN. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [DNS Tunneling](https://trescout.com/fr/dictionary/dns-tunneling/)
- [Resolver Load Balancing](https://trescout.com/fr/dictionary/resolver-load-balancing/)
- [DNS](https://trescout.com/fr/dictionary/dns/)
- [VPN](https://trescout.com/fr/dictionary/vpn/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux chercheurs et aux utilisateurs avancés qui souhaitent fournir un accès Internet de haute stabilité dans des conditions de réseau restreintes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/masterking32/MasterDnsVPN)
- [Lire en turc →](https://trescout.com/discover/masterdnsvpn/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-11 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/masterdnsvpn/
