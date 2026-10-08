# Qu'est-ce que Rendering ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le rendering (ou rendu) est le processus de conversion des données brutes en l'image que vous voyez à l'écran.

## Définition et origine du mot

En anglais, « render » signifie restituer ou dessiner. Les ordinateurs stockent les données sous forme de chiffres. Le rendu (rendering) convertit ces données numériques en une image visible en calculant les propriétés de lumière, de couleur et de forme. Ce processus nécessite des calculs mathématiques intenses, c'est pourquoi il est généralement pris en charge par la carte graphique (GPU).

***Analogie :** C'est comme un chef utilisant les matières premières (données) dont il dispose et les transformant en une assiette (visuel) prête à être présentée.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Pages Web :** Le dessin pixel par pixel du code HTML et CSS par votre navigateur à l'écran.
**Jeux :** La production de nouvelles images 30 ou 60 fois par seconde.
**Montage vidéo :** Conversion de la chronologie avec effets en une vidéo exploitable (exportation).
**Cartes :** Affichage de nouveaux détails à mesure que l'on zoome.

## Profondeur technique et architecture

Il existe deux manières principales de générer des images :

**Rasterisation (Rasterization) :** La scène tridimensionnelle est divisée en triangles, chaque triangle est converti en pixels. C'est rapide, c'est le standard dans les jeux.
**Lancer de rayons (Ray Tracing) :** Le trajet des rayons lumineux dans la scène est tracé en sens inverse. Les reflets et les ombres sont réalistes, mais c'est beaucoup plus coûteux en ressources.

Deux approches sont également discutées du côté du web :

**Rendu côté serveur (SSR) :** La page est rendue sur le serveur et le HTML prêt à l'emploi est envoyé. Le chargement initial est rapide.
**Rendu côté client (CSR) :** Une page blanche apparaît, le contenu est rendu dans le navigateur avec JavaScript. La suite est fluide, le premier chargement est lent.

La fréquence d'images (FPS) détermine l'expérience : plus la valeur baisse, plus vous ressentez des saccades. La cause de la lenteur est généralement que la quantité de données à traiter dépasse les capacités du matériel.

## Utilisation dans différentes disciplines

**Imprimerie :** Conversion de la conception de page en matrice d'impression.
**Architecture :** Visuel tridimensionnel réaliste du projet (plan de masse).
**Cinéma :** Calcul image par image des effets post-tournage.

## Foire aux questions

**Pourquoi le rendu peut-il être lent ?**

Si la quantité de données à traiter dépasse la capacité du matériel, le processus ralentit. La solution consiste généralement à réduire les détails, à améliorer le matériel ou à diviser le travail en parties.

**Qu'est-ce que le ray tracing ?**

C'est une méthode qui calcule de manière réaliste les reflets et les ombres en suivant le trajet des rayons lumineux dans la scène. C'est de haute qualité, mais cela demande beaucoup plus de puissance de calcul que la rastérisation.

**Quelle est la différence entre SSR et CSR ?**

Le SSR rend la page sur le serveur et l'envoie prête, le premier chargement est rapide. Le CSR laisse le rendu au navigateur, le premier chargement est lent mais la suite est fluide.

**Une carte graphique puissante est-elle indispensable pour le rendu ?**

Pas toujours. Pour les pages Web et les tâches de bureautique, le processeur suffit. En revanche, les jeux, la conception 3D et le montage vidéo nécessitent une carte graphique puissante.

## Termes liés

- [GUI](https://trescout.com/fr/dictionary/gui/)
- [User Interface](https://trescout.com/fr/dictionary/user-interface/)
- [Frontend Stack](https://trescout.com/fr/dictionary/frontend-stack/)

## Outils liés

- [Next.js](https://trescout.com/fr/discover/next-js/)
- [Nuxt](https://trescout.com/fr/discover/nuxt/)
- [Meshoptimizer](https://trescout.com/fr/discover/meshoptimizer/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/rendering/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/rendering/
