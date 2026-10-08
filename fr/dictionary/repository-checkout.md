# Qu'est-ce que Repository Checkout ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

L'extraction du référentiel est le processus de téléchargement d'une version spécifique du référentiel sur votre espace de travail.

## Définition et origine du mot

Vous récupérez la version actuelle du projet sur le serveur et l'apportez à votre bureau. C'est comme emprunter un livre à la bibliothèque : la source reste, vous travaillez avec la copie. Les informations sur l’historique et la version sont fournies avec la copie.

***Analogie :** C'est comme emprunter un livre à la bibliothèque, l'apporter à votre bureau et commencer à lire les pages une par une.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Nouveau projet :** Téléchargement du référentiel pour la première fois.
**Migration de versions :** Ne revenez pas à l’ancienne balise et examinez l’erreur.
**Essayez la branche :** N'ouvrez pas la succursale de votre ami localement.

## Profondeur technique et architecture

Le flux est le suivant :

```
git clone https://github.com/ornek/proje.git
cd proje
git checkout v2.0.0
```

Distinctions :

**Cloner:** Téléchargement de l'intégralité du référentiel pour la première fois.
**Vérifier:** Changement de version ou de branche dans le référentiel téléchargé.
**Changer/Restaurer :** Branchement et récupération de commandes dans Git moderne.
**Clairsemé:** Téléchargement uniquement du dossier requis dans l'immense référentiel.

Règle : Ne réussissez pas tant que votre travail est enregistré, validez-le ou enregistrez-le d'abord.

## Utilisation dans différentes disciplines

**Bibliothèque :** Ne retirez pas le livre de l'étagère et ne l'apportez pas à la table.
**Archive:** Supprimez le dossier du stockage et examinez-le.
**Photographier:** Ne subissez pas la pression du négatif.

## Foire aux questions

**Est-ce qu'il télécharge uniquement des fichiers ?**

Non. Les informations sur l'historique et la version sont également incluses, vous pouvez donc revenir à l'ancienne version.

**Quelle est la différence avec Cloner ?**

Le clonage est le téléchargement initial, la validation est le passage par le référentiel téléchargé. L’ordre va dans ce sens.

**Comment revenir à l'ancienne version ?**

Il est transmis avec une balise ou un hachage de validation. S'il existe une tâche enregistrée, elle est stockée en premier.

**Qu’est-ce que Switch ?**

C'est la commande moderne de créer une branche. Comme le paiement fait beaucoup de travail, Git l'a divisé en deux : passer à la branche, restaurer le fichier.

## Termes liés

- [Git Push](https://trescout.com/fr/dictionary/git-push/)
- [Tech Stack](https://trescout.com/fr/dictionary/tech-stack/)
- [Cloning](https://trescout.com/fr/dictionary/cloning/)

## Outils liés

- [Checkout](https://trescout.com/fr/discover/checkout/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/repository-checkout/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/repository-checkout/
