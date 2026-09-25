# Suite d'ingénierie inverse logicielle et d'analyse

Ghidra est une suite logicielle d'ingénierie inverse (SRE) complète et open-source développée par la National Security Agency (NSA). Équipée d'un moteur de décompilation performant en C++ et d'un environnement Java, elle traduit les binaires compilés en code source intelligible et offre une analyse symbolique avancée sur des dizaines d'architectures.

- ★ 78.142
- Java
- GitHub Trending · 2026-08-28

## Mises à jour
- 17 septembre 2026: Étoiles 78 142, dernière version Ghidra_12.1.3_build (support Java 21, optimisations des décompilateurs RISC-V et ARM64).

## Ce que ça vous apporte
- Décompilateur C robuste intégré: Convertit le langage machine et l'assembleur en pseudo-code C lisible de haut niveau.
- Large support multi-architecture: Prise en charge de x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC et de multiples microcontrôleurs.
- Collaboration multi-utilisateurs: Travaillez en équipe sur le même fichier binaire avec annotations partagées et gestion de versions via Ghidra Server.
- Analyse headless automatisée: Lancez des scripts d'audit de vulnérabilités et de détection de malwares en ligne de commande sans interface graphique.
- Extensibilité Java et Python: Développez des plugins personnalisés, déballeurs de code et parseurs de types de données.

## Installation et prérequis système

**Installation de JDK 21 et Ghidra**

```
# Sur macOS via Homebrew :
brew install --cask ghidra

# Linux / Windows (Démarrage manuel depuis l'archive) :
# Nécessite un JDK 21 64-bit installé.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Exécution et analyse automatisée en ligne de commande

**Lancer l'interface graphique**

```
./ghidraRun
```

**Exécuter une analyse headless sans GUI**

```
analyzeHeadless /chemin/projet NomProjet -import cible.bin -postScript AuditSecurite.py
```

## Architecture technique : Sleigh et moteur de décompilation

Les piliers techniques qui font de Ghidra un standard de la sécurité comprennent :
- Langage de spécification Sleigh: Langage déclaratif dédié permettant de décrire les jeux d'instructions et registres de nouveaux processeurs.
- Représentation intermédiaire P-Code: Normalise toutes les instructions assembleur en un langage intermédiaire commun pour une analyse de flux indépendante du matériel.
- Moteur de décompilation natif en C++: Élimine le code mort, structure les boucles de contrôle et reconstitue les types de variables avec une grande rapidité.

## Scénarios d'ingénierie inverse et d'audit de sécurité

Ghidra intervient au cœur des investigations de sécurité offensive et défensive :
- Analyse de logiciels malveillants (Malware Triage): Déchiffre les chaînes obfusquées et identifie les appels d'API système et serveurs C2.
- Diffing de binaires (Program Diff): Compare deux versions d'un binaire pour isoler les correctifs de sécurité et comprendre la vulnérabilité corrigée.
- Audit de microprogrammes (Firmware): Cartographie les images mémoire de cartes électroniques pour analyser bootloaders et firmwares IoT.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite inspecter un exécutable suspect avec Ghidra. Peux-tu m'expliquer pas à pas comment créer un projet, importer le fichier, exécuter l'Auto Analysis, naviguer dans la fenêtre du décompilateur et repérer les appels d'API potentiellement dangereux ?

- **Pour qui:** Analystes de malwares, chercheurs en vulnérabilités, ingénieurs en rétro-ingénierie et développeurs firmware.
- **Licence:** Apache-2.0 (Licence open-source permissive)
- **Développeur:** National Security Agency (NSA) et communauté open-source
- **Prérequis:** Java Development Kit (JDK) 21 64-bit

## Questions fréquentes
- Quelles sont les différences clés entre Ghidra et IDA Pro ? Contrairement à IDA Pro qui impose des licences commerciales onéreuses par architecture, Ghidra est totalement gratuit, open-source, inclut le décompilateur pour toutes les cibles et intègre un serveur collaboratif.
- L'analyse avec Ghidra présente-t-elle un danger face à un malware ? Non, l'analyse statique ne fait que désassembler les octets sans jamais exécuter le binaire. Néanmoins, opérer au sein d'une machine virtuelle isolée reste indispensable.
- Comment mettre en place un serveur Ghidra ? Le script svrAdmin inclus dans l'archive permet de lancer un serveur collaboratif sur votre réseau local en quelques minutes avec gestion des comptes utilisateurs.
- Peut-on utiliser Python 3 dans Ghidra ? Bien que Jython (Python 2.7) soit intégré par défaut, le module PyGhidra permet d'exécuter du code Python 3 moderne avec accès à l'ensemble des bibliothèques externes.

## Liens
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## Termes associés du glossaire
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/fr/discover/ghidra/
