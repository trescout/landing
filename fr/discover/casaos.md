# Gérez votre serveur cloud personnel

CasaOS est un système d'exploitation cloud personnel open-source, léger et élégant, conçu pour gérer des applications Docker en un clic sur serveurs domestiques, mini PC et Raspberry Pi. Développé en Go, il permet de bâtir sa souveraineté numérique sans commandes complexes en ligne de commande.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Mises à jour
- 2 août 2026: Étoiles 34 992 → 36 953, dernière version v0.4.15 (19 décembre 2024).

## Ce que ça vous apporte
- Magasin d'applications riche en un clic: Installez Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant et plus de 100 services auto-hébergés en quelques secondes.
- Tableau de bord web sobre et intuitif: Surveillez l'utilisation du processeur, la RAM, l'espace disque, le débit réseau et l'état des conteneurs via des widgets élégants.
- Stockage visuel et gestion de fichiers: Montez automatiquement vos disques durs externes et clés USB, et partagez des dossiers sur Windows et Mac via Samba (SMB).
- Support Docker Compose personnalisé: Déployez n'importe quel fichier Docker Compose personnalisé absent de la boutique en le collant dans l'interface web.
- Cœur Go léger sans surcoût système: Consomme un minimum de mémoire en arrière-plan et tourne avec fluidité sur Raspberry Pi 4/5 ou vieux ordinateurs portables.

## Installation

**Commande d'installation**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Exécution

**Commande de mise à jour**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Architecture technique et principe de fonctionnement

Au lieu de fournir un noyau Linux complet, CasaOS opère comme une couche d'orchestration Docker moderne au-dessus de votre distribution Debian, Ubuntu ou Raspberry Pi OS existante. Cette architecture préserve la compatibilité matérielle tout en structurant les services via des microservices modulaires :
- Architecture de microservices en Go: Le cœur de CasaOS (Gateway, MessageBus, LocalStorage et UserService) se compose de microservices Go indépendants communicant via REST et WebSocket.
- Abstraction du cycle de vie des conteneurs: Dialogue directement avec le démon Docker pour détecter les conflits de ports et convertir variables d'environnement et volumes en champs ergonomiques.
- Écosystème ZimaOS et IceWhale: Développé par IceWhale Technology (créateurs de ZimaBoard et ZimaBlade), le système garantit une parfaite synergie avec le matériel cloud personnel.
- Agrégation intelligente de disques: Regroupe des disques de tailles variées en un seul espace de stockage logique pour les sauvegardes et le multimédia domestique.

## Guide pas à pas pour créer son serveur domestique

Pour transformer un ancien ordinateur ou mini PC en véritable cloud personnel, suivez ces étapes clés :
- Installation de Linux: Installez Ubuntu Server ou Debian minimal sur la machine et raccordez-la à votre box Internet par câble Ethernet.
- Installation de CasaOS en une ligne: Lancez le script officiel dans le terminal ; il installe et configure automatiquement Docker et ses dépendances.
- Accès au tableau de bord: Depuis n'importe quel appareil du réseau local, saisissez l'adresse IP du serveur (ex. http://192.168.1.100) et créez votre compte administrateur.
- Déploiement des applications: Ouvrez l'App Store pour installer Nextcloud pour vos fichiers ou Jellyfin pour vos films et séries en un clic.

## Si vous ne codez pas
🤖 Si vous ne codez pas
J'ai installé CasaOS sur mon serveur domestique. Je souhaite configurer AdGuard Home (bloqueur de publicités), Jellyfin (streaming multimédia) et Tailscale (accès distant sécurisé) pour tous les appareils de la maison. Peux-tu m'expliquer pas à pas comment installer ces services via l'App Store de CasaOS ou Docker Compose, et comment partager mes disques de stockage ?

- **Pour qui:** Passionnés de homelab et utilisateurs souhaitant gérer leur cloud personnel et conteneurs Docker sans ligne de commande.
- **Licence:** Apache-2.0 (Licence open-source permissive)
- **Développeur:** IceWhale Technology et communauté open-source
- **Systèmes supportés:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Questions fréquentes
- CasaOS efface-t-il mon système Linux ou mes fichiers existants ? Non. CasaOS n'écrase pas votre système ; il s'installe comme couche de gestion au-dessus de Linux. Vos fichiers existants sont préservés et deviennent accessibles dans l'interface.
- Comment accéder à CasaOS hors de chez soi en toute sécurité ? Plutôt que d'ouvrir des ports non sécurisés sur votre box, installez Tailscale ou WireGuard sur CasaOS. Vous bénéficiez ainsi d'un tunnel VPN chiffré accessible partout dans le monde.
- Quelle est la différence entre CasaOS, TrueNAS et Unraid ? TrueNAS et Unraid sont des systèmes de stockage complets orientés sur les configurations RAID complexes et ZFS. CasaOS privilégie la simplicité, la légèreté et une approche centrée sur les applications.
- Les applications redémarrent-elles automatiquement après une coupure de courant ? Oui. Tous les conteneurs Docker démarrent avec la directive <code>restart: unless-stopped</code>, reprenant automatiquement leur fonctionnement dès le démarrage du serveur.

## Liens
- [GitHub →](https://github.com/IceWhaleTech/CasaOS)

## Termes associés du glossaire
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/fr/discover/casaos/
