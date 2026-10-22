# Gestion centrale des services Grok

Développée pour les plateformes Grok Build, Grok Web et Grok Console, cette passerelle (passerelle API) regroupe la gestion multi-comptes dans un centre unique. Écrit en langage Go, l'outil offre une interface gérable en standardisant l'accès des utilisateurs aux différents services Grok.

- ★ 7 840
- Go
- GitHub Trending · 2026-07-15

## Mises à jour

- **22 octobre 2026:** Étoiles 7,817 → 7,840, dernière version v3.1.8 (22 octobre 2026).
- **18 octobre 2026:** Étoiles 7,669 → 7,817, dernière version v3.1.7 (18 octobre 2026).
- **16 septembre 2026:** Étoiles 7,543 → 7,669, dernière version v3.1.6 (16 septembre 2026).
- **27 août 2026:** Étoiles 7,459 → 7,543, dernière version v3.1.5 (25 août 2026).

## Ce que ça vous apporte

- Grok Build combine les comptes Web et console dans un seul panneau
- Fournit une interface API standard compatible avec OpenAI et Anthropic
- Fournit une gestion avancée des comptes, un routage de modèles et une gestion des erreurs

## Installation

**Installation rapide avec Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Démarrer le service**

```
docker compose pull
docker compose up -d
```

## Exécution

**gestion des services**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

J'ai terminé l'installation de Grok2API et me suis connecté au panneau d'administration. Maintenant, comment puis-je définir mes comptes Grok Build, Web ou Console sur le système, comment puis-je effectuer des correspondances de modèles et quelles étapes puis-je suivre pour générer la clé API pour une utilisation externe ? Veuillez expliquer ce processus étape par étape.

Dépôt : https://github.com/chenyme/grok2api. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Si une clé API est nécessaire, ne me demande pas de l'écrire dans la conversation. Montre-moi comment l'ajouter au fichier .env et assure-toi que ce fichier n'est pas envoyé sur Git.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [API Gateway](https://trescout.com/fr/dictionary/api-gateway/)
- [Gateway](https://trescout.com/fr/dictionary/gateway/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent gérer plusieurs comptes Grok et utiliser ces services dans leurs applications via une API standard.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/chenyme/grok2api)
- [Lire en turc →](https://trescout.com/discover/grok2api/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-15 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/grok2api/
