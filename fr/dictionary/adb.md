# Qu'est-ce que ADB ?

> Android Debug Bridge

ADB (Android Debug Bridge), un outil permettant d'établir une communication de commande et de débogage entre un ordinateur et un appareil Android.

## Définition et origine du mot
Debug signifie débogage et bridge signifie pont. ADB assure la communication entre le client sur l'ordinateur et le démon adb sur l'appareil ; il est utilisé pour l'installation d'applications, la collecte de journaux, le débogage et la gestion limitée des appareils. Il fait partie du package Android SDK Platform-Tools.

## Comment connaître et utiliser dans la vie quotidienne ?
Développement: Installation d'applications et enregistrement.Test : Test sur plusieurs appareils.Personnalisation : Paramètre avancé.

## Profondeur technique et architecture
Disposition triple :

## Choses fréquemment mélangées
On le confond avec le transfert de fichiers. Celui-ci ne fait que copier, alors qu'ADB intervient dans le système. La différence d'autorisation est grande.

## Utilisation dans différentes disciplines
Câble : La ligne transportant le signal.Interprète: La langue des deux parties.Contrôle : Gestion à distance.

## Foire aux questions
**Tout le monde peut-il l'utiliser ?**
Les commandes de base peuvent être apprises ; cependant, l'utilisation d'adb shell et les opérations de suppression nécessitent des connaissances techniques. Il est nécessaire de vérifier l'effet d'une commande avant de l'exécuter.

**Est-ce que cela fonctionne sans fil ?**
Oui. Sur les versions Android prises en charge, une connexion peut être établie via Wi-Fi après l'appairage avec l'appareil. La stabilité et la vitesse dépendent de la qualité du réseau local.

**Est-ce sécuritaire?**
Si vous avez l'appareil, oui. L'autorisation n'est pas accordée sur un appareil branché sur un ordinateur inconnu.

**Quelle est la différence avec Fastboot ?**
ADB communique avec le système d'exploitation pendant qu'Android est en cours d'exécution. Fastboot, quant à lui, est utilisé pour les images de partition ou les opérations de micrologiciel lorsque l'appareil est en mode bootloader ; les commandes prises en charge et le processus de déverrouillage varient selon l'appareil.


## Termes liés
- [CLI](/fr/dictionary/cli/)
- [SDK](/fr/dictionary/sdk/)
- [Emulator](/fr/dictionary/emulator/)

## Outils liés
- [Universal Android Debloater Next Generation](/fr/discover/universal-android-debloater-next-generation/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/adb/
