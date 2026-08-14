# ¿Qué es Vector Database?

Es un tipo especial de base de datos donde la inteligencia artificial almacena datos para poder encontrarlos rápidamente en función de su significado.

## Definición
Una base de datos vectorial es un sistema de almacenamiento especial que almacena datos como vectores numéricos que representan su significado, en lugar de filas y columnas tradicionales. Esta estructura permite a la inteligencia artificial encontrar los datos más relevantes entre millones de datos en milisegundos.

## Cómo funciona
Primero, los datos se convierten en vectores numéricos mediante el método de incrustación. Cuando se realiza una consulta, la base de datos mide la distancia entre el vector de la consulta y los vectores de los datos. Aquellos con la distancia más corta, es decir, los más cercanos en significado, se devuelven como resultados.

## Dónde se usa
Se utiliza en sistemas de búsqueda inteligentes, motores de recomendación y sistemas RAG donde la inteligencia artificial crea memoria a largo plazo.

## Suele confundirse con
Se confunde con las bases de datos clásicas como SQL, pero las bases de datos clásicas buscan coincidencias exactas mientras que las bases de datos vectoriales buscan similitudes.

## Preguntas frecuentes
**¿Es más lento que las bases de datos clásicas?**
No, es mucho más rápido que los métodos clásicos para búsquedas de similitudes en conjuntos de datos muy grandes.

**¿Qué datos se pueden almacenar?**
Se puede almacenar cualquier dato cuyo significado pueda convertirse en vector, como texto, imagen, audio o vídeo.


## Términos relacionados
- [Embedding](/es/dictionary/embedding/)
- [RAG](/es/dictionary/rag/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/vector-database/
