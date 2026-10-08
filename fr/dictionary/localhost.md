# Qu'est-ce que Localhost ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Localhost est le nom de réseau privé par lequel votre ordinateur se désigne lui-même. Son équivalent est l'adresse 127.0.0.1.

## Définition et origine du mot

"Local" signifie local et "host" désigne l'ordinateur hôte. Le développeur ne met pas immédiatement le site en ligne, il le teste d'abord sur son propre ordinateur avec cette adresse. Votre ordinateur joue alors lui-même le rôle de serveur. Personne de l'extérieur ne peut le voir, vous êtes le seul à le voir.

***Analogie :** C'est comme répéter une pièce de théâtre dans une pièce vide uniquement avec les acteurs avant de la monter sur scène ; il n'y a pas encore de public.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Développement web :** l'adresse qui s'ouvre dans le navigateur après npm run dev.
**Base de données :** Connexion Postgres ou Redis installée en local.
**Test d'API :** Test des points de terminaison non encore publiés.

## Profondeur technique et architecture

Ce que vous devez savoir :

**127.0.0.0/8 :** Plage de bouclage (loopback), 127.0.0.1 est généralement utilisé.
**Port :** Numéro de port sur le même ordinateur. Si deux applications utilisent le même port, elles entrent en conflit.
**La différence avec 0.0.0.0 :** Localhost n'est accessible qu'à vous-même, tandis que 0.0.0.0 écoute tout le monde sur le réseau.

Exemple de contrôle de santé :

```
curl http://localhost:3000/api/health
```

Si aucune réponse n'arrive, l'application ne fonctionne pas ou le port est incorrect. Le pare-feu autorise généralement le trafic localhost.

## Choses fréquemment mélangées

On pense qu'il s'agit d'un site web. Pourtant, localhost est propre à votre seul ordinateur, il ne nécessite ni nom de domaine ni publication.

## Utilisation dans différentes disciplines

**Théâtre :** Une salle de répétition sans public.
**Musique :** Vérification du son avant l'enregistrement.
**Cuisine :** Dégustation avant le service.

## Foire aux questions

**Pourquoi utilisons-nous localhost ?**

Pour corriger les erreurs en toute sécurité sur notre propre ordinateur sans les exposer sur Internet.

**Qu'est-ce que 127.0.0.1 ?**

C'est l'équivalent numérique du nom localhost. Il désigne l'ordinateur lui-même sur chaque machine.

**Qu'est-ce qu'un port et pourquoi est-il nécessaire ?**

C'est un numéro de porte qui différencie les applications sur le même ordinateur. Il se trouve après les deux points dans l'adresse du navigateur.

**Est-il accessible de l'extérieur ?**

Non. Pour qu'il soit visible par d'autres, une diffusion et un nom de domaine sont nécessaires. Des outils de tunnelisation sont utilisés pour partager une connexion de test.

## Termes liés

- [IDE](https://trescout.com/fr/dictionary/ide/)
- [Deployment](https://trescout.com/fr/dictionary/deployment/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)

## Outils liés

- [Penpot](https://trescout.com/fr/discover/penpot/)
- [Project N.O.M.A.D](https://trescout.com/fr/discover/project-nomad/)
- [Freellmapi](https://trescout.com/fr/discover/freellmapi/)
- [Jenkins](https://trescout.com/fr/discover/jenkins/)
- [Omlx](https://trescout.com/fr/discover/omlx/)
- [OpenStock](https://trescout.com/fr/discover/openstock/)
- [Personal_AI_Infrastructure](https://trescout.com/fr/discover/personal-ai-infrastructure/)
- [Portless](https://trescout.com/fr/discover/portless/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/localhost/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/localhost/
