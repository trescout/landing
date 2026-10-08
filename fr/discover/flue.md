# Framework TypeScript pour les agents IA

Développé par l'équipe Astro, Flue se distingue comme un framework d'agent sandbox basé sur TypeScript. Cette structure permet aux développeurs de créer des agents d'intelligence artificielle dans des environnements sécurisés et isolés.

- ★ 8 393
- TypeScript
- GitHub Trending · 2026-06-06

## Mises à jour

- **29 septembre 2026:** Étoiles 8,374 → 8,393, dernière version @flue/cli@2.2.2 (28 septembre 2026).
- **27 septembre 2026:** Étoiles 8,295 → 8,374, dernière version @flue/cli@2.1.1 (23 septembre 2026).
- **19 septembre 2026:** Étoiles 8,255 → 8,295, dernière version @flue/cli@2.1.0 (18 septembre 2026).
- **17 septembre 2026:** Étoiles 8,244 → 8,255, dernière version @flue/cli@2.0.8 (16 septembre 2026).

## Ce que ça vous apporte

- Création d'agents programmables et sans tête basés sur TypeScript.
- Environnement de travail rapide et évolutif avec bac à sable virtuel.
- Déploiement polyvalent sur les processus Node.js, Cloudflare et CI/CD.

## Installation

**Serveur de développement Node.js**

```
flue dev --target node
```

**Compilation**

```
flue build --target node          # Node.js server (single bundled .mjs)
flue build --target cloudflare    # Cloudflare Workers + Durable Objects
```

## Exécution

**Exécution du workflow Hello World**

```
flue run hello --target node \
  --payload '{"text": "Hello world", "language": "French"}'
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite développer un agent d'intelligence artificielle en utilisant le framework Flue. Comment puis-je définir un workflow à l'aide de TypeScript dans mon projet ? Plus précisément, comment puis-je configurer le modèle avec la fonction createAgent et interagir avec mon agent avec session.prompt ? À l'aide d'un exemple simple « hello-world », pouvez-vous expliquer étape par étape comment démarrer un agent au moment de l'exécution et obtenir des résultats ?

## Termes liés du glossaire

- [Sandbox Agent Framework](https://trescout.com/fr/dictionary/sandbox-agent-framework/)
- [Prompt](https://trescout.com/fr/dictionary/prompt/)
- [CI/CD](https://trescout.com/fr/dictionary/ci-cd/)
- [Sandbox](https://trescout.com/fr/dictionary/sandbox/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Framework](https://trescout.com/fr/dictionary/framework/)

- **Pour qui:** Il convient aux développeurs de logiciels qui souhaitent développer leurs propres agents d'intelligence artificielle autonomes avec TypeScript et les exécuter sur différentes plateformes.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/withastro/flue)
- [Lire en turc →](https://trescout.com/discover/flue/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-06 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/flue/
