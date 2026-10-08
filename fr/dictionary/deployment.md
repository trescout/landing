# Qu'est-ce que Deployment ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Le déploiement (deployment) est le processus par lequel un composant logiciel, développé et testé dans un environnement local, est compilé, installé sur des serveurs cibles ou une infrastructure cloud, et rendu accessible aux utilisateurs finaux.

## Cadre conceptuel, étymologie et transformation historique

Le terme « déploiement » repose étymologiquement sur la terminologie militaire ; il désigne l'envoi de troupes, de munitions ou de la marine vers des positions de combat stratégiques afin de les rendre opérationnelles (« to deploy »). En génie logiciel, il a débuté dans les années 1970 et 1980 avec le chargement de cartes perforées ou de bandes magnétiques sur des ordinateurs centraux (mainframes) ; il a évolué vers des transferts de fichiers FTP/SSH manuels dans les années 1990, pour aboutir aujourd'hui à des pipelines cloud entièrement déclaratifs et automatisés (GitOps).

Dans le génie logiciel moderne, le déploiement a cessé d'être une opération ponctuelle, pénible et risquée effectuée au milieu de la nuit. Grâce aux mécanismes d'Intégration Continue et de Déploiement Continu (CI/CD), il s'agit désormais d'un flux de travail standard où le code est transféré en toute sécurité vers l'environnement de production des centaines de fois par jour.

***Analogie :** Cela ressemble à une opération de changement de voie pour un train à grande vitesse rempli de passagers. Dans la méthode traditionnelle, il fallait arrêter le train en gare et souder les rails (temps d'arrêt / downtime) ; le déploiement moderne consiste à ce que l'aiguillage automatique bascule sur la nouvelle voie en quelques millisecondes alors que le train roule à 300 km/h, sans que les passagers ne ressentent la moindre secousse.*

## Stratégies de déploiement sans interruption (Zero-Downtime)

Les principaux modèles de déploiement développés pour éviter que les utilisateurs ne subissent d'interruption de service lors de la mise à jour des applications sont les suivants :

1. Déploiement bleu-vert (Blue-Green Deployment) : Deux environnements de serveur identiques sont maintenus, l'un traitant le trafic en direct (Bleu) et l'autre restant inactif (Vert). Le nouveau code est déployé dans l'environnement vert, des tests de fumée (smoke tests) sont effectués et, une fois que tout fonctionne parfaitement, l'équilibreur de charge (Load Balancer) redirige le trafic vers le vert en quelques millisecondes. En cas de problème, un retour immédiat au bleu est effectué (rollback instantané).
2. Déploiement canari (Canary Deployment) : tire son nom de la pratique des mineurs de charbon du XIXe siècle qui emportaient des canaris en cage pour détecter précocement les fuites de gaz toxiques. La nouvelle version est d'abord déployée auprès de seulement 1 % à 5 % du trafic total des utilisateurs. Les taux d'erreur (HTTP 5xx), la consommation de mémoire et les temps de réponse sont surveillés ; si le système est stable, le taux est progressivement augmenté à 25 %, 50 % puis 100 %.
3. Déploiement progressif (Rolling Deployment) : il s'agit de mettre à jour les conteneurs un par un (par exemple par tranches de 20 %) dans des clusters Kubernetes ou des flottes de serveurs. Les anciens pods sont arrêtés successivement et remplacés par des pods de la nouvelle version. Cette méthode ne nécessite pas de coûts matériels supplémentaires, mais impose de gérer une période de transition durant laquelle deux versions différentes fonctionnent simultanément en production.
4. Déploiement fantôme (Shadow Deployment) : Le trafic des utilisateurs réels est dupliqué (miroir de trafic) et envoyé simultanément à la nouvelle version fonctionnant en arrière-plan. Cependant, les réponses générées par cette nouvelle version ne sont pas transmises à l'utilisateur ; elles servent uniquement à mesurer la performance du système sous une charge réelle et la précision de l'algorithme.

## Pipeline CI/CD, GitOps et migrations de bases de données

Une architecture de déploiement réussie repose sur trois piliers d'ingénierie critiques :

- Automatisation CI/CD et métriques DORA : lorsqu'un ingénieur s'engage dans le référentiel Git, le code est automatiquement vérifié, des tests unitaires et des tests d'intégration sont exécutés, l'image du conteneur Docker est compilée et lancée dans l'environnement cible. Selon les métriques DevOps Research and Assessment (DORA), les équipes performantes réduisent la fréquence de déploiement à quelques heures, tout en minimisant le délai de livraison des modifications (Lead Time) et le taux d'échec.
- Principe GitOps : Les versions d'infrastructure et d'application sont déclarées directement par un dépôt Git avec des outils comme ArgoCD ou Flux. Le référentiel Git est la seule source de vérité ; Si l'état réel sur les serveurs diffère de l'état dans Git, le système se synchronise automatiquement.
- Dilemme de schéma de base de données (modèle d'extension-contrat) : le code peut être mis à jour sans aucun temps d'arrêt, mais une suppression de colonne dans les tables de base de données peut provoquer le blocage de l'ancienne version. Par conséquent, les ingénieurs appliquent le modèle « Développer-Réduire » (exécution parallèle) : tout d'abord, la nouvelle colonne est ajoutée et écrite dans les deux versions, après la mise à niveau de tous les serveurs vers la nouvelle version, l'ancienne colonne est supprimée en toute sécurité.

## Gestion des erreurs, observabilité et architecture de retour arrière (Rollback)

Il existe deux bouées de sauvetage essentielles pour les erreurs en environnement de production qui passent inaperçues, même dans les environnements de test les plus avancés :

- Rollback automatique : dès que les outils APM (Datadog, Prometheus) détectent des anomalies dans les seuils d'erreur (par exemple, le taux d'erreur dépasse 1 %), ils reviennent à l'image Docker stable précédente ou à la balise Git sans nécessiter d'intervention humaine.
- Indicateurs de fonctionnalité : sépare les processus de déploiement et de publication. Même si le code s'exécute sur le serveur, la nouvelle fonctionnalité peut rester désactivée dans l'interface utilisateur ; En cas de risque, il peut être désactivé instantanément avec une seule touche du tableau de bord.

## Souvent confondu avec

- Développement vs déploiement : le développement se produit lorsque le chef prépare et goûte les plats dans la cuisine ; Le déploiement se produit lorsque la nourriture est servie à table et présentée au client pour consommation.
- Déploiement vs Release : le déploiement est une action technique ; Il fait référence au téléchargement du code sur le serveur. La publication signifie rendre une fonctionnalité visible aux utilisateurs, faire une annonce marketing et l'ouvrir officiellement par l'unité commerciale.

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

- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Compile-time](https://trescout.com/fr/dictionary/compile-time/)
- [Cloud Computing](https://trescout.com/fr/dictionary/cloud-computing/)
- [Production Pipeline](https://trescout.com/fr/dictionary/production-pipeline/)
- [Tech Stack](https://trescout.com/fr/dictionary/tech-stack/)
- [Git Push](https://trescout.com/fr/dictionary/git-push/)

## Outils liés

- [Rocket.Chat](https://trescout.com/fr/discover/rocket-chat/)
- [Chatwoot](https://trescout.com/fr/discover/chatwoot/)
- [Argo Cd](https://trescout.com/fr/discover/argo-cd/)
- [Openship](https://trescout.com/fr/discover/openship/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/deployment/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/deployment/
