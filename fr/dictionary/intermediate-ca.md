# Qu'est-ce que Intermediate CA ?

*Développement · Dernière mise à jour : 21 octobre 2026*

> Intermediate Certificate Authority

Autorité intermédiaire située entre le certificat racine, qui authentifie l'identité des sites web sécurisés, et l'utilisateur final.

## Définition

Une autorité de certification intermédiaire (intermediate CA) est une entité de confiance intermédiaire, habilitée par une autorité de certification racine, qui constitue la base des connexions HTTPS sécurisées sur Internet. L'utilisation directe du certificat racine sur des serveurs exposés à Internet présentant un risque de sécurité, cette tâche est déléguée aux certificats intermédiaires. Ainsi, la chaîne de confiance principale est préservée tout en permettant de distribuer en toute sécurité des certificats de sécurité numérique aux sites web.

***Analogie :** Cela ressemble au cas où l'État, au lieu de délivrer directement des pièces d'identité depuis son administration centrale, confère une habilitation à la mairie de quartier pour gérer les approbations par son intermédiaire.*

## Comment ça marche

Lorsque votre navigateur accède à un site web, le serveur vous présente une chaîne de certificats. Cette chaîne commence par le certificat de l'utilisateur final, passe par le certificat intermédiaire et atteint le certificat racine principal préinstallé sur votre appareil, établissant ainsi un lien de confiance.

## Où est-ce utilisé

Il est activement présent dans la gestion des certificats SSL/TLS, les configurations de serveurs web et les infrastructures de sécurité d'entreprise.

## Souvent confondu avec

Il ne s'agit pas directement du certificat racine lui-même, mais d'une étape intermédiaire faisant office de pont pour transporter la confiance entre la racine et le point final.

## Questions fréquentes

**Pourquoi n'utilise-t-on pas directement le certificat racine pour le certificat intermédiaire ?**

Si la clé privée du certificat racine est compromise, toute la sécurité d'Internet peut s'effondrer ; c'est pourquoi le risque est limité grâce aux certificats intermédiaires.

**Comment les navigateurs vérifient-ils le certificat intermédiaire ?**

Le serveur transmet les certificats intermédiaires manquants au navigateur, et celui-ci achève la vérification à l'aide de la chaîne de confiance intégrée.

## Termes liés

- [End-to-End Encryption](https://trescout.com/fr/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/fr/dictionary/identity-provider/)
- [OIDC](https://trescout.com/fr/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/fr/dictionary/vulnerability-scanning/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/intermediate-ca/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/intermediate-ca/
