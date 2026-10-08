# ¿Qué es Experts Streamed from Disk?

*Glosario · AI · Última actualización: 14 de septiembre de 2026*

Es un método en el que partes de modelos de inteligencia artificial masivos se cargan instantáneamente desde el disco cuando no caben en la memoria.

## Definición

Los modelos de inteligencia artificial a veces son tan grandes que no caben en la capacidad de RAM de la computadora. En esta técnica, solo las partes del modelo que se necesitan en ese momento (los expertos) se leen rápidamente desde el disco y se llevan a la memoria. De esta manera, los modelos muy grandes pueden funcionar incluso en hardware limitado.

***Analogía:** No puedes poner todos los libros de una biblioteca gigante sobre tu escritorio; por eso, solo tomas del estante la página que vas a leer en ese momento y la devuelves cuando terminas.*

## Cómo funciona

El sistema divide los pesos del modelo en partes pequeñas y los almacena en el disco. Cuando un usuario hace una pregunta, las partes relevantes del modelo se transfieren muy rápidamente del disco a la memoria, se procesan y luego se libera la memoria.

## Dónde se usa

Se utiliza especialmente para desarrolladores que desean ejecutar modelos de lenguaje muy grandes en computadoras domésticas y en servidores con limitaciones de hardware.

## Suele confundirse con

Puede confundirse con cargar todo el modelo en la memoria; aquí solo se trata de cargar bajo demanda.

## Preguntas frecuentes

**¿Este método reduce la velocidad?**

Sí, dado que la operación de lectura desde el disco es más lenta que la RAM, puede haber un ligero retraso en el tiempo de respuesta del modelo.

**¿Puede cualquier modelo funcionar de esta manera?**

El modelo debe estar diseñado con esta arquitectura; es decir, es obligatorio que tenga una estructura fragmentada (Mixture of Experts).

## Términos relacionados

- [Mixture of Experts](https://trescout.com/es/dictionary/mixture-of-experts/)
- [RAM](https://trescout.com/es/dictionary/ram/)
- [Inference Engine](https://trescout.com/es/dictionary/inference-engine/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/experts-streamed-from-disk/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/experts-streamed-from-disk/
