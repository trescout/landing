# Qu'est-ce que Assembly ?

*Développement · Dernière mise à jour : 19 septembre 2026*

En informatique, le terme « assembly » (assemblage) correspond à deux concepts fondamentaux : premièrement, le langage de programmation symbolique de plus bas niveau qui commande directement le processeur matériel (CPU) (langage d'assemblage) ; deuxièmement, le regroupement de modules logiciels compilés (.NET assembly) en un seul paquet distribuable.

## 1. Langage de programmation de bas niveau (langage d'assemblage)

Le processeur d'un ordinateur ne comprend que les signaux binaires 0 et 1 (code machine / opcodes). Le langage assembleur est constitué d'abréviations symboliques lisibles par l'homme (mnémoniques) qui correspondent à ces codes machine bruts :

- MOV : Copie des données d'un registre à un autre ou vers une adresse mémoire.
- ADD / SUB : Effectue des opérations mathématiques d'addition et de soustraction.
- PUSH / POP : Ajoute ou retire des données de la pile d'appels (call stack).
- JMP / JE / JNE : Branche le flux du programme vers une autre adresse mémoire en fonction du résultat de la comparaison.

Le code assembleur écrit est converti directement en code machine via des traducteurs appelés assembleurs (nasm, gas) ; il n'y a pas de couche de machine virtuelle intermédiaire.

***Analogie :** Le langage assembleur ressemble à l'installation, une par une, des engrenages, des ressorts et des axes d'une montre sous un microscope avec une pince à épiler ; il offre la plus haute précision et performance, mais exige une grande attention. L'assemblage logiciel, quant à lui, consiste à placer ce mécanisme précis dans le boîtier et à l'emballer comme une montre-bracelet fonctionnelle.*

## 2. Registres de processeur et architecture x86-64

Dans un processeur x86-64 64 bits moderne, les registres les plus critiques sont les suivants :

- Registres à usage général : RAX (accumulateur et retour de fonction), RBX (pointeur de données de base), RCX (compteur de boucle), RDX (données d'entrée/sortie), RDI et RSI (pointeurs de destination et de source).
- Registres à usage spécifique : RSP (Stack Pointer - pointeur de pile), RBP (Base Pointer - pointeur de base du cadre de pile), RIP (Instruction Pointer - adresse de la prochaine instruction à exécuter) et RFLAGS (indicateurs Zero, Carry).

## 3. CISC vs RISC : différence entre x86-64 et ARM64

L'architecture x86-64 fonctionne selon la philosophie CISC (Complex Instruction Set Computer) ; elle dispose d'instructions de taille variable et d'un jeu d'instructions riche capable d'opérer directement sur la mémoire. L'architecture ARM64 (Apple Silicon, Mobile), quant à elle, est basée sur le RISC (Reduced Instruction Set Computer) ; grâce à une longueur d'instruction fixe de 32 bits et à une architecture Load-Store, elle offre une supériorité majeure en matière d'efficacité énergétique.

## 4. Appels système (Syscall) et exemple Linux x86-64

```
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; metnin bellek adresi
    mov rdx, 8          ; metin uzunluğu
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. Assembly .NET et WebAssembly (WASM)

- Assembly .NET : Lorsque le code C# est compilé, un package d'assemblage logique est créé sous la forme d'un fichier .dll ou .exe contenant des octets CIL/MSIL et des métadonnées.
- WebAssembly (WASM) : un format de bytecode pour machine virtuelle à pile, portable, permettant aux codes C, C++ et Rust de s'exécuter dans le navigateur avec des performances proches de la vitesse native.

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

- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Compilation](https://trescout.com/fr/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/fr/dictionary/emulator/)

## Outils liés

- [Ghidra](https://trescout.com/fr/discover/ghidra/)
- [Apollo-11](https://trescout.com/fr/discover/apollo-11/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/assembly/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/assembly/
