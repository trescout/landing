# Qu'est-ce que Declarative Continuous Deployment ?

C'est la méthode qui définit l'état final du système et garantit que les mises à jour atteignent automatiquement cet objectif.

## Définition
Vous n'êtes pas intéressé par la manière de mettre à jour le système, mais par le résultat. Vous dites simplement « laissez le système être dans cet état » et les outils prendront toutes les mesures nécessaires pour capturer cet état. Cela évite les mises à jour manuelles erronées.

## Comment ça marche
Vous préparez un fichier de configuration. Le système automatique lit ce fichier, le compare à la situation actuelle et effectue les ajustements nécessaires pour combler l'écart.

## Où est-ce utilisé
Il est utilisé dans les applications basées sur le cloud et dans la gestion de serveurs à grande échelle.

## Souvent confondu avec
Elle peut être confondue avec les méthodes impératives (orientées vers les commandes) ; Dans cette méthode, vous racontez chaque étape une par une.

## Questions fréquentes
**Pourquoi devrions-nous choisir cette méthode ?**
Il minimise les erreurs humaines et garantit que le système reste toujours dans l'état souhaité.

**Que se passe-t-il si je fais une erreur ?**
Le système se rend compte que vous avez défini un mauvais état et revient généralement à l'ancien état de fonctionnement.


## Termes liés
- [Cloud Native](/fr/dictionary/cloud-native/)
- [Deployment](/fr/dictionary/deployment/)

## Outils liés
- [Argo Cd](/fr/discover/argo-cd/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/declarative-continuous-deployment/
