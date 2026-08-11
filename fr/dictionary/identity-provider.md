# Qu'est-ce que Identity Provider ?

Service central qui vérifie les informations de connexion des utilisateurs et fournit un accès sécurisé aux applications.

## Définition
Il vous permet de prouver votre identité via un système central, au lieu de créer à chaque fois un nouveau mot de passe pour une application. L'application demande à ce service qui vous êtes et obtient une confirmation.

## Comment ça marche
L'utilisateur se connecte, le service s'authentifie et envoie une clé « connecté » à l'application.

## Où est-ce utilisé
Il est utilisé dans les systèmes sur site, les structures SSO (Single Sign-On) et les applications Web modernes.

## Souvent confondu avec
Ce n'est pas seulement un gestionnaire de mots de passe, c'est une autorité d'authentification.

## Questions fréquentes
**Est-ce sécuritaire?**
Oui, c'est plus sécurisé car vous ne donnez pas votre mot de passe à chaque application.

**Que se passe-t-il si le système tombe en panne ?**
Puisqu'il s'agit d'un service central, l'accès à toutes les applications connectées peut être interrompu.


## Termes liés
- [SSO](/fr/dictionary/sso/)
- [OIDC](/fr/dictionary/oidc/)
- [RBAC](/fr/dictionary/rbac/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/identity-provider/
