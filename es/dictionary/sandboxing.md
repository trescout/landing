# ¿Qué es Sandboxing?

*Glosario · Dev · Última actualización: 3 de octubre de 2026*

Técnica de ejecutar software o código sospechoso en un entorno aislado para evitar que dañe el sistema principal y el entorno.

## Definición

El sandboxing es la práctica de ejecutar fragmentos de código no confiables o en fase de prueba en un área controlada, aislándolos de los recursos del sistema. Este mecanismo limita el acceso directo de la aplicación al sistema de archivos, la red local o el núcleo del sistema operativo. Es una capa de seguridad indispensable para evitar la propagación de vulnerabilidades en el sistema y reducir a cero el impacto del software malicioso.

***Analogía:** Es similar a realizar un experimento químico potencialmente peligroso no en medio de la habitación, sino dentro de una campana de cristal resistente a explosiones.*

## Cómo funciona

Se establece una barrera protegida mediante restricciones a nivel de sistema operativo o herramientas de virtualización. Cuando se ejecuta el código, solo puede utilizar la memoria limitada y el espacio de disco permitidos. Las llamadas al sistema se monitorizan continuamente; cuando se detecta un intento de operación no permitida, el software se detiene de inmediato.

## Dónde se usa

Se utiliza en la ejecución de scripts de terceros en navegadores web, en software de seguridad que analiza archivos sospechosos en archivos adjuntos de correo electrónico y en entornos de desarrollo donde los agentes de inteligencia artificial ejecutan código.

## Suele confundirse con

Mientras que el término sandbox define el área aislada en sí, el sandboxing se refiere al proceso de crear, gestionar y limitar este entorno seguro.

## Preguntas frecuentes

**¿Reduce significativamente el sandboxing el rendimiento del sistema?**

Aunque la supervisión de las llamadas al sistema introduce una ligera carga de procesamiento, en los sistemas operativos modernos esta pérdida suele ser insignificante.

**¿Por qué es necesario el sandboxing en las herramientas de inteligencia artificial?**

Dado que el código generado y ejecutado por los modelos de inteligencia artificial puede conllevar el riesgo de eliminar archivos críticos en el sistema operativo, estas operaciones se llevan a cabo en una capa de aislamiento seguro.

## Términos relacionados

- [Sandbox](https://trescout.com/es/dictionary/sandbox/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Virtual Machines](https://trescout.com/es/dictionary/virtual-machines/)
- [Security Scanner](https://trescout.com/es/dictionary/security-scanner/)

## Herramientas relacionadas

- [Agent Governance Toolkit](https://trescout.com/es/discover/agent-governance-toolkit/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/sandboxing/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/sandboxing/
