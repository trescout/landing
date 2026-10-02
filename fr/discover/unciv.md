# Jeu de stratégie léger et open source

Unciv est une adaptation open-source, minimaliste et multiplateforme pour bureau et Android du jeu Civilization V. Développé avec l'infrastructure Kotlin et LibGDX, le projet propose les mécaniques du jeu de stratégie 4X original avec une charge matérielle nulle et un support élevé des mods.

- ★ 11 379
- Kotlin
- GitHub Trending · 2026-06-18

## Ce que ça vous apporte
- Architecture économe en batterie et peu gourmande en ressources : en utilisant des graphismes vectoriels 2D et en pixel art au lieu de moteurs de rendu 3D lourds, elle fonctionne sans aucune surchauffe, même sur les appareils mobiles les plus basiques.
- Les mécaniques originales de Civilization V : la planification urbaine, l'arbre technologique, les politiques sociales, la diplomatie et le système de combat tactique hexagonal sont intégralement préservés.
- Sauvegarde multiplateforme et prise en charge du mode multijoueur : vous pouvez transférer directement vos fichiers de sauvegarde entre le bureau et Android ou jouer à des matchs multijoueurs au tour par tour par e-mail ou sur serveur.
- Écosystème de mods riche et axé sur la communauté : de nouvelles civilisations, unités, scénarios fantastiques et thèmes graphiques peuvent être téléchargés et activés en un seul clic depuis l'interface du jeu.
- Expérience entièrement libre et sans publicité : distribué sous licence MPL-2.0, l'application ne contient aucun achat intégré, publicité, suivi ou collecte de données.

## Comment démarrer et options de configuration
- Page Google Play Store →
- Dépôt Open Source F-Droid →
- Versions de bureau itch.io →

## Architecture technique et principe de fonctionnement
- Moteur de jeu orienté état : chaque case hexagonale, unité, ville et relation diplomatique sur le plateau de jeu est stockée sous forme d'objets JSON purs. Cette structure maintient la taille des fichiers de sauvegarde à seulement quelques centaines de kilo-octets.
- Moteur de modding déclaratif : les caractéristiques des civilisations, les arbres technologiques et les coûts des bâtiments sont définis via des fichiers JSON sans toucher au code source. Cela permet aux développeurs de mods de se passer de compilateur externe.
- Calcul de tour déterministe : les mouvements d'intelligence artificielle et les résultats de combat sont calculés à l'aide d'algorithmes prédictifs. Cela évite les pertes de synchronisation dans les jeux multijoueurs asynchrones.
- Compilation multiplateforme : grâce à LibGDX, une base de code Kotlin unique est packagée pour le bureau (JVM) et le mobile (runtime Android) avec des performances natives.

## Stratégies de gameplay et dynamiques 4X
- Exploration de la carte lors des premiers tours : Récupérez les ruines antiques en déployant tôt vos unités de guerriers et d'éclaireurs sur la carte, et générez des revenus en or en établissant le premier contact avec les cités-états.
- Équilibre entre bonheur et nourriture : veillez à vous installer à portée des ressources de luxe lors de la fondation de nouvelles villes. Lorsque votre taux de bonheur devient négatif, la croissance démographique et la production ralentissent considérablement.
- Feuille de route technologique : Au lieu d'effectuer des recherches au hasard, concentrez-vous sur les points forts de votre civilisation ; suivez les voies de la forge et de la poudre à canon pour une victoire militaire, et de la philosophie et de l'éducation pour une victoire culturelle.
- Exploiter les avantages du terrain : repoussez de grandes armées avec peu d'unités en utilisant la défense derrière les rivières, l'avantage des hauteurs et en créant des goulots d'étranglement.

## Si vous ne codez pas
Je souhaite préparer une structure de mod JSON valide pour le jeu Unciv. Pourrais-tu créer un modèle de mod Unciv d'exemple incluant une capacité de leader accordant un bonus à la production de science et de culture, une unité de cavalerie spéciale et un bâtiment de bibliothèque spécial ? Peux-tu expliquer étape par étape dans quelle structure de dossiers je dois enregistrer les fichiers JSON et comment je peux tester cela via l'interface du gestionnaire de mods (Mod Manager) en jeu ?

## Questions fréquemment posées
- À quel point Unciv ressemble-t-il à Civilization V ? Les mécaniques de jeu, les statistiques des unités, l'arbre technologique et les conditions de victoire sont en grande partie identiques aux extensions Gods and Kings et Brave New World de Civilization V. La différence réside principalement dans l'utilisation d'un design visuel 2D épuré plutôt que de graphismes 3D.
- Une connexion Internet est-elle nécessaire pour jouer ? Non. Unciv peut être joué entièrement hors ligne. Aucune connexion réseau n'est requise pour jouer contre des adversaires contrôlés par l'IA en mode solo. La connexion n'est nécessaire que pour le téléchargement de mods et les parties multijoueurs.
- Comment installer des mods pour Unciv ? En accédant à l'onglet Mods du menu principal, vous pouvez consulter la liste des centaines de mods créés par la communauté et les télécharger sur votre appareil en un seul clic. Vous pouvez également effectuer une installation directe en ajoutant le lien vers n'importe quel dépôt de mod sur GitHub.
- Est-il possible de transférer un fichier de sauvegarde entre un ordinateur de bureau et un téléphone ? Oui. Depuis le menu de sauvegarde en jeu, vous pouvez copier le fichier dans le presse-papiers, l'envoyer sous forme de texte par e-mail ou par message vers votre autre appareil, puis utiliser l'option de chargement depuis le presse-papiers pour reprendre votre partie là où vous vous étiez arrêté.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/unciv/
