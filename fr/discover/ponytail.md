# Jeu de règles pour agents de codage IA

Ensemble de règles et système de plugins conçus pour appliquer la validation, la gestion des erreurs, la sécurité et l'accessibilité dans les flux de codage assistés par IA.

- ★ 158 247
- JavaScript
- GitHub Trending · 2026-08-25

## Mises à jour

- **8 octobre 2026:** Étoiles 158,137 → 158,247, dernière version v5.1.0 (8 octobre 2026).
- **8 octobre 2026:** Étoiles 156,385 → 158,137, dernière version v5.0.0 (8 octobre 2026).
- **6 octobre 2026:** Étoiles 155,501 → 156,385, dernière version v4.13.0 (5 octobre 2026).
- **5 octobre 2026:** Étoiles 152,240 → 155,501, dernière version v4.12.0 (5 octobre 2026).

## Installation

**Ajouter le marketplace Claude Code**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Installer le plugin Claude Code**

```
/plugin install ponytail@ponytail
```

## Exécution

**Sélectionner le niveau Ponytail**

```
/ponytail full
```

**Démarrer la revue de diff**

```
/ponytail-review
```

## Que fait cet outil ?

L'escalier de règles est appliqué après lecture du code affecté par une modification. Le benchmark agentic corrigé a rapporté, sur 12 tâches d'un dépôt réel FastAPI et React avec Haiku 4.5 versus la ligne de base no‑skill, en moyenne 54 % de lignes de code en moins, 22 % de tokens en moins, 20 % de coût en moins et 27 % de durée en moins. Ces résultats sont limités à des conditions de test spécifiques.

## Pour qui ?

Ceux qui souhaitent ajouter des règles de validation, sécurité et accessibilité aux flux de codage sur Claude Code, Codex, Gemini CLI et autres hôtes d'agents pris en charge.

## À quoi ne faut-il pas s’attendre ?

Ne doit pas être utilisé pour généraliser des résultats de benchmark à tous les projets ni pour appliquer des modifications critiques en production sans revue humaine.

## Points forts

- Règles ciblées sur la tâche visant à réduire le code inutile
- Approche de revue qui préserve la validation, la gestion des erreurs, la sécurité et l'accessibilité
- Plugins ou adaptateurs d'instructions pour Claude Code, Codex, Gemini CLI et autres hôtes

## Premiers pas

1. Installez l'intégration Ponytail pour votre hôte d'agent
2. Vérifiez que l'installation est active dans l'hôte
3. Sélectionnez le niveau Ponytail approprié
4. Exécutez le flux de revue ou d'audit sur les modifications

## Démarrage prudent

Les pourcentages sont des moyennes du benchmark agentic corrigé sur 12 tâches d'un dépôt réel FastAPI et React, avec Haiku 4.5 et n=4. Une couche adversariale distincte a rapporté une sécurité à 100 %. La fourchette 80–94 % du mode one‑shot antérieur n'est pas une moyenne générale.

## Premier prompt

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Écris seulement le code nécessaire à la tâche, puis révise les modifications pour validation, gestion des erreurs, sécurité et accessibilité.

## Termes liés du glossaire

- [Benchmark](https://trescout.com/fr/dictionary/benchmark/)
- [Agentic](https://trescout.com/fr/dictionary/agentic/)
- [Token](https://trescout.com/fr/dictionary/token/)
- [Agent](https://trescout.com/fr/dictionary/agent/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

## Liens

- [Dépôt GitHub →](https://github.com/DietrichGebert/ponytail)
- [README officiel →](https://github.com/DietrichGebert/ponytail)
- [Méthode du benchmark agentique →](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)
- [Lire en turc →](https://trescout.com/discover/ponytail/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ponytail/
