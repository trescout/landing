# ¿Qué es Shellcode?

*Desarrollo · Última actualización: 24 de octubre de 2026*

Es un código de máquina de pequeño tamaño que permite obtener acceso a la línea de comandos o ejecutar comandos personalizados en una máquina objetivo aprovechando las vulnerabilidades de los sistemas.

## Definición

Este fragmento de código especial, utilizado en el mundo de la ciberseguridad y en las pruebas de penetración, se inyecta directamente en la memoria del sistema. Históricamente, recibe su nombre de su objetivo de abrir una shell de comandos en el sistema objetivo. Hoy en día, está diseñado no solo para abrir una shell de comandos, sino para ejecutar cualquier tipo de instrucción personalizada deseada en el sistema.

***Analogía:** Se puede comparar con una pequeña tarjeta de acceso que se desliza secretamente a través de la puerta cerrada de un edificio para tomar el control del panel de control de la sala de seguridad.*

## Cómo funciona

Los investigadores de seguridad o los atacantes detectan vulnerabilidades en el software, como el desbordamiento de memoria (buffer overflow). Luego, colocan el pequeño código de máquina que han preparado en la memoria en forma de una secuencia de bytes que el procesador puede entender directamente. Cuando el procesador ejecuta estos comandos, se obtiene un control no autorizado sobre el sistema objetivo.

## Dónde se usa

Aparece en análisis de seguridad, pruebas de penetración y análisis de malware.

## Suele confundirse con

No debe confundirse con los scripts de shell. Mientras que los scripts de shell son códigos de alto nivel basados en texto, este concepto es un código binario de bytes que se ejecuta directamente a nivel de procesador.

## Preguntas y respuestas

**¿El shellcode se utiliza solo con fines maliciosos?**

Los expertos en seguridad también utilizan estos códigos para probar la resistencia defensiva de los sistemas y cerrar vulnerabilidades.

**¿Por qué estos fragmentos de código se escriben con un tamaño tan pequeño?**

Se diseñan lo más pequeños posible para poder infiltrarse en áreas restringidas de la memoria y ejecutarse sin ser detectados por los filtros de seguridad.

## Términos relacionados

- [Exploit](https://trescout.com/es/dictionary/exploit/)
- [Penetration Testing](https://trescout.com/es/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/es/dictionary/vulnerability-scanning/)
- [Backdoor](https://trescout.com/es/dictionary/backdoor/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/shellcode/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/shellcode/
