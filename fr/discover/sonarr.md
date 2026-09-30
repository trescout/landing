# Gérez automatiquement vos archives de séries

Sonarr est un enregistreur vidéo personnel (PVR) intelligent et open source et un gestionnaire d'automatisation des médias développé pour les utilisateurs Usenet (groupes de discussion) et BitTorrent. Plateforme développée avec une infrastructure C# et .NET ; assure le suivi des épisodes nouvellement publiés, communique avec les clients de téléchargement, renomme et transfère régulièrement les fichiers vers les bibliothèques Plex et Jellyfin.

- ★ 16 274
- C#
- GitHub Trending · 2026-09-12

## Ce que ça vous apporte
- Suivi automatique des épisodes et calendrier : suivez les dates de diffusion de votre série préférée grâce au calendrier intégré et téléchargez automatiquement les nouveaux épisodes dès leur sortie.
- Mises à niveau intelligentes de la qualité : remplacez automatiquement les sections de résolution inférieure (HDTV 720p) par des versions de qualité supérieure (1080p / 4K HDR WEB-DL) au fil du temps.
- Prise en charge du hardlinking : conserver les fichiers téléchargés dans le partage torrent et les présenter au serveur multimédia sur le même disque sans les dupliquer.
- Large intégration du client et de l'indexeur : travail sans friction avec qBittorrent, Transmission, Deluge, SABnzbd et NZBGet.
- Dénomination de fichiers personnalisable : Dénomination et classement automatiques des fichiers d'épisode selon les standards des serveurs multimédias (Plex, Jellyfin, Emby).

## Options d'installation : Docker et service local
**Installation avec Docker Compose**

```
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```


## Fonctionnement et configuration de base
**Démarrage du conteneur**

```
docker compose up -d
```

**Accès à l'interface Web**

```
http://localhost:8989
```


## Architecture technique et principe de fonctionnement
- Pont de protocole Torznab et Newznab : communique avec les indexeurs (via Jackett ou Prowlarr) via l'API XML/JSON standard sur les flux RSS et les requêtes de recherche.
- Déplacement de fichiers atomiques et lien dur : réduit à zéro la charge d'écriture sur le disque et le gaspillage de stockage en montant l'inode du système de fichiers au lieu de copier le fichier une fois le téléchargement terminé.
- Moteur de notation des formats personnalisés : sélectionne la meilleure version en notant les codecs audio préférés (Atmos, DTS-HD), les formats vidéo (AV1, HEVC) et les groupes d'éditeurs.

## Intégration de l'écosystème média (Plex, Jellyfin, Prowlarr)
- Synchronisation de l'indexeur avec Prowlarr : importez automatiquement les trackers torrent et les indexeurs Usenet vers Sonarr à partir d'un seul centre.
- Gestion des téléchargements avec qBittorrent / SABnzbd : contrôlez la vitesse de téléchargement et le taux de partage via des catégories désignées.
- Notification de bibliothèque Plex ou Jellyfin : envoyez une notification instantanée au serveur multimédia lorsqu'un nouvel épisode est écrit sur le disque et analysez la bibliothèque.

## Si vous ne codez pas
Je souhaite exécuter ensemble les services Sonarr, qBittorrent, Prowlarr et Jellyfin sur Docker sur mon serveur domestique. Pouvez-vous s'il vous plaît expliquer étape par étape le fichier docker-compose.yml complet contenant une structure de montage de volume unique et les premiers paramètres que je dois effectuer dans le panneau Web Sonarr pour que les liens physiques fonctionnent correctement ?

## Questions fréquemment posées
- Sonarr télécharge-t-il le fichier lui-même directement ? Non. Sonarr n'est pas un client de téléchargement ; est un gestionnaire. Il recherche, envoie le fichier torrent/NZB vers des clients comme qBittorrent ou SABnzbd et déplace le fichier téléchargé vers le dossier d'archive.
- Qu’est-ce que le hardlink et remplit-il le disque deux fois plus ? Non. Le hardlinking consiste à placer un deuxième pointeur de chemin vers les données physiques du fichier sur le disque. Il apparaît à la fois dans les dossiers de téléchargement et dans le dossier tv, mais occupe autant d'espace sur le disque qu'un seul fichier.
- Quelle est la différence entre Sonarr et Radarr ? Tandis que Sonarr réalise des séries télévisées, des saisons et des épisodes ; Radarr propose la même architecture pour les longs métrages.
- Est-il nécessaire d'utiliser un VPN ? Étant donné que Sonarr effectue uniquement des requêtes RSS et des métadonnées, il ne nécessite généralement pas de VPN ; cependant, il est recommandé que le client de téléchargement torrent (qBittorrent) s'exécute derrière un tunnel VPN.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sonarr/
