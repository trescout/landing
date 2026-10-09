# Servidor de IA para computadoras Mac

Omlx es un servidor de inferencia de modelo de lenguaje grande (LLM) nativo de próxima generación que ofrece capacidades de procesamiento por lotes continuo y almacenamiento en caché SSD para computadoras Mac con procesadores Apple Silicon (M1/M2/M3/M4). Combina la infraestructura Apple MLX con una API compatible con OpenAI y una interfaz de barra de menús de macOS.

- ★ 22.655
- Python
- GitHub Trending · 2026-08-18

## Actualizaciones

- **9 de octubre de 2026:** Estrellas 22,409 → 22,655, última versión v0.7.1.dev1 (9 de octubre de 2026).
- **1 de octubre de 2026:** Estrellas 22,280 → 22,409, última versión v0.7.0 (30 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 21,147 → 22,280, última versión v0.7.0rc1 (24 de septiembre de 2026).
- **31 de agosto de 2026:** Estrellas 20,793 → 21,147, última versión v0.6.4 (29 de agosto de 2026).

## Qué aporta

- Aceleración de hardware Apple MLX y Metal: elimina por completo el cuello de botella de copia de memoria entre la CPU y la GPU mediante el uso directo de la arquitectura de memoria unificada (UMA) de los procesadores Apple Silicon.
- Procesamiento por lotes continuo: aumenta la eficiencia del servidor hasta 3 veces al combinar múltiples solicitudes simultáneas de usuarios y agentes en un solo ciclo de cálculo.
- Almacenamiento en caché de SSD y relleno previo de fragmentos: evita fallas por falta de memoria (OOM) al almacenar el caché de valor clave (KV) en el SSD NVMe durante ventanas de contexto largas.
- API estándar compatible con OpenAI: funciona sin configuración con las herramientas Cursor, Open WebUI, Continuar y LangChain gracias a los puntos finales /v1/chat/completions y /v1/models.
- Control de la barra de menú de macOS: Ofrece la comodidad de iniciar, detener, seleccionar modelos y monitorear el consumo de memoria con gráficos en vivo sin ingresar al terminal.

## Instalación

**Instalación con cerveza casera**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Ejecución

**Iniciando el servicio en segundo plano**

```
omlx start
```

**Descargar y enviar un modelo específico**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Arquitectura técnica y principio de funcionamiento

- Uso completo de la memoria unificada (UMA): a diferencia de las PC con gráficos discretos, en las Apple Silicon Macs, los núcleos de GPU pueden direccionar directamente 128 GB o 192 GB de RAM. Omlx procesa este enorme conjunto de memoria con latencia cero con núcleos Metal Shading Language (MSL).
- Gestión dinámica de caché KV (PaggedAttention): asigna tensores de valores clave como bloques paginados para evitar la fragmentación de la memoria en varias sesiones. La memoria utilizada se libera inmediatamente cuando finaliza la solicitud.
- Capa de caché que se desborda a SSD: cuando la caché KV excede la RAM en ventanas de contexto grandes como 32K y 128K, Omlx busca automáticamente el disco SSD integrado de alta velocidad de Apple. Por lo tanto, el modelo continúa la inferencia sin fallar.

## Integración de API nativa compatible con OpenAI

**Pruebas API con cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Apple Silicon mimarisinin temel avantajı nedir?"}],
    "temperature": 0.7
  }'
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar un modelo de lenguaje nativo grande usando el servidor Omlx en mi Apple Silicon Mac. Después de completar la instalación con Homebrew, ¿puede explicar paso a paso cómo ejecutar el servidor en segundo plano, administrar la selección del modelo desde la barra de menú y conectarse a este modelo local a través del editor de código de cursor o la biblioteca openai de Python?

## Preguntas frecuentes

- ¿Cuál es la principal diferencia entre Omlx y Ollama? Mientras que Ollama generalmente utiliza la infraestructura llama.cpp basada en C++, Omlx se ejecuta directamente en el marco MLX desarrollado por Apple. De esta manera, proporciona una integración más profunda con las unidades metálicas y motoras neuronales de los chips Apple Silicon, proporcionando una mayor tasa de generación de tokens, especialmente en apilamiento continuo y contextos prolongados.
- ¿Qué modelos se pueden ejecutar con 16 GB o 24 GB de RAM? Los modelos con parámetros 8B cuantificados de 4 bits (Llama 3, Qwen 2.5, Mistral) ocupan aproximadamente entre 5 y 6 GB de memoria y funcionan de manera extremadamente fluida en Mac de 16 GB. En dispositivos con memoria combinada de 24 GB o 36 GB, se pueden instalar fácilmente modelos de 14B o 32B.
- ¿El almacenamiento en caché SSD agota la vida útil del disco de Mac? No. Omlx utiliza algoritmos de almacenamiento en búfer inteligentes para evitar ciclos de escritura innecesarios en las operaciones de almacenamiento en caché. Sólo se activa cuando la memoria contextual se acerca al límite de RAM, manteniendo el desgaste del disco al mínimo.
- ¿Funciona en computadoras Mac antiguas basadas en Intel? No. Omlx está optimizado específicamente para Apple Silicon (arquitectura ARM) y el marco Apple MLX. No se ejecuta en Mac con Intel ni en computadoras Windows/Linux x86.

## Términos relacionados del glosario

- [Continuous Batching](https://trescout.com/es/dictionary/continuous-batching/)
- [SSD Caching](https://trescout.com/es/dictionary/ssd-caching/)
- [Context Window](https://trescout.com/es/dictionary/context-window/)
- [Caching](https://trescout.com/es/dictionary/caching/)
- [Apple Silicon](https://trescout.com/es/dictionary/apple-silicon/)
- [RAM](https://trescout.com/es/dictionary/ram/)

- **Para quién es:** Para desarrolladores de IA que desean ejecutar modelos de lenguaje grandes (LLM) a máxima velocidad y con privacidad nativa en computadoras Mac con procesadores Apple Silicon.
- **Licencia:** Apache-2.0 (Açık kaynak lisansı)
- **Marco:** Motor de inferencia nativo basado en Apple MLX y Python
- **Hardware:** Serie Apple Silicon M1, M2, M3, M4 (compatible con Pro, Max, Ultra)

## Enlaces

- [Repositorio en GitHub →](https://github.com/jundot/omlx)
- [Leer en turco →](https://trescout.com/discover/omlx/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-18: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/omlx/
