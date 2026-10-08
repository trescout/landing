# Qu'est-ce que Clone ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le clonage est le processus de création d'une copie locale d'un dépôt Git distant, avec l'ensemble de son historique.

## Définition et origine du mot

Clone signifie copie exacte en anglais. Dans le monde de Git, il est utilisé avec la commande git clone : vous téléchargez non seulement les fichiers actuels, mais aussi l'historique complet des commits, les branches et les tags du projet.

***Analogie :** C'est comme prendre non pas seulement une photo d'une page d'un livre de la bibliothèque, mais prendre une copie entière du livre pour la placer sur votre propre étagère.*

## Comment connaître et utiliser dans la vie quotidienne ?

Lorsque vous souhaitez examiner ou contribuer à un projet open source, la première étape consiste généralement à le cloner :

```
git clone https://github.com/kullanici/proje.git
```

Lorsque la commande s'exécute, un dossier de projet est créé dans votre répertoire actuel. Si le dépôt est trop volumineux, un clonage superficiel est utilisé pour n'en récupérer qu'une partie :

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Profondeur technique et architecture

Le répertoire .git à l'intérieur du dossier cloné est la mémoire du dépôt : tous les objets de commit, les pointeurs de branches et les adresses distantes s'y trouvent. Après le clonage :

git fetch télécharge les modifications distantes sans toucher à vos fichiers.
git pull télécharge et fusionne les modifications dans votre branche actuelle.
git push envoie vos commits vers un dépôt distant (si vous en avez l'autorisation).
Le fork, quant à lui, crée une copie côté serveur. Le clone télécharge cette copie ou le dépôt d'origine sur votre ordinateur. Ce sont deux concepts différents.

## Utilisation dans différentes disciplines

**Biologie :** Copie génétique d'un organisme vivant. En logiciel, un clone est une copie de données, cela n'a rien à voir avec un organisme vivant.
**Médias :** Costumes de rechange sur lesquels travailler pendant que l'original est conservé.
**Virtualisation :** Création d'une nouvelle machine à partir d'un modèle prédéfini.

## Foire aux questions

**Puis-je modifier le projet après le clonage ?**

Oui. Vous apportez les modifications de votre choix sur votre propre copie. Le dépôt d'origine n'est pas affecté. Si vous souhaitez proposer votre modification au projet, vous ouvrez une pull request.

**Quelle est la différence entre fork et clone ?**

Un fork crée une copie sur le serveur (sur votre compte), un clone télécharge cette copie sur votre ordinateur. Le flux de contribution se fait généralement par un fork, puis un clone.

**Que dois-je faire si le dépôt est trop volumineux ?**

Effectuez un clonage superficiel avec --depth 1 ou téléchargez uniquement une seule branche (--single-branch). Vous pourrez approfondir l'historique plus tard si nécessaire.

**Vais-je garder le clone à jour ?**

Oui. Il vous suffit d'exécuter git pull dans le dossier. Si vous avez des modifications, vous devez d'abord les valider (commit) ou les remiser (git stash).

## Termes liés

- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/fr/dictionary/self-hosting/)

## Outils liés

- [MoneyPrinterTurbo](https://trescout.com/fr/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/fr/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/fr/discover/clone-wars/)
- [Univer](https://trescout.com/fr/discover/univer/)
- [OpenStock](https://trescout.com/fr/discover/openstock/)
- [Hermes WebUI](https://trescout.com/fr/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/fr/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/fr/discover/flowsint/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/clone/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/clone/
