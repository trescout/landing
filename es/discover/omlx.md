# Servidor de IA para ordenadores Mac

Omlx es un servidor de inferencia de modelos grandes de lenguaje (LLM) local de última generación para ordenadores Mac con Apple Silicon (M1/M2/M3/M4), ofreciendo procesamiento por lotes continuo (continuous batching) y caché en SSD. Combina el framework Apple MLX con una API compatible con OpenAI y control desde la barra de menús de macOS.

- ★ 21.147
- Python
- GitHub Trending · 2026-08-18

## Actualizaciones
- 31 de agosto de 2026: Estrellas 20.793 → 21.147, última versión v0.6.4 (29 de agosto de 2026).
- 27 de agosto de 2026: Estrellas 20.069 → 20.793, última versión v0.6.3rc3 (24 de agosto de 2026).
- 20 de agosto de 2026: Estrellas 19.758 → 20.069, última versión v0.6.3rc2 (20 de agosto de 2026).
- 19 de agosto de 2026: Estrellas 19.519 → 19.758, última versión v0.6.3rc1 (19 de agosto de 2026).

## Qué te aporta
- Aceleración por hardware Apple MLX y Metal: Aprovecha directamente la Arquitectura de Memoria Unificada (UMA) de Apple Silicon para erradicar el cuello de botella al copiar memoria entre CPU y GPU.
- Procesamiento por lotes continuo (Continuous Batching): Consolida peticiones simultáneas de múltiples usuarios y agentes en un único ciclo de cómputo, triplicando el rendimiento del servidor.
- Caché en SSD y precarga por bloques (Chunked Prefill): Guarda la caché clave-valor (KV) en el disco SSD NVMe en ventanas de contexto extensas, previniendo errores de falta de memoria (OOM).
- API estándar compatible con OpenAI: Se integra sin configuración previa con Cursor, Open WebUI, Continue y LangChain a través de los endpoints /v1/chat/completions y /v1/models.
- Control desde la barra de menús de macOS: Inicia, detén, cambia de modelo y monitoriza el consumo de memoria en tiempo real sin tocar el terminal.

## Instalación

**Instalación con Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Ejecución

**Iniciar el servicio en segundo plano**

```
omlx start
```

**Descargar y servir un modelo específico**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Arquitectura técnica y principio de funcionamiento

Omlx está desarrollado sobre el framework de machine learning MLX de Apple. Se asienta sobre tres pilares arquitectónicos concebidos para superar los límites habituales en Mac (como llama.cpp u Ollama):
- Aprovechamiento pleno de la memoria unificada (UMA): A diferencia de los PC con tarjetas gráficas dedicadas, en Apple Silicon los núcleos GPU acceden directamente a 128 GB o 192 GB de RAM. Omlx procesa este volumen sin latencia mediante kernels Metal Shading Language (MSL).
- Gestión dinámica de caché KV (PagedAttention): Asigna tensores clave-valor en bloques paginados para evitar la fragmentación de memoria en sesiones múltiples, liberando espacio en cuanto concluye la respuesta.
- Capa de desbordamiento hacia SSD: Cuando la caché KV en contextos de 32K o 128K desborda la RAM, Omlx pagina automáticamente al almacenamiento SSD NVMe ultrarrápido sin provocar caídas en el modelo.

## Integración de API local compatible con OpenAI

Al iniciarse, Omlx expone una API REST local compatible con OpenAI (por defecto en http://localhost:8000). Puedes conectar tus editores de código y herramientas de IA con facilidad:

**Prueba de API con cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Cual es la ventaja principal de la arquitectura Apple Silicon?"}],
    "temperature": 0.7
  }'
```

## Si no programas
🤖 Si no programas
Quiero ejecutar un modelo de lenguaje local en mi Mac con Apple Silicon mediante Omlx. Tras instalarlo con Homebrew, ¿podrías explicarme paso a paso cómo arrancar el servidor en segundo plano, gestionar los modelos desde la barra de menús y conectar Cursor o un script en Python con la librería openai a dicho modelo local?

- **Para quién:** Desarrolladores de IA y usuarios de Mac con Apple Silicon que buscan la mayor velocidad de inferencia y total privacidad local.
- **Licencia:** Apache-2.0 (Licencia de código abierto)
- **Framework:** Motor de inferencia local basado en Apple MLX y Python
- **Hardware:** Apple Silicon series M1, M2, M3, M4 (soporte para Pro, Max y Ultra)

## Preguntas frecuentes
- ¿Cuál es la principal diferencia entre Omlx y Ollama? Mientras que Ollama usa principalmente la base en C++ de llama.cpp, Omlx se ejecuta de forma nativa sobre el framework MLX de Apple. Esta integración profunda con Metal y el Neural Engine ofrece mayor velocidad de generación de tokens, sobre todo en procesamiento por lotes y contextos largos.
- ¿Qué modelos pueden ejecutarse con 16 GB o 24 GB de RAM? Los modelos de 8B cuantizados a 4 bits (Llama 3, Qwen 2.5, Mistral) ocupan entre 5 y 6 GB de memoria y funcionan de manera muy fluida en Macs de 16 GB. Con 24 GB o 36 GB de memoria unificada, se pueden cargar cómodamente modelos de 14B o 32B.
- ¿Desgasta el disco SSD del Mac el uso de caché en disco? No. Omlx implementa mecanismos de amortiguación inteligente para evitar escrituras innecesarias. Solo entra en acción cuando el contexto satura la RAM física, manteniendo el desgaste al mínimo.
- ¿Funciona en Macs antiguos con Intel o en PC con Windows/Linux? No. Omlx está estrictamente optimizado para los chips Apple Silicon (arquitectura ARM) y Apple MLX. No es compatible con procesadores Intel ni sistemas x86.

## Enlaces
- [GitHub →](https://github.com/jundot/omlx)

## Términos relacionados del glosario
Apple Silicon Continuous Batching LLM Local Open Source

---
Source: TreScout Discover · https://trescout.com/es/discover/omlx/
