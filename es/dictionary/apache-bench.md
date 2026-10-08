# ¿Qué es ApacheBench (ab)?

*Glosario · Dev · Última actualización: 29 de septiembre de 2026*

> Apache HTTP Server Benchmarking Tool

Es una herramienta de línea de comandos que mide el rendimiento y los límites de los servidores web bajo un intenso tráfico de solicitudes simultáneas.

## Definición

ApacheBench (ab) es una herramienta de medición de rendimiento liviana y popular que se utiliza para probar cuántas solicitudes pueden manejar los servidores web en un período de tiempo determinado. Informa la capacidad de respuesta del sistema iniciando cientos de conexiones simultáneas con un solo comando desde la línea de comando. Ayuda a los desarrolladores a verificar las configuraciones del servidor y las optimizaciones del código.

***Analogía:** Es como enviar 500 clientes a la puerta de una tienda al mismo tiempo y medir con un cronómetro cuántas personas pueden cortar los cajeros por minuto y cuánto se alarga la cola.*

## Cómo funciona

El usuario determina la dirección de destino a probar a través del terminal, el número total de solicitudes y la cantidad de conexiones (concurrencia) a abrir simultáneamente. La herramienta reenvía rápidamente las solicitudes identificadas al servidor, recopila tiempos de respuesta y presenta métricas básicas, como solicitudes por segundo (RPS), en forma de tabla.

## Dónde se usa

Se utiliza en pruebas de carga antes del lanzamiento del sitio web, en comparaciones de hardware del servidor y para medir el éxito de las optimizaciones de la caché.

## Suele confundirse con

A diferencia de las herramientas avanzadas de prueba de carga que simulan escenarios de usuario complejos, se centra únicamente en la carga de carga secuencial o simultánea en una conexión HTTP específica.

## Preguntas frecuentes

**¿Se requiere el servidor web Apache para utilizar ApacheBench?**

No. Se puede ejecutar de forma independiente para probar Nginx, Node.js o cualquier servidor HTTP.

**¿Qué valor se mira más en los resultados de las pruebas?**

La cantidad de solicitudes completadas por segundo (Solicitudes por segundo) y los tiempos de demora de respuesta en milisegundos son los indicadores más críticos.

## Términos relacionados

- [Benchmark](https://trescout.com/es/dictionary/benchmark/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Concurrency](https://trescout.com/es/dictionary/concurrency/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)

## Herramientas relacionadas

- [HEY](https://trescout.com/es/discover/hey/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/apache-bench/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/apache-bench/
