# ¿Qué es I/O?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

> Input/Output

I/O (Input/Output, entrada/salida) es el intercambio de datos de un sistema con el mundo exterior.

## Definición y origen de la palabra

La entrada de teclado, un archivo descargado, el resultado impreso en pantalla: todo es una operación de E/S. El sistema se comunica con el mundo exterior a través de este canal. Es como los sentidos y las manos de la computadora.

***Analogía:** Es como que una persona reciba información del mundo exterior y responda a él; los ojos son la entrada y el habla es la salida.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Teclado:** Entrada de texto.
**Red:** Descarga de archivos.
**Pantalla:** Mostrar resultados.

## Profundidad técnica y arquitectura

Conceptos:

**Bloqueante (Blocking):** Esperar hasta que finalice la operación.
**No bloqueante (Non-blocking):** Continuar sin esperar, avísame cuando llegue el resultado.
**Búfer:** Almacenamiento intermedio que equilibra la diferencia de velocidad.
**Cuello de botella:** El eslabón más lento ralentiza toda la línea, por lo general es el disco o la red.

Ejemplo de lectura de archivos:

```
const veri = await fs.readFile("not.txt", "utf8");
```

Esta línea no espera a que llegue el archivo, las demás tareas continúan. Se continúa cuando el resultado está listo.

## Uso en diferentes disciplinas

**Humano:** Entrada por ojos y oídos, salida por voz.
**Restaurante:** Entrada de pedidos, salida de servicio.
**Fábrica:** Entrada de materia prima, salida de producto.

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

- [API](https://trescout.com/es/dictionary/api/)
- [Data Pipeline](https://trescout.com/es/dictionary/data-pipeline/)
- [Streaming Applications](https://trescout.com/es/dictionary/streaming-applications/)

## Herramientas relacionadas

- [Asio](https://trescout.com/es/discover/asio/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/io/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/io/
