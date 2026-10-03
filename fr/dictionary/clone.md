# Qu'est-ce que Clone ?

Le clonage est le processus de création d'une copie locale d'un dépôt Git distant, avec l'ensemble de son historique.

## Définition et origine du mot
Clone signifie copie exacte en anglais. Dans le monde de Git, il est utilisé avec la commande git clone : vous téléchargez non seulement les fichiers actuels, mais aussi l'historique complet des commits, les branches et les tags du projet.

## Comment connaître et utiliser dans la vie quotidienne ?
Lorsque vous souhaitez examiner ou contribuer à un projet open source, la première étape consiste généralement à le cloner :

## Profondeur technique et architecture
Le répertoire .git à l'intérieur du dossier cloné est la mémoire du dépôt : tous les objets de commit, les pointeurs de branches et les adresses distantes s'y trouvent. Après le clonage :

## Utilisation dans différentes disciplines
Biologie : Copie génétique d'un organisme vivant. En logiciel, un clone est une copie de données, cela n'a rien à voir avec un organisme vivant.Médias : Costumes de rechange sur lesquels travailler pendant que l'original est conservé.Virtualisation : Création d'une nouvelle machine à partir d'un modèle prédéfini.

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
- [CLI](/fr/dictionary/cli/)
- [Open Source](/fr/dictionary/open-source/)
- [Self-Hosting](/fr/dictionary/self-hosting/)

## Outils liés
- [MoneyPrinterTurbo](/fr/discover/moneyprinterturbo/)
- [VoxCPM](/fr/discover/voxcpm/)
- [Clone-Wars](/fr/discover/clone-wars/)
- [Univer](/fr/discover/univer/)
- [OpenStock](/fr/discover/openstock/)
- [Hermes WebUI](/fr/discover/hermes-webui/)
- [Production Agentic RAG Course](/fr/discover/production-agentic-rag-course/)
- [Flowsint](/fr/discover/flowsint/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/clone/
