# ¿Qué es Looped Transformer?

Es una arquitectura de inteligencia artificial que reduce el uso de memoria al utilizar las mismas capas de procesamiento una y otra vez.

## Definición
Mientras que los modelos tradicionales requieren una unidad de procesamiento separada para cada capa, esta arquitectura utiliza la misma capa repetidamente en un bucle. De esta manera, el tamaño del modelo se reduce y consume menos memoria. Su objetivo es ejecutar modelos grandes en dispositivos más pequeños sin sacrificar el rendimiento.

## Cómo funciona
Los datos entran en el modelo y pasan por el mismo bloque de capas varias veces. En cada paso, los datos se procesan un poco más hasta llegar al resultado final.

## Dónde se usa
Se prefiere en dispositivos con pocos recursos o en aplicaciones de inteligencia artificial móvil.

## Suele confundirse con
Puede confundirse con la arquitectura transformer estándar, pero aquí el número de capas es físicamente menor.

## Preguntas frecuentes
**¿Funciona más lento?**
Dado que reutiliza las capas, puede requerir un poco más de tiempo de procesamiento, pero ahorra memoria.

**¿Por qué no todos los modelos son así?**
Para algunas tareas complejas, es mejor que cada capa esté especializada para obtener mejores resultados.


## Términos relacionados
- [Transformer](/es/dictionary/transformer/)
- [Quantization](/es/dictionary/quantization/)
- [SLM](/es/dictionary/slm/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/looped-transformer/
