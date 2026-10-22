# Qu'est-ce que Self-hosted ?

*Développement · Dernière mise à jour : 19 septembre 2026*

L'auto-hébergement (self-hosted) est une architecture permettant d'exécuter et de gérer un logiciel, une base de données ou un service numérique sur son propre serveur physique, matériel local (homelab) ou serveur privé virtuel (VPS), sous son contrôle total, sans dépendre d'une entreprise de cloud tierce (SaaS).

## Étymologie et équivalent en turc

Issu de la fusion des mots anglais self et host, ce terme est désigné en français par auto-hébergement, hébergement sur ses propres serveurs ou hébergement local.

Dans le modèle SaaS (Software as a Service) traditionnel, les utilisateurs ne sont que des locataires ; les données et l'infrastructure sont verrouillées dans les centres de données d'entreprises tierces. Avec l'approche auto-hébergée (self-hosted), vous êtes directement l'administrateur système et le propriétaire : la base de données, les disques de stockage, les règles réseau et les clés de chiffrement sont entièrement votre propriété physique ou logique.

## 1. De la fatigue du SaaS au rapatriement vers le cloud (Cloud Repatriation)

Au cours de la dernière décennie, le passage de chaque logiciel à un modèle d'abonnement mensuel récurrent a créé une fatigue importante des abonnements chez les particuliers et les entreprises :

- L'impasse des coûts : les outils SaaS facturés entre 10 et 50 dollars par utilisateur et par mois se transforment en coûts incontrôlés de centaines de milliers de dollars à mesure que l'équipe grandit. D'ailleurs, le retour des leaders technologiques mondiaux du cloud vers leur propre matériel (Cloud Repatriation), à l'image de 37signals (Basecamp), a prouvé la rationalité économique de l'approche auto-hébergée.
Souveraineté des données et confidentialité : L'auto-hébergement constitue le bouclier le plus puissant contre les risques de modification unilatérale des conditions d'utilisation par les entreprises, d'utilisation des données pour entraîner des modèles d'intelligence artificielle ou de fermeture soudaine de comptes. Conserver des données clients sensibles au sein de vos propres frontières, conformément aux normes RGPD, garantit également la conformité légale.

## 2. Architecture matérielle et écosystème Homelab

Le monde de l'auto-hébergement est passé aujourd'hui des coûteuses baies de serveurs d'entreprise aux salons et aux laboratoires domestiques (Homelab) :

- Matériel à faible consommation : les mini PC basés sur l'Intel N100, le Raspberry Pi 5 ou les anciens ordinateurs portables peuvent fonctionner 24 h/24 et 7 j/7 pour seulement quelques dizaines d'euros d'électricité par an.
Stockage et sécurité des données (ZFS & RAID) : Les configurations RAID, où plusieurs disques durs sont mis en miroir, et le système de fichiers ZFS rendent la perte de données impossible, même si un disque brûle physiquement. Des systèmes d'exploitation tels que TrueNAS et unRAID transforment ces matériels en pools de stockage professionnels.
- Alternative au VPS Cloud : Pour ceux qui ne souhaitent pas héberger de matériel chez eux, les serveurs virtuels (VPS) bon marché loués auprès de fournisseurs tels que Hetzner ou OVH associent la liberté de l'auto-hébergement (self-hosted) à la fiabilité du cloud.

## 3. Pile logicielle moderne d'auto-hébergement

L'époque où il fallait compiler manuellement PHP et MySQL sur Linux est révolue. L'architecture moderne repose sur trois piliers :

- Conteneurisation (Docker & Docker Compose) : Chaque service (Nextcloud, Vaultwarden, Jellyfin) fonctionne dans son propre conteneur Docker isolé avec ses propres bibliothèques. Grâce au fichier docker-compose.yml, des dizaines de services peuvent être lancés d'une seule commande.
- Proxy inverse : Nginx, Traefik ou Caddy ; intercepte les requêtes Web entrantes, achemine les noms de domaine vers le bon conteneur et renouvelle automatiquement les certificats SSL/TLS gratuits via Let's Encrypt.
- Tunnels de réseau sécurisés (Zero-Trust & Mesh VPN) : Ouvrir des ports sur le routeur domestique expose aux cyberattaques. Les utilisateurs modernes d'auto-hébergement (self-hosted) utilisent Tailscale, WireGuard ou Cloudflare Tunnels pour faire fonctionner leurs systèmes en toute sécurité sur un réseau interne (Mesh VPN) fermé au monde extérieur et accessible uniquement à leurs appareils autorisés.

