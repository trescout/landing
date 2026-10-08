# Qu'est-ce que Jailed ?

*Glossaire · Dev · Dernière mise à jour : 29 septembre 2026*

Il s'agit d'une situation dans laquelle un programme est exécuté dans une zone isolée et restreinte, l'empêchant d'accéder au reste du système d'exploitation.

## Définition

Emprisonné fait référence à l'état de sécurité dans lequel un processus logiciel ne peut accéder qu'au répertoire de fichiers, à la mémoire et aux ressources réseau pour lesquels il est autorisé. Cette limitation, appliquée au niveau du système d'exploitation, empêche le programme de nuire au système hôte ou aux autres utilisateurs. Il crée une ligne de défense critique lors du test de code non fiable ou pour isoler le risque de malware.

***Analogie :** C'est comme laisser un invité de la maison s'asseoir uniquement dans la chambre d'amis et verrouiller toutes les autres portes, au lieu de lui permettre de visiter toutes les pièces.*

## Comment ça marche

Le noyau du système d'exploitation limite la racine du processus et ses appels système à des restrictions spéciales. Même si le processus pense se trouver sur le système principal, il ne peut en réalité voir qu'un sous-répertoire virtuel. Si un programme situé dans cette zone isolée plante ou est attaqué, les dégâts subsistent uniquement dans cette zone restreinte.

## Où est-ce utilisé

Il est largement utilisé pour séparer les actions des utilisateurs sur les serveurs Web, dans les applications qui exécutent des plug-ins et dans les plateformes d'exécution de code en ligne.

## Souvent confondu avec

C’est très proche du concept de sandbox ; cependant, prison est un terme plus traditionnel qui se concentre généralement sur l'isolation du système de fichiers sur les systèmes Unix/Linux (tels que chroot ou prison FreeBSD).

## Questions fréquentes

**Un programme emprisonné peut-il accéder au système principal ?**

Dans des circonstances normales, non. Cependant, ces limites peuvent être dépassées si une vulnérabilité au niveau du noyau (vulnérabilité de jailbreak) est détectée.

**Les technologies de conteneurs sont-elles aussi des prisons ?**

Les structures de conteneurs modernes (telles que Docker) constituent une évolution beaucoup plus avancée et plus intéressante de la logique de prison traditionnelle.

## Termes liés

- [Sandbox](https://trescout.com/fr/dictionary/sandbox/)
- [Containers](https://trescout.com/fr/dictionary/containers/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Security Scanner](https://trescout.com/fr/dictionary/security-scanner/)

## Outils liés

- [Madeira](https://trescout.com/fr/discover/madeira/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/jailed/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/jailed/
