# Analizando largas grabaciones de audio con inteligencia artificial

Publicado por Microsoft, VibeVoice fue desarrollado como un marco de inteligencia artificial de voz de código abierto. Con su estructura basada en Python, el sistema permite a los usuarios entrenar sus propios modelos de sonido e integrarlos en sus aplicaciones.

- ★ 51.860
- GitHub Trending · 2026-06-07

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
Quiero analizar la grabación de audio de 60 minutos que tengo usando el modelo VibeVoice. Necesito recuperar quiénes son los oradores, cuándo hablaron y el contenido que dijeron como un archivo de texto estructurado. También quiero agregar palabras clave personalizadas para que el modelo reconozca los términos técnicos con mayor precisión. ¿Cómo puedo estructurar este proceso?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vibevoice/
