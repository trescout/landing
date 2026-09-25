# Jeu de stratégie léger et open-source

Unciv est une adaptation open-source, minimaliste et multiplateforme de Civilization V pour bureau et Android. Développé avec Kotlin et LibGDX, le projet offre les mécaniques originales de stratégie 4X avec une consommation matérielle nulle et un riche support des mods.

- ★ 11.285
- Kotlin
- GitHub Trending · 2026-06-18

## Mises à jour
- 18 septembre 2026: Étoiles 11 276 → 11 285, dernière version 4.22.1 (17 septembre 2026).
- 15 septembre 2026: Étoiles 11 257 → 11 276, dernière version 4.22.0 (14 septembre 2026).
- 10 septembre 2026: Étoiles 11 241 → 11 257, dernière version 4.21.19 (9 septembre 2026).
- 8 septembre 2026: Étoiles 11 223 → 11 241, dernière version 4.21.18 (7 septembre 2026).

## Ce que ça vous apporte
- Architecture légère et économe en batterie: Utilise des graphismes 2D vectoriels et en pixels pour tourner sans surchauffe même sur les appareils d'entrée de gamme.
- Mécaniques fidèles de Civilization V: Planification urbaine, arbre technologique, politiques sociales, diplomatie et combats hexagonaux tactiques intacts.
- Sauvegardes multiplateformes et multijoueur: Transférez facilement vos sauvegardes entre bureau et Android, ou jouez des parties au tour par tour.
- Écosystème riche de mods communautaires: Installez de nouvelles civilisations, unités et scénarios d'un simple clic depuis le jeu.
- Expérience libre et sans publicité: Sous licence MPL-2.0, sans achats intégrés, traçage ni collecte de données personnelles.

## Pour commencer et options d'installation

Unciv est disponible sur plusieurs plateformes. Sur Android, installez via Google Play Store ou F-Droid. Sur ordinateur (Windows, Linux, macOS), utilisez les archives autonomes, Flatpak ou itch.io.
- [Page Google Play Store →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [Dépôt open-source F-Droid →](https://f-droid.org/packages/com.unciv.app/)
- [Versions bureau itch.io →](https://yairm210.itch.io/unciv)

## Architecture technique et fonctionnement interne

Unciv repose sur LibGDX et Kotlin pour isoler la logique du jeu dans une structure de données déterministe et ultra-légère :
- Moteur de jeu orienté état: Chaque case hexagonale, ville et unité est sérialisée en JSON pur, gardant les sauvegardes sous les 500 Ko.
- Moteur de modding déclaratif: Règles et statistiques sont définies via JSON sans avoir besoin de recompiler le code source.
- Calcul de tours déterministe: Décisions de l'IA et combats sont calculés de manière prévisible pour éviter les désynchronisations.
- Compilation multiplateforme: Une base de code Kotlin unique cible à la fois le JVM bureau et le runtime Android.

## Stratégies de jeu et dynamiques 4X

Unciv illustre fidèlement le cycle 4X : eXplore, eXpand, eXploit et eXterminate :
- Exploration initiale de la carte: Envoyez rapidement éclaireurs et guerriers pour ramasser les ruines antiques et contacter les cités-États.
- Équilibre de bonheur et de nourriture: Fondez vos villes près de ressources de luxe pour éviter les pénalités de croissance.
- Feuille de route technologique: Spécialisez vos recherches en fonction des forces uniques de votre civilisation.
- Maîtrise du terrain: Profitez des fleuves et collines pour repousser des armées plus nombreuses avec peu d'unités.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite créer un mod JSON valide pour Unciv. Peux-tu me générer un modèle de mod avec un dirigeant apportant des bonus en science et culture, une unité montée sur mesure et un bâtiment de bibliothèque unique ? Explique-moi la structure des dossiers et le test dans le Mod Manager en jeu.

- **Pour qui:** Joueurs et créateurs de mods cherchant un jeu de stratégie 4X léger, sans pub et open-source.
- **Licence:** MPL-2.0 (Mozilla Public License 2.0)
- **Moteur de jeu:** LibGDX (Kotlin multiplateforme)
- **Plateformes:** Android, Windows, Linux, macOS

## Foire aux questions
- Unciv est-il fidèle à Civilization V ? Oui, les statistiques, l'arbre technologique et les conditions de victoire sont calqués sur Civ V (Gods & Kings et Brave New World) avec une interface 2D.
- Faut-il une connexion internet pour jouer ? Non, Unciv se joue entièrement hors ligne contre l'ordinateur. La connexion n'est utile que pour les mods et le multijoueur.
- Comment installer des mods ? Le menu Mods en jeu permet de parcourir et installer des centaines de créations communautaires en un clic.
- Peut-on transférer ses parties entre mobile et PC ? Oui, copiez la sauvegarde textuelle dans le presse-papiers et importez-la sur l'autre appareil.

## Liens
- [GitHub →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

## Termes liés du glossaire
Open Source Offline

---
Source: TreScout Discover · https://trescout.com/fr/discover/unciv/
