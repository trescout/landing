# Qu'est-ce que End-to-End Encryption ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

> E2EE

Le chiffrement de bout en bout est un système de sécurité que seules les extrémités lisent.

## Définition et origine du mot

Les données sont verrouillées sur l'appareil et déverrouillées à destination. Le transporteur et le serveur ne peuvent pas voir le contenu. C'est le bouclier fondamental de la confidentialité. WhatsApp et Signal en sont des exemples connus.

***Analogie :** C'est comme correspondre avec une boîte dont vous seuls possédez la clé.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Message :** Conversations privées.
**Fichier :** Transfert sécurisé.
**Sauvegarde :** Copie chiffrée.

## Profondeur technique et architecture

Disposition :

**Paire de clés :** Clé publique et clé privée.
**Vérification :** Identité de la partie adverse.
**Confidentialité de la transmission :** La clé de session est rafraîchie.

Règle : La sauvegarde est conservée chiffrée, la clé est stockée séparément. En cas de perte de l'appareil, un code de récupération est nécessaire.

## Choses fréquemment mélangées

On pense au TLS. Le TLS protège en transit, le serveur voit le contenu. Dans le chiffrement de bout en bout, même le serveur ne peut pas le voir. L'un est une armure de coursier, l'autre est une enveloppe scellée.

## Utilisation dans différentes disciplines

**Boîte verrouillée :** Le transporteur ne peut pas voir le contenu.
**Sceau :** Enveloppe dont l'ouverture est visible.
**Circuit fermé :** Ligne fermée vers l'extérieur.

## Foire aux questions

**Si c'est volé, est-ce lisible ?**

Non. La clé est aux extrémités, le tas volé est dénué de sens.

**Est-il disponible dans toutes les applications ?**

Non. C'est vérifié dans les paramètres, aucune supposition n'est faite.

**Comment effectuer une sauvegarde ?**

Une sauvegarde chiffrée et un code de récupération sont nécessaires. Il n'y a pas de retour possible sans le code.

**Est-ce adapté aux entreprises ?**

C'est équilibré avec les besoins d'enregistrement et d'audit. La politique est définie.

## Termes liés

- [Security Scanner](https://trescout.com/fr/dictionary/security-scanner/)
- [Linux Server Security](https://trescout.com/fr/dictionary/linux-server-security/)
- [SSO](https://trescout.com/fr/dictionary/sso/)

## Outils liés

- [Croc](https://trescout.com/fr/discover/croc/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/end-to-end-encryption/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/end-to-end-encryption/
