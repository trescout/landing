# Qu'est-ce que Cloud Native ?

Le cloud native (ou natif du cloud en français) est une approche de conception des applications visant à exploiter pleinement la flexibilité et l'évolutivité du cloud.

## Définition et origine du mot
Le concept est chapeauté par la CNCF (Cloud Native Computing Foundation). La distinction essentielle est la suivante : télécharger un logiciel dans le cloud ne le rend pas cloud native. Le cloud native signifie que l'application est conçue dès le départ pour s'adapter à la nature dynamique du cloud, sous forme de petits morceaux indépendants.

## Comment connaître et utiliser dans la vie quotidienne ?
Jours de forte affluence : Augmentation automatique de la capacité lorsque le trafic des jours de campagne est multiplié.Moment de panne : Transfert silencieux du travail vers une autre réplique lorsqu'un serveur tombe en panne.Mise à jour : Renouvellement progressif de l'application pendant qu'elle fonctionne, et non lorsqu'elle est fermée.

## Profondeur technique et architecture
Composants de la pile cloud native :

## Utilisation dans différentes disciplines
Construction préfabriquée : Une maison modulaire à laquelle il est possible d'ajouter des pièces selon les besoins.Réseau électrique : Des centrales qui s'activent selon la demande.Logistique : Des lignes de distribution qui s'ouvrent et se ferment selon la densité.

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
- [Containers](/fr/dictionary/containers/)
- [Virtual Machines](/fr/dictionary/virtual-machines/)
- [Runtime](/fr/dictionary/runtime/)

## Outils liés
- [Meshery](/fr/discover/meshery/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/cloud-native/
