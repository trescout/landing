# Qu'est-ce que IaaS ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

> Infrastructure as a Service

IaaS (Infrastructure as a Service, infrastructure en tant que service) consiste à louer du matériel informatique.

## Définition et origine du mot

Lorsque la puissance est insuffisante, une partie est louée dans un centre de données géant. Le système d'exploitation et le logiciel sont à votre charge, la responsabilité du matériel incombe au fournisseur. L'analogie du terrain vide est appropriée : l'infrastructure est prête, le bâtiment est à vous.

***Analogie :** Similaire à la location d'un terrain nu ; l'infrastructure est prête, le bâtiment vous appartient.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Site :** Machine selon le trafic.
**Sauvegarde :** Disque distant.
**Test :** Environnement temporaire.

## Profondeur technique et architecture

Couches :

**Machine virtuelle :** Tranche de processeur et de mémoire.
**Stockage :** Espace bloc et objet.
**Réseau :** Réseau virtuel et adresse.

Machine par code :

```
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}
```

Règle de coût : La machine oubliée allumée coûte cher. La discipline en matière d'étiquetage et d'alertes est indispensable.

## Choses fréquemment mélangées

Souvent confondu avec le PaaS. L'IaaS fournit le matériel, le PaaS offre un environnement prêt à l'emploi. L'un est un terrain nu, l'autre est un appartement meublé.

## Utilisation dans différentes disciplines

**Terrain :** Terrain nu avec infrastructure.
**Entrepôt :** Entrepôt avec étagères prêtes.
**Champ :** Location de terre labourée.

## Foire aux questions

**L'IaaS est-il sécurisé ?**

L'infrastructure est sécurisée, la sécurité interne est de votre ressort. La discipline en matière de correctifs et d'accès est indispensable.

**Quelle est la différence avec le PaaS ?**

L'IaaS fournit du matériel, le PaaS offre un environnement. Si vous voulez le contrôle, choisissez le premier ; si vous voulez de la rapidité, choisissez le second.

**Comment maîtriser les coûts ?**

Éteignez ce qui n'est pas utilisé, choisissez la bonne taille et configurez des alertes.

**Quand le choisir ?**

Lorsqu'un contrôle total et une installation personnalisée sont nécessaires. Pour un travail standard, le PaaS est suffisant.

## Termes liés

- [SaaS](https://trescout.com/fr/dictionary/saas/)
- [PaaS](https://trescout.com/fr/dictionary/paas/)
- [Virtual Machines](https://trescout.com/fr/dictionary/virtual-machines/)

## Outils liés

- [Free for Dev](https://trescout.com/fr/discover/free-for-dev/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/iaas/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/iaas/
