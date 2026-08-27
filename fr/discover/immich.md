# Sauvegarde de photos et de vidéos sur votre propre serveur

Immich est une solution haute performance conçue pour sauvegarder vos photos et vidéos personnelles, que vous pouvez héberger directement sur votre propre serveur.

- ★ 109 538
- GitHub Trending · 2026-07-05

## Que fait cet outil ?
Immich est une solution haute performance conçue pour sauvegarder vos photos et vidéos personnelles, que vous pouvez héberger directement sur votre propre serveur. Elle vous permet de gérer votre bibliothèque multimédia via des applications mobiles et web.

## Pour qui ?
Pour ceux qui souhaitent stocker et gérer leurs photos et vidéos sur leur propre matériel plutôt que sur des services cloud tiers.

## À quoi ne faut-il pas s’attendre ?
Pour les utilisateurs qui ne souhaitent pas gérer leur propre serveur ou qui ne veulent pas s'occuper des processus d'installation technique.

## Points forts
- Sauvegarde les photos et vidéos dans leur qualité originale.
- Offre un accès via des applications web et mobiles.
- Assure la confidentialité des données en étant hébergé sur votre propre matériel.
- Crée des espaces pour les membres de la famille ou les équipes grâce à la prise en charge multi-utilisateurs.

## Premiers pas
- Assurez-vous de répondre aux exigences matérielles spécifiées dans la documentation officielle.
- Démarrez les conteneurs Immich en utilisant Docker et Docker Compose.
- Téléchargez l'application mobile sur votre appareil et connectez-vous en saisissant l'adresse de votre serveur.
- Créez le premier compte administrateur et lancez le processus de sauvegarde.

## Démarrage prudent

## Premier prompt
Comment ajouter un nouvel utilisateur dans l'installation d'Immich ?

## Installation
**Télécharger la configuration de Docker Compose**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```


## Exécution
**Démarrer les services Docker**

```
docker compose up -d
```


## Liens
- Dépôt GitHub →
- README officiel d'Immich →
- Site officiel d'Immich →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/immich/
