# ¿Qué es ARQ?

*Glosario · Dev · Última actualización: 12 de junio de 2026*

> Automatic Repeat Request

Es un mecanismo de control de errores que garantiza que la información se reenvíe automáticamente cuando ocurre un error durante la transmisión de datos.

## Definición

Al enviar datos a través de Internet, a veces los paquetes pueden perderse o dañarse. ARQ comprueba si el receptor ha recibido los datos y si detecta un error, le dice al remitente 'No recibí esto, envía de nuevo'. De esta forma se asegura que los datos se reciban íntegramente y sin errores.

***Analogía:** Mientras habla por teléfono, la otra parte dice: "No entendí, ¿puedes repetirlo?". Es como decir y repetir esa frase.*

## Cómo funciona

El remitente envía el paquete de datos y espera una confirmación. Si no se recibe la confirmación en un plazo determinado, el paquete se considera dañado o perdido y se envía nuevamente.

## Dónde se usa

Se utiliza en los protocolos básicos y protocolos de red de Internet, como el protocolo TCP.

## Preguntas frecuentes

**¿Por qué es tan importante?**

Las conexiones a Internet no siempre son perfectas; ARQ garantiza la fiabilidad de los datos.

**¿Causará retraso?**

Sí, reenviar paquetes defectuosos puede ralentizar un poco el proceso.

## Términos relacionados

- [API](https://trescout.com/es/dictionary/api/)
- [DNS Tunneling](https://trescout.com/es/dictionary/dns-tunneling/)
- [Computer Science](https://trescout.com/es/dictionary/computer-science/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/arq/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/arq/
