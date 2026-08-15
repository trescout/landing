# Producción de vídeo con inteligencia artificial en el sistema local.

Desarrollado por Lightricks, LTX-2 ofrece un paquete de entrenamiento de inferencia de Python y adaptación de bajo rango (LoRA) para modelos de inteligencia artificial que producen audio y video. Este conjunto de herramientas permite a los usuarios entrenar modelos LTX-2 con sus propios datos y ejecutar resultados del modelo en sistemas locales.

- ★ 8.587
- GitHub Trending · 2026-06-19

## Qué aporta
- Proporciona sincronización de audio y vídeo.
- Puedes entrenar LoRA con tus propios datos
- Producción de vídeo de alta calidad en sistema local.

## Instalación
**Clona el repositorio de GitHub e ingresa al directorio**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Descargar pesos de modelo (CLI de Hugging Face)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```


## Ejecución
**ejecutar canalización de inferencia con uv**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```


## Si no programa
Cree un video usando el modelo LTX-2 que describa la escena que quiero en detalle e incluya sincronización de audio y video. Haga que el modelo produzca resultados especificando los detalles de la escena, la apariencia del personaje, el ángulo de la cámara y el texto del habla.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ltx-2/
