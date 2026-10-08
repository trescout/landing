# Producción de vídeo con inteligencia artificial en el sistema local.

Desarrollado por Lightricks, LTX-2 ofrece un paquete de entrenamiento de inferencia de Python y adaptación de bajo rango (LoRA) para modelos de inteligencia artificial que producen audio y video. Este conjunto de herramientas permite a los usuarios entrenar modelos LTX-2 con sus propios datos y ejecutar resultados del modelo en sistemas locales.

- ★ 9.567
- GitHub Trending · 2026-06-19

## Actualizaciones

- **2 de octubre de 2026:** Estrellas 9,562 → 9,567, última versión v1.4.2 (2 de octubre de 2026).
- **1 de octubre de 2026:** Estrellas 9,552 → 9,562, última versión v1.4.1 (30 de septiembre de 2026).
- **29 de septiembre de 2026:** Estrellas 9,267 → 9,552, última versión v1.4.0 (29 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 8,587 → 9,267, última versión v1.3.0 (26 de agosto de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Cree un video usando el modelo LTX-2 que describa la escena que quiero en detalle e incluya sincronización de audio y video. Haga que el modelo produzca resultados especificando los detalles de la escena, la apariencia del personaje, el ángulo de la cámara y el texto del habla.

## Términos relacionados del glosario

- [LoRA](https://trescout.com/es/dictionary/lora/)
- [Inference](https://trescout.com/es/dictionary/inference/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para usuarios que desean crear videos de IA de audio y video o entrenar modelos en su propio sistema local.

## Enlaces

- [Repositorio en GitHub →](https://github.com/Lightricks/LTX-2)
- [Leer en turco →](https://trescout.com/discover/ltx-2/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-19: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ltx-2/
