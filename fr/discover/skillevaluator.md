# Outil d'évaluation des capacités des agents d'intelligence artificielle

Développé par NVIDIA, SkillEvaluator est un cadre multicouche qui évalue les compétences des agents d'intelligence artificielle à l'aide de méthodes telles que le contrôle qualité, la détection des conflits sémantiques et la génération de données synthétiques. Cet outil propose des processus d'évaluation en direct afin de mesurer les impacts sur les comportements des agents.

- ★ 4 448
- Python
- GitHub Trending · 2026-11-16

## Mises à jour

- **23 novembre 2026:** Étoiles 3,655 → 4,448, dernière version v1.1.0 (23 novembre 2026).
- **18 novembre 2026:** Étoiles 2,913 → 3,655, dernière version v1.0.1 (18 novembre 2026).
- **17 novembre 2026:** Étoiles 1,912 → 2,913, dernière version v0.9.0 (13 novembre 2026).
- **16 novembre 2026:** Étoiles 1,897 → 1,912, dernière version v0.9.0 (13 novembre 2026).

## Ce que ça vous apporte

- Contrôle la qualité des capacités des agents d'intelligence artificielle
- Mesure l'impact des compétences des agents sur les résultats des tâches
- Fournit des rapports détaillés grâce à un cadre multicouche

## Installation

**Installer le paquet**

```
pip install skillevaluator
```

## Exécution

**Effectuer un contrôle qualité**

```
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite évaluer les capacités de l'agent d'intelligence artificielle. À cette fin, effectue l'installation en exécutant la commande pip install skillevaluator via le terminal, puis lance la commande uv run --python 3.13 skillevaluator quality-check \
src/skillevaluator/tier3/reference_skills/text-analyzer \
-r cli -r json -o reports/first-quality afin de réaliser un test de contrôle qualité d'exemple.

Dépôt : https://github.com/NVIDIA/SkillEvaluator. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Framework](https://trescout.com/fr/dictionary/framework/)
- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux développeurs qui conçoivent des agents d'intelligence artificielle et souhaitent tester les performances de leurs compétences.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/NVIDIA/SkillEvaluator)
- [Lire en turc →](https://trescout.com/discover/skillevaluator/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-16 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/skillevaluator/
