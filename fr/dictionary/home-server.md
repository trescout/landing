# Qu'est-ce qu'un Home Server ?

> Serveur Domestique Personnel

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-22

Un home server (serveur domestique) est un ordinateur connecté en continu au réseau local d'un foyer pour héberger des sauvegardes, des bibliothèques multimédias et des services auto-hébergés.

## Définition et étymologie
Le serveur domestique incarne le principe de souveraineté numérique et de priorité au local. Au lieu de confier l'intégralité de sa vie numérique à des serveurs cloud distants, l'utilisateur conserve la propriété et le contrôle physique de ses données.

## Usage quotidien et contexte pratique
- **Diffusion multimédia :** Hébergement d'un catalogue personnel de films et de musique via Jellyfin sans abonnement.
- **Sauvegardes automatisées :** Sauvegardes régulières de tous les ordinateurs et téléphones de la maison.
- **Domotique résiliente :** Exécution de Home Assistant sans aucune dépendance envers une connexion Internet externe.

## Profondeur technique et architecture
Architecture matérielle et logicielle :- **Matériel :** Mini-PC compacts basse consommation, anciens ordinateurs de bureau reconditionnés ou monocartes ARM.
- **Système d'exploitation :** Debian, Ubuntu Server ou hyperviseurs de virtualisation comme Proxmox VE.
- **Conteneurisation :** Déploiement isolé des services avec Docker et routage par proxy inverse (Caddy, Traefik).

## Souvent confondu avec
Souvent confondu avec un simple boîtier NAS grand public. Si le NAS se limite souvent au stockage réseau basique (SMB), le serveur domestique exécute des bases de données et des applications complètes.

## Perspectives interdisciplinaires
- **Culture :** Une bibliothèque personnelle chez soi plutôt que la location de livres à l'extérieur.
- **Énergie :** Des panneaux solaires sur le toit face à la dépendance exclusive au réseau électrique général.
- **Logistique :** Un cellier familial privé face aux livraisons quotidiennes à flux tendu.

## Par analogie
Il agit comme un bibliothécaire et archiviste privé à domicile, gérant vos archives numériques et vos services multimédias.

## Questions fréquentes

**Quelle est la consommation électrique d'un serveur domestique ?**  
Les mini-PC modernes consomment généralement entre 5 et 15 watts au repos, pour un coût électrique mensuel minime.

**Peut-on y accéder de l'extérieur en toute sécurité ?**  
Oui, grâce à des VPN chiffrés modernes comme WireGuard ou Tailscale sans ouvrir de ports vulnérables sur votre box.

**Quel système choisir pour débuter ?**  
Ubuntu Server avec Docker, ou des environnements prêts à l'emploi comme CasaOS ou TrueNAS.

**Faut-il du matériel professionnel coûteux ?**  
Non, un ordinateur reconditionné ou un mini-PC silencieux convient parfaitement pour la grande majorité des usages.

## Termes liés
- [Auto-hébergement](/fr/dictionary/self-hosted/)
- [Domotique](/fr/dictionary/home-automation/)
- [Cloud Personnel](/fr/dictionary/personal-cloud/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/home-server/