## 4. Solutions de self-hosting populaires

- Cloud personnel et photo : Nextcloud à la place de Google Drive, et Immich avec reconnaissance faciale par IA à la place de Google Photos.
- Gestion des mots de passe : Vaultwarden (compatible Bitwarden), open-source et léger, à la place de 1Password.
- Diffusion multimédia : Jellyfin et Plex, pour gérer votre propre archive au lieu de Netflix et Spotify.
- IA locale : Ollama et Open WebUI fonctionnant sur votre propre carte graphique au lieu d'un abonnement ChatGPT.
- Maison intelligente : Home Assistant fonctionnant entièrement en local au lieu de fabricants dépendants du cloud.

## 5. Responsabilités : La règle de sauvegarde 3-2-1

La liberté apporte des responsabilités. En cas de panne matérielle, il n'y a pas d'entreprise de cloud auprès de laquelle ouvrir un ticket de support. C'est pourquoi la règle de sauvegarde 3-2-1 est obligatoire :

Conservez au moins 3 copies de vos données.
Conservez ces copies sur 2 supports physiques différents (par exemple, un disque interne et un disque USB externe).
Hérbergez au moins l'une des copies dans un emplacement physique différent (serveur distant chiffré ou stockage externe) à l'abri du feu et du vol.

## Questions et réponses

**Qu'est-ce que le self-hosted et que signifie-t-il en français ?**

C'est un concept d'origine anglaise qui signifie en français « auto-hébergement » ou « hébergement sur son propre serveur ». Il s'agit de faire fonctionner des logiciels sur le matériel ou le serveur de l'utilisateur plutôt que chez des fournisseurs de cloud tiers.

**Faut-il avoir des connaissances avancées en programmation pour installer une solution auto-hébergée ?**

Non, vous n'avez pas besoin de savoir coder. Une connaissance de base de la ligne de commande Linux et la compréhension de la logique Docker suffisent. De plus, des systèmes modernes comme CasaOS et Umbrel offrent une installation en un clic grâce à une logique de boutique d'applications.

**Est-il sûr d'exécuter des services auto-hébergés sur un serveur domestique (Homelab) ?**

S'il est correctement configuré, c'est plus sûr que les clouds commerciaux car vos données ne sont pas partagées avec des entreprises. Cependant, il est impératif d'utiliser des tunnels VPN comme Tailscale au lieu d'ouvrir directement des ports sur le modem et de ne pas négliger les mises à jour de sécurité.

**Pourquoi la règle de sauvegarde 3-2-1 est-elle d'une importance vitale ?**

Dans les systèmes auto-hébergés, il n'y a pas de service client pour récupérer les données en cas de panne matérielle. La règle des 3 copies, sur 2 supports différents et 1 emplacement externe, permet d'éviter la perte de données en cas d'incendie ou de défaillance matérielle.

## Termes liés

- [Local](https://trescout.com/fr/dictionary/local/)
- [Offline](https://trescout.com/fr/dictionary/offline/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)

## Outils liés

- [Immich](https://trescout.com/fr/discover/immich/)
- [Chatwoot](https://trescout.com/fr/discover/chatwoot/)
- [CasaOS](https://trescout.com/fr/discover/casaos/)
- [Open-Generative-AI](https://trescout.com/fr/discover/open-generative-ai/)
- [OpenWA](https://trescout.com/fr/discover/openwa/)
- [Openship](https://trescout.com/fr/discover/openship/)
- [Instatic](https://trescout.com/fr/discover/instatic/)
- [TREK](https://trescout.com/fr/discover/trek/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/self-hosted/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/self-hosted/
