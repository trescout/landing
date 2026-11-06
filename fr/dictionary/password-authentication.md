# Qu'est-ce que Password Authentication ?

*Développement · Dernière mise à jour : 6 novembre 2026*

Il s'agit du processus d'utilisation d'un mot de passe pour vérifier l'identité d'un utilisateur lors de la connexion au système.

## Définition

L'authentification par mot de passe est une méthode qui consiste à vérifier le mot de passe secret défini par un utilisateur pour déterminer s'il a le droit d'accéder à un système numérique. Le système demande à l'utilisateur de prouver qu'il est bien la personne qu'il prétend être. Le mot de passe saisi est comparé à sa correspondance chiffrée stockée de manière sécurisée dans la base de données.

***Analogie :** C'est semblable à insérer une clé dans la serrure d'une porte pour entrer chez soi et à la tourner. Si la clé est correcte, la porte s'ouvre ; si elle est incorrecte, vous restez dehors.*

## Comment ça marche

Le nom d'utilisateur et le mot de passe sont saisis dans l'écran correspondant et envoyés. Le logiciel côté serveur ne stocke pas le mot de passe directement en texte clair, mais le fait passer par des fonctions de hachage mathématiques sécurisées. Si le hachage du mot de passe reçu correspond au hachage présent dans la base de données, l'accès est autorisé.

## Où est-ce utilisé

Il est utilisé comme couche de sécurité de base lors des connexions des membres sur les sites Web, sur les écrans de connexion aux ordinateurs, dans les panneaux de gestion des serveurs cloud et lors des accès aux réseaux d'entreprise.

## Souvent confondu avec

Il peut être confondu avec l'autorisation. La validation par mot de passe prouve qui vous êtes, tandis que l'autorisation détermine ce à quoi vous pouvez accéder une fois entré dans le système.

## Questions et réponses

**Comment les mots de passe sont-ils stockés dans la base de données ?**

Pour des raisons de sécurité, ils ne sont jamais stockés en texte clair. Ils sont chiffrés de manière irréversible à l'aide d'algorithmes de hachage spéciaux et de techniques de salage.

**Est-ce suffisamment sécurisé en soi ?**

Aujourd'hui, comme ils sont faciles à voler ou à deviner, ils sont généralement renforcés par des mesures supplémentaires telles que la vérification en deux étapes.

## Termes liés

- [SSO](https://trescout.com/fr/dictionary/sso/)
- [OIDC](https://trescout.com/fr/dictionary/oidc/)
- [RBAC](https://trescout.com/fr/dictionary/rbac/)
- [Security Scanner](https://trescout.com/fr/dictionary/security-scanner/)

Cette explication a été rédigée en langage clair pour TreScout avec l’IA puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/password-authentication/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/password-authentication/
