# Sintetizador de voz ligero con IA que se ejecuta en la CPU

Desarrollado por Kyutai Labs, Pocket-TTS es un modelo ligero de conversión de texto a voz que se ejecuta únicamente en la unidad central de procesamiento (CPU) sin necesidad de una unidad de procesamiento de gráficos. Gracias a su bajo consumo de recursos, ofrece una síntesis de sonido rápida y eficiente en dispositivos con restricciones de hardware.

- ★ 9.151
- Python
- GitHub Trending · 2026-07-08

## Qué aporta
- Funciona sólo con el procesador, sin necesidad de tarjeta gráfica
- Proporciona una reproducción de sonido rápida con un bajo consumo de recursos.
- Ofrece clonación de voz y soporte en varios idiomas.

## Instalación
**Instalación del paquete**

```
pip install pocket-tts
# or
uv add pocket-tts
```


## Ejecución
**Crear un archivo de audio**

```
uvx pocket-tts generate
# or if you installed it manually with pip:
pocket-tts generate
```

**Inicio del servidor local**

```
uvx pocket-tts serve
# or if you installed it manually with pip:
pocket-tts serve
```


## Si no programa
Quiero convertir texto a voz usando la herramienta Pocket TTS. Explicar cómo configurar los comandos necesarios y el modelo de sonido para producir rápidamente un archivo de audio en mi computadora usando solo la potencia del procesador. En particular, explique paso a paso cómo puedo cambiar la configuración de audio predeterminada y clonar mi audio usando mi propio archivo de audio.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/pocket-tts/
