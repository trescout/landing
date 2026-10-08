# Qu'est-ce que Amazon Web Services ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

> Amazon Web Services

AWS (Amazon Web Services), serveurs, stockage et bases de données sont des services informatiques que vous louez via Internet sur cette plateforme cloud.

## Définition et origine du mot

Au lieu de configurer votre propre serveur physique, vous louez les centres de données d'Amazon. La capacité augmente lorsque les besoins augmentent et diminue lorsque le travail est terminé. Il fonctionne sur un modèle de paiement à l'utilisation. Presque toutes les applications modernes ont ce type d'infrastructure cloud en arrière-plan.

***Analogie :** C'est comme acheter de l'électricité sur le réseau au lieu de construire votre propre centrale électrique ; Vous ne payez que ce que vous utilisez.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Site web:** Serveurs qui évoluent en fonction du trafic.
**Sauvegarde :** Un coffre-fort de fichiers qui semble illimité.
**Vidéo:** Contenu distribué au fur et à mesure qu'il est visionné.
**Démarrer:** Mise en ligne sans avoir à installer de salle de serveurs.

## Profondeur technique et architecture

Services de base :

**EC2 :** Serveur virtuel à louer.
**S3 :** Stockage d'objets, coffre-fort pour sauvegardes et fichiers statiques.
**RDS :** Base de données relationnelle gérée.
**Lambda :** Fonction sans serveur exécutée lors d'un événement.

Concepts :

**Région et zone de disponibilité :** Emplacement physique des données et redondance.
**Responsabilité partagée :** La sécurité du cloud est la responsabilité d'Amazon, la sécurité des données qu'il contient est la vôtre.
**Offre gratuite :** Utilisation gratuite limitée pour les nouveaux comptes.

Pour lister les serveurs en cours d'exécution :

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

Il est recommandé de configurer une alerte budgétaire pour éviter les surprises sur la facture, car les ressources oubliées ouvertes continuent d'être facturées.

## Choses fréquemment mélangées

On pense souvent qu'il ne s'agit que d'un service d'hébergement de sites. Pourtant, c'est une plateforme d'infrastructure complète couvrant les bases de données, l'intelligence artificielle, les réseaux et les couches de sécurité avec plus de 200 services.

## Utilisation dans différentes disciplines

**Réseau électrique :** Débrancher la prise au lieu d'installer un standard téléphonique.
**Entrepôt à louer :** Louer des étagères selon les besoins.
**Taxi :** Voyager sans posséder de véhicule.

## Foire aux questions

**Pourquoi devrais-je utiliser AWS ?**

Vous accédez instantanément à une infrastructure d'entreprise sans investir dans du matériel. Si le trafic est fluctuant, la mise à l'échelle et les services prêts à l'emploi permettent de gagner du temps.

**Est-il possible de commencer gratuitement ?**

Oui. Le plan gratuit, les crédits et les conditions de durée pour les nouveaux comptes peuvent changer avec le temps ; vous devez vérifier les limites actuelles sur la page AWS Free Tier avant de commencer.

**Où mes données sont-elles conservées ?**

Il est conservé dans la région que vous avez choisie. Pour les réglementations telles que la KVKK, vous devez effectuer le choix de la région et le chiffrement conformément à votre politique.

**Comment garder le contrôle sur la facture ?**

Grâce aux alertes budgétaires, au nettoyage des ressources inutilisées et au dimensionnement approprié. Pour les petites équipes, une discipline d'étiquetage est indispensable.

## Termes liés

- [Cloud Computing](https://trescout.com/fr/dictionary/cloud-computing/)
- [IaaS](https://trescout.com/fr/dictionary/iaas/)
- [PaaS](https://trescout.com/fr/dictionary/paas/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/aws/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/aws/
