# Cree escenas tridimensionales a partir de datos en streaming

Lingbot-map es un modelo básico 3D de avance diseñado para reconstruir escenas a partir de datos en tiempo real. El proyecto optimiza los procesos de visualización mediante el procesamiento de datos ambientales complejos, gracias a su arquitectura desarrollada en lenguaje Python.

- ★ 17.060
- Python
- GitHub Trending · 2026-06-29

## Actualizaciones

- **16 de septiembre de 2026:** Estrellas 16,054 → 17,060.
- **2 de agosto de 2026:** Estrellas 8,439 → 16,054.

## Qué aporta

- Reconstrucción 3D estable de largas secuencias de vídeo
- Soporte de inferencia de transmisión de baja latencia
- Arquitectura de inteligencia artificial que puede procesar datos ambientales complejos

## Instalación

**Preparación del entorno y configuración básica.**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Instalación de las bibliotecas necesarias**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

## Ejecución

**Comenzando la escena de muestra**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear una escena 3D a partir de datos en streaming usando LingBot-Map. Completé la instalación y mi archivo de modelo está listo. ¿Cómo puedo iniciar la interfaz de visualización en mi navegador local usando el comando requerido para ejecutar la instancia de Courthouse?

## Términos relacionados del glosario

- [Foundation Model](https://trescout.com/es/dictionary/foundation-model/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para investigadores y desarrolladores interesados ​​en la visión por computadora 3D y el procesamiento de datos en streaming.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/Robbyant/lingbot-map)
- [Leer en turco →](https://trescout.com/discover/lingbot-map/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-29: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/lingbot-map/
