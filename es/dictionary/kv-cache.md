# ¿Qué es KV Cache?

> Key-Value Cache

Se trata de un método de aceleración que evita que la inteligencia artificial repita las mismas operaciones manteniendo en su memoria las palabras que ha procesado previamente.

## Definición
Al producir un texto, en lugar de pensar desde cero para cada palabra, la inteligencia artificial almacena la información previamente procesada en un caché como valores 'Clave' y 'Valor'. Este sistema permite al modelo recordar rápidamente el pasado sin tener que volver a calcularlo al predecir la siguiente palabra. De esta forma, se reduce la carga de procesamiento y los tiempos de respuesta se acortan significativamente.

## Cómo funciona
Mientras el modelo se ejecuta, se crea automáticamente en segundo plano y se guarda en la memoria. Este caché comienza a llenarse cuando el usuario inicia una conversación larga. Cuando la memoria se llena, el sistema desarrolla estrategias para borrar información antigua o dejar espacio para datos nuevos.

## Dónde se usa
Se utiliza en los procesos de trabajo de los LLM y especialmente en las interfaces de chat donde se producen textos largos.

## Suele confundirse con
Puede confundirse con la ventana de contexto, pero no se trata de un límite de capacidad, sino de un método para utilizar esta capacidad de forma eficiente.

## Preguntas frecuentes
**¿Por qué es importante la caché KV?**
Al evitar que la IA calcule la misma frase una y otra vez, reduce la carga en el procesador y acelera la respuesta.

**¿Qué pasa si la memoria se llena?**
Es posible que el sistema no pueda procesar datos nuevos o comience a olvidar información antigua.


## Términos relacionados
- [LLM](/es/dictionary/llm/)
- [Context Window](/es/dictionary/context-window/)
- [Inference](/es/dictionary/inference/)
- [Memory Management](/es/dictionary/memory-management/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/kv-cache/
