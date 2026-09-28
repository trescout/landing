# Cadre d'analyse pour l'ingénierie inverse de logiciels

Ghidra est un cadre complet d'ingénierie inverse logicielle (SRE) développé par la National Security Agency (NSA) et partagé en open source. Plateforme développée avec le noyau Java et C++ ; Il convertit les fichiers binaires compilés en code source, offrant aux chercheurs en sécurité des décompilations avancées, une analyse symbolique et une prise en charge multi-architecture.

- ★ 79 733
- Java
- GitHub Trending · 2026-08-28

## Ce que ça vous apporte
- Décompilateurs C puissants intégrés : conversion du code machine et des instructions d'assemblage en une syntaxe lisible et de haut niveau de type C.
- Large gamme de processeurs et d'architectures : prise en charge de x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC et des centaines d'architectures de microcontrôleurs embarqués.
- Analyse collaborative multi-utilisateurs : annotation, dénomination de fonctions et contrôle de version simultanés sur le même fichier binaire avec l'infrastructure Ghidra Server.
- Automatisation et analyse Headless : analyse automatique de milliers de logiciels malveillants sur le serveur à partir de la ligne de commande sans entrer dans l'interface graphique.
- Extensibilité avec Java et Python : personnalisez l'analyse avec des scripts personnalisés, des plug-ins et des bibliothèques de types de données.

## Configuration requise pour l'installation et le système
**Installation du JDK 21 et de Ghidra**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```


## Exécution et analyse de ligne de commande sans tête
**Démarrage de l'interface graphique**

```
./ghidraRun
```

**Exécution d'une analyse automatique sans tête**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```


## Architecture technique : moteur Sleigh et décompilateur
- Langage de modélisation de processeur Sleigh : langage de description déclaratif utilisé pour introduire un nouveau processeur ou une nouvelle architecture de jeu d'instructions (ISA) dans Ghidra.
- Couche de représentation intermédiaire (IR) P-Code : réalisation d'une analyse de flux de données et de flux de contrôle indépendante de l'architecture en traduisant toutes les instructions du processeur dans un langage intermédiaire commun (P-Code).
- Moteur de décompilation basé sur C++ : moteur natif hautes performances qui simplifie les graphiques de flux de contrôle, extrait les types de variables et réduit les boucles complexes au code C.

## Workflows d’ingénierie inverse et d’analyse de vulnérabilité
- Analyse des logiciels malveillants (Malware Triage) : ouverture isolée des exécutables suspects et révélation des appels API cachés, des domaines C2 et des clés de chiffrement.
- Comparaison de fichiers binaires (Program Diff) : Détection de la vulnérabilité fermée en visualisant les différences entre deux fichiers avant et après le correctif de sécurité.
- Analyse du micrologiciel : placer les vidages de mémoire flash brute des appareils IoT dans la carte mémoire et analyser les fonctions du chargeur de démarrage et du noyau.

## Si vous ne codez pas
Je souhaite examiner un fichier binaire suspect à l'aide de Ghidra. Pouvez-vous expliquer étape par étape comment ouvrir un nouveau projet dans Ghidra, importer le fichier, exécuter Auto Analysis, examiner les fonctions dans la fenêtre du décompilateur et détecter les fonctions API suspectes appelées ?

## Questions fréquemment posées
- Quelles sont les principales différences entre Ghidra et IDA Pro ? Bien qu'IDA Pro ait des frais de licence commerciaux et élevés, Ghidra est entièrement gratuit et open source. Ghidra propose des décompilateurs intégrés pour toutes les architectures et comprend un serveur de collaboration multi-utilisateurs.
- Ghidra est-il sûr lors de l’analyse de logiciels malveillants ? Oui, lors de l'analyse statique, le fichier n'est pas exécuté, seulement décodé. Cependant, il est essentiel pour la sécurité que l'analyse soit effectuée dans une machine virtuelle (VM) isolée.
- Comment installer le serveur Ghidra ? Avec le script svrAdmin dans le répertoire du serveur inclus dans le package Ghidra, un serveur d'équipe peut être ouvert sur le réseau local en quelques minutes et des privilèges utilisateur peuvent être attribués.
- Les scripts Python 3 peuvent-ils être exécutés dans Ghidra ? Bien que Ghidra soit livré par défaut avec Jython (Python 2.7), les environnements Python 3 modernes et les bibliothèques externes (NumPy, Capstone) peuvent être utilisés directement grâce au plugin PyGhidra.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ghidra/
