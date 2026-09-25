# Répertoire d'infrastructures SaaS et cloud gratuites pour développeurs

free-for-dev est un vaste répertoire communautaire open-source répertoriant plus de 1 000 services SaaS, PaaS et IaaS proposant des offres gratuites permanentes (free tiers). Conçu pour les développeurs et fondateurs de projets, il permet de concevoir et déployer des MVP complets sans coût d'infrastructure.

- ★ 137.565
- HTML
- GitHub Trending · 2026-06-27

## Mises à jour
- 16 septembre 2026: Étoiles 137 565, enrichi de bases de données serverless, stockage vectoriel et APIs d'inférence IA vérifiées.

## Ce que ça vous apporte
- Développement de MVP sans investissement: Validez vos concepts auprès de réels utilisateurs sans facturation mensuelle ni surprise bancaire.
- Plus de 1 000 services classés: Hébergement cloud, serverless, bases de données, CDN, authentification, CI/CD et observabilité.
- Uniquement de vrais forfaits gratuits permanents: Exclusion stricte des versions d'essai temporaires de 14 jours.
- Validation continue par la communauté: Testé et actualisé chaque jour par des milliers de développeurs qui retirent les liens obsolètes.
- Combinaison multi-cloud: Associez les quotas gratuits de différents fournisseurs pour créer une infrastructure hybride robuste.

## Catégories phares et offres gratuites

Le répertoire free-for-dev répond à l'ensemble des besoins d'un projet web ou mobile moderne :
- Hébergement et calcul cloud (IaaS/PaaS): Oracle Cloud (Always Free 4 vCPU ARM / 24 Go RAM), Cloudflare Workers, Fly.io et Render.
- Bases de données et stockage (DBaaS): Supabase (PostgreSQL), Neon (Postgres serverless), Cloudflare D1/R2 et Upstash (Redis).
- Authentification et sécurité: Clerk, Auth0, Stytch et certificats Let's Encrypt.
- Intégration continue (CI/CD): GitHub Actions (2 000 min/mois gratuites), GitLab CI et Codecov.
- Observabilité et suivi des erreurs: Grafana Cloud, Better Stack, Sentry et Axiom.

## Règles communautaires et critères d'admission

Chaque ressource soumise doit respecter des règles d'admission très précises :
- Offre gratuite permanente obligatoire: Seuls les services utilisables sans limite de durée sont retenus.
- Transparence bancaire: Mention expresse des services exigeant ou non une carte bancaire lors de l'inscription.
- Contrôle automatisé des liens: Chaque Pull Request est soumise à des tests CI GitHub Actions pour éliminer les liens brisés.

## Approche architecturale pour lancer son MVP

Une architecture moderne à coût zéro bâtie avec les meilleures offres de free-for-dev :
- Front-end et CDN: Déploiement mondial de vos applications Next.js sur Cloudflare Pages ou Vercel.
- Base de données relationnelle: Instance PostgreSQL gratuite de 500 Mo avec Row-Level Security (RLS) sur Supabase.
- Envoi d'e-mails transactionnels: Envoi gratuit de jusqu'à 3 000 e-mails par mois via Resend ou Brevo.

## Optimisation des coûts et gestion des quotas

Les meilleures pratiques pour garantir que vos projets restent strictement gratuits :
- Plafond de dépenses strict à zéro: Verrouillez le seuil de dépense à 0 USD dans vos tableaux de bord pour parer tout dérapage.
- Mise en cache maximale sur le réseau CDN: Placez Cloudflare devant vos APIs pour absorber plus de 80 % du trafic sans solliciter la base.
- Gestion des pools de connexion: Utilisez PgBouncer dans les environnements serverless pour éviter la saturation des connexions.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite lancer un projet web en utilisant exclusivement les services gratuits listés dans free-for-dev. Peux-tu concevoir une architecture complète combinant hébergement, base de données serverless, authentification et envoi d'e-mails à coût zéro garanti, en précisant les étapes de configuration ?

- **Pour qui:** Développeurs, créateurs de startups, étudiants et ingénieurs cherchant à annuler leurs coûts d'infrastructure.
- **Licence:** CC BY 4.0 (Licence de contenu ouvert)
- **Curateur:** R.I. Pienaar et plus de 1 000 contributeurs open-source
- **Nombre d'offres:** Plus de 1 000 services gratuits vérifiés

## Questions fréquentes
- Quelle différence entre formule gratuite et essai gratuit ? Les essais gratuits expirent après 7 à 30 jours et deviennent payants. Les forfaits de free-for-dev restent utilisables indéfiniment tant que vous respectez les quotas.
- Peut-on s'inscrire sans carte bancaire ? Oui. Une grande partie des services (Supabase, Cloudflare, Vercel) ne réclament aucun moyen de paiement lors de l'inscription.
- Que se passe-t-il en cas de dépassement du quota ? Si vous avez fixé un plafond de dépense à zéro, le service renvoie une erreur (HTTP 429 ou 503) sans jamais débiter votre compte.
- Ces forfaits suffisent-ils pour une mise en production ? Ils sont parfaitement adaptés pour les prototypes et premiers milliers d'utilisateurs. Dès que le projet dégage des revenus, le passage aux formules payantes s'effectue en un clic.

## Liens
- [GitHub →](https://github.com/ripienaar/free-for-dev)

## Termes associés du glossaire
SaaS PaaS IaaS Cloud Computing Open Source API

---
Source: TreScout Discover · https://trescout.com/fr/discover/free-for-dev/
