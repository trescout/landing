# Qu'est-ce que Environment Variables ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Les variables d'environnement sont des identifiants qui permettent de conserver les paramètres en dehors du code.

## Définition et origine du mot

« Environnement » signifie environnement. Le mot de passe et l'adresse ne restent pas dans le code, ils restent dans le système. Le même code se comporte différemment dans différents environnements.

***Analogie :** C'est comme une carte insérée et remplaçable au lieu d'un réglage intégré à l'appareil.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Présentateur:** Chaînes de connexion.
**Application :** Sélection du mode.
**CI :** Clés secrètes.

## Profondeur technique et architecture

Disposition :

**.env :** Fichier local, n'est pas inclus dans le dépôt.
**Priorité :** Le système d'environnement écrase le fichier.
**Schéma :** Liste des noms requis.

Valeur exemple :

```
DATABASE_URL=postgres://kullanici:parola@localhost:5432/db
```

Règle : La valeur réelle n'est pas écrite dans l'exemple, un espace réservé est utilisé. La clé divulguée est annulée.

## Choses fréquemment mélangées

Considéré comme une valeur fixe. Il reste dans le code fixe, la variable est à l'extérieur. L'un est un tatouage, l'autre est un badge.

## Utilisation dans différentes disciplines

**Carte :** Carte de réglage variable.
**Pile de télécommande :** Alimentation amovible.
**Porte-clés :** Accès transportable.

## Foire aux questions

**Pourquoi est-ce gardé secret ?**

S'il est partagé, il peut être intercepté et le compte peut être ouvert. S'il reste secret, le risque est réduit.

**Qu'est-ce que .env ?**

C'est un fichier de valeurs locales. Il n'entre pas dans le dépôt, seul son exemple y est inclus.

**Que se passe-t-il s'il fuit ?**

La clé est révoquée et les journaux sont audités. Le délai est important.

**Quelle est la priorité ?**

L'environnement système écrase le fichier. La valeur réelle provient du système.

## Termes liés

- [Secrets](https://trescout.com/fr/dictionary/secrets/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [API](https://trescout.com/fr/dictionary/api/)

## Outils liés

- [Mise](https://trescout.com/fr/discover/mise/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/environment-variables/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/environment-variables/
