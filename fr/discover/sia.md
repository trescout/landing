# Testez les modèles d’IA de manière autonome

SIA est un cadre d'IA auto-améliorable développé pour améliorer de manière autonome les performances des modèles et des agents d'IA sur des tâches de référence spécifiques. Ce système basé sur Python permet aux systèmes d'intelligence artificielle d'optimiser leurs processus en analysant leurs propres résultats.

- ★ 1 478
- Python
- GitHub Trending · 2026-06-12

## Ce que ça vous apporte
- Il améliore de manière autonome les performances des tâches des modèles d’intelligence artificielle.
- Meta fournit un raffinement cyclique entre les agents cibles et les agents de rétroaction.
- Il offre une grande précision et une vitesse de traitement efficace dans les tâches de référence.

## Installation
**Installation avec Claude Modèles**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Configuration avec plusieurs fournisseurs (OpenHands)**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..."   # for anthropic/* models
export GEMINI_API_KEY="..."      # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..."      # for openai/* models
```


## Exécution
**Démarrer le cycle d’auto-guérison**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Panneau de visualisation**

```
sia web
```


## Si vous ne codez pas
Je souhaite améliorer les performances d'un agent IA en utilisant le framework SIA. Une fois l'installation terminée, quelle commande dois-je utiliser pour démarrer le cycle d'auto-amélioration en sélectionnant l'une des tâches disponibles (par exemple gpqa) et comment dois-je interpréter les résultats à la fin du processus (target_agent.py, agent_execution.json, enhancement.md) ? De plus, comment puis-je inclure mon propre répertoire de tâches personnalisé dans le système ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sia/
