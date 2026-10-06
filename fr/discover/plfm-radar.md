# Radar multiéléments open source

PLFM RADAR est un système radar à balayage de phase open source fonctionnant à une fréquence de 10,5 GHz (bande X), doté de capacités de pilotage électronique de faisceau (electronic beam steering) et de traitement numérique du signal basé sur FPGA. Il détecte et suit les cibles aériennes et terrestres avec une grande précision sans utiliser de pièces mécaniques mobiles.

- ★ 26 713
- C++
- GitHub Trending · 2026-08-18

## Ce que ça vous apporte
- Orientation de faisceau électronique : balayage d'un secteur de 90 degrés en quelques millisecondes grâce à des déphaseurs, sans nécessiter de moteur mécanique ou d'antenne rotative.
- Mode de fonctionnement double portée : capacité opérationnelle de 3 km à courte portée (détection d'UAV/drone) et de 20 km à longue portée (surveillance périmétrique et suivi d'aéronefs).
- Traitement du signal en temps réel basé sur FPGA : traitement matériel des échos radar bruts sur FPGA avec des algorithmes FFT et CFAR à grande vitesse.
- Matériel accessible à faible coût : réduire le coût des radars commerciaux et militaires, qui se chiffre en centaines de milliers de dollars, à moins de mille dollars grâce à des conceptions de circuits imprimés open source.
- Intégration Python et SDR : surveillance en direct des données radar numériques via du matériel SDR open source et une interface Python.

## Composants matériels et architecture radar
- Réseau d'antennes micro-ruban bande X 10,5 GHz : éléments d'antenne patch multiples conçus sur des substrats Rogers/FR4 à faibles pertes.
- Déphaseurs à commande numérique : circuits intégrés RF qui orientent le faisceau dans l'espace en retardant la phase du signal de chaque élément d'antenne avec une précision de 5,6 degrés.
- Synthétiseur de fréquence FMCW : oscillateur local à haute stabilité (VCO/PLL) générant une onde continue à modulation de fréquence linéaire.

## Logiciel de traitement du signal et de contrôle
- FFT de portée-Doppler (FFT 2D) : calcul simultané de la distance et de la vitesse radiale d'une cible en appliquant d'abord une FFT de portée, puis une FFT Doppler au signal entrant.
- Détecteur CFAR (Constant False Alarm Rate) : filtrage des cibles mobiles réelles parmi le bruit de fond et les échos de sol (clutter) grâce à un seuil dynamique.
- Interface graphique Python et écran PPI : visualisation des traces de cibles sur une carte en direct via un écran radar circulaire traditionnel (PPI).

## Principe de fonctionnement technique : FMCW et réseau de phase
- Mesure de distance par différence de fréquence : le signal de battement (beat frequency) est obtenu en mélangeant le signal chirp émis avec le signal réfléchi par la cible. Cette fréquence est directement proportionnelle à la distance.
- Formation de faisceau par interférence constructive : En appliquant un déphasage spécifique à chaque élément d'antenne du réseau, le signal est rendu constructif dans la direction souhaitée et destructif dans les autres directions.

## Scénarios d'utilisation et tests sur le terrain
- Défense contre les drones et les UAV à basse altitude : détection de petits véhicules aériens sans pilote dans des conditions de brouillard ou de nuit où les caméras optiques s'avèrent insuffisantes.
- Sécurité périmétrique des sites critiques : surveillance des approches non autorisées de personnes ou de véhicules dans un rayon de 3 km autour des aéroports, centres de données et sites industriels.
- Recherches météorologiques et atmosphériques : analyse des mouvements nuageux et de l'intensité des précipitations à l'échelle locale par des méthodes micro-Doppler.

## Si vous ne codez pas
Je souhaite examiner les schémas matériels à commande de phase 10,5 GHz et les blocs de traitement du signal FPGA du projet PLFM RADAR. Pourriez-vous préparer un script Python de simulation expliquant la génération du signal chirp FMCW, le calcul FFT 2D Portée-Doppler et le transfert de données vers un écran radar PPI basé sur Python ? Pourriez-vous montrer étape par étape l'algorithme de détection de distance et de vitesse pour une cible artificielle ?

## Questions fréquemment posées
- Est-il possible de fabriquer le système à la maison ou en laboratoire ? Oui. Tous les schémas PCB, les fichiers de production Gerber et les codes FPGA Verilog/VHDL du projet sont disponibles en open source dans le dépôt GitHub. Les cartes peuvent être commandées auprès de fabricants de PCB standard et soudées en laboratoire.
- Quel est l'avantage du balayage électronique par rapport aux radars mécaniques ? Alors que les radars mécaniques effectuent 1 à 2 tours par seconde, les radars à balayage électronique peuvent modifier la direction du faisceau en quelques microsecondes. Il n'y a aucune pièce mécanique sujette à l'usure et ils peuvent se verrouiller instantanément sur plusieurs cibles.
- Une autorisation de radiofréquence spécifique est-elle nécessaire pour l'utiliser ? La bande des 10,5 GHz est soumise dans de nombreux pays à des attributions de fréquences pour radioamateurs ou à usage industriel/scientifique (ISM). Bien que les tests en laboratoire à faible puissance de sortie soient libres, les réglementations locales doivent être respectées pour les transmissions longue portée en extérieur.
- Avec quelles cartes de développement FPGA est-il compatible ? Les séries Xilinx Zynq-7000 ou les cartes modernes AMD UltraScale+ RFSoC sont directement prises en charge ; les interfaces ADC/DAC haute vitesse se connectent via le connecteur FMC.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/plfm-radar/
