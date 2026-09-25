# Qu'est-ce qu'OpenStreetMap (OSM) ?

> Anglais : OpenStreetMap · Étymologie : anglais open (ouvert) + street (rue) + map (carte)

**Catégorie:** Data  
**Dernière mise à jour:** 2026-09-22

OpenStreetMap (OSM) est une base de données géographiques mondiale, libre et collaborative, créée et constamment enrichie par des millions de contributeurs bénévoles à travers la planète.

## Définition et étymologie
Lancé en 2004 par Steve Coast en réaction aux restrictions imposées par les cartographes propriétaires, OpenStreetMap est souvent désigné comme le Wikipédia de la cartographie. Contrairement aux services commerciaux qui facturent chaque affichage de tuile géographique, OSM met à disposition ses données vectorielles brutes sous licence libre ODbL.

## Usage quotidien et contexte pratique
Applications directes d'OpenStreetMap dans le numérique :
- **Navigation mobile hors ligne :** Des applications comme OsmAnd, Organic Maps ou MAPS.ME fonctionnent sans connexion grâce aux données OSM.- **Services technologiques :** Des entreprises comme Strava, Mapbox et Apple exploitent les calques OSM pour enrichir leurs produits.- **Aide humanitaire d'urgence :** L'équipe HOT (Humanitarian OpenStreetMap Team) cartographie les zones de crise pour guider les secours sur le terrain.

## Profondeur technique et architecture
Le modèle de données d'OSM repose sur trois primitives géométriques :
- **Nœud (Node) :** Point géographique précis repéré par ses coordonnées de latitude et longitude.- **Ligne (Way) :** Suite ordonnée de nœuds formant un tracé linéaire (rue, sentier) ou un polygone fermé (contour d'immeuble, forêt).- **Relation :** Structure logique regroupant plusieurs nœuds et lignes pour modéliser des lignes de bus ou des frontières complexes.- **Étiquettes Clé/Valeur (Tags) :** Attributs sémantiques universels (ex. highway=residential, amenity=pharmacy).

## Perspectives interdisciplinaires
Analogies avec d'autres initiatives de biens communs :
- **Encyclopédies :** Le modèle d'écriture et de relecture collective de Wikipédia.- **Logiciel libre :** L'effort collectif mondial autour du noyau Linux mêlant passionnés et grandes entreprises.- **Sciences participatives :** Les réseaux d'observation citoyenne de la faune ou des relevés météorologiques locaux.

## Par analogie
C'est comme le Wikipédia des cartes géographiques : chacun peut ajouter le nouveau sentier de son quartier, corriger le nom d'une rue et contribuer à un atlas universel appartenant à tous.

## Questions fréquentes

**L'utilisation d'OpenStreetMap est-elle vraiment gratuite ?**  
Oui, les données sont fournies sous licence ODbL, autorisant l'usage personnel et commercial sous réserve de citer la source.

**Comment la qualité des données est-elle vérifiée sans géomètres officiels ?**  
Grâce aux outils de relecture communautaire, aux détecteurs automatiques d'incohérences et à la veille des contributeurs locaux.

**Une entreprise peut-elle héberger son propre serveur cartographique OSM ?**  
Tout à fait ; la chaîne logicielle libre (PostGIS, Mapnik) permet de déployer son propre serveur de tuiles sans dépendre d'un tiers.

**Quelle est la différence fondamentale avec Google Maps ?**  
Google Maps est un service propriétaire dont les données restent fermées ; OSM distribue la donnée brute, manipulable et téléchargeable à volonté.

## Termes liés
- [Data Pipeline](/fr/dictionary/data-pipeline/)
- [Open Source](/fr/dictionary/open-source/)
- [API](/fr/dictionary/api/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/openstreetmap/
