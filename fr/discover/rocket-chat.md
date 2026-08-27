# Communication d'équipe sécurisée et personnalisable

Rocket.Chat propose un système d'exploitation de communications sécurisé conçu pour les opérations critiques. La plateforme, développée avec le langage TypeScript, vise à centraliser les processus de messagerie et de collaboration internes.

- ★ 46 005
- TypeScript
- GitHub Trending · 2026-06-18

## Ce que ça vous apporte
- Sécurité des données avec cryptage de bout en bout
- Possibilité d'hébergement sur votre propre serveur
- Large intégration et prise en charge des applications

## Installation
**Cloner le dépôt officiel de compose**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Créer le fichier d'environnement**

```
cd rocketchat-compose
cp .env.example .env
```

**Démarrer les services MongoDB et Rocket.Chat**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```


## Exécution
**Accéder à l'interface locale**

```
http://localhost:3000
```


## Pour commencer
- Source officielle →

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rocket-chat/
