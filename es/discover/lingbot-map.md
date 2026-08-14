# Cree escenas tridimensionales a partir de datos en streaming

Lingbot-map es un modelo básico 3D de avance diseñado para reconstruir escenas a partir de datos en tiempo real. El proyecto optimiza los procesos de visualización mediante el procesamiento de datos ambientales complejos, gracias a su arquitectura desarrollada en lenguaje Python.

- ★ 16.054
- Python
- GitHub Trending · 2026-06-29

## Actualizar
- 2 de agosto de 2026: Estrella 8.439 → 16.054.

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
Quiero crear una escena 3D a partir de datos en streaming usando LingBot-Map. Completé la instalación y mi archivo de modelo está listo. ¿Cómo puedo iniciar la interfaz de visualización en mi navegador local usando el comando requerido para ejecutar la instancia de Courthouse?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/lingbot-map/
