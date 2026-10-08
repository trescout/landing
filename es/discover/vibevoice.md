# Analizando largas grabaciones de audio con inteligencia artificial

Publicado por Microsoft, VibeVoice fue desarrollado como un marco de inteligencia artificial de voz de código abierto. Con su estructura basada en Python, el sistema permite a los usuarios entrenar sus propios modelos de sonido e integrarlos en sus aplicaciones.

- ★ 54.502
- GitHub Trending · 2026-06-07

**Nota de TreScout:** El repositorio cambió después de su publicación: la parte que convierte sonido en texto permanece, la parte que convierte texto en sonido ha sido retirada. Su característica distintiva es que puede procesar registros largos a la vez. Es un proyecto que cambia rápidamente, eche un vistazo al estado actual del almacén antes de agregarlo a su negocio.

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 51,860 → 54,502.
- **2 de agosto de 2026:** Estrellas 48,569 → 51,860.

## Qué aporta

- Convierte hasta 60 minutos de grabación de audio en texto a la vez.
- Proporciona identificación del hablante, marca de tiempo y detalles del contenido de forma estructurada.
- Proporciona compatibilidad con palabras clave definidas por el usuario para términos y nombres personalizados.

## Instalación

**Instalar desde GitHub**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```

## Ejecución

**Demostración de Gradio**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Transcripción del archivo**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero analizar la grabación de audio de 60 minutos que tengo usando el modelo VibeVoice. Necesito recuperar quiénes son los oradores, cuándo hablaron y el contenido que dijeron como un archivo de texto estructurado. También quiero agregar palabras clave personalizadas para que el modelo reconozca los términos técnicos con mayor precisión. ¿Cómo puedo estructurar este proceso?

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para usuarios que desean convertir de forma rápida y estructurada grabaciones de audio de larga duración, resúmenes de reuniones o contenido de podcasts en texto.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/microsoft/VibeVoice)
- [Leer en turco →](https://trescout.com/discover/vibevoice/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-07: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vibevoice/
