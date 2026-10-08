# Qu'est-ce que Virtual Machines ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Une machine virtuelle (en anglais *virtual machine*) est un ordinateur indépendant qui partage le matériel.

## Définition et origine du mot

"Virtual" signifie virtuel. Plusieurs systèmes d'exploitation s'exécutent sur une seule machine. Chacun fonctionne de manière isolée avec ses propres ressources et ne nuit pas au système hôte.

***Analogie :** C'est semblable à la location de chambres avec des portes séparées dans une même maison.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Présentateur:** Hébergement multi-locataire.
**Test :** Essai de différents systèmes.
**Développement:** Environnement de test propre.

## Profondeur technique et architecture

Couches :

**Hyperviseur :** Le logiciel qui partitionne le matériel.
**Invité :** Le système qui s'exécute au-dessus.
**Instantané :** Image instantanée, billet de retour.

Machine rapide :

```
multipass launch --name test --cpus 2 --memory 4G
```

Différence des conteneurs : La machine transporte le système, le conteneur transporte l'application. L'isolation est plus forte dans la machine.

## Choses fréquemment mélangées

On le prend pour un conteneur. La machine est un système complet, le conteneur a un noyau partagé. L'un est un appartement, l'autre de la colocation.

## Utilisation dans différentes disciplines

**Chambres :** Compartiments aux portes indépendantes.
**Appartement :** Immeuble commun, espace privé.
**Conteneur :** Transport compartimenté.

## Foire aux questions

**Est-ce que cela ralentit ?**

Il y a un coût de partage. Il ne se remarque pas avec un dimensionnement correct.

**Le virus peut-il passer ?**

Généralement non. L'isolation est forte, le dossier partagé est surveillé.

**Combien de ressources sont attribuées ?**

Elles sont déterminées selon la tâche. Ajustées progressivement grâce à la surveillance.

**Quelle est la différence avec le conteneur ?**

La machine transporte le système, le conteneur transporte l'application. L'isolation et la vitesse sont échangées.

## Termes liés

- [Containers](https://trescout.com/fr/dictionary/containers/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Self-hosting](https://trescout.com/fr/dictionary/self-hosting/)

## Outils liés

- [Container](https://trescout.com/fr/discover/container/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/virtual-machines/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/virtual-machines/
