# Qu'est-ce que OpenStreetMap ?

*Glossaire · Data · Dernière mise à jour : 22 septembre 2026*

OpenStreetMap (OSM en abrégé) est une carte du monde gratuite et ouverte élaborée par des bénévoles.

## Définition et origine du mot

Le projet a été lancé en 2004. Contrairement aux cartes commerciales, les données ne sont pas produites par une entreprise, mais par une communauté de bénévoles : n'importe qui peut ajouter de nouvelles routes, bâtiments ou points de repère, et corriger les erreurs. Les données sont accessibles au public sous une licence ODbL. Cela signifie que vous pouvez utiliser les données gratuitement, mais vous devez indiquer la source lors du partage.

***Analogie :** C'est comme Wikipédia des cartes ; Tout le monde peut ajouter quelque chose, corriger des bugs et il reste constamment mis à jour grâce à la communauté.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Applications de navigation :** Des applications telles que OsmAnd et MAPS.ME obtiennent leurs cartes à partir des données OSM.
**Logistique :** Planification des itinéraires des sociétés de distribution.
**Secours en cas de catastrophe :** Les bénévoles cartographient rapidement les zones de crise (par exemple la communauté HOT).
**Urbanisme:** Analyse de pistes cyclables et d'espaces verts.

## Profondeur technique et architecture

Les données OSM se composent de trois éléments constitutifs :

**Nœud:** Un seul point (par exemple emplacement de la pharmacie).
**Chemin:** Combinaison de nœuds (rue, périmètre du bâtiment).
**Relation:** Groupe logique (ligne de bus) de pièces.

Des étiquettes sont attachées à chaque élément : des paires clé-valeur, telles que Highway=Residential. Pour l'édition, l'éditeur iD dans le navigateur ou l'application avancée JOSM est utilisé.

L'API Overpass est interrogée pour récupérer des données spécifiques. Par exemple, une petite requête qui trouve des pharmacies dans la région :

```
[out:json];
node["amenity"="pharmacy"](around:1000,41.0,29.0);
out;
```

Les données brutes peuvent être téléchargées depuis Planet.osm. Les images cartographiques sont extraites pièce par pièce des serveurs de tuiles.

## Utilisation dans différentes disciplines

**Encyclopédie:** Le modèle Wikipédia où tout le monde écrit et édite.
**Logiciel open source :** Noyau Linux en croissance avec contribution volontaire.
**Science citoyenne :** Collecte des enregistrements d'observations d'oiseaux dans une base de données commune.

## Foire aux questions

**Est-ce vraiment gratuit ?**

Les données sont gratuites avec une licence ODbL. Si vous l'hébergez sur votre propre serveur, vous ne paierez aucun frais supplémentaire. Les entreprises proposant des services de carrelage prêts à l'emploi peuvent facturer des frais supplémentaires.

**Quelle est la différence avec Google Maps ?**

Google produit les données en interne et les lie aux quotas de l'API. Les données OSM sont produites par la communauté, vous pouvez télécharger les données brutes et les traiter de manière illimitée.

**Comment puis-je contribuer à la carte ?**

Vous pouvez créer un compte et démarrer avec l'éditeur iD dans le navigateur. Ajouter le magasin manquant dans votre rue est une bonne première étape.

**Puis-je l'utiliser dans mon produit commercial ?**

Oui, mais comme l'exige ODbL, vous devez visiblement fournir l'attribution OpenStreetMap et partager les données dérivées avec la même licence.

## Termes liés

- [Data Pipeline](https://trescout.com/fr/dictionary/data-pipeline/)
- [OSINT](https://trescout.com/fr/dictionary/osint/)
- [Graph-based Investigation](https://trescout.com/fr/dictionary/graph-based-investigation/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/openstreetmap/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/openstreetmap/
