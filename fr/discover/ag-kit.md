# Kit IA autonome pour l'antigravité

Ag-kit est une bibliothèque de développement qui fournit les outils et structures nécessaires pour créer des agents d'intelligence artificielle autonomes (agents IA) dans des projets basés sur TypeScript. Il permet aux développeurs de concevoir rapidement des systèmes d'agents capables de gérer des flux de travail complexes.

- ★ 8 084
- TypeScript
- GitHub Trending · 2026-07-28

## Ce que ça vous apporte
- 20 rôles d'experts en IA différents
- Contrôle sécurisé de l’exécution des commandes
- Mémoire persistante et gestion des flux de travail

## Installation
**Installation dans le projet**

```
npx @vudovn/ag-kit init
```

**Installation globale**

```
npm install -g @vudovn/ag-kit
ag-kit init
```


## Exécution
**Vérification de l'espace de travail**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Tester le hook de sécurité**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```


## Si vous ne codez pas
Dans ce projet, j'ai mis en place un espace de travail Antigravity et activé les outils AG Kit. Je souhaite gérer mes tâches en utilisant les règles, les rôles d'agent expert et les workflows définis dans le dossier .agents/ du répertoire du projet. Assurez-vous que le hook de sécurité est actif et planifiez des flux de travail complexes avec les commandes /coordonner ou /orchestrate.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ag-kit/
