# Convierte tu historial de ubicaciones en vídeo en movimiento

El Google Timeline Visualizer, que visualiza los datos históricos de localización de Google, permite analizar rutas de viaje a lo largo del año en un mapa. Desarrollado con el lenguaje Kotlin, esta herramienta crea resultados de personas que viajan convirtiendo datos históricos de localización en gráficos significativos.

- ★ 2.075
- Kotlin
- GitHub Trending · 2026-08-20

## Qué aporta
- Convierte los datos del historial de Google Maps a vídeo MP4
- Anima rutas de viaje en el mapa.
- Protege la privacidad mediante el procesamiento de datos personales en el dispositivo

## Instalación
**Instalar y ejecutar las dependencias necesarias.**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configurar herramientas de desarrollo**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```


## Si no programa
Quiero crear un video que muestre mis viajes usando el archivo Timeline.json que tengo. Después de instalar las dependencias necesarias en el entorno Python, ¿qué comando debo usar para convertir mis datos de 2025 en un archivo llamado 'my_trip_2025.mp4' con un movimiento de cámara 'constante' y configuraciones de compresión 'equilibradas'?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/google-timeline-visualizer/
