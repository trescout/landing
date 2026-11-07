# ¿Qué es Time Series Database?

*Datos e infraestructura · Última actualización: 7 de noviembre de 2026*

Una base de datos especial que almacena los cambios a lo largo del tiempo en orden cronológico.

## Definición

Una base de datos de series temporales es un tipo de base de datos de alta velocidad donde los datos se registran junto con una marca de tiempo y se analizan los cambios en cuestión de segundos. A diferencia de las bases de datos tradicionales, en lugar de actualizar los datos, añade continuamente un nuevo registro temporal en la parte inferior. Está optimizada para supervisar el estado instantáneo de millones de sensores o servidores.

***Analogía:** Es como si un deportista llevara un cuaderno con cronómetro, anotando verticalmente su pulso y velocidad cada segundo durante todo el entrenamiento.*

## Cómo funciona

Los sistemas envían informes de estado a intervalos regulares y esta base de datos escribe dichos informes en su disco ordenados por tiempo. Al realizar consultas, te permite graficar tendencias históricas y cambios instantáneos con gran rapidez.

## Dónde se usa

Se utiliza en herramientas de monitorización del rendimiento de servidores, flujos de datos bursátiles y sistemas de sensores para hogares inteligentes.

## Suele confundirse con

Se puede confundir con las bases de datos relacionales; mientras que las relacionales actualizan los estados instantáneos, estos sistemas acumulan todo el historial a lo largo del tiempo.

## Preguntas y respuestas

**¿Por qué no se utiliza una base de datos normal para esta tarea?**

Las bases de datos normales se ralentizan bajo el peso de enormes acumulaciones de datos con el tiempo, mientras que estos sistemas están diseñados para procesar datos temporales a gran velocidad.

**¿Se borran los datos antiguos?**

Por lo general, después de un cierto período, los datos antiguos se resumen automáticamente o se eliminan del disco.

## Términos relacionados

- [Database](https://trescout.com/es/dictionary/database/)
- [Monitoring Tool](https://trescout.com/es/dictionary/monitoring-tool/)
- [Data Processing](https://trescout.com/es/dictionary/data-processing/)

## Herramientas relacionadas

- [Prometheus](https://trescout.com/es/discover/prometheus/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/time-series-database/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/time-series-database/
