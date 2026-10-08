# Moteur de recherche privé pour pages et fichiers personnels

Moteur de recherche privé AGPLv3 pour interroger les pages web consultées et les fichiers personnels, avec indexation en texte intégral et recherche sémantique optionnelle.

- ★ 5 740
- Go
- GitHub Trending · 2026-08-25

## Mises à jour

- **27 septembre 2026:** Étoiles 4,602 → 5,740, dernière version v0.20.0 (24 septembre 2026).
- **18 septembre 2026:** Étoiles 3,574 → 4,602, dernière version v0.19.0 (3 septembre 2026).
- **4 septembre 2026:** Étoiles 3,100 → 3,574, dernière version v0.19.0 (3 septembre 2026).
- **27 août 2026:** Étoiles 2,620 → 3,100, dernière version v0.18.0 (23 août 2026).

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

1. Téléchargez le binaire adapté à votre plateforme et rendez‑le exécutable sur Linux ou macOS
2. Démarrez le serveur Hister en mode écoute locale
3. Ouvrez l'interface Web locale
4. Installez l'extension Chrome ou Firefox et choisissez les pages à indexer

## Démarrage prudent

L'extension du navigateur envoie le contenu des pages indexées au serveur Hister configuré, à l'exception du téléchargement de favicon. La recherche sémantique optionnelle envoie le texte des documents au point de terminaison d'embeddings sélectionné.

## Premier prompt

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Ouvrez l'interface locale, indexez les pages sélectionnées via l'extension du navigateur et vérifiez la recherche en utilisant les filtres de requête.

## Termes liés du glossaire

- [TUI](https://trescout.com/fr/dictionary/tui/)
- [Binary](https://trescout.com/fr/dictionary/binary/)
- [MCP](https://trescout.com/fr/dictionary/mcp/)
- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [CLI](https://trescout.com/fr/dictionary/cli/)

## Liens

- [Dépôt GitHub →](https://github.com/asciimoo/hister)
- [Démarrage rapide →](https://hister.org/docs/quickstart)
- [README sur la confidentialité et l’utilisation →](https://github.com/asciimoo/hister)
- [Flux d’utilisation →](https://hister.org/posts/how-i-use-hister)
- [Lire en turc →](https://trescout.com/discover/hister/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-25 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/hister/
