# Communication d'équipe sécurisée et personnalisable

Rocket.Chat propose un système d'exploitation de communications sécurisé conçu pour les opérations critiques. La plateforme, développée avec le langage TypeScript, vise à centraliser les processus de messagerie et de collaboration internes.

- ★ 46 215
- TypeScript
- GitHub Trending · 2026-06-18

## Mises à jour

- **6 octobre 2026:** Étoiles 46,098 → 46,215, dernière version 8.9.0 (5 octobre 2026).
- **10 septembre 2026:** Étoiles 46,064 → 46,098, dernière version 8.8.1 (9 septembre 2026).
- **2 septembre 2026:** Étoiles 46,005 → 46,064, dernière version 8.8.0 (1 septembre 2026).
- **19 août 2026:** Étoiles 45,941 → 46,005, dernière version 8.7.1 (19 août 2026).

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

- [Communications Operating System](https://trescout.com/fr/dictionary/communications-operating-system/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)

- **Pour qui:** Il a été développé pour les organisations soucieuses de la confidentialité des données et souhaitant avoir un contrôle total sur leur propre infrastructure.

## Liens

- [Dépôt GitHub →](https://rocket.chat/)
- [Lire en turc →](https://trescout.com/discover/rocket-chat/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-18 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/rocket-chat/
