# Qu'est-ce que LSP ?

> Language Server Protocol

Le LSP (Language Server Protocol) est un protocole ouvert basé sur JSON-RPC qui assure une communication standardisée entre les éditeurs de code modernes et les moteurs d'analyse des langages de programmation.

## 1. Définition et problème mathématique résolu : complexité M × N
Le Language Server Protocol (LSP) est un protocole universel développé en 2016 sous l'impulsion de Microsoft (équipe VS Code), Red Hat et Codenvy, devenu aujourd'hui la pierre angulaire des outils de développement.

## 2. Comment fonctionne le LSP ? Architecture du protocole et JSON-RPC 2.0
LSP, l'éditeur (Client) et le moteur d'analyse linguistique (Server) communiquent via le protocole de messagerie JSON-RPC 2.0, fonctionnant généralement par le biais d'entrées/sorties standard locales (stdin/stdout) ou de sockets locaux (IPC).

## 3. Les serveurs de langage les plus utilisés dans l'écosystème

## 4. LSP vs DAP vs LSIF / SCIP

## Questions fréquentes
**Que signifie LSP, quel est son acronyme ?**
Il signifie Language Server Protocol (Protocole de serveur de langage). C'est un protocole ouvert qui standardise la communication entre les éditeurs de code et les moteurs de syntaxe, de vérification de type et de saisie semi-automatique des langages de programmation.

**Pourquoi le LSP résout-il le problème M × N ?**
Dans l'ancien modèle, pour M langages et N éditeurs, il fallait écrire M × N plugins spécifiques à chaque éditeur. Avec le LSP, chaque langage écrit un seul serveur et chaque éditeur un seul client, permettant ainsi d'atteindre la formule d'intégration M + N.

**Comment le LSP empêche-t-il l'éditeur de ralentir ?**
L'analyse lourde de l'arbre syntaxique abstrait (AST) du langage et les résolutions de types sont exécutées dans des processus d'arrière-plan isolés du processus principal de l'éditeur (via JSON-RPC) ; ainsi, l'interface ne se bloque jamais.

**Quelle est la différence entre le DAP et le LSP ?**
Alors que le LSP analyse l'écriture du code, la complétion du code et les erreurs de syntaxe, le DAP (Debug Adapter Protocol) permet de déboguer le code étape par étape en plaçant des points d'arrêt (breakpoints) lors de l'exécution.


## Termes liés
- [Agentic Coding Tool](/fr/dictionary/agentic-coding-tool/)
- [CLI](/fr/dictionary/cli/)
- [Keybindings](/fr/dictionary/keybindings/)
- [Code Snippets](/fr/dictionary/code-snippets/)
- [Runtime](/fr/dictionary/runtime/)

## Outils liés
- [Oh My Pi](/fr/discover/oh-my-pi/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/lsp/
