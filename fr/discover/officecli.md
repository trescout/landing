# Gérer les fichiers bureautiques avec l'intelligence artificielle

OfficeCLI propose une suite bureautique open source qui permet aux agents IA de lire, modifier et automatiser directement les fichiers Word, Excel et PowerPoint. Développé en C#, cet outil permet d'effectuer des opérations via un seul fichier binaire sans nécessiter aucune installation de logiciel bureautique.

- ★ 28 422
- C#
- GitHub Trending · 2026-07-08

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
Vous pouvez gérer des fichiers Word, Excel et PowerPoint avec l'outil OfficeCLI préparé pour vous. Pour utiliser cet outil, installez le fichier de compétences requis en exécutant la commande suivante : curl -fsSL https://officecli.ai/SKILL.md. Après ce processus, vous pouvez lire, modifier et créer des documents bureautiques via la ligne de commande.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/officecli/
