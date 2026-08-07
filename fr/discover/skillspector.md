# Capacités d’IA sécurisées

Développé par NVIDIA, SkillSpector est un outil d'analyse qui détecte les vulnérabilités et les modèles malveillants dans les packages de compétences des agents d'intelligence artificielle. Ce logiciel basé sur Python vise à analyser les risques de sécurité rencontrés lors du processus de développement de systèmes basés sur des agents.

- ★ 14 313
- Python
- GitHub Trending · 2026-06-12

## Mise à jour
- 7 août 2026 : Star 14 260 → 14 313, dernière version v2.8.1 (7 août 2026).
- 6 août 2026 : Star 14 066 → 14 260, dernière version v2.5.3 (5 août 2026).
- 2 août 2026 : Étoile 2 967 → 14 066, dernière version v2.5.1 (31 juillet 2026).

## Ce que ça vous apporte
- L'IA détecte les vulnérabilités et les modèles malveillants dans les capacités des agents.
- Il propose une analyse de sécurité en deux étapes avec une analyse statique et une évaluation facultative de l'IA.
- Il permet de vérifier la sécurité des agents avec une notation des risques et des rapports détaillés.

## Installation
**Clonage du référentiel et création d'un environnement virtuel**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Terminez la configuration**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```


## Exécution
**Analyser le répertoire local**

```
skillspector scan ./my-skill/
```

**Scanner le dépôt Git**

```
skillspector scan https://github.com/user/my-skill
```


## Si vous ne codez pas
Je souhaite contrôler la sécurité d'une compétence d'agent IA à l'aide de l'outil SkillSpector. Comment utiliser la commande « skillsspector scan ./my-skill/ » pour rechercher des talents dans un répertoire local et quels paramètres dois-je ajouter à la commande pour enregistrer les résultats de l'analyse dans « report.json » au format JSON ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/skillspector/
