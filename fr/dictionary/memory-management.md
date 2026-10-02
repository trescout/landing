# Qu'est-ce que Memory Management ?

La gestion de la mémoire (Memory Management) est le processus d'allocation, de protection et de restitution au système de la mémoire vive (RAM) physique et virtuelle de l'ordinateur entre les logiciels en cours d'exécution, une fois leur utilisation terminée.

## 1. Anatomie de la mémoire : Distinction entre la pile (Stack) et le tas (Heap)
Lorsqu'un programme est exécuté, le système d'exploitation alloue un espace d'adressage virtuel dédié à ce processus. Les deux composants les plus critiques de cet espace sont la pile (Stack) et le tas (Heap) :

## 2. Trois paradigmes fondamentaux de gestion de la mémoire

## 3. Mémoire au niveau du système d'exploitation : Mémoire virtuelle et OOM Killer
Les systèmes d'exploitation modernes utilisent une architecture de mémoire virtuelle et de pagination pour empêcher les programmes de lire la mémoire les uns des autres. L'unité de gestion de la mémoire (MMU) du processeur traduit les adresses virtuelles en adresses physiques matérielles à l'aide du cache TLB. Lorsque la RAM physique et le swap sont totalement épuisés, le mécanisme OOM Killer (Out of Memory Killer) du noyau Linux met fin au processus le plus agressif avec un signal SIGKILL afin de sauver le système.

## Questions fréquentes
**Que signifie « Memory management » et quelle est sa traduction en turc ?**
« Memory Management » signifie « gestion de la mémoire » en turc. Il s'agit de l'ensemble des processus d'allocation, de suivi et de libération des ressources RAM lors de l'exécution d'un programme informatique.

**Quelle est la différence fondamentale entre la pile (Stack) et le tas (Heap) ?**
La pile gère les variables locales connues au moment de la compilation de manière extrêmement rapide selon la logique LIFO ; le tas est un pool de mémoire flexible alloué aux objets qui grandissent dynamiquement au moment de l'exécution, dont la gestion est plus complexe.

**Comment fonctionne le Garbage Collection (ramasse-miettes) ?**
Dans les langages où le développeur n'effectue pas de suppression manuelle (Java, Go, JS, etc.), un moteur fonctionnant en arrière-plan détecte les objets orphelins inaccessibles depuis les variables racines et nettoie la RAM.

**Comment prévenir une fuite de mémoire (Memory Leak) ?**
Dans les langages manuels, cela se prévient en écrivant un « free » pour chaque « malloc » ou en établissant des modèles RAII ; dans les langages avec ramasse-miettes, cela se prévient en nettoyant les références de tableaux globaux et les écouteurs d'événements (event listeners) non fermés.


## Termes liés
- [Runtime](/fr/dictionary/runtime/)
- [State Management](/fr/dictionary/state-management/)
- [Serialization](/fr/dictionary/serialization/)
- [Network Stack](/fr/dictionary/network-stack/)
- [Assembly](/fr/dictionary/assembly/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/memory-management/
