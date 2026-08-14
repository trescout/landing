# Motor de ejecución DeepSeek en hardware nativo

Desarrollado por Salvatore Sanfilippo, el creador de Redis, ds4 es un motor de inferencia que permite ejecutar modelos DeepSeek en hardware local. Esta herramienta, escrita en lenguaje C, ofrece la oportunidad de ejecutar modelos de alto rendimiento en diferentes procesadores gráficos gracias al soporte Metal, CUDA y ROCm.

- ★ 21.134
- C
- GitHub Trending · 2026-08-03

## Actualizar
- 11 de agosto de 2026: Estrella 20,117 → 21,134.

## Qué aporta
- Ejecuta modelos de IA de alto rendimiento en hardware de consumo
- Permite el uso del modelo incluso con capacidad de memoria limitada mediante la transmisión de datos a través de SSD
- Permite crear un servidor LLM de nivel empresarial con soporte para múltiples GPU

## Instalación
**Construya para adaptarse a su hardware**

```
make                  # macOS Metal
make cuda-spark       # Linux CUDA, DGX Spark / GB10
make cuda-generic     # Linux CUDA, other local CUDA GPUs
make strix-halo       # Linux ROCm, AMD Strix Halo
make cpu              # CPU-only diagnostics build
```

**Descarga el modelo**

```
./download_model.sh q2-imatrix   # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix  # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix   # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix  # 512 GB RAM machines, PRO q2 imatrix quant
```


## Ejecución
**Inicializar el modelo**

```
./download_model.sh q2-imatrix

./ds4 \
  -m ./ds4flash.gguf \
  --ssd-streaming \
  --ssd-streaming-cache-experts 32GB \
  --ctx 32768 \
  --nothink
```


## Si no programa
Ayúdame a elegir el modelo de DeepSeek o GLM más adecuado según las características de hardware de mi sistema. ¿Qué comando de descarga debo usar y cómo puedo superar el cuello de botella de la memoria activando la función de transmisión a través de SSD? Además, explíqueme los ajustes de configuración básicos necesarios para utilizar este sistema de inteligencia artificial que he instalado como servidor local.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ds4/
