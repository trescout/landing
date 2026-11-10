# ¿Qué es Dense Transformer?

*Inteligencia artificial · Última actualización: 10 de noviembre de 2026*

Es la arquitectura Transformer estándar donde todos sus parámetros están activos en cada paso.

## Definición

El Transformer denso se refiere a la estructura tradicional en la que todas las unidades de cálculo en una capa de un modelo de inteligencia artificial trabajan conjuntamente para cada entrada. A medida que los datos de entrada pasan por el modelo, se activa toda la red, lo que requiere una alta potencia de cálculo. A medida que aumenta la capacidad del modelo, la energía y el tiempo consumidos aumentan en proporción directa.

***Analogía:** Esto es similar a que todos los empleados de una fábrica entren en la línea de producción al mismo tiempo para cada pedido simple que llega.*

## Cómo funciona

Después de que los textos de entrada se tokenizan, pasan por todos los parámetros del modelo simultáneamente mediante multiplicaciones de matrices. Este proceso permite una comprensión profunda de los datos, pero consume intensamente los recursos de hardware. Especialmente en modelos de gran tamaño, esta participación total genera un costo de hardware significativo.

## Dónde se usa

Esta arquitectura es comúnmente preferida en modelos de lenguaje grandes estándar y sistemas básicos de generación de texto.

## Suele confundirse con

A menudo se confunde con la arquitectura Mixture of Experts (MoE), donde solo funciona la parte relevante de los parámetros.

## Preguntas y respuestas

**¿Por qué los modelos Transformer densos son lentos?**

Debido a que toda la red debe trabajar simultáneamente para cada palabra u operación, genera una gran carga sobre el hardware.

**¿En qué áreas se utiliza?**

Sirve como bloque de construcción fundamental en tareas de procesamiento de lenguaje natural de propósito general y en infraestructuras de inteligencia artificial estándar.

## Términos relacionados

- [Transformer](https://trescout.com/es/dictionary/transformer/)
- [Mixture of Experts](https://trescout.com/es/dictionary/mixture-of-experts/)
- [LLM](https://trescout.com/es/dictionary/llm/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/dense-transformer/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/dense-transformer/
