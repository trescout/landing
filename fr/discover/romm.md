# Centralisez votre bibliothèque de jeux

Romm est un gestionnaire de bibliothèque de jeux qui vous permet d'organiser votre collection de jeux rétro via une interface web moderne et élégante.

- ★ 12 170
- GitHub Trending · 2026-07-04

## Que fait cet outil ?
Romm est un gestionnaire de bibliothèque de jeux auto-hébergé qui vous permet d'organiser votre collection de jeux rétro via une interface web moderne et élégante. Il récupère automatiquement les métadonnées des jeux grâce à l'intégration IGDB.

## Pour qui ?
Les passionnés de jeux rétro qui souhaitent transformer des fichiers de jeux éparpillés en une archive centrale et visuellement riche.

## À quoi ne faut-il pas s’attendre ?
Ceux qui souhaitent effectuer des achats de jeux numériques ou qui recherchent un client pour gérer des plateformes actuelles.

## Points forts
- Offre une interface de bibliothèque moderne accessible via un navigateur.
- Télécharge automatiquement des informations telles que la jaquette du jeu, la date de sortie et la description.
- Prend en charge le multi-utilisateur et le suivi de l'historique de jeu.

## Premiers pas
- Téléchargez les fichiers Docker et Docker Compose nécessaires pour Romm.
- Générez les clés nécessaires pour l'accès à l'API et ajoutez-les au fichier de configuration.
- Démarrez le service en montant le répertoire où se trouvent vos fichiers de jeu.
- Connectez-vous à l'interface web pour lancer le premier scan de la bibliothèque.

## Démarrage prudent

## Premier prompt
Comment ajouter une nouvelle plateforme (par exemple, SNES) à la bibliothèque Romm ?

## Installation
**Obtenir un exemple de fichier de composition**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/rommapp/romm/master/examples/docker-compose.example.yml
```


## Exécution
**commencer**

```
docker compose up -d
```


## Liens
- Dépôt GitHub →
- README officiel de Romm →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/romm/
