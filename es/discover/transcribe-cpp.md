# Rápida conversión de voz en sistemas locales

Transcribe.cpp es una biblioteca de inferencia de voz a texto desarrollada en C++ que admite más de 16 familias de modelos. Utilizando la infraestructura ggml, esta herramienta permite que diferentes modelos de procesamiento de audio se ejecuten de manera eficiente en sistemas locales.

- ★ 1.802
- C++
- GitHub Trending · 2026-07-21

## Qué aporta
- Soporte para 16 familias de modelos diferentes.
- Alto rendimiento en GPU y CPU
- Inferencia eficiente con formato GGUF

## Instalación
**Instalación de Linux compatible con Vulkan**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```


## Si no programa
Quiero convertir un archivo de audio local a texto usando la herramienta Transcribe.cpp. ¿Sistemimderlenmiş olan transcribe-cli aracını e indirdiğim formato GGUF dosyasını kullanarak, formato WAV mono de 16 kHz ses dosyamı nasıl işleyebilirim? Explique la estructura de comandos requerida para este proceso y las rutas de archivos a las que debo prestar atención.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/transcribe-cpp/
