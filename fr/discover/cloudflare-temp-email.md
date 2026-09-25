# E-mail temporaire gratuit sur Cloudflare

Cloudflare Temp Email est une plateforme open-source permettant de déployer un service d'e-mails temporaires gratuit, sans serveur (serverless) et avec votre propre nom de domaine via Cloudflare Workers, Pages et D1/KV. Il préserve votre vie privée grâce à la gestion de boîte de réception, au stockage des pièces jointes, à un bot Telegram et à un nettoyage automatisé.

- ★ 11 734
- TypeScript
- GitHub Trending · 2026-07-23

## Mises à jour
- 13 septembre 2026: Étoiles 11 391 → 11 734, dernière version v1.12.0 (13 septembre 2026).
- 23 août 2026: Étoiles 11 332 → 11 391, dernière version v1.11.1 (22 août 2026).
- 19 août 2026: Étoiles 11 156 → 11 332, dernière version v1.11.0 (19 août 2026).
- 2 août 2026: Étoiles 10 884 → 11 156, dernière version v1.10.0 (31 juillet 2026).

## Ce que ça vous apporte
- Coût de serveur et d'exploitation nul: Fonctionne sur le palier gratuit généreux de Cloudflare (100 000 requêtes Workers/jour, Email Routing et Pages gratuits) sans louer de serveur dédié.
- Nom de domaine personnalisé et adresses non bloquables: Génère des adresses jetables avec votre propre domaine pour contourner les listes noires visant les services publics d'e-mails temporaires.
- Analyse rapide des e-mails avec Rust et WASM: Traite les e-mails complexes (MIME, multipart, HTML) en quelques millisecondes grâce à un module WebAssembly compilé en Rust.
- Bot Telegram et notifications instantanées: Recevez des alertes en direct sur Telegram à l'arrivée d'un message, lisez son contenu ou créez une nouvelle adresse via des commandes simples.
- Nettoyage automatique et accès sécurisé: Purge automatiquement les messages et pièces jointes expirés après une période définie et protège l'administration par mot de passe.

## Pour commencer et options de déploiement

Le déploiement nécessite uniquement un compte Cloudflare et un domaine géré sur Cloudflare DNS. Vous pouvez déployer en un clic via Cloudflare Pages en reliant le dépôt GitHub, ou exécuter le déploiement de la base D1 et des Workers en local via l'interface Wrangler CLI.
- [Guide d'installation officiel →](https://temp-mail-docs.awsl.uk)
- [Interface de démonstration en direct →](https://mail.awsl.uk)

## Architecture technique et fonctionnement interne

Cloudflare Temp Email élimine la complexité de gestion des serveurs de messagerie traditionnels (Postfix, Dovecot) grâce à une conception moderne sans serveur:
- Routage d'e-mails Cloudflare (Email Routing): Le trafic MX entrant est capté par l'infrastructure Cloudflare et redirigé vers la fonction Worker réceptrice (catch-all).
- Edge Worker et parseur Rust WASM: Le flux brut de l'e-mail est traité par le moteur WASM Rust optimisé pour extraire les en-têtes, le corps, le code HTML et les pièces jointes.
- Stockage Cloudflare D1 et R2: Les textes et métadonnées sont enregistrés dans la base SQLite distribuée Cloudflare D1, tandis que les pièces jointes peuvent être déchargées sur Cloudflare R2.
- Application monopage moderne (SPA): L'interface utilisateur web est distribuée avec une latence quasi nulle via le réseau CDN mondial de Cloudflare Pages.
- API REST et intégrations externes: Des points de terminaison programmables permettent aux suites de tests automatisés ou aux pipelines CI/CD de générer des adresses et de récupérer les codes de validation.

## Installation et exemple de déploiement

```bash
# 1. Cloner le depot et installer les dependances
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Creer la base de donnees Cloudflare D1
npx wrangler d1 create temp_email_db

# 3. Executer le schema et deployer
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## Si vous ne codez pas
🤖 Collez ceci dans votre agent IA (Claude Code · Codex · Antigravity) 
Je souhaite installer le projet open-source dreamhunter2333/cloudflare_temp_email sur Cloudflare avec mon propre nom de domaine. J'ai un compte Cloudflare et un domaine configuré sur Cloudflare DNS. Peux-tu m'expliquer étape par étape comment configurer les règles de redirection Email Routing (catch-all), initialiser la base D1 et déployer l'interface web sur Cloudflare Pages ? De plus, quelles variables d'environnement dois-je renseigner pour recevoir les notifications sur mon bot Telegram ?

- **Pour qui:** Développeurs, testeurs QA et utilisateurs soucieux de leur vie privée souhaitant héberger gratuitement un service d'e-mails jetables avec leur propre domaine. 
- **Licence:** MIT (Licence libre open-source) 
- **Infrastructure:** Cloudflare Workers, Pages, D1 (SQLite) et Email Routing 
- **Langages et Outils:** TypeScript, Rust (WASM), Vue 3, Wrangler 

## Foire aux questions
- Le forfait gratuit de Cloudflare est-il suffisant pour un usage personnel ? Oui. L'offre gratuite propose 100 000 requêtes Workers par jour, ainsi que les quotas gratuits d'Email Routing et de base D1. Pour un usage individuel ou en petite équipe, dépasser ces limites est presque impossible; le service fonctionne à coût nul.
- Un nom de domaine personnalisé est-il obligatoire ? Oui. Pour recevoir des messages, vous devez disposer d'un nom de domaine (ou sous-domaine) géré sur Cloudflare DNS. Cela garantit également que vos adresses ne soient pas rejetées par les sites web.
- Les e-mails reçus sont-ils conservés indéfiniment ? Non, il s'agit d'un service temporaire. L'administrateur peut configurer une durée de rétention (par exemple 1 heure, 24 heures ou 7 jours); les messages expirés sont automatiquement supprimés du stockage.
- Le service permet-il d'envoyer des réponses vers l'extérieur ? Oui. Bien que Cloudflare Email Routing ne gère que la réception, le projet supporte l'envoi et la réponse à des e-mails lorsqu'il est couplé aux API de Resend, Brevo ou d'un serveur SMTP tiers.

## Liens
- [Dépôt GitHub →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Lire en turc →](https://trescout.com/discover/cloudflare-temp-email/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et résumé en français. Cette page décrit le dépôt à la date du 2026-07-23.

## Termes liés du glossaire
Self-Hosted Cloud Computing Digital Privacy Open Source API Rust

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/cloudflare-temp-email/
