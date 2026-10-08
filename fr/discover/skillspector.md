# Capacités d’IA sécurisées

Développé par NVIDIA, SkillSpector est un outil d'analyse qui détecte les vulnérabilités et les modèles malveillants dans les packages de compétences des agents d'intelligence artificielle. Ce logiciel basé sur Python vise à analyser les risques de sécurité rencontrés lors du processus de développement de systèmes basés sur des agents.

- ★ 19 418
- Python
- GitHub Trending · 2026-06-12

## Mises à jour

- **5 octobre 2026:** Étoiles 18,381 → 19,418, dernière version v2.12.0 (23 septembre 2026).
- **27 septembre 2026:** Étoiles 16,828 → 18,381, dernière version v2.12.0 (23 septembre 2026).
- **10 septembre 2026:** Étoiles 16,595 → 16,828, dernière version v2.11.2 (9 septembre 2026).
- **8 septembre 2026:** Étoiles 16,471 → 16,595, dernière version v2.11.1 (7 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite contrôler la sécurité d'une compétence d'agent IA à l'aide de l'outil SkillSpector. Comment utiliser la commande « skillsspector scan ./my-skill/ » pour rechercher des talents dans un répertoire local et quels paramètres dois-je ajouter à la commande pour enregistrer les résultats de l'analyse dans « report.json » au format JSON ?

## Termes liés du glossaire

- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels qui développent des agents d'IA et souhaitent analyser les risques de sécurité des packages de fonctionnalités qu'ils utilisent.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/NVIDIA/SkillSpector)
- [Lire en turc →](https://trescout.com/discover/skillspector/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-12 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/skillspector/
