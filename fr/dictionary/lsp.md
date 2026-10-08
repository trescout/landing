# Qu'est-ce que LSP ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

> Language Server Protocol

Le LSP (Language Server Protocol) est un protocole ouvert basé sur JSON-RPC qui assure une communication standardisée entre les éditeurs de code modernes et les moteurs d'analyse des langages de programmation.

## 1. Définition et problème mathématique résolu : complexité M × N

Le Language Server Protocol (LSP) est un protocole universel développé en 2016 sous l'impulsion de Microsoft (équipe VS Code), Red Hat et Codenvy, devenu aujourd'hui la pierre angulaire des outils de développement.

La plus grande révolution apportée par le LSP est de réduire la complexité M × N, dont le monde du logiciel souffre depuis des années, au niveau M + N :

- Avant LSP (M × N) : Si le marché compte 5 éditeurs de code populaires (VS Code, Neovim, Sublime Text, Emacs, Eclipse) et 10 langages de programmation populaires (Python, Rust, Go, TypeScript, C++, etc.), il fallait écrire et mettre à jour séparément 5 × 10 = 50 extensions différentes pour assurer l'autocomplétion et la vérification de syntaxe pour chaque langage.
- Après LSP (M + N) : Chaque communauté linguistique n'écrit qu'un seul « Language Server » (serveur de langage) ; chaque développeur d'éditeur n'intègre qu'un seul « LSP Client » (client LSP). Résultat : 5 + 10 = 15 composants. Un nouveau langage de programmation devient parfaitement opérationnel dès le premier jour sur des dizaines d'éditeurs du marché en écrivant un seul serveur LSP.

***Analogie :** Le LSP est l'interprète simultané entre des experts locaux parlant toutes les langues du monde selon les règles de leur propre pays et une assemblée diplomatique internationale qui écoute ces experts ; peu importe qui est l'éditeur dans l'assemblée, le message est transmis parfaitement.*

## 2. Comment fonctionne le LSP ? Architecture du protocole et JSON-RPC 2.0

LSP, l'éditeur (Client) et le moteur d'analyse linguistique (Server) communiquent via le protocole de messagerie JSON-RPC 2.0, fonctionnant généralement par le biais d'entrées/sorties standard locales (stdin/stdout) ou de sockets locaux (IPC).

Les opérations lourdes d'analyse sémantique et de résolution de types sont exécutées dans un processus du système d'exploitation distinct du thread principal de l'éditeur (thread UI) ; ainsi, même sur des projets de 100 000 lignes, votre éditeur ne se fige jamais et ne ralentit pas.

```
   Editör (LSP Client)                   Dil Sunucusu (Language Server)
          │                                            │
          │─────── textDocument/didOpen ──────────────>│ (Dosya açıldı, AST kurulur)
          │─────── textDocument/didChange ───────────>│ (Kullanıcı harf yazdı, artımlı senk.)
          │<────── textDocument/publishDiagnostics ────│ (Kırmızı dalgalı alt çizgi / Hatalar)
          │                                            │
          │─────── textDocument/completion ───────────>│ (Ctrl+Space: Öneriler istendi)
          │<────── CompletionItem[] ───────────────────│ (Metot ve değişken listesi döner)
          │                                            │
          │─────── textDocument/definition ───────────>│ (F12: Tanıma git / Go to definition)
          │<────── Location (Dosya, Satır, Sütun) ────│ (İlgili kaynak kod konumu açılır)
```

1. Initialisation : lors du lancement de l'éditeur, celui-ci communique ses capacités (client capabilities) au serveur, qui confirme ensuite les fonctionnalités qu'il prend en charge (server capabilities).
2. Synchronisation de document (didChange) : Au fur et à mesure que l'utilisateur écrit du code, seules les lignes et les plages de caractères modifiées (synchronisation incrémentale de document) sont transmises au serveur, au lieu du fichier complet.
3. Diagnostic (publishDiagnostics) : Le serveur de langage met à jour l'arbre de syntaxe abstraite (AST) et la table des types en arrière-plan sans compiler le code. En cas d'erreur, il envoie des soulignements rouges à l'éditeur sous forme de notification asynchrone.
4. Requêtes enrichies (survol, complétion, renommage) : lorsqu'un utilisateur survole une fonction avec la souris ou effectue un renommage, le serveur calcule toutes les références dans le projet et renvoie une réponse.

## 3. Les serveurs de langage les plus utilisés dans l'écosystème

- Rust : rust-analyzer (Inférence de type, expansion de macros et avertissements du borrow checker d'une rapidité exceptionnelle)
- Python : pyright / basedpyright / ruff (Vérification de typage statique et linting à la microseconde près avec Ruff)
- Go : gopls (serveur prenant en charge les modules et les paquets, développé par l'équipe officielle de Go)
- TypeScript / JS : vtsls / typescript-language-server (IntelliSense et refactoring)
- C / C++ : clangd (basé sur LLVM, précision supérieure sur les grands projets grâce à compile_commands.json)
- Lua : lua-language-server (annotations de type personnalisées pour les développeurs d'extensions Neovim)

## 4. LSP vs DAP vs LSIF / SCIP

- LSP (Language Server Protocol) : Gère les fonctionnalités intelligentes dynamiques lors de l'écriture du code (autocomplétion, détection d'erreurs, formatage).
- DAP (Debug Adapter Protocol) : Gère les opérations de débogage au moment de l'exécution. Les points d'arrêt (breakpoints), le suivi des variables et l'exécution pas à pas communiquent via le DAP.
- SCIP / LSIF : Ce sont des formats d'indexation statique qui permettent d'indexer au préalable des bases de code volumineuses lors de la compilation, afin de naviguer dans le code via des interfaces web sans avoir à exécuter de serveur.

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

- [Agentic Coding Tool](https://trescout.com/fr/dictionary/agentic-coding-tool/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Keybindings](https://trescout.com/fr/dictionary/keybindings/)
- [Code Snippets](https://trescout.com/fr/dictionary/code-snippets/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [Oh My Pi](https://trescout.com/fr/discover/oh-my-pi/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/lsp/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/lsp/
