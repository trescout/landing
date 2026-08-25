# Jeu de règles pour agents de codage IA

Ensemble de règles et système de plugins conçus pour appliquer la validation, la gestion des erreurs, la sécurité et l'accessibilité dans les flux de codage assistés par IA.

- ★ 110 483
- JavaScript
- GitHub Trending · 2026-08-25

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
- Installez l'intégration Ponytail pour votre hôte d'agent
- Vérifiez que l'installation est active dans l'hôte
- Sélectionnez le niveau Ponytail approprié
- Exécutez le flux de revue ou d'audit sur les modifications

## Démarrage prudent

## Premier prompt
Écris seulement le code nécessaire à la tâche, puis révise les modifications pour validation, gestion des erreurs, sécurité et accessibilité.

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


## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- README officiel →
- Méthode du benchmark agentique →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ponytail/
