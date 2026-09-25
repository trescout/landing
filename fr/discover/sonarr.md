# Automatisez votre médiathèque de séries

Sonarr est un gestionnaire d'enregistrement vidéo personnel (PVR) et d'automatisation multimédia open-source conçu pour les utilisateurs d'Usenet et de BitTorrent. Développé en C# et .NET, il surveille la sortie des nouveaux épisodes, pilote les clients de téléchargement et organise les fichiers pour Plex et Jellyfin.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Mises à jour
- 17 septembre 2026: Étoiles 16 274, dernière version v4.0.20.3014 (optimisations du runtime .NET 8 et scoring des Custom Formats).

## Ce que ça vous apporte
- Suivi automatique et calendrier des épisodes: Surveille les dates de diffusion et déclenche le téléchargement dès la mise en ligne.
- Mise à niveau intelligente de qualité: Remplace automatiquement les versions basse résolution par des rips 1080p ou 4K HDR au fil du temps.
- Support des liens physiques (Hardlinks): Partagez vos torrents sans dupliquer l'espace disque tout en rendant le fichier accessible à vos serveurs multimédias.
- Large compatibilité avec les clients de téléchargement: Connexion fluide avec qBittorrent, Transmission, Deluge, SABnzbd et NZBGet.
- Renommage et organisation automatique: Normalise la nomenclature des dossiers et épisodes selon les standards de Plex, Jellyfin et Emby.

## Options d'installation : Docker et service local

**Configuration avec Docker Compose**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Paris
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Exécution et configuration initiale

**Lancer le conteneur**

```
docker compose up -d
```

**Accéder à l'interface web**

```
http://localhost:8989
```

## Architecture technique et fonctionnement interne

Sonarr constitue le chef d'orchestre d'une chaîne multimédia auto-hébergée moderne :
- Passerelle de protocoles Torznab et Newznab: Interroge les indexeurs via Prowlarr ou Jackett au moyen d'APIs XML et JSON standardisées.
- Opérations atomiques et Hardlinks: Lie l'inode du système de fichiers plutôt que de recopier des gigaoctets, annulant l'usure prématurée du disque.
- Moteur de notation de formats personnalisés: Pondère les releases selon les codecs audio (Atmos, DTS-HD), vidéo (HEVC, AV1) et les équipes de release.

## Intégration dans l'écosystème multimédia (Plex, Jellyfin, Prowlarr)

Pour un homelab optimal, Sonarr se connecte aux briques complémentaires :
- Synchronisation des indexeurs avec Prowlarr: Centralisez la configuration de vos trackers et transférez-les automatiquement à Sonarr.
- Gestion des flux avec qBittorrent / SABnzbd: Définissez des répertoires distincts et plafonnez les vitesses d'envoi.
- Notification automatique de médiathèque: Déclenche l'actualisation instantanée de Plex ou Jellyfin dès l'importation.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je veux déployer Sonarr avec qBittorrent, Prowlarr et Jellyfin sur Docker. Peux-tu me fournir un fichier docker-compose.yml complet configuré avec une arborescence de volumes partagés permettant le fonctionnement des hardlinks sans duplication d'espace disque, et m'expliquer la configuration initiale de Sonarr ?

- **Pour qui:** Passionnés de homelab, cinéphiles et amateurs de séries souhaitant une médiathèque autonome.
- **Licence:** GPL-3.0 (Licence libre open-source)
- **Technologie:** Application web C# et .NET
- **Port Web:** 8989 par défaut

## Questions fréquentes
- Sonarr télécharge-t-il directement les vidéos ? Non. Sonarr est un orchestrateur. Il recherche les contenus, envoie les ordres de téléchargement à qBittorrent ou SABnzbd, puis déplace et classe les fichiers finaux.
- Qu'est-ce qu'un hardlink et cela prend-il le double d'espace ? Non. Un hardlink crée un deuxième pointeur vers les mêmes blocs physiques sur le disque. Le fichier apparaît dans deux répertoires sans consommer un octet de plus.
- Quelle différence entre Sonarr et Radarr ? Sonarr est dédié aux séries télévisées et saisons, tandis que Radarr applique la même logique aux longs métrages.
- Faut-il installer Sonarr sous VPN ? Sonarr ne fait que des requêtes de métadonnées et ne nécessite pas de VPN. En revanche, router le client de téléchargement (qBittorrent) à travers un VPN est vivement recommandé.

## Liens
- [GitHub →](https://github.com/Sonarr/Sonarr)

## Termes associés du glossaire
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/fr/discover/sonarr/
