# Gérez votre serveur cloud personnel

CasaOS est un système d'exploitation cloud personnel open source, léger et élégant qui permet la gestion en un clic des applications basées sur Docker sur les serveurs domestiques, les mini PC et les appareils Raspberry Pi. Développée avec le langage Go, la plateforme vous permet d'établir votre propre souveraineté numérique sans avoir besoin de commandes de terminal complexes.

- ★ 36 953
- Go
- GitHub Trending · 2026-06-26

## Ce que ça vous apporte
- Boutique d'applications riche en un clic : configurez Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant et plus de 100 services auto-hébergés populaires en quelques secondes.
- Tableau de bord Web élégant et intuitif : surveillez le processeur, la charge de la RAM, les taux d'occupation des disques, l'activité réseau et les conteneurs en cours d'exécution en direct via des cartes widget élégantes.
- Stockage visuel et gestion des fichiers : connectez automatiquement les disques durs externes et les clés USB, partagez vos dossiers avec vos appareils Windows/Mac sur le réseau local via le protocole Samba (SMB).
- Prise en charge de Docker Compose personnalisé : implémentez sans effort vos conteneurs personnalisés en collant tout fichier Docker Compose non disponible dans la boutique officielle dans l'interface Web.
- Noyau Go léger et charge système nulle : consomme un minimum de mémoire en arrière-plan et offre des performances fluides, même sur les ordinateurs portables Raspberry Pi 4/5 ou plus anciens.

## Installation
**commande d'installation**

```
curl -fsSL https://get.casaos.io | sudo bash
```


## Exécution
**commande de mise à jour**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```


## Architecture technique et principe de fonctionnement
- Architecture de microservices Go : CasaOS Core (CasaOS-Gateway, MessageBus, LocalStorage et UserService) se compose de services Go légers qui s'exécutent indépendamment les uns des autres. La communication entre les services s'effectue via REST et WebSocket.
- Abstraction du cycle de vie des conteneurs : détecte automatiquement les conflits de ports en communiquant directement avec le démon Docker, transforme les variables d'environnement et les chemins de montage de volumes en formulaires conviviaux.
- Écosystème ZimaOS et IceWhale : Soutenu par IceWhale Technology, fabricant du matériel ZimaBoard et ZimaBlade, le projet est entièrement compatible avec le matériel cloud local.
- Défragmentation intelligente des disques : crée un espace flexible pour les médias personnels et la sauvegarde en combinant des disques durs de différentes tailles dans un seul pool de stockage logique.

## Guide étape par étape pour configurer votre propre serveur domestique
- Installation de base de Linux : installez un serveur Ubuntu propre ou Debian minimal sur votre appareil et connectez-le à votre réseau local avec un câble Ethernet.
- Installation CasaOS en une ligne : exécutez le script d'installation officiel via le terminal ; Le script configure automatiquement Docker et ses dépendances.
- Accéder à l'interface depuis le navigateur : Créez votre premier compte administrateur en saisissant l'adresse IP de votre serveur (par exemple http://192.168.1.100) dans votre navigateur depuis n'importe quel ordinateur du réseau.
- Déploiement d'applications : accédez à l'onglet App Store et téléchargez votre cloud personnel avec Nextcloud et votre bibliothèque de films/séries avec Jellyfin en un seul clic.

## Si vous ne codez pas
CasaOS est installé sur mon serveur personnel. Je souhaite installer et configurer les services AdGuard Home (bloqueur de publicité), Jellyfin (streaming multimédia) et Tailscale (accès sécurisé depuis l'extérieur de la maison) pour tous les appareils de ma maison. Pouvez-vous expliquer étape par étape comment installer ces services et configurer le partage de disque à partir du panneau Web CasaOS via Docker Compose personnalisé ou l'App Store ?

## Questions fréquemment posées
- CasaOS effacera-t-il mon système d'exploitation Linux ou mes données existantes ? Non. CasaOS n’efface pas votre système d’exploitation existant ; Il est construit en tant que couche de gestion de bureau et Docker. Les fichiers existants sur vos disques sont conservés et deviennent accessibles via le panneau.
- Comment puis-je accéder en toute sécurité à mon serveur CasaOS lorsque je ne suis pas chez moi ? Au lieu d'une redirection de port non sécurisée, vous pouvez installer Tailscale ou WireGuard sur CasaOS en un seul clic. De cette façon, vous pouvez accéder au tableau de bord depuis n'importe où dans le monde via un tunnel VPN crypté comme si vous étiez sur votre réseau domestique.
- Quelle est la différence entre CasaOS et TrueNAS ou Unraid ? TrueNAS et Unraid sont des systèmes d'exploitation autonomes axés sur la gestion approfondie du stockage et les configurations RAID. CasaOS, quant à lui, offre une expérience cloud domestique légère, extrêmement facile à utiliser et centrée sur les applications.
- Les applications installées démarreront-elles automatiquement après une panne de courant ? Oui. Tous les conteneurs Docker sur CasaOS sont démarrés avec la politique restart:sauf-stopped par défaut. Lorsque votre serveur sera redémarré, tous vos services continueront automatiquement à fonctionner là où ils s'étaient arrêtés.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/casaos/
