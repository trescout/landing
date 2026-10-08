# Qu'est-ce que Secrets ?

*Glossaire · Dev · Dernière mise à jour : 4 juin 2026*

Il s'agit des mots de passe, des clés API et des codes d'accès dont les applications logicielles ont besoin pour fonctionner en toute sécurité.

## Définition

Les secrets sont des informations secrètes qu'un programme utilise pour s'authentifier lors de la connexion à un autre système. Il peut souvent s'agir de mots de passe de base de données, de clés privées ou de jetons d'accès aux services. Étant donné que l'intégration de ces informations dans le code présente un risque pour la sécurité, elles sont généralement stockées dans des systèmes de coffre-fort spéciaux.

***Analogie :** C'est comme la clé que vous utilisez pour ouvrir la porte de votre maison ; Si vous placez cette clé sous le paillasson, n'importe qui peut entrer par effraction, vous devez donc la conserver dans un coffre-fort.*

## Comment ça marche

Au lieu d'écrire ces informations confidentielles dans des fichiers de code, les développeurs les définissent en toute sécurité dans l'application à l'aide de variables d'environnement ou d'outils de gestion confidentielles.

## Où est-ce utilisé

Il est utilisé dans les services cloud, les connexions de bases de données et les processus d'authentification des applications.

## Souvent confondu avec

Il peut être confondu avec les mots de passe des utilisateurs classiques, mais il s’agit d’identités numériques conçues pour les machines et non pour les personnes.

## Questions fréquentes

**Pourquoi les secrets ne sont-ils pas conservés dans le code ?**

Lorsque vous partagez votre code ou que vous le téléchargez accidentellement sur Internet, n’importe qui peut obtenir ces clés et infiltrer vos systèmes.

**Que dois-je faire si Secrets est volé ?**

Vous devez immédiatement annuler cette clé, en créer une nouvelle et vérifier s'il y a une infiltration dans votre système.

## Termes liés

- [API](https://trescout.com/fr/dictionary/api/)
- [Self-hosting](https://trescout.com/fr/dictionary/self-hosting/)
- [Observability](https://trescout.com/fr/dictionary/observability/)

## Outils liés

- [Trivy](https://trescout.com/fr/discover/trivy/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/secrets/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/secrets/
