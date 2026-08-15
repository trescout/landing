# ¿Qué es Durable Objects?

Son pequeñas unidades de software que se ejecutan continuamente en Internet y pueden almacenar datos sin perder su estado.

## Definición
Normalmente, los programas en Internet son temporales, pero estas estructuras funcionan sin interrupción manteniendo los datos dentro de sí mismas. No olvidan los datos incluso cuando finaliza la interacción del usuario. Ideal para mantener la coherencia en sistemas distribuidos.

## Cómo funciona
Viven en el servidor con una identidad específica y procesan cada solicitud entrante con el estado actual en su memoria.

## Dónde se usa
Se utiliza en juegos en tiempo real, aplicaciones de chat y servicios web cuyo estado debe mantenerse.

## Suele confundirse con
No confundir con funciones de servidor temporales (sin servidor); porque siempre empiezan desde cero.

## Preguntas frecuentes
**¿Dónde se almacenan los datos?**
Se almacena dentro del propio volumen, es decir, directamente como parte del entorno operativo.


## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [State Management](/es/dictionary/state-management/)
- [Distributed](/es/dictionary/distributed/)

## Herramientas relacionadas
- [Celld](/es/discover/celld/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/durable-objects/
