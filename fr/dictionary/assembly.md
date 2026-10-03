# Qu'est-ce que Assembly ?

En informatique, le terme « assembly » (assemblage) correspond à deux concepts fondamentaux : premièrement, le langage de programmation symbolique de plus bas niveau qui commande directement le processeur matériel (CPU) (langage d'assemblage) ; deuxièmement, le regroupement de modules logiciels compilés (.NET assembly) en un seul paquet distribuable.

## 1. Langage de programmation de bas niveau (langage d'assemblage)
Le processeur d'un ordinateur ne comprend que les signaux binaires 0 et 1 (code machine / opcodes). Le langage assembleur est constitué d'abréviations symboliques lisibles par l'homme (mnémoniques) qui correspondent à ces codes machine bruts :

## 2. Registres de processeur et architecture x86-64
Dans un processeur x86-64 64 bits moderne, les registres les plus critiques sont les suivants :

## 3. CISC vs RISC : différence entre x86-64 et ARM64
L'architecture x86-64 fonctionne selon la philosophie CISC (Complex Instruction Set Computer) ; elle dispose d'instructions de taille variable et d'un jeu d'instructions riche capable d'opérer directement sur la mémoire. L'architecture ARM64 (Apple Silicon, Mobile), quant à elle, est basée sur le RISC (Reduced Instruction Set Computer) ; grâce à une longueur d'instruction fixe de 32 bits et à une architecture Load-Store, elle offre une supériorité majeure en matière d'efficacité énergétique.

## 4. Appels système (Syscall) et exemple Linux x86-64

## 5. Assembly .NET et WebAssembly (WASM)

## Questions fréquentes
**Que signifie l'assembleur et à quoi sert-il ?**
L'assembleur est le langage de programmation symbolique de plus bas niveau qui correspond 1 pour 1 au jeu d'instructions matériel du processeur. Il est utilisé pour contrôler directement les registres du CPU et la mémoire.

**Quelle est la différence entre un assembleur et un compilateur ?**
Le compilateur (C, C++, Rust) analyse la logique humaine complexe et les boucles pour les traduire et les optimiser en code machine. L'assembleur, quant à lui, convertit directement les instructions assembleur, qui sont déjà une forme symbolique du code machine, en code binaire.

**Où le langage assembleur est-il encore utilisé aujourd'hui ?**
Les chargeurs de démarrage (bootloaders), les pilotes de périphériques matériels, l'ingénierie inverse, l'analyse de logiciels malveillants, la détection de vulnérabilités en cybersécurité et les systèmes embarqués (IoT/microcontrôleurs) sont activement utilisés.

**Quelle est la différence entre CISC et RISC ?**
Le CISC (x86-64) possède un jeu d'instructions riche capable d'effectuer plusieurs sous-opérations et accès mémoire en une seule instruction ; le RISC (ARM) est une architecture simplifiée et à haute efficacité énergétique où chaque instruction est conçue pour s'exécuter en un seul cycle d'horloge.


## Termes liés
- [Memory Management](/fr/dictionary/memory-management/)
- [Runtime](/fr/dictionary/runtime/)
- [Compilation](/fr/dictionary/compilation/)
- [Apple Silicon](/fr/dictionary/apple-silicon/)
- [Emulator](/fr/dictionary/emulator/)

## Outils liés
- [Ghidra](/fr/discover/ghidra/)
- [Apollo-11](/fr/discover/apollo-11/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/assembly/
