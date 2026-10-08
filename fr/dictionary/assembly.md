# Assembly : Définition, registres et architecture système

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Le terme Assembly désigne deux réalités en informatique : d'une part le langage de programmation symbolique de plus bas niveau contrôlant directement le processeur (CPU), et d'autre part les unités de déploiement modulaires (.NET assembly).

## 1. Langage de programmation bas niveau (Assembly Language)

Le processeur ne traite que des signaux binaires (code machine / opcodes). Le langage d'assemblage remplace ces octets bruts par des abréviations mnémotechniques lisibles :

- `MOV` : copie des données entre registres ou adresses mémoire.
- `ADD` / `SUB` : effectue des calculs arithmétiques.
- `PUSH` / `POP` : empile ou dépile des valeurs sur la pile d'appels (stack).
- `JMP` / `JE` / `JNE` : modifie l'ordre d'exécution selon les indicateurs d'état.

Les fichiers sources sont transformés directement en code machine par un assembleur (nasm, gas) sans machine virtuelle intermédiaire.

## 2. Registres processeur et architecture x86-64

Dans un processeur 64 bits x86-64, les registres essentiels se divisent en deux groupes :

- **Registres généraux :** `RAX` (accumulateur et valeur de retour), `RBX` (registre de base), `RCX` (compteur de boucle), `RDX` (données), `RDI` et `RSI` (destinations et sources de transferts de blocs).
- **Registres spécialisés :** `RSP` (pointeur de pile), `RBP` (pointeur de trame), `RIP` (pointeur d'instruction vers la commande suivante) et `RFLAGS` (drapeaux d'état).

## 3. CISC vs RISC : différences entre x86-64 et ARM64

L'architecture x86-64 repose sur le modèle **CISC** (jeu d'instructions complexe) permettant des instructions à longueur variable manipulant directement la mémoire. ARM64 (Apple Silicon, smartphones) adopte le modèle **RISC** (jeu d'instructions réduit) à longueur fixe de 32 bits et architecture Load-Store, offrant un rendement énergétique remarquable.

## 4. Appels système (Syscall) et exemple sous Linux x86-64

```
section .text
global _start

_start:
    ; 1. Écriture sur la sortie standard (sys_write = syscall 1)
    mov rax, 1          ; numéro de syscall: 1 (sys_write)
    mov rdi, 1          ; descripteur de fichier: 1 (stdout)
    mov rsi, msg        ; adresse mémoire du texte
    mov rdx, 14         ; longueur du message
    syscall             ; basculement en mode noyau

    ; 2. Terminaison propre (sys_exit = syscall 60)
    mov rax, 60         ; numéro de syscall: 60 (sys_exit)
    xor rdi, rdi        ; code de sortie 0
    syscall

section .data
    msg db "Bonjour monde!", 10
```

## 5. .NET Assembly et WebAssembly (WASM)

- **.NET Assembly :** Lors de la compilation d'un projet C#, le code intermédiaire CIL et ses métadonnées sont encapsulés dans un fichier `.dll` ou `.exe` nommé assembly.
- **WebAssembly (WASM) :** Format binaire portable permettant d'exécuter du code compilé (Rust, C++) dans le navigateur avec des performances quasi natives.

*Le langage assembleur ressemble au montage minutieux des ressorts, rouages et balanciers d'une montre mécanique à la pince de précision : il offre une puissance absolue au prix d'une rigueur sans concession.*

## Questions fréquentes

**Qu'est-ce que le langage Assembly et à quoi sert-il ?**

C'est le langage symbolique le plus proche du matériel, correspondant directement aux instructions du processeur, indispensable pour les pilotes et l'ingénierie inverse.

**Quelle est la différence entre un assembleur et un compilateur ?**

Le compilateur transforme un code de haut niveau structuré en instructions machines, tandis que l'assembleur traduit les mnémoniques un pour un en octets binaires sans restructuration logique.

**Où utilise-t-on encore l'assembleur aujourd'hui ?**

Dans les chargeurs d'amorçage (bootloaders), les systèmes embarqués critiques, l'analyse de malwares et l'optimisation de moteurs graphiques.

## Termes liés

- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Compilation](https://trescout.com/fr/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/fr/dictionary/emulator/)

## Outils liés

- [Apollo-11](https://trescout.com/fr/discover/apollo-11/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l'original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/assembly/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/assembly/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/assembly/
