# Plateforme de support client open source

Chatwoot est une plateforme open source qui offre un chat en direct, une assistance par e-mail et une gestion de bureau omnicanal. Développé comme alternative aux logiciels commerciaux tels qu'Intercom et Zendesk, cet outil vous permet de gérer les interactions clients à partir d'un centre unique.

- ★ 36 927
- GitHub Trending · 2026-06-12

**Note TreScout :** Il collecte les messages des clients sur un seul écran : chat du site, e-mail, WhatsApp. Les services prêts à l'emploi qui font le même travail facturent des frais mensuels par personne, mais comme ils fonctionnent sur votre propre serveur, il n'y a pas de tels frais, en retour, le serveur et la maintenance deviennent votre travail. Son installation n'est pas monolithique, nécessite plusieurs utilitaires et rencontre des difficultés avec les packages serveur les moins chers.

## Mises à jour

- **18 septembre 2026:** Étoiles 36,253 → 36,927, dernière version v4.18.0 (18 septembre 2026).
- **27 août 2026:** Étoiles 36,001 → 36,253, dernière version v4.17.1 (27 août 2026).
- **20 août 2026:** Étoiles 35,290 → 36,001, dernière version v4.17.0 (20 août 2026).
- **1 août 2026:** Étoiles 30,493 → 35,290, dernière version v4.16.2 (27 juillet 2026).

## Ce que ça vous apporte

- Il regroupe tous les canaux clients dans une seule boîte de réception.
- Répond automatiquement aux questions de routine avec un assistant basé sur l'intelligence artificielle.
- Il vous donne un contrôle total sur vos données clients en les hébergeant sur votre propre serveur.

## Installation

**Télécharger le fichier d'environnement**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Télécharger le fichier Docker Compose**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Préparer la base de données**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Exécution

**Démarrer les services**

```
docker compose up -d
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Répondez aux questions en vous faisant passer pour un représentant du support client. En tant qu'assistant Captain AI sur Chatwoot, résolvez automatiquement les questions fréquemment posées et dirigez les problèmes complexes vers les coéquipiers concernés. Améliorez l’expérience du support client en fournissant toujours des informations courtoises, rapides et précises.

## Termes liés du glossaire

- [Omni-channel Desk](https://trescout.com/fr/dictionary/omni-channel-desk/)
- [Omni-channel](https://trescout.com/fr/dictionary/omni-channel/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux entreprises qui souhaitent gérer les interactions clients à partir d'un centre unique et automatiser les processus d'assistance.

## Liens

- [Dépôt GitHub →](https://github.com/chatwoot/chatwoot)
- [Lire en turc →](https://trescout.com/discover/chatwoot/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-12 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/chatwoot/
