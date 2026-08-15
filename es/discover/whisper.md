# Transcribe sonidos con inteligencia artificial

Desarrollado por OpenAI, Whisper es un modelo de reconocimiento de voz entrenado mediante un método de aprendizaje de supervisión débil a gran escala. Ofrece altas tasas de precisión en la conversión y traducción de datos de audio multilingües a texto.

- ★ 106.452
- Python
- GitHub Trending · 2026-06-07

## Qué aporta
- Convierta archivos de audio a texto con alta precisión.
- Traducir conversaciones de diferentes idiomas al inglés.
- Identificación del idioma y detección de actividad del habla en contenido de audio.

## Instalación
**Dependencias del sistema**

```
sudo apt update && sudo apt install ffmpeg
```

**Requisito de instalación adicional**

```
pip install setuptools-rust
```


## Ejecución
**Convertir archivo de audio a texto**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Transcripción en un idioma específico**

```
whisper japanese.wav --language Japanese
```


## Si no programa
Quiero convertir mi archivo de audio en texto usando la herramienta Whisper. Hice las instalaciones necesarias en mi sistema. ¿Cuál es la estructura de comando básica que necesito escribir en la terminal para traducir el contenido de mi archivo de audio a texto y cómo debo usar el parámetro de especificación de idioma para archivos de audio en diferentes idiomas?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/whisper/
