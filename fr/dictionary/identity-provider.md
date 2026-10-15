# Qu'est-ce que Identity Provider ?

*Développement · Dernière mise à jour : 22 septembre 2026*

Un fournisseur d'identité (identity provider en anglais) est un service centralisé qui authentifie les connexions.

## Définition et origine du mot

Au lieu d'un mot de passe différent pour chaque application, la connexion s'effectue à partir d'un point central. L'application demande qui vous êtes au service et reçoit une approbation. Votre mot de passe n'est pas distribué aux applications, il reste au centre.

***Analogie :** C'est similaire à présenter son passeport à la réception d'un hôtel pour obtenir une clé magnétique ; la porte de la chambre fait confiance à l'approbation de la réception.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Entreprise:** Tous les systèmes avec une seule connexion.
**Web :** Connexion avec un compte social.
**Entreprise :** Cycle de vie des employés.

## Profondeur technique et architecture

Flux :

```
giriş → doğrulama → jeton → uygulama
```

Parties:

**Jeton d'identité :** La preuve de qui vous êtes.
**Jeton d'accès :** L'autorisation de ce que vous pouvez faire.
**MFA :** Preuve supplémentaire en plus du mot de passe.
**Session :** Authentification unique (SSO).

Règle : La durée du jeton est courte, le renouvellement s'effectue en arrière-plan.

## Choses fréquemment mélangées

On le prend pour un gestionnaire de mots de passe. L'un stocke le mot de passe, l'autre confirme l'identité. L'un est un coffre-fort, l'autre un notaire.

## Utilisation dans différentes disciplines

**Réception:** Clé magnétique contre passeport.
**Notaire :** Vérification d'identité.
**Contrôle des passeports :** Passage par tampon.

## Foire aux questions

**Est-ce sécuritaire?**

Oui. Comme le mot de passe n'est pas diffusé à chaque application, la surface d'attaque est réduite.

**Que se passe-t-il si le système tombe en panne ?**

Les applications connectées sont affectées. La redondance et un plan d'accès d'urgence sont indispensables.

**Quelle est la différence avec le SSO ?**

Le SSO est une expérience de connexion unique, c'est l'infrastructure du fournisseur. L'un est le visage, l'autre est la colonne vertébrale.

**Puis-je l'installer moi-même ?**

Oui, il existe des options open source. La discipline des correctifs et des sauvegardes vous incombe.

## Termes liés

- [SSO](https://trescout.com/fr/dictionary/sso/)
- [OIDC](https://trescout.com/fr/dictionary/oidc/)
- [RBAC](https://trescout.com/fr/dictionary/rbac/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/identity-provider/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/identity-provider/
