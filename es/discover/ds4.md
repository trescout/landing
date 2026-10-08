# Motor de ejecución DeepSeek en hardware nativo

Desarrollado por Salvatore Sanfilippo, el creador de Redis, ds4 es un motor de inferencia que permite ejecutar modelos DeepSeek en hardware local. Esta herramienta, escrita en lenguaje C, ofrece la oportunidad de ejecutar modelos de alto rendimiento en diferentes procesadores gráficos gracias al soporte Metal, CUDA y ROCm.

- ★ 23.530
- C
- GitHub Trending · 2026-08-03

## Actualizaciones

- **5 de octubre de 2026:** Estrellas 22,197 → 23,530.
- **10 de septiembre de 2026:** Estrellas 21,134 → 22,197.
- **11 de agosto de 2026:** Estrellas 20,117 → 21,134.

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Ayúdame a elegir el modelo de DeepSeek o GLM más adecuado según las características de hardware de mi sistema. ¿Qué comando de descarga debo usar y cómo puedo superar el cuello de botella de la memoria activando la función de transmisión a través de SSD? Además, explíqueme los ajustes de configuración básicos necesarios para utilizar este sistema de inteligencia artificial que he instalado como servidor local.

## Términos relacionados del glosario

- [Inference Engine](https://trescout.com/es/dictionary/inference-engine/)
- [Inference](https://trescout.com/es/dictionary/inference/)
- [LLM](https://trescout.com/es/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a desarrolladores de software y administradores de sistemas que desean ejecutar modelos de inteligencia artificial de alto rendimiento en su propio hardware local.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/antirez/ds4)
- [Leer en turco →](https://trescout.com/discover/ds4/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-03: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ds4/
