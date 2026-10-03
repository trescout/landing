# Qu'est-ce que Thread-safety ?

La sécurité des threads (thread safety) désigne la capacité d'un code à ne pas corrompre les données lorsqu'il est exécuté simultanément par plusieurs threads.

## Définition et origine du mot
Thread signifie fil d'exécution et safety signifie sécurité. La sécurité ici ne concerne pas la protection contre les pirates, mais la cohérence des données : si deux processus mettent à jour le même compte simultanément, le résultat peut être erroné. Un code thread-safe régule cette concurrence. Les applications bancaires, les serveurs web et tous les logiciels multiprocesseurs en ont besoin.

## Comment connaître et utiliser dans la vie quotidienne ?
Banque : S'assurer que deux demandes de retrait sur le même compte ne rendent pas le solde négatif.Vente de billets : Ne pas vendre le dernier siège à deux personnes en même temps.Compteurs : Le compteur de visiteurs doit augmenter exactement de un à chaque requête.

## Profondeur technique et architecture
Les outils typiques sont :

## Choses fréquemment mélangées
Il ne s'agit pas de cybersécurité. Le sujet n'est pas le piratage, mais la cohérence des données : éviter que deux processus accédant simultanément aux mêmes données ne s'écrasent mutuellement.

## Utilisation dans différentes disciplines
Trafic : Les feux de signalisation qui déterminent l'ordre de passage sur un pont à voie unique.Cuisine : Des chefs cuisiniers utilisant un seul couteau à tour de rôle.Bibliothèque : Le transfert d'un exemplaire unique d'un livre via un registre de prêt.

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
- [Concurrency](/fr/dictionary/concurrency/)
- [System Programming Language](/fr/dictionary/system-programming-language/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/thread-safety/
