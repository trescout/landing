# Qu'est-ce que Cloud Native ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le cloud native (ou natif du cloud en français) est une approche de conception des applications visant à exploiter pleinement la flexibilité et l'évolutivité du cloud.

## Définition et origine du mot

Le concept est chapeauté par la CNCF (Cloud Native Computing Foundation). La distinction essentielle est la suivante : télécharger un logiciel dans le cloud ne le rend pas cloud native. Le cloud native signifie que l'application est conçue dès le départ pour s'adapter à la nature dynamique du cloud, sous forme de petits morceaux indépendants.

***Analogie :** C'est un peu comme concevoir non pas une maison à installer une seule fois au même endroit, mais une structure modulaire qui peut être déplacée n'importe quand et dont les pièces peuvent être agrandies selon les besoins.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Jours de forte affluence :** Augmentation automatique de la capacité lorsque le trafic des jours de campagne est multiplié.
**Moment de panne :** Transfert silencieux du travail vers une autre réplique lorsqu'un serveur tombe en panne.
**Mise à jour :** Renouvellement progressif de l'application pendant qu'elle fonctionne, et non lorsqu'elle est fermée.

## Profondeur technique et architecture

Composants de la pile cloud native :

**Conteneur :** Boîte portable contenant l'application et ses dépendances.
**Orchestration :** Exécution, réplication et contrôle de l'état des boîtes (ex. Kubernetes).
**Microservices :** Division d'une grande application en petits services déployables indépendamment.
**Observabilité :** Maintien de la visibilité interne du système grâce aux logs, métriques et traces.

La mise à l'échelle se fait en une seule commande :

```
kubectl scale deployment web --replicas=5
```

Cette commande fait passer le nombre de réplicas du service web à cinq. Lorsque le trafic diminue, le nombre est réduit.

## Utilisation dans différentes disciplines

**Construction préfabriquée :** Une maison modulaire à laquelle il est possible d'ajouter des pièces selon les besoins.
**Réseau électrique :** Des centrales qui s'activent selon la demande.
**Logistique :** Des lignes de distribution qui s'ouvrent et se ferment selon la densité.

## Foire aux questions

**Déplacer une application vers le cloud en fait-elle une application native cloud (cloud native) ?**

Non. Transférer tel quel un ancien type d'application ne fait que la déplacer. Pour le cloud native, l'architecture doit être découpée en petits morceaux et adaptée à une gestion automatique.

**Est-ce nécessaire pour un petit projet ?**

Pas toujours. Pour un blog qui tourne sans problème sur un seul serveur, ce dispositif peut être excessif. Cela prend tout son sens si le trafic est fluctuant ou si l'équipe grandit.

**Est-ce que cela augmente les coûts ?**

Il y a des coûts d'installation et d'apprentissage. En contrepartie, le temps d'indisponibilité et les coûts de mise à l'échelle diminuent. Vous devez faire le calcul en fonction de votre charge de travail.

**Par où faut-il commencer ?**

Commencez par conteneuriser l'application. Ensuite, ajoutez la vérification de l'état de santé (health check), la journalisation (logging) et le déploiement automatique. L'orchestration est la dernière étape.

## Termes liés

- [Containers](https://trescout.com/fr/dictionary/containers/)
- [Virtual Machines](https://trescout.com/fr/dictionary/virtual-machines/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)

## Outils liés

- [Meshery](https://trescout.com/fr/discover/meshery/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/cloud-native/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/cloud-native/
