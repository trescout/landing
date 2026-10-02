# Qu'est-ce que Deployment ?

Le déploiement (deployment) est le processus par lequel un composant logiciel, développé et testé dans un environnement local, est compilé, installé sur des serveurs cibles ou une infrastructure cloud, et rendu accessible aux utilisateurs finaux.

## Cadre conceptuel, étymologie et transformation historique
Le terme « déploiement » repose étymologiquement sur la terminologie militaire ; il désigne l'envoi de troupes, de munitions ou de la marine vers des positions de combat stratégiques afin de les rendre opérationnelles (« to deploy »). En génie logiciel, il a débuté dans les années 1970 et 1980 avec le chargement de cartes perforées ou de bandes magnétiques sur des ordinateurs centraux (mainframes) ; il a évolué vers des transferts de fichiers FTP/SSH manuels dans les années 1990, pour aboutir aujourd'hui à des pipelines cloud entièrement déclaratifs et automatisés (GitOps).

## Stratégies de déploiement sans interruption (Zero-Downtime)
Les principaux modèles de déploiement développés pour éviter que les utilisateurs ne subissent d'interruption de service lors de la mise à jour des applications sont les suivants :

## Pipeline CI/CD, GitOps et migrations de bases de données
Une architecture de déploiement réussie repose sur trois piliers d'ingénierie critiques :

## Gestion des erreurs, observabilité et architecture de retour arrière (Rollback)
Il existe deux bouées de sauvetage essentielles pour les erreurs en environnement de production qui passent inaperçues, même dans les environnements de test les plus avancés :

## Souvent confondu avec

## Questions fréquentes
**Que signifie « Deployment » et quel est son équivalent en français ?**
C'est un terme d'origine anglaise qui signifie « déploiement » ou « mise en production ». Il s'agit du processus consistant à compiler le paquet logiciel et à le rendre opérationnel sur les serveurs cibles ou dans un environnement cloud.

**Quelle est la différence entre le déploiement et la mise en ligne (release) ?**
Le déploiement est l'installation technique et l'exécution du code sur le serveur. La mise en production (release) est l'ouverture officielle de la fonctionnalité à l'utilisateur final via des Feature Flags ou des étapes marketing.

**Quelle est la différence fondamentale entre le déploiement Bleu-Vert (Blue-Green) et le déploiement Canary ?**
Dans le déploiement Bleu-Vert, il existe deux environnements identiques et le trafic est basculé à 100 % vers le nouvel environnement en une seule fois via un équilibreur de charge. Dans le déploiement Canary, la nouvelle version est présentée progressivement, d'abord à une petite tranche d'utilisateurs de 1 à 5 %, puis le taux est augmenté après observation des métriques.

**Comment les changements de schéma de base de données sont-ils gérés dans un déploiement sans interruption (Zero-Downtime) ?**
Ils sont gérés avec le modèle Expand-Contract (Expansion-Contraction). De nouveaux champs rétrocompatibles sont d'abord ajoutés, puis une fois que tous les serveurs du système sont passés au nouveau code et que le flux de données est assuré, les anciens champs sont supprimés.


## Termes liés
- [Runtime](/fr/dictionary/runtime/)
- [Compile-time](/fr/dictionary/compile-time/)
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [Production Pipeline](/fr/dictionary/production-pipeline/)
- [Tech Stack](/fr/dictionary/tech-stack/)
- [Git Push](/fr/dictionary/git-push/)

## Outils liés
- [Rocket.Chat](/fr/discover/rocket-chat/)
- [Chatwoot](/fr/discover/chatwoot/)
- [Argo Cd](/fr/discover/argo-cd/)
- [Openship](/fr/discover/openship/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/deployment/
