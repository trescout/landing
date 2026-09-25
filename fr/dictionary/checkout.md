# Qu'est-ce que le Checkout ? E-Commerce et Git

> Anglais : Checkout · Étymologie : anglais check (vérifier) + out (achèvement, sortie)

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-19

Le mot Checkout possède deux sens informatiques majeurs : l'étape finale de commande et de paiement dans le commerce en ligne, et la commande Git qui permet de changer de branche ou de restaurer des fichiers.

## Par analogie
Dans un supermarché, le checkout est le passage en caisse où l'on règle ses achats avant de sortir ; dans une bibliothèque, le checkout est l'emprunt d'un livre précis à la banque de prêt pour pouvoir l'étudier chez soi.

## 1. Architecture du Checkout en E-Commerce et SaaS
Dans les plateformes marchandes, le checkout désigne l'étape décisive où le panier d'achats se transforme en commande réglée. Il orchestre la réservation de stocks, le calcul dynamique des taxes et le dialogue avec les passerelles de paiement sécurisées via des iframes tokenisées (Stripe, Adyen) pour respecter les normes PCI-DSS sans exposer les données bancaires sur le serveur marchand.

## 2. Commande Checkout dans le gestionnaire Git
Dans l'écosystème des développeurs, <code>git checkout</code> est l'instruction historique servant à déplacer le pointeur HEAD pour basculer sur une autre branche ou restaurer l'état d'un fichier. Dans les versions modernes de Git (2.23+), cette commande polyvalente est avantageusement complétée par <code>git switch</code> (pour changer de branche) et <code>git restore</code> (pour annuler des modifications de fichiers).

## Comparaison : E-Commerce contre Git Checkout
Distinctions majeures entre les deux usages :
- **Checkout E-Commerce :** Processus financier et logistique associant validation d'adresse, verrous d'inventaire et webhooks bancaires.- **Git Checkout :** Manipulation locale du système de fichiers modifiant l'index et restaurant des objets Git sur le disque de travail.- **Conséquences d'erreurs :** En e-commerce, un dysfonctionnement entraîne une perte directe de chiffre d'affaires ; sous Git, un usage maladroit mène à un état HEAD détaché (detached HEAD).

## Questions fréquentes

**Pourquoi Git a-t-il créé 'git switch' et 'git restore' ?**  
Pour séparer les rôles : git checkout servait à la fois à changer de branche et à écraser des fichiers locaux, ce qui provoquait de fréquentes erreurs de manipulation.

**Comment réduire les abandons de panier lors du checkout e-commerce ?**  
En proposant des paiements rapides en un clic (Apple Pay, Google Pay) et la possibilité de commander sans créer préalablement de mot de passe.

**Qu'est-ce qu'un état 'detached HEAD' dans Git ?**  
C'est lorsqu'on se positionne sur un commit précis plutôt que sur une branche active ; les nouveaux commits créés dans cet état risquent de ne plus être référencés.

**À quoi sert une clé d'idempotence lors d'un paiement en ligne ?**  
Elle garantit qu'en cas de coupure réseau ou de double clic, la passerelle de paiement ne prélèvera le montant de la commande qu'une seule fois.

## Termes liés
- [API](/fr/dictionary/api/)
- [SaaS](/fr/dictionary/saas/)
- [Git Push](/fr/dictionary/git-push/)

## Outils liés
- [Checkout](/fr/discover/checkout/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/checkout/
