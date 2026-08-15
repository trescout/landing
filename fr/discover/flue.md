# Framework TypeScript pour les agents IA

Développé par l'équipe Astro, Flue se distingue comme un framework d'agent sandbox basé sur TypeScript. Cette structure permet aux développeurs de créer des agents d'intelligence artificielle dans des environnements sécurisés et isolés.

- ★ 7 625
- TypeScript
- GitHub Trending · 2026-06-06

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
Je souhaite développer un agent d'intelligence artificielle en utilisant le framework Flue. Comment puis-je définir un workflow à l'aide de TypeScript dans mon projet ? Plus précisément, comment puis-je configurer le modèle avec la fonction createAgent et interagir avec mon agent avec session.prompt ? À l'aide d'un exemple simple « hello-world », pouvez-vous expliquer étape par étape comment démarrer un agent au moment de l'exécution et obtenir des résultats ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/flue/
