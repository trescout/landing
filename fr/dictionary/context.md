# Qu'est-ce que le Contexte (Context) ? IA et Systèmes

> Anglais : Context · Étymologie : latin contexere (tisser ensemble, assembler)

**Catégorie:** AI  
**Dernière mise à jour:** 2026-09-19

Le contexte (context) est une notion clé de l'informatique désignant soit la fenêtre de mémoire textuelle d'un grand modèle de langage, soit l'état matériel d'un processeur lors de l'exécution de processus.

## Par analogie
Si vous lancez à un ami 'Oui, ils sont d'accord', il ne comprendra rien ; mais si vous précisez 'Au sujet du film dont nous parlions hier', vous lui donnez le contexte indispensable à la compréhension.

## 1. Le contexte en Intelligence Artificielle et LLM
Les modèles de langage ne disposent pas d'une mémoire continue comme le cerveau humain. Pour interpréter une question et y répondre précisément, ils s'appuient sur la **fenêtre de contexte** : la suite de jetons (tokens) transmise lors de chaque appel (consignes système, historique d'échange, documents RAG). La taille de cette fenêtre détermine la quantité d'informations qu'un modèle peut analyser en un seul calcul.

## 2. Le contexte dans les systèmes d'exploitation
En programmation système, le contexte correspond à l'état complet d'un processeur à un instant T pour un fil d'exécution : registres CPU, compteur ordinal (PC) et pointeur de pile. Lorsqu'un système multitâche met en pause une tâche pour en exécuter une autre, il effectue un **changement de contexte (context switch)** en sauvegardant cet état en mémoire.

## Tableau comparatif entre disciplines
Manifestations concrètes du contexte selon le domaine :
- **IA Générative :** Jetons textuels et cache d'attention (KV Cache) fournissant la mémoire de travail immédiate.- **Systèmes d'exploitation :** Bloc de contrôle de processus (PCB) sauvegardant les registres matériels du CPU.- **Développement Web :** Objets de contexte (comme dans React ou Go) transmettant signaux d'annulation et droits d'accès à travers l'arbre d'exécution.

## Questions fréquentes

**Qu'appelle-t-on l'effet 'lost in the middle' dans les LLMs ?**  
Le phénomène où un modèle d'IA mémorise mieux le début et la fin de son invite que les informations situées au cœur de longs textes.

**Pourquoi les changements de contexte CPU sont-ils coûteux ?**  
Parce qu'ils obligent à vider les caches processeur rapides et à recharger les tables de pages virtuelles en mémoire.

**À quoi sert le contexte dans React ?**  
À propager des données globales (thème, utilisateur connecté) aux composants enfants sans devoir passer manuellement des props à chaque étage.

**Comment les Transformers calculent-ils le contexte ?**  
Par des matrices d'attention qui mesurent le lien sémantique existant entre chaque mot de la séquence active.

## Termes liés
- [Context Window](/fr/dictionary/context-window/)
- [Working Memory](/fr/dictionary/working-memory/)
- [Attention Mechanism](/fr/dictionary/attention-mechanism/)

## Outils liés
- [Goose](/fr/discover/goose/)
- [Chrome Devtools MCP](/fr/discover/chrome-devtools-mcp/)
- [Openclaude](/fr/discover/openclaude/)
- [Code Review Graph](/fr/discover/code-review-graph/)
- [Fastmcp](/fr/discover/fastmcp/)
- [Context Mode](/fr/discover/context-mode/)
- [Unity MCP](/fr/discover/unity-mcp/)
- [DesktopCommanderMCP](/fr/discover/desktopcommandermcp/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/context/
