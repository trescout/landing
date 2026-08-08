# Mémoire en couches pour les agents IA

TencentDB Agent Memory offre une solution de mémoire à long terme entièrement locale pour les agents d'intelligence artificielle avec un processus en quatre étapes. Il effectue des opérations de stockage et de rappel de données sans avoir besoin d'interfaces de programmation d'applications (API) externes.

- ★ 17 887
- TypeScript
- GitHub Trending · 2026-07-09

## Mise à jour
- 8 août 2026 : Étoile 16 699 → 17 887, dernière version v2.0.0 (3 août 2026).
- 7 août 2026 : Étoile 15 363 → 16 699, dernière version v2.0.0 (3 août 2026).
- 6 août 2026 : Star 12 420 → 15 363, dernière version v2.0.0 (3 août 2026).
- 4 août 2026 : Star 10 727 → 12 420, dernière version v2.0.0 (3 août 2026).

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
Configurez la mémoire à long terme de mon agent IA à l'aide de la mémoire de l'agent TencentDB. Au lieu d'une pile vectorielle plate de données, utilisez des graphiques symboliques Mermaid pour les tâches à court terme et une pyramide de mémoire en couches L0-L3 pour les expériences à long terme. Permettez à l'agent de stocker les conversations passées, les faits atomiques et les préférences de l'utilisateur dans cette structure hiérarchique et de les rappeler chaque fois que nécessaire avec une traçabilité complète via node_id.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/tencentdb-agent-memory/
