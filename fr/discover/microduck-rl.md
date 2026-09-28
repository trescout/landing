# Environnement d'apprentissage par renforcement pour Pollen Robotics Microduck

Développé par Pollen Robotics, microduck_rl fournit des environnements de formation d'apprentissage par renforcement et des politiques de contrôle sur MuJoCo et mjlab pour la plateforme robotique Microduck.

- ★ 2 281
- Python
- GitHub Trending · 2026-08-31

## Ce que ça vous apporte
- Simulation physique réaliste de MuJoCo : Possibilité de simuler les couples articulaires, les frottements et les effets de gravité du robot à grande vitesse.
- Tâches de locomotion et d'équilibre prêtes à l'emploi : fonctions de récompense prédéfinies pour les scénarios de marche, d'équilibre et de dépassement d'obstacles.
- Adapté au transfert Sim-to-Real : politiques de contrôle résistantes au bruit qui peuvent être facilement transférées au matériel physique Microduck.
- Algorithmes modernes d’apprentissage par renforcement : infrastructure de formation prise en charge par PPO (Proximal Policy Optimization) et SAC.
- Interface d'évaluation visuelle 3D : Suivi instantané des mouvements de l'agent robot formé dans le simulateur 3D sur l'écran.

## Installation
**Clonage du référentiel et mise en place de l'environnement de simulation**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```


## Exécution
**Organiser une formation ou une évaluation des politiques**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```


## Architecture technique et principe de fonctionnement
- MuJoCo et mjlab Physics Layer : fichiers XML/MJCF qui définissent la cinématique du robot, les limites des articulations et les modèles d'actionneurs.
- Espaces d'observation et d'action compatibles avec les gymnases : normalisation des angles des moteurs, des vitesses, des données de l'accéléromètre (IMU) et des vecteurs de couple cibles.
- Mécanisme de randomisation du domaine : formation de modèles robustes du monde réel en faisant varier de manière aléatoire les coefficients de friction, la distribution de masse et le bruit des capteurs.

## Politiques de simulation physique et de contrôle robotique
- Prévenir les dommages matériels : résolvez les risques de chutes de robots et de fractures de jambes dans un environnement entièrement virtuel avant de passer au robot physique.
- Entraînement de millions d'étapes en temps accéléré : terminez des journées d'entraînement en quelques heures en faisant fonctionner le moteur physique 100 fois plus vite qu'en temps réel.
- Mission personnalisée et conception du terrain : testez l'adaptabilité du robot à différents terrains en ajoutant des escaliers, des pentes et des surfaces glissantes.

## Si vous ne codez pas
Je souhaite former une politique de marche pour le robot Microduck à l'aide de la bibliothèque microduck_rl de Pollen Robotics. Pouvez-vous expliquer les étapes à suivre pour configurer l'environnement MuJoCo, initialiser la commande d'entraînement avec l'algorithme PPO et transférer la politique de contrôle résultante au robot physique ?

## Questions fréquemment posées
- Est-il nécessaire d'avoir un robot Microduck physique pour exécuter microduck_rl ? Non. La base de code peut être exécutée entièrement virtuellement sur le simulateur MuJoCo ; Vous pouvez regarder la simulation 3D du robot sur votre ordinateur.
- La prise en charge du GPU est-elle requise ? MuJoCo fonctionne également assez rapidement sur le processeur ; Cependant, lors de la formation à l’apprentissage par renforcement avec des environnements parallèles, un GPU pris en charge par CUDA accélère considérablement le processus.
- Comment le modèle entraîné est-il transféré au robot physique ? Une fois la formation terminée, le fichier de point de contrôle ONNX ou PyTorch généré est chargé dans l'ordinateur de contrôle embarqué de Microduck et directement connecté aux couples du moteur.
- Est-il compatible avec différents modèles de robots ? microduck_rl est optimisé principalement pour Microduck ; Cependant, grâce à sa structure modulaire, il peut être adapté à des modèles similaires de robots bipèdes ou quadrupèdes MJCF.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/microduck-rl/
