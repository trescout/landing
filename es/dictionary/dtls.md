# ¿Qué es DTLS?

*Desarrollo · Última actualización: 7 de noviembre de 2026*

> Datagram Transport Layer Security

Es un protocolo de comunicación seguro adaptado a situaciones que requieren velocidad y continuidad en la transmisión de datos.

## Definición

DTLS es una versión rediseñada del protocolo TLS, que normalmente opera sobre TCP, para redes como UDP que son continuas pero presentan riesgo de pérdida de paquetes. Minimiza la latencia sin comprometer la seguridad en situaciones donde el flujo de datos en tiempo real es vital.

***Analogía:** Es como enviar documentos valiosos con un servicio de mensajería rápida en moto en lugar de correo postal normal; el orden de los paquetes a veces puede alterarse, pero se gana velocidad.*

## Cómo funciona

Toma las reglas de cifrado y seguridad de la lógica de TLS, pero las flexibiliza para manejar situaciones de pérdida de paquetes o alteración en el orden de los mismos.

## Dónde se usa

Se utiliza en aplicaciones de llamadas de voz y video, juegos en línea y protocolos de transmisión en directo.

## Suele confundirse con

Se confunde con el TLS estándar; la diferencia principal es que uno es seguro pero lento, mientras que el otro es adecuado para el flujo en tiempo real.

## Preguntas y respuestas

**¿Por qué no se utiliza el TLS estándar?**

El TLS estándar no tolera la pérdida de paquetes y provoca interrupciones en las transmisiones en vivo.

**¿En qué tipo de red funciona?**

Generalmente funciona sobre protocolos de red basados en UDP.

## Términos relacionados

- [TLS](https://trescout.com/es/dictionary/tls/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Streaming Applications](https://trescout.com/es/dictionary/streaming-applications/)

## Herramientas relacionadas

- [Openssl](https://trescout.com/es/discover/openssl/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/dtls/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/dtls/
