# ¿Qué es I/O?

> Input/Output

I/O (Input/Output, entrada/salida) es el intercambio de datos de un sistema con el mundo exterior.

## Definición y origen de la palabra
La entrada de teclado, un archivo descargado, el resultado impreso en pantalla: todo es una operación de E/S. El sistema se comunica con el mundo exterior a través de este canal. Es como los sentidos y las manos de la computadora.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Teclado: Entrada de texto.Red: Descarga de archivos.Pantalla: Mostrar resultados.

## Profundidad técnica y arquitectura
Conceptos:

## Uso en diferentes disciplinas
Humano: Entrada por ojos y oídos, salida por voz.Restaurante: Entrada de pedidos, salida de servicio.Fábrica: Entrada de materia prima, salida de producto.

## Preguntas frecuentes
**¿Por qué la E/S es un cuello de botella?**
El procesador es rápido, el disco y la red son lentos. Cuando los datos no llegan a tiempo, el sistema espera, aquí es donde se forma el cuello de botella.

**¿Qué es el bloqueo (blocking)?**
Es una llamada que espera hasta que llega el resultado. Bloquea la interfaz y desperdicia trabajo en el servidor.

**¿Cómo se acelera?**
Con caché, lectura por lotes y llamadas asíncronas. Primero se mide, luego se corrige el eslabón más débil.

**¿Qué tiene que ver el asíncrono?**
Es el mecanismo para hacer otros trabajos durante la espera. Se manejan muchas tareas con un solo hilo.


## Términos relacionados
- [API](/es/dictionary/api/)
- [Data Pipeline](/es/dictionary/data-pipeline/)
- [Streaming Applications](/es/dictionary/streaming-applications/)

## Herramientas relacionadas
- [Asio](/es/discover/asio/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/io/
