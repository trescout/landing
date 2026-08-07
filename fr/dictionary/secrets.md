# Qu'est-ce que Secrets ?

Il s'agit des mots de passe, des clés API et des codes d'accès dont les applications logicielles ont besoin pour fonctionner en toute sécurité.

## Définition
Les secrets sont des informations secrètes qu'un programme utilise pour s'authentifier lors de la connexion à un autre système. Il peut souvent s'agir de mots de passe de base de données, de clés privées ou de jetons d'accès aux services. Étant donné que l'intégration de ces informations dans le code présente un risque pour la sécurité, elles sont généralement stockées dans des systèmes de coffre-fort spéciaux.

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
- [API](/fr/dictionary/api/)
- [Self-hosting](/fr/dictionary/self-hosting/)
- [Observability](/fr/dictionary/observability/)

## Outils liés
- [Trivy](/fr/discover/trivy/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/secrets/
