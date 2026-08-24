# Turn your location history into motion video

O Google Timeline Visualizer, que visualiza os dados do Histórico de localização do Google, permite analisar routes de viagem ao longo do ano em um mapa. Desenvolvido com a linguagem Kotlin, esta ferramenta cria resumos pessoais de viagens convertendo dados do histórico de localização em gráficos significativos.

- ★ 2,712
- Kotlin
- GitHub Trending · 2026-08-20

## What you get
- Converts Google Maps history data to MP4 video
- Animates travel routes on the map
- Protects privacy by processing personal data on device

## Installation
**Install and run the necessary dependencies**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configure development tools**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```


## If you don't write code
I want to create a video showing my travels using the Timeline.json file I have. After installing the necessary dependencies in the Python environment, what command should I use to convert my 2025 data into a file named 'my_trip_2025.mp4' with 'steady' camera motion and 'balanced' compression settings?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/google-timeline-visualizer/
