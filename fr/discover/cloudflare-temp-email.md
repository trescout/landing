# E-mail temporaire gratuit sur Cloudflare

Cloudflare Temp Email est une plate-forme open source qui vous permet de configurer un service de messagerie temporaire entièrement gratuit, sans serveur, qui fonctionne avec votre propre nom de domaine, en utilisant l'infrastructure de base de données Cloudflare Workers, Pages et D1/KV. Il protège votre vie privée grâce à la gestion de la boîte de réception, au stockage des pièces jointes, à l'intégration du robot Telegram et aux mécanismes de nettoyage automatique.

- ★ 11 734
- TypeScript
- GitHub Trending · 2026-07-23

## Ce que ça vous apporte
- Zéro coût de serveur et d'exploitation : fonctionne avec le généreux plan gratuit de Cloudflare (100 000 requêtes Workers par jour, routage d'e-mails et hébergement de pages gratuits) sans louer de serveur externe.
- Nom de domaine personnalisé et adresses débloquables : contrairement aux services de messagerie temporaires généraux, il produit des adresses jetables avec votre propre nom de domaine qui ne sont pas mises sur liste noire par les sites Web.
- Analyse rapide des e-mails avec Rust et WASM : traite les e-mails complexes entrants MIME, multipart et HTML en quelques millisecondes grâce au module WebAssembly compilé avec Rust.
- Bot Telegram et notifications instantanées : recevez des notifications directement sur Telegram lorsqu'un nouvel e-mail arrive, lisez le contenu du message ou créez instantanément une nouvelle adresse avec les commandes du bot.
- Nettoyage automatique et accès sécurisé : nettoie automatiquement les anciens messages et pièces jointes après une période de temps spécifiée ; Empêche tout accès non autorisé avec le mot de passe administrateur.

## Comment démarrer et options de configuration
- Guide d'installation officiel →
- Interface de démonstration en direct →

## Architecture technique et principe de fonctionnement
- Intégration de Cloudflare Email Routing : tout le trafic MX arrivant sur votre domaine est reçu dans l'infrastructure Cloudflare et dirigé directement vers la fonction catcher Worker avec la règle catch-all.
- Analyseur Edge Worker et Rust WASM : le flux de courrier électronique entrant (flux brut) est transféré vers le moteur Rust WASM optimisé exécuté dans Worker, où les en-têtes, le corps, le code HTML et les pièces jointes sont rapidement analysés.
- Stockage Cloudflare D1 et R2 : les textes et métadonnées des e-mails sont stockés sur Cloudflare D1, une base de données Edge SQLite. Les pièces jointes sont éventuellement écrites dans le stockage d'objets Cloudflare R2.
- Application moderne à page unique (SPA) : l'interface Web conviviale est servie avec une latence nulle via le réseau CDN mondial de Cloudflare Pages.
- API REST et intégrations externes : offre la possibilité de dériver de nouvelles adresses e-mail et d'interroger la boîte de réception via les points de terminaison de l'API REST pour des tests automatisés ou des logiciels tiers.

## Installation et exemple de déploiement
**Étapes de déploiement avec Wrangler CLI**

```
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```


## Si vous ne codez pas
Je souhaite configurer le projet de messagerie temporaire open source dreamhunter2333/cloudflare_temp_email exécuté sur Cloudflare avec mon propre domaine. J'ai un compte Cloudflare et un domaine connecté au DNS Cloudflare. Pouvez-vous s'il vous plaît me dire étape par étape comment configurer le routage du routage des e-mails, la base de données D1 et l'interface Cloudflare Pages à partir de zéro via le tableau de bord Cloudflare ? De plus, quelles étapes de configuration dois-je suivre pour transférer les e-mails entrants vers mon bot Telegram ?

## Questions fréquemment posées
- Le forfait gratuit de Cloudflare est-il suffisant pour un usage personnel ? Oui. Cloudflare propose 100 000 requêtes Worker par jour, un routage d'e-mails gratuit et un quota de base de données D1 dans son forfait gratuit. Pour un usage personnel et de petites équipes, ces limites sont quasiment impossibles à dépasser ; Le système fonctionne à un coût totalement nul.
- Un domaine personnalisé est-il requis pour utiliser le service ? Oui. Pour recevoir des e-mails, vous devez disposer d'un domaine (ou sous-domaine, par exemple mail.votredomaine.com) géré sur Cloudflare DNS. De cette façon, vous pouvez facilement contourner les sites qui bloquent les services de messagerie temporaires généraux.
- Les e-mails entrants sont-ils stockés de manière permanente ? Non, il s'agit d'un service de messagerie temporaire. En tant qu'administrateur système, vous pouvez déterminer la durée de conservation des e-mails (par exemple, 1 heure, 24 heures ou 7 jours) à partir du panneau ; Les enregistrements expirés sont automatiquement supprimés du stockage D1 et R2.
- Les réponses par e-mail peuvent-elles être envoyées à l’extérieur via le service ? Oui. Bien que Cloudflare Email Routing ne prenne en charge que la réception d'e-mails ; Le projet prend également en charge l'envoi et la réponse aux e-mails du panneau Web vers le monde extérieur lorsque Resend, Brevo ou une API de serveur SMTP personnalisée est connecté.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/cloudflare-temp-email/
