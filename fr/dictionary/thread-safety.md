# Qu'est-ce que Thread-safety ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

La sécurité des threads (thread safety) désigne la capacité d'un code à ne pas corrompre les données lorsqu'il est exécuté simultanément par plusieurs threads.

## Définition et origine du mot

Thread signifie fil d'exécution et safety signifie sécurité. La sécurité ici ne concerne pas la protection contre les pirates, mais la cohérence des données : si deux processus mettent à jour le même compte simultanément, le résultat peut être erroné. Un code thread-safe régule cette concurrence. Les applications bancaires, les serveurs web et tous les logiciels multiprocesseurs en ont besoin.

***Analogie :** C'est comme mettre un verrou à la porte dans une maison avec une seule toilette ; si quelqu'un est à l'intérieur, l'autre doit attendre.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Banque :** S'assurer que deux demandes de retrait sur le même compte ne rendent pas le solde négatif.
**Vente de billets :** Ne pas vendre le dernier siège à deux personnes en même temps.
**Compteurs :** Le compteur de visiteurs doit augmenter exactement de un à chaque requête.

## Profondeur technique et architecture

Les outils typiques sont :

**Verrou (Mutex/Lock) :** Un seul thread entre dans la section critique à la fois, l'autre attend.
**Opération atomique :** Lecture et écriture en une seule étape indivisible.
**Données immuables (Immutable) :** Les données immuables ne sont pas sujettes aux conditions de concurrence, une copie est créée.
**Messagerie :** Communication via une file d'attente au lieu de données partagées (ex: canaux Go).

Un petit exemple en Python :

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

Lorsqu'une ligne est verrouillée, aucun autre thread ne peut intervenir. Si le verrou est oublié ou acquis dans le mauvais ordre, le programme peut se bloquer (interblocage ou deadlock). C'est pourquoi la section critique doit être maintenue courte.

## Choses fréquemment mélangées

Il ne s'agit pas de cybersécurité. Le sujet n'est pas le piratage, mais la cohérence des données : éviter que deux processus accédant simultanément aux mêmes données ne s'écrasent mutuellement.

## Utilisation dans différentes disciplines

**Trafic :** Les feux de signalisation qui déterminent l'ordre de passage sur un pont à voie unique.
**Cuisine :** Des chefs cuisiniers utilisant un seul couteau à tour de rôle.
**Bibliothèque :** Le transfert d'un exemplaire unique d'un livre via un registre de prêt.

## Foire aux questions

**Que se passe-t-il s’il n’est pas thread-safe ?**

Les données se mélangent, les calculs deviennent erronés ou l'application plante. Comme l'erreur ne se reproduit pas à chaque exécution, elle est difficile à déboguer.

**Faut-il ajouter des verrous à chaque code ?**

Non. Dans un code monothread, le verrouillage impose une charge inutile. Seules les sections simultanées accédant à des données partagées doivent être protégées.

**Qu'est-ce qu'un deadlock et comment l'éviter ?**

C'est lorsqu'un processus attend le verrou de l'autre, provoquant un blocage. Acquérir les verrous toujours dans le même ordre et garder la section critique courte réduit le risque.

**Est-ce détectable par un test ?**

C'est difficile à détecter, car l'erreur dépend du timing. On utilise des tests de charge et des détecteurs de race (race detectors) spécialisés.

## Termes liés

- [Concurrency](https://trescout.com/fr/dictionary/concurrency/)
- [System Programming Language](https://trescout.com/fr/dictionary/system-programming-language/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/thread-safety/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/thread-safety/
