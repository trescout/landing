# Rápida conversión de voz en sistemas locales

Transcribe.cpp es una biblioteca de inferencia de voz a texto desarrollada en C++ que admite más de 16 familias de modelos. Utilizando la infraestructura ggml, esta herramienta permite que diferentes modelos de procesamiento de audio se ejecuten de manera eficiente en sistemas locales.

- ★ 1.982
- C++
- GitHub Trending · 2026-07-21

## Actualizaciones

- **4 de octubre de 2026:** Estrellas 1,981 → 1,982, última versión v0.3.1 (4 de octubre de 2026).
- **3 de octubre de 2026:** Estrellas 1,963 → 1,981, última versión v0.3.0 (3 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 1,865 → 1,963, última versión v0.2.4 (25 de septiembre de 2026).
- **31 de agosto de 2026:** Estrellas 1,825 → 1,865, última versión v0.2.3 (30 de agosto de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero convertir un archivo de audio local a texto usando la herramienta Transcribe.cpp. ¿Sistemimderlenmiş olan transcribe-cli aracını e indirdiğim formato GGUF dosyasını kullanarak, formato WAV mono de 16 kHz ses dosyamı nasıl işleyebilirim? Explique la estructura de comandos requerida para este proceso y las rutas de archivos a las que debo prestar atención.

## Términos relacionados del glosario

- [Speech-to-Text](https://trescout.com/es/dictionary/speech-to-text/)
- [STT](https://trescout.com/es/dictionary/stt/)
- [GGUF](https://trescout.com/es/dictionary/gguf/)
- [Inference](https://trescout.com/es/dictionary/inference/)
- [CPU](https://trescout.com/es/dictionary/cpu/)
- [GPU](https://trescout.com/es/dictionary/gpu/)

- **Para quién es:** Es para desarrolladores que desean ejecutar sistemas de reconocimiento de voz rápidos y centrados en la privacidad en su propio hardware.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/handy-computer/transcribe.cpp)
- [Leer en turco →](https://trescout.com/discover/transcribe-cpp/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-21: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/transcribe-cpp/
