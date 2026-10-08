# Sauvegardez vos données en toute sécurité en les chiffrant

Développé avec le langage Go, Restic propose un programme de sauvegarde open source qui sauvegarde les données rapidement et efficacement en les chiffrant. Cet outil, qui prend en charge différents systèmes de stockage, économise de l'espace de stockage grâce à la méthode de sauvegarde incrémentielle.

- ★ 35 302
- GitHub Trending · 2026-06-12

**Note TreScout :** Il stocke vos sauvegardes en les chiffrant et ne prend pas de place car il n'écrit pas deux fois le même fichier. Il n'a pas d'interface cliquable, il s'exécute à partir de la ligne de commande et vous définissez la tâche de nettoyer les anciennes sauvegardes, sinon le stockage gonflera avec le temps. Essayez de restaurer un fichier le jour même de son installation : vous ne pourrez pas savoir autrement que la sauvegarde a réellement fonctionné.

## Mises à jour

- **2 août 2026:** Étoiles 34,273 → 35,302, dernière version v0.19.1 (5 juillet 2026).

## Ce que ça vous apporte

- Fournit une haute sécurité en cryptant les données
- Économise de l'espace de stockage avec une sauvegarde incrémentielle
- Compatible avec différents systèmes de stockage cloud et locaux

## Installation

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Exécution

**Créer un dépôt de sauvegarde**

```
restic init --repo /path/to/repo
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite sauvegarder mes données en toute sécurité à l'aide de Restic. Comment puis-je exporter un dossier local ou un répertoire spécifique vers un stockage de sauvegarde crypté ? Pouvez-vous s'il vous plaît expliquer étape par étape comment créer le magasin de sauvegarde et démarrer le processus de sauvegarde initial afin que mes données soient cryptées ?

## Termes liés du glossaire

- [Backup Program](https://trescout.com/fr/dictionary/backup-program/)
- [Incremental Backup](https://trescout.com/fr/dictionary/incremental-backup/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient à tous les utilisateurs qui souhaitent sauvegarder leurs données rapidement et efficacement en les chiffrant.
- **Licence:** BSD-2-Clause

## Liens

- [Dépôt GitHub →](https://github.com/restic/restic)
- [Lire en turc →](https://trescout.com/discover/restic/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-12 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/restic/
