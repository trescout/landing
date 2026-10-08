# Kit IA autonome pour l'antigravité

Ag-kit est une bibliothèque de développement qui fournit les outils et structures nécessaires pour créer des agents d'intelligence artificielle autonomes (agents IA) dans des projets basés sur TypeScript. Il permet aux développeurs de concevoir rapidement des systèmes d'agents capables de gérer des flux de travail complexes.

- ★ 8 159
- TypeScript
- GitHub Trending · 2026-07-28

## Mises à jour

- **31 août 2026:** Étoiles 8,084 → 8,159, dernière version v2026.8.31 (31 août 2026).
- **2 août 2026:** Étoiles 8,020 → 8,084, dernière version v2026.7.27 (26 juillet 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Dans ce projet, j'ai mis en place un espace de travail Antigravity et activé les outils AG Kit. Je souhaite gérer mes tâches en utilisant les règles, les rôles d'agent expert et les workflows définis dans le dossier .agents/ du répertoire du projet. Assurez-vous que le hook de sécurité est actif et planifiez des flux de travail complexes avec les commandes /coordonner ou /orchestrate.

## Termes liés du glossaire

- [Agentic](https://trescout.com/fr/dictionary/agentic/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels qui utilisent l'espace de travail Antigravity dans leurs projets basés sur TypeScript et souhaitent développer des systèmes d'agents autonomes.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/vudovn/ag-kit)
- [Lire en turc →](https://trescout.com/discover/ag-kit/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-28 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ag-kit/
