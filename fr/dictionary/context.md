# Qu'est-ce que Context ?

*Intelligence artificielle · Dernière mise à jour : 19 septembre 2026*

Le contexte est l'ensemble des informations environnementales et sémantiques dont une donnée, une commande ou un processus a besoin pour être interprété et exécuté correctement.

## 1. Le contexte (Context) dans l'Intelligence Artificielle et les LLM

Les grands modèles de langage (LLM) ne possèdent pas de mémoire permanente ou de mémoire d'expérience semblable à celle des humains ; à chaque requête, ils "se souviennent" uniquement des données incluses à ce moment-là dans la fenêtre de contexte (context window).

### Le mécanisme de Transformer et d'Attention (Self-Attention)

Dans l'architecture Transformer, le contexte est établi en pondérant la relation entre un mot au début d'une phrase et un mot à la fin (via les vecteurs Requête/Query, Clé/Key, Valeur/Value). Le modèle détermine si le mot "banque" désigne une institution financière ou une rive de rivière uniquement en examinant le contexte de la phrase dans laquelle il apparaît.

### Fenêtre de contexte (Context Window) et ses limites

- Capacité en jetons : Il s'agit de la longueur maximale qu'un modèle peut lire et générer en une seule fois (par ex. 8K, 32K, 128K ou 1M+ de jetons).
- Coût de la mémoire (KV Cache) : à mesure que le contexte s'allonge, les besoins en mémoire de la matrice d'attention augmentent de manière quadratique. Pour alléger cette charge, des optimisations telles que FlashAttention et KV-Cache sont utilisées.
- Problème du milieu perdu (Lost in the Middle) : Des recherches montrent que les LLM se concentrent mieux sur les informations situées au début et à la fin des longs textes par rapport à celles qui se trouvent au milieu.
- RAG (Retrieval-Augmented Generation) : au lieu d'intégrer des millions de pages de données d'entreprise dans la fenêtre de contexte, seuls les paragraphes les plus pertinents par rapport à la requête sont filtrés à l'aide d'un moteur de recherche ou d'une base de données vectorielle et transmis au modèle en tant que contexte.

***Analogie :** Lorsque vous discutez avec un ami, si vous dites simplement "Oui, il a dit ça aussi", il ne vous comprendra pas ; mais si vous dites "Je parle de ce film dont nous avons parlé hier", vous fournissez le contexte nécessaire.*

## 2. Contexte dans les systèmes d'exploitation et la programmation

En programmation système, le « contexte » désigne l'ensemble des valeurs de variables et de registres qui reflètent parfaitement l'état actuel d'un programme lors de son exécution.

### Changement de contexte (Context Switching)

Un système d'exploitation multitâche partage le cœur du CPU entre différents processus et threads :

1. Les registres du CPU du processus en cours d'exécution (RAX, RSP, RIP, etc.), le pointeur de pile et les pages mémoire sont enregistrés dans le bloc de contrôle de processus (PCB - Process Control Block).
2. Les registres du processus suivant sont rechargés dans le CPU.
3. Coût : Le changement de contexte est très coûteux au niveau matériel, car il provoque l'invalidation des caches L1/L2 du processeur et des tables de correspondance d'adresses TLB (Translation Lookaside Buffer), ce qui entraîne une pollution du cache.

### Gestion du contexte dans les langages

- Go (context.Context) : utilisé pour transporter des signaux d'annulation, des délais (deadline) et des métadonnées contextuelles de requête entre des requêtes réseau ou des goroutines asynchrones.
- Python (blocs with) : Les gestionnaires de contexte (Context Managers) sécurisent les opérations de nettoyage des ressources, telles que la lecture de fichiers ou l'ouverture/fermeture de connexions à des bases de données.
- React (Context API) : c'est une méthode permettant de transmettre l'état global en profondeur dans l'arbre des composants sans avoir à passer les props un par un aux composants intermédiaires (sans prop drilling).

## Comparaison : Le concept de contexte dans différentes disciplines

| Domaine | Valeur représentée par le contexte | Composants typiques | Problèmes rencontrés |
|---|---|---|---|
| Intelligence Artificielle (LLM) | Invite d'entrée + Historique de discussion + Documents | Jetons, Masques d'attention, Cache KV | Limite de jetons, Hallucination, Consommation de mémoire |
| Systèmes d'exploitation | État instantané matériel d'un processus | Registres, Compteur de programme, Tables de pages | Latence du CPU, Échecs de cache, Actualisations du TLB |
| Développement logiciel | Cycle de vie de la requête et données d'environnement | Signal de délai d'attente (Timeout), Jeton d'authentification | Fuite de mémoire, Appels asynchrones non annulés |

## Questions et réponses

**Que signifie Context et quel est son équivalent en turc ?**

Son équivalent en turc est "bağlam" (contexte). Il désigne l'ensemble des conditions, de l'arrière-plan et des situations complémentaires qui entourent une expression, une donnée ou une opération.

**Quelle est la différence entre Prompt et Context ?**

Le prompt est l'entrée, la question ou la consigne d'action directement donnée à l'intelligence artificielle ("Explique ce code"). Le context, quant à lui, est l'information supplémentaire fournie pour que le modèle exécute cette consigne correctement, telle que le code complet, les variables d'environnement ou l'historique des conversations.

**Pourquoi le Context Window (Fenêtre de contexte) est-il limité ?**

Dans l'architecture Transformer, chaque jeton est mis en corrélation croisée avec tous les autres jetons. Ce calcul mathématique et la mémoire stockée (KV-Cache) augmentent proportionnellement au carré de la longueur du contexte, ce qui fait que la mémoire du GPU constitue une limite matérielle.

**Pourquoi le "Context Switch" (changement de contexte) dans le système d'exploitation entraîne-t-il une perte de performance ?**

Lors du passage d'un processus à un autre, le processeur doit sauvegarder ses registres, charger l'espace mémoire du nouveau processus et vider puis recharger les caches du processeur (L1/L2/L3 et TLB). Cette situation entraîne une perte directe de temps de traitement de l'ordre de la microseconde.

**Pourquoi le paquet context en Go est-il transmis en tant que premier paramètre à chaque fonction ?**

En Go, le paramètre ctx context.Context empêche le gaspillage des ressources du serveur en garantissant que, lorsqu'une requête HTTP est annulée ou expire, les requêtes de base de données sous-jacentes et les tâches en arrière-plan sont également interrompues.

## Termes liés

- [Context Window](https://trescout.com/fr/dictionary/context-window/)
- [Prompt](https://trescout.com/fr/dictionary/prompt/)
- [RAG](https://trescout.com/fr/dictionary/rag/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [REA](https://trescout.com/fr/discover/rea/)
- [Servers](https://trescout.com/fr/discover/servers/)
- [Goose](https://trescout.com/fr/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/fr/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/fr/discover/openclaude/)
- [Context Mode](https://trescout.com/fr/discover/context-mode/)
- [Code Review Graph](https://trescout.com/fr/discover/code-review-graph/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/context/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/context/
