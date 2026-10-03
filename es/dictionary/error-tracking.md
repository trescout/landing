# ¿Qué es Error Tracking?

El proceso de seguimiento que captura, agrupa y notifica a los desarrolladores en tiempo real los errores de ejecución que ocurren en las aplicaciones.

## Definición
El seguimiento de errores es un enfoque de monitorización que registra automáticamente los bloqueos y situaciones inesperadas que encuentran los usuarios en el software en producción. El sistema documenta paso a paso la fuente del error, los detalles del sistema operativo y las acciones del usuario que desencadenaron el fallo. De este modo, los equipos de software tienen la oportunidad de intervenir antes de que los problemas sean reportados por los usuarios.

## Cómo funciona
Una pequeña biblioteca de monitorización integrada en la aplicación escucha todas las excepciones de software no controladas. Cuando ocurre un fallo, el seguimiento de la pila (stack trace) y los datos ambientales se empaquetan y se envían al servidor de análisis. El servidor recopila errores similares bajo un mismo techo y envía notificaciones a los desarrolladores por correo electrónico o mensaje instantáneo.

## Dónde se usa
Se prefiere activamente en aplicaciones móviles donde la experiencia del usuario es crítica, en proyectos web de página única (SPA) y en arquitecturas de microservicios que se ejecutan en el backend.

## Suele confundirse con
Es diferente del concepto de registro (logging), que almacena todos los eventos del sistema cronológicamente: el seguimiento de errores se centra directamente en las excepciones y analiza y agrupa automáticamente estos problemas.

## Preguntas frecuentes
**¿Las herramientas de seguimiento de errores guardan los datos confidenciales de los usuarios?**
Los sistemas correctamente configurados filtran y enmascaran automáticamente los datos personales como contraseñas o tarjetas de crédito antes de enviarlos al servidor.

**¿Se pierde el informe de errores cuando la aplicación se cierra repentinamente?**
No, la información recopilada en el momento del bloqueo se escribe en la memoria local del dispositivo y se transmite al centro cuando la aplicación se vuelve a abrir.


## Términos relacionados
- [Logging](/es/dictionary/logging/)
- [Observability](/es/dictionary/observability/)
- [Traces](/es/dictionary/traces/)
- [QA](/es/dictionary/qa/)
- [Session Replay](/es/dictionary/session-replay/)

## Herramientas relacionadas
- [Sentry](/es/discover/sentry/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/error-tracking/
