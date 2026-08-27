# Transformez votre historique de localisation en vidéo animée

Google Timeline Visualizer visualise une année de vos voyages avec vos données d'historique de localisation Google.

- ★ 2 871
- Kotlin
- GitHub Trending · 2026-08-20

## Ce que ça vous apporte
- Convertit les données de l'historique Google Maps en vidéo MP4
- Anime les itinéraires de voyage sur la carte
- Protège la confidentialité en traitant les données personnelles sur l'appareil

## Installation
**Installez et exécutez les dépendances nécessaires**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configurer les outils de développement**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```


## Si vous ne codez pas
Je souhaite créer une vidéo montrant mes voyages en utilisant le fichier Timeline.json dont je dispose. Après avoir installé les dépendances nécessaires dans l'environnement Python, quelle commande dois-je utiliser pour convertir mes données 2025 en un fichier nommé « my_trip_2025.mp4 » avec un mouvement de caméra « stable » et des paramètres de compression « équilibrés » ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/google-timeline-visualizer/
