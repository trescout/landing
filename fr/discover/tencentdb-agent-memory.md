# Mémoire en couches pour les agents IA

TencentDB Agent Memory offre une solution de mémoire à long terme entièrement locale pour les agents d'intelligence artificielle avec un processus en quatre étapes. Il effectue des opérations de stockage et de rappel de données sans avoir besoin d'interfaces de programmation d'applications (API) externes.

- ★ 27 855
- TypeScript
- GitHub Trending · 2026-07-09

## Mises à jour

- **9 octobre 2026:** Étoiles 27,396 → 27,855, dernière version v2.0.2 (9 octobre 2026).
- **28 septembre 2026:** Étoiles 26,048 → 27,396, dernière version v2.0.1 (25 août 2026).
- **7 septembre 2026:** Étoiles 24,804 → 26,048, dernière version v2.0.1 (25 août 2026).
- **27 août 2026:** Étoiles 23,144 → 24,804, dernière version v2.0.1 (25 août 2026).

## Ce que ça vous apporte

- Réduit l'utilisation des jetons jusqu'à 61 %
- Augmente le taux de réussite dans les tâches complexes
- Stocke les données dans une structure symbolique et en couches

## Installation

**Installation du paquet**

```
mkdir -p ~/.memory-tencentdb
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest --omit=dev
cp -r node_modules/@tencentdb-agent-memory/memory-tencentdb \
      ~/.memory-tencentdb/tdai-memory-openclaw-plugin
rm -rf "$TEMP_DIR"
```

**Installation des dépendances**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npm install --omit=dev
npm install tsx
```

## Exécution

**Démarrage du serveur**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
  npx tsx src/gateway/server.ts
```

**Vérifier la connexion**

```
curl http://127.0.0.1:8420/health
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Configurez la mémoire à long terme de mon agent IA à l'aide de la mémoire de l'agent TencentDB. Au lieu d'une pile vectorielle plate de données, utilisez des graphiques symboliques Mermaid pour les tâches à court terme et une pyramide de mémoire en couches L0-L3 pour les expériences à long terme. Permettez à l'agent de stocker les conversations passées, les faits atomiques et les préférences de l'utilisateur dans cette structure hiérarchique et de les rappeler chaque fois que nécessaire avec une traçabilité complète via node_id.

## Termes liés du glossaire

- [Long-term Memory](https://trescout.com/fr/dictionary/long-term-memory/)
- [Mermaid](https://trescout.com/fr/dictionary/mermaid/)
- [Memory](https://trescout.com/fr/dictionary/memory/)
- [Token](https://trescout.com/fr/dictionary/token/)
- [Agent](https://trescout.com/fr/dictionary/agent/)
- [API](https://trescout.com/fr/dictionary/api/)

- **Pour qui:** Il s'adresse aux développeurs qui ne veulent pas que leurs agents IA oublient le contexte et visent à obtenir des résultats plus cohérents en réduisant les coûts des jetons.

## Liens

- [Dépôt GitHub →](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [Lire en turc →](https://trescout.com/discover/tencentdb-agent-memory/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-09 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/tencentdb-agent-memory/
