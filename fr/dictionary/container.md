# Qu'est-ce que Container ?

Un conteneur permet de regrouper le code d'une application et ses dépendances dans un seul paquet afin qu'il fonctionne de la même manière dans n'importe quel environnement.

## Définition et origine du mot
Les conteneurs regroupent le code, les bibliothèques et les configurations d'une application dans un seul paquet. Il fonctionne sur le serveur exactement comme sur votre ordinateur. L'idée est ancienne (chroot, LXC), elle s'est popularisée avec Docker après 2013 et est définie aujourd'hui par la norme OCI.

## Comment connaître et utiliser dans la vie quotidienne ?
Distribution : Le même paquet, du développeur à la production.Microservices : Chaque service a sa propre boîte.CI : Chaque test s'exécute dans une boîte propre.

## Profondeur technique et architecture
Concepts :

## Choses fréquemment mélangées
Souvent confondu avec une machine virtuelle. La machine transporte un système d'exploitation complet, le conteneur ne transporte que l'application. L'isolation est forte sur la machine, suffisante dans le conteneur ; le choix dépend de la charge.

## Utilisation dans différentes disciplines
Transport : Compatibilité navire, train, camion grâce à des conteneurs de taille standard.Cuisine : Une boîte de repas prête avec ses ingrédients à l'intérieur.Camping : Un kit de camping transporté avec son organisation dans son sac.

## Foire aux questions
**Pourquoi le conteneur est-il si populaire ?**
Parce qu'il garantit le même fonctionnement et une installation rapide dans tous les environnements. Il est devenu la norme avec les microservices et l'orchestration cloud.

**Quelle est la différence entre un conteneur et une machine virtuelle ?**
La machine transporte son propre système d'exploitation, tandis que le conteneur partage le noyau hôte. Le conteneur est léger et rapide, la machine est forte en isolation.

**Un conteneur est-il sécurisé ?**
Puisque le noyau est partagé, il n'est pas aussi isolé qu'une machine. Vous devez extraire les images d'une source fiable et les maintenir à jour.

**Quand privilégie-t-on une machine virtuelle ?**
Lorsqu'un système d'exploitation différent ou une isolation renforcée est nécessaire. Pour la plupart des autres charges de travail, un conteneur suffit.


## Termes liés
- [Containers](/fr/dictionary/containers/)
- [Virtual Machines](/fr/dictionary/virtual-machines/)
- [Deployment](/fr/dictionary/deployment/)

## Outils liés
- [N8n](/fr/discover/n8n/)
- [Stirling-PDF](/fr/discover/stirling-pdf/)
- [Core](/fr/discover/core/)
- [Container](/fr/discover/container/)
- [Mattermost](/fr/discover/mattermost/)
- [Keycloak](/fr/discover/keycloak/)
- [Trivy](/fr/discover/trivy/)
- [PPF Contact Solver](/fr/discover/ppf-contact-solver/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/container/
