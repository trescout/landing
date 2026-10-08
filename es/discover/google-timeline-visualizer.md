# Convierte tu historial de ubicaciones en vídeo en movimiento

Google Timeline Visualizer visualiza los viajes de un año con los datos del historial de ubicaciones de Google.

- ★ 3.030
- Kotlin
- GitHub Trending · 2026-08-20

## Actualizaciones

- **5 de octubre de 2026:** Estrellas 2,990 → 3,030, última versión v3.1.0 (5 de octubre de 2026).
- **13 de septiembre de 2026:** Estrellas 2,980 → 2,990, última versión v3.0.18 (12 de septiembre de 2026).
- **9 de septiembre de 2026:** Estrellas 2,972 → 2,980, última versión v3.0.17 (9 de septiembre de 2026).
- **7 de septiembre de 2026:** Estrellas 2,969 → 2,972, última versión v3.0.16 (6 de septiembre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear un video que muestre mis viajes usando el archivo Timeline.json que tengo. Después de instalar las dependencias necesarias en el entorno Python, ¿qué comando debo usar para convertir mis datos de 2025 en un archivo llamado 'my_trip_2025.mp4' con un movimiento de cámara 'constante' y configuraciones de compresión 'equilibradas'?

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para cualquiera que quiera visualizar el historial de ubicaciones en Google Maps y guardar recuerdos de viaje en formato de vídeo.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/mahlernim/google-timeline-visualizer)
- [Leer en turco →](https://trescout.com/discover/google-timeline-visualizer/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-20: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/google-timeline-visualizer/
