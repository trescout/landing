# ¿Qué es Load Balancer?

*Desarrollo · Última actualización: 20 de noviembre de 2026*

Es un enrutador de tráfico que distribuye el tráfico de red entrante entre múltiples servidores, evitando que el sistema colapse y mejorando el rendimiento.

## Definición

Un balanceador de carga (Load Balancer) distribuye de manera equilibrada las solicitudes de los usuarios que llegan a un sitio web o servicio digital hacia un grupo de servidores en segundo plano. Evita que un solo servidor se sobrecargue y, en caso de fallos de hardware, redirige el tráfico instantáneamente a servidores en buen estado. De esta manera, garantiza que su sistema funcione de forma ininterrumpida, rápida y confiable.

***Analogía:** Es similar a un sistema de gestión de turnos en una sucursal bancaria concurrida, que dirige a los clientes a las ventanillas que quedan libres para evitar aglomeraciones frente a una sola ventanilla.*

## Cómo funciona

La solicitud de red del usuario, en lugar de ir directamente al servidor, llega primero al balanceador de carga. El sistema utiliza algoritmos como la distribución secuencial (Round Robin), el menor número de conexiones o el tiempo de respuesta del servidor para dirigir la solicitud al servidor más adecuado. Simultáneamente, verifica el estado de salud de los servidores y elimina automáticamente del flujo de tráfico a aquellos que presentan fallos.

## Dónde se usa

Se utiliza en plataformas de comercio electrónico que sirven a millones de usuarios, en arquitecturas de nube basadas en microservicios y en sistemas financieros que no toleran interrupciones.

## Suele confundirse con

Puede confundirse con un API Gateway. Mientras que el API Gateway se centra en funciones como la autenticación, la transformación de solicitudes y la gestión de API, el balanceador de carga tiene como objetivo principal distribuir el tráfico de manera eficiente entre los servidores.

## Preguntas y respuestas

**¿Es obligatorio utilizar un balanceador de carga?**

No es obligatorio para sitios sencillos con poco tráfico, pero se vuelve indispensable para evitar interrupciones cuando su aplicación crece y un solo servidor ya no es suficiente.

**¿Cuál es la diferencia entre un balanceador de carga por software y uno por hardware?**

Los modelos de hardware son dispositivos físicos especializados que se instalan en centros de datos. Los modelos de software, como NGINX o HAProxy, son programas flexibles que se ejecutan en entornos de nube y servidores estándar.

## Términos relacionados

- [API Gateway](https://trescout.com/es/dictionary/api-gateway/)
- [Reverse Proxy](https://trescout.com/es/dictionary/reverse-proxy/)
- [Microservices](https://trescout.com/es/dictionary/microservices/)
- [Cloud Computing](https://trescout.com/es/dictionary/cloud-computing/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/load-balancer/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/load-balancer/
