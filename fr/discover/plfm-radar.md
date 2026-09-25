# Système radar à balayage électronique open-source

PLFM RADAR est un système radar à balayage électronique (phased array) open-source fonctionnant à 10,5 GHz (bande X), doté d'une orientation de faisceau électronique et d'un traitement numérique du signal sur FPGA. Il détecte et suit des cibles aériennes et terrestres sans pièces mécaniques rotatives.

- ★ 24.168
- C++
- GitHub Trending · 2026-08-18

## Mises à jour
- 18 août 2026: Étoiles 24 168, version stable v2.0.2-p0-audit (filtrage de signal sur FPGA et calibration de portée).

## Ce que ça vous apporte
- Orientation électronique du faisceau: Balaye un secteur de 90 degrés en quelques millisecondes via des déphaseurs sans usure mécanique.
- Deux modes de portée opérationnels: Mode tactique 3 km pour la détection de drones et mode longue portée 20 km pour la surveillance périmétrique.
- Traitement temps réel sur FPGA: Calculs de FFT et algorithmes CFAR exécutés directement sur le silicium du FPGA.
- Matériel accessible à coût réduit: Réduit les coûts de centaines de milliers de dollars des radars militaires à moins de mille dollars.
- Intégration Python et SDR: Visualisez les vecteurs de cibles en direct via des récepteurs SDR et une interface graphique Python PPI.

## Composants matériels et architecture radar

Le système PLFM RADAR s'articule autour d'un étage RF frontal, d'un réseau d'antennes et d'un étage numérique :
- Réseau d'antennes patch 10,5 GHz bande X: Éléments rayonnants micro-ruban conçus sur substrat Rogers/FR4 à faibles pertes.
- Déphaseurs à commande numérique: Modulent la phase de chaque élément d'antenne avec une précision de 5,6 degrés pour orienter le faisceau dans l'espace.
- Synthétiseur de fréquence FMCW: Oscillateur local haute stabilité (VCO/PLL) produisant des ondes entretenues modulées en fréquence.

## Traitement du signal et logiciel de contrôle

Les échos radar bruts sont filtrés matériellement pour extraire distance, vitesse et azimut des cibles :
- 2D FFT Distance-Doppler: Transformée de Fourier rapide bidimensionnelle pour distinguer simultanément la distance et la vitesse radiale.
- Détecteur CFAR (Taux de fausse alarme constant): Isole dynamiquement les cibles mobiles des bruits de sol et des échos parasites.
- Interface graphique Python et affichage PPI: Affiche les cibles détectées sur un écran radar panoramique classique superposé à une carte.

## Principe technique : FMCW et balayage de phase

PLFM RADAR emploie l'émission continue modulée en fréquence (FMCW) plutôt que des impulsions haute puissance :
- Mesure de distance par fréquence de battement: Le mélange de l'onde émise avec l'écho reçu génère une fréquence intermédiaire proportionnelle à la distance.
- Formation de faisceau par interférences constructives: L'ajustement des phases relatives sur chaque antenne focalise l'onde dans la direction souhaitée.

## Cas d'usage et scénarios opérationnels

Cette technologie radar open-source ouvre de nombreuses applications concrètes :
- Défense anti-drones à basse altitude: Détecte les micro-drones par temps de brume ou de nuit quand les caméras optiques sont inopérantes.
- Sécurité des sites sensibles: Surveille les intrusions de véhicules ou de piétons sur un rayon de 3 km autour d'aéroports ou de centres de données.
- Recherche météorologique: Mesure les vitesses de vent localisées et l'intensité des précipitations par micro-Doppler.

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite analyser les schémas matériels 10,5 GHz et le traitement DSP sur FPGA du projet PLFM RADAR. Peux-tu générer un script de simulation en Python qui modélise l'émission d'un signal FMCW, applique la 2D FFT Distance-Doppler et extrait la position et la vitesse d'un drone simulé ?

- **Pour qui:** Chercheurs en radar, ingénieurs défense, développeurs de systèmes anti-drones et passionnés de SDR.
- **Licence:** Licence matérielle et logicielle open-source
- **Bande de fréquence:** 10,5 GHz (Bande X) FMCW
- **Portée cible:** 3 km (tactique anti-drone) à 20 km (surveillance large)

## Questions fréquentes
- Peut-on fabriquer ce système en atelier ou laboratoire ? Oui. Tous les schémas PCB, fichiers Gerber et codes Verilog/VHDL sont disponibles sur le dépôt GitHub. Les circuits peuvent être commandés chez un fabricant de PCB standard.
- Quel est le principal avantage par rapport à un radar tournant ? L'orientation électronique permet de basculer le faisceau en quelques microsecondes sans aucune pièce en mouvement, augmentant la fiabilité et le suivi simultané.
- Une licence d'émission RF spécifique est-elle requise ? La bande 10,5 GHz fait l'objet d'allocations radioamateurs ou ISM dans plusieurs pays. En laboratoire à faible puissance l'usage est toléré, mais l'émission extérieure est soumise aux réglementations locales.
- Quelles cartes de développement FPGA sont compatibles ? Les familles Xilinx Zynq-7000 et AMD UltraScale+ RFSoC sont directement prises en charge via connecteurs FMC pour les convertisseurs ADC/DAC rapides.

## Liens
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## Termes associés du glossaire
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/fr/discover/plfm-radar/
