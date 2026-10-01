# ¿Qué es Apple Silicon?

Apple Silicon es una familia de procesadores SoC (System on a Chip) de alto rendimiento basados en ARM que Apple diseña internamente para sus dispositivos Mac y iPad, combinando CPU, GPU, Neural Engine y memoria unificada (Unified Memory) en una sola placa de silicio.

## Génesis conceptual, historia y la gran migración de x86 a ARM
"Silicon" (silicio) es el elemento químico fundamental utilizado en la fabricación de microchips semiconductores. Apple Silicon, por su parte, representa el diseño de microprocesadores personalizados de Apple con el que pone fin a su dependencia de fabricantes de chips externos (Intel, Motorola, IBM) para integrar verticalmente su propio hardware y software.

## Sistema en un chip (SoC) y Arquitectura de Memoria Unificada (UMA)
En una computadora de escritorio o portátil tradicional, el hardware está fragmentado: hay un zócalo de CPU separado en la placa base, una tarjeta gráfica externa dedicada (GPU) conectada a una ranura PCIe, módulos de RAM separados y puentes en la placa base. Para que la CPU muestre en pantalla una imagen que ha procesado, los datos deben copiarse desde la RAM a través del bus de la placa base hacia la propia VRAM de la GPU. Esto genera latencia y un alto consumo de energía.

## Anatomía del núcleo, aceleradores y Rosetta 2
El equilibrio de rendimiento puro y eficiencia de Apple Silicon se basa en tres componentes de ingeniería fundamentales:

## Preguntas frecuentes
**¿Qué significa Apple Silicon y qué procesadores abarca?**
Es la familia de procesadores System on a Chip (SoC) basados en ARM diseñados por Apple. Abarca los chips de la serie A en iPhones y iPads, y los procesadores de la serie M (M1, M2, M3, M4 y sus variantes) que alimentan a las computadoras Mac.

**¿En qué se diferencia la Arquitectura de Memoria Unificada (UMA) de la RAM y la VRAM tradicionales?**
En los sistemas tradicionales, la CPU tiene su propia memoria RAM del sistema y la tarjeta gráfica tiene su propia VRAM, y los datos se copian entre ambas. En la UMA, la memoria está directamente en el paquete del procesador; la CPU, la GPU y el motor de inteligencia artificial acceden al mismo grupo de memoria con un coste cero de latencia de copia.

**¿Funcionan las aplicaciones antiguas de Intel en un Mac con procesador Apple Silicon?**
Sí, gracias al motor de traducción Rosetta 2 integrado en el sistema operativo macOS, la gran mayoría de las aplicaciones escritas para Intel (x86_64) se ejecutan a alta velocidad sin que el usuario lo note.

**¿Por qué es tan popular Apple Silicon en el desarrollo de inteligencia artificial (LLM) local?**
Porque gracias a la Arquitectura de Memoria Unificada, la GPU puede utilizar directamente enormes grupos de memoria como 64 GB, 96 GB o 128 GB como VRAM. Esto permite ejecutar localmente grandes modelos de lenguaje con más de 70B parámetros sin necesidad de costosas GPUs de servidor.


## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [Computer Science](/es/dictionary/computer-science/)
- [Assembly](/es/dictionary/assembly/)
- [Memory Management](/es/dictionary/memory-management/)
- [Emulator](/es/dictionary/emulator/)
- [Cloud Computing](/es/dictionary/cloud-computing/)

## Herramientas relacionadas
- [Minimind](/es/discover/minimind/)
- [Container](/es/discover/container/)
- [Airllm](/es/discover/airllm/)
- [Omlx](/es/discover/omlx/)
- [Palmier Pro](/es/discover/palmier-pro/)
- [Openmed](/es/discover/openmed/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/apple-silicon/
