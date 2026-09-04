# Moteur de recherche privé pour pages et fichiers personnels

Moteur de recherche privé AGPLv3 pour interroger les pages web consultées et les fichiers personnels, avec indexation en texte intégral et recherche sémantique optionnelle.

- ★ 3 574
- Go
- GitHub Trending · 2026-08-25

## Installation
**Rendre le binaire exécutable**

```
chmod +x hister
```


## Exécution
**Démarrer le serveur Hister**

```
./hister listen
```

**Accéder à l'interface locale**

```
http://127.0.0.1:4433
```


## Que fait cet outil ?
Hister peut fonctionner localement ou sur une infrastructure que vous contrôlez ; il n'exige pas de service cloud obligatoire ni de télémétrie. Il indexe les pages via des extensions Chrome et Firefox, propose le crawling de sites et l'import de l'historique du navigateur. Si la recherche sémantique est activée, le texte du document est envoyé au point de terminaison d'embeddings sélectionné.

## Pour qui ?
Ceux qui veulent interroger des pages web et des fichiers personnels dans une infrastructure de recherche qu'ils contrôlent.

## À quoi ne faut-il pas s’attendre ?
Pas pour les scénarios nécessitant un service cloud obligatoire ou de la télémétrie, ni pour les flux d'indexation de navigateur qui n'autorisent pas l'envoi du contenu vers un serveur Hister configuré.

## Points forts
- Fonctionne localement ou sur une infrastructure que vous contrôlez, sans télémétrie ni service cloud obligatoire
- Requêtes en texte intégral avec filtres de champs, expressions, jokers, négation et priorisation
- Recherche sémantique optionnelle et clients Web, terminal, TUI, CLI et MCP

## Premiers pas
- Téléchargez le binaire adapté à votre plateforme et rendez‑le exécutable sur Linux ou macOS
- Démarrez le serveur Hister en mode écoute locale
- Ouvrez l'interface Web locale
- Installez l'extension Chrome ou Firefox et choisissez les pages à indexer

## Démarrage prudent

## Premier prompt
Ouvrez l'interface locale, indexez les pages sélectionnées via l'extension du navigateur et vérifiez la recherche en utilisant les filtres de requête.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Démarrage rapide →
- README sur la confidentialité et l’utilisation →
- Flux d’utilisation →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/hister/
