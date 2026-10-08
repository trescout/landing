# Qu'est-ce que CI/CD ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

> Continuous Integration / Continuous Deployment

CI/CD (Continuous Integration/Continuous Deployment) est le test et la publication automatiques du code.

## Définition et origine du mot

Il s'agit d'une ligne automatique établie pour garantir que le code écrit parvienne à l'utilisateur sans aucune erreur. CI assemble et teste constamment le code, et le transfère sur un live CD. L’ère des publications manuelles touche à sa fin.

***Analogie :** C'est comme un ruban adhésif qui garantit que la nourriture est préparée dans la cuisine du restaurant, qu'elle a réussi le test de goût et qu'elle est servie au client.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Équipe:** Test après chaque commit.
**Mobile:** Libération automatique en magasin.
**Web :** Relâchez une fois combiné.

## Profondeur technique et architecture

Étapes de la ligne :

**Peluche:** Contrôle du style.
**Test :** Unité et bout à bout.
**Compilation :** Réalisation de colis.
**Publication :** Ouverture progressive.

Exemple d'étape :

```
steps:
  - run: npm ci
  - run: npm test
```

Une porte d'approbation manuelle est placée dans les publications critiques. Différence avec la livraison : la livraison prépare, le déploiement imprime. Le premier attend, le second s'en va.

## Choses fréquemment mélangées

On pense qu'il s'agit d'un test manuel. Cependant, la ligne est complètement automatique : le code arrive, le test s'exécute, le résultat sort. On attend juste à la porte.

## Utilisation dans différentes disciplines

**Ruban de cuisine :** Préparation, dégustation et service.
**Chaîne de montage:** Pièce, inspection et emballage.
**Bande de bagage :** Inscription, navigation et téléchargement.

## Foire aux questions

**Pourquoi est-ce si important ?**

Il traduit le code défectueux en direct et augmente la vitesse. Les diffusions fréquentes se font en toute sécurité.

**Doit-il toujours être automatique ?**

Généralement oui, une porte manuelle est ajoutée dans la version critique.

**Quelle est la différence avec la livraison ?**

La livraison se prépare et attend, le déploiement se déroule de manière aléatoire. Le premier est homologué, le second est entièrement automatique.

**Que se passe-t-il s'il casse ?**

La ligne s'arrête et la diffusion est interrompue. C'est pourquoi un plan de sauvegarde et une récupération rapide sont essentiels.

## Termes liés

- [Continuous Integration](https://trescout.com/fr/dictionary/continuous-integration/)
- [Continuous Deployment](https://trescout.com/fr/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [QA](https://trescout.com/fr/dictionary/qa/)

## Outils liés

- [Free for Dev](https://trescout.com/fr/discover/free-for-dev/)
- [Strix](https://trescout.com/fr/discover/strix/)
- [Googletest](https://trescout.com/fr/discover/googletest/)
- [Trivy](https://trescout.com/fr/discover/trivy/)
- [Openship](https://trescout.com/fr/discover/openship/)
- [Ipatool](https://trescout.com/fr/discover/ipatool/)
- [Checkstyle](https://trescout.com/fr/discover/checkstyle/)
- [Flue](https://trescout.com/fr/discover/flue/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/ci-cd/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/ci-cd/
