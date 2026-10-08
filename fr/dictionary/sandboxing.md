# Qu'est-ce que Sandboxing ?

*Glossaire · Dev · Dernière mise à jour : 3 octobre 2026*

Technique consistant à exécuter des logiciels ou du code suspect dans un environnement isolé afin d'éviter qu'ils n'endommagent le système principal et son environnement.

## Définition

Le sandboxing est la pratique consistant à exécuter des fragments de code non fiables ou en phase de test dans une zone contrôlée, en les isolant des ressources système. Ce mécanisme limite l'accès direct de l'application au système de fichiers, au réseau local ou au noyau du système d'exploitation. C'est une couche de sécurité indispensable pour empêcher la propagation de vulnérabilités dans le système et réduire à néant l'impact des logiciels malveillants.

***Analogie :** Cela revient à réaliser une expérience chimique potentiellement dangereuse non pas au milieu de la pièce, mais à l'intérieur d'une cloche en verre antidéflagrante.*

## Comment ça marche

Une barrière de protection est mise en place à l'aide de restrictions au niveau du système d'exploitation ou d'outils de virtualisation. Lorsque le code est exécuté, il ne peut utiliser que l'espace mémoire et disque restreint qui lui a été autorisé. Les appels système sont constamment surveillés ; lorsqu'une tentative d'opération non autorisée est détectée, le logiciel est immédiatement arrêté.

## Où est-ce utilisé

Il est utilisé pour exécuter des scripts tiers dans les navigateurs Web, dans les logiciels de sécurité qui analysent des fichiers suspects en pièces jointes d'e-mails, et dans les environnements de développement où les agents d'intelligence artificielle exécutent du code.

## Souvent confondu avec

Alors que le terme sandbox désigne l'espace isolé lui-même, le sandboxing fait référence au processus de création, de gestion et de limitation de cet environnement sécurisé.

## Questions fréquentes

**Le sandboxing réduit-il de manière significative les performances du système ?**

Bien que la surveillance des appels système entraîne une légère charge de traitement, cette perte est généralement minime et imperceptible dans les systèmes d'exploitation modernes.

**Pourquoi le sandboxing est-il nécessaire dans les outils d'intelligence artificielle ?**

Étant donné que le code généré et exécuté par les modèles d'intelligence artificielle peut présenter un risque de suppression de fichiers critiques sur le système d'exploitation, ces opérations sont exécutées dans une couche d'isolation sécurisée.

## Termes liés

- [Sandbox](https://trescout.com/fr/dictionary/sandbox/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Virtual Machines](https://trescout.com/fr/dictionary/virtual-machines/)
- [Security Scanner](https://trescout.com/fr/dictionary/security-scanner/)

## Outils liés

- [Agent Governance Toolkit](https://trescout.com/fr/discover/agent-governance-toolkit/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/sandboxing/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/sandboxing/
