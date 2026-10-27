# Gérer les fichiers bureautiques avec l'intelligence artificielle

OfficeCLI propose une suite bureautique open source qui permet aux agents IA de lire, modifier et automatiser directement les fichiers Word, Excel et PowerPoint. Développé en C#, cet outil permet d'effectuer des opérations via un seul fichier binaire sans nécessiter aucune installation de logiciel bureautique.

- ★ 32 527
- C#
- GitHub Trending · 2026-07-08

## Mises à jour

- **27 octobre 2026:** Étoiles 32,214 → 32,527, dernière version v1.0.159 (27 octobre 2026).
- **20 octobre 2026:** Étoiles 31,905 → 32,214, dernière version v1.0.158 (20 octobre 2026).
- **12 octobre 2026:** Étoiles 31,762 → 31,905, dernière version v1.0.157 (12 octobre 2026).
- **9 octobre 2026:** Étoiles 31,612 → 31,762, dernière version v1.0.156 (9 octobre 2026).

## Ce que ça vous apporte

- Modifiez des fichiers Word, Excel et PowerPoint avec du code
- Effectuez des transactions directement sans installer de logiciel bureautique
- Donnez aux agents IA la possibilité de créer des documents

## Installation

**Installation sur macOS ou Linux**

```
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

**Installation sous Windows**

```
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

## Exécution

**Créer une présentation vierge**

```
officecli create deck.pptx
```

**Ajouter des diapositives à une présentation**

```
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Vous pouvez gérer des fichiers Word, Excel et PowerPoint avec l'outil OfficeCLI préparé pour vous. Pour utiliser cet outil, installez le fichier de compétences requis en exécutant la commande suivante : curl -fsSL https://officecli.ai/SKILL.md. Après ce processus, vous pouvez lire, modifier et créer des documents bureautiques via la ligne de commande.

Dépôt : https://github.com/iOfficeAI/OfficeCLI. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [PowerPoint](https://trescout.com/fr/dictionary/powerpoint/)
- [Binary](https://trescout.com/fr/dictionary/binary/)
- [Skill](https://trescout.com/fr/dictionary/skill/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent automatiser les documents bureautiques et aux utilisateurs qui souhaitent intégrer des agents d'intelligence artificielle dans leurs processus bureautiques.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/iOfficeAI/OfficeCLI)
- [Lire en turc →](https://trescout.com/discover/officecli/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-08 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/officecli/
