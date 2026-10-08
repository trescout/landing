# CRM moderne et open source

Twenty est une alternative open source à Salesforce qui permet aux équipes techniques de créer un CRM moderne pouvant être personnalisé en fonction de leurs processus métier. Vous pouvez héberger ce système, axé sur les flux de travail basés sur l'intelligence artificielle, sur votre propre serveur.

- ★ 57 935
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Mises à jour

- **5 octobre 2026:** Étoiles 57,768 → 57,935, dernière version twenty/v2.45.0 (5 octobre 2026).
- **1 octobre 2026:** Étoiles 57,699 → 57,768, dernière version twenty/v2.44.0 (1 octobre 2026).
- **29 septembre 2026:** Étoiles 57,541 → 57,699, dernière version twenty/v2.43.0 (28 septembre 2026).
- **27 septembre 2026:** Étoiles 56,924 → 57,541, dernière version sdk/v2.41.0 (23 septembre 2026).

## Ce que ça vous apporte

- Une alternative gratuite et open source à Salesforce.
- Contrôle total sur vos données avec l'option d'auto-hébergement.
- Des flux de travail modernes alimentés par l’IA.
- Des éléments de base flexibles qui peuvent être adaptés aux besoins de votre entreprise.

## Installation

**Télécharger le modèle d'environnement**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Télécharger le fichier Compose**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Générer une clé de chiffrement**

```
openssl rand -base64 32
```

**Démarrer les services**

```
docker compose up -d
```

## Exécution

**Accéder à l'interface locale**

```
http://localhost:3000
```

## Comment installer ?

Il est généralement installé sur votre propre serveur avec Docker ; les étapes d'installation sont dans la documentation. Sa gestion nécessite quelques connaissances techniques.

## Comment installer, comment utiliser ?

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer un CRM open source appelé Twenty ; créez une nouvelle application dans le terminal avec la commande 'npx create-twenty-app my-app', puis publiez-la sur mon espace de travail avec 'npx Twenty app:publish --private'. Dites-moi également comment l'exécuter avec Docker Compose pour l'auto-hébergement.

## Termes liés du glossaire

- [CRM](https://trescout.com/fr/dictionary/crm/)
- [SaaS](https://trescout.com/fr/dictionary/saas/)
- [Self-hosting](https://trescout.com/fr/dictionary/self-hosting/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Les équipes techniques qui souhaitent établir leur propre CRM
- **Difficulté:** Suivant · auto-hébergement (développeur requis)
- **Quelles offres:** CRM personnalisable et alimenté par l'IA
- **Frais:** Open source · auto-hébergé gratuitement
- **Licence:** Standart-dışı (NOASSERTION) · ayrıntı aşağıda

**Licence:** ⚠️ Sa licence est non standard (GitHub 'NOASSERTION'). Il est appelé « open source », mais l'utilisation autonome/auto-hébergée et la relivraison commerciale/SaaS peuvent être soumises à des conditions différentes. Assurez-vous de lire le fichier LICENSE dans le dépôt avant toute utilisation commerciale.

## Liens

- [Dépôt GitHub →](https://github.com/twentyhq/twenty)
- [Lire en turc →](https://trescout.com/discover/twenty/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-05-26 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/twenty/
