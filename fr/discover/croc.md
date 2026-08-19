# Transfert de fichiers sécurisé et facile

Croc est un outil qui permet un transfert sécurisé de fichiers et de données entre deux ordinateurs grâce au cryptage de bout en bout. Ce logiciel, développé avec le langage de programmation Go, utilise un mécanisme de relais temporaire pour faciliter le processus de transfert.

- ★ 39 880
- Go
- GitHub Trending · 2026-07-22

## Ce que ça vous apporte
- Transmission de données cryptées de bout en bout
- Compatibilité entre différents systèmes d'exploitation
- Reprendre les transferts interrompus là où ils s'étaient arrêtés

## Installation
**Installation générale**

```
curl https://getcroc.schollz.com | bash
```

**Installation sur macOS**

```
brew install croc
```


## Exécution
**envoyer le fichier**

```
croc send [file(s)-or-folder]
```

**recevoir des fichiers**

```
croc code-phrase
```


## Si vous ne codez pas
Je souhaite transférer des fichiers en toute sécurité entre deux ordinateurs à l'aide de l'outil Croc. Comment puis-je faire correspondre l'expression de code qui m'est donnée lorsque j'exécute la commande « croc send [file_name] » du côté de l'expéditeur avec la commande « croc [code_expression] » du côté récepteur et que je démarre le transfert ? Y a-t-il un paramètre spécial auquel je dois prêter attention pour garantir que le cryptage de bout en bout est fourni pendant le transfert et que le processus est sécurisé ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/croc/
