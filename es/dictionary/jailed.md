# ¿Qué es Jailed?

*Glosario · Dev · Última actualización: 29 de septiembre de 2026*

Es una situación en la que un programa se ejecuta en un área aislada y restringida, impidiéndole acceder al resto del sistema operativo.

## Definición

Encarcelado se refiere al estado de seguridad en el que un proceso de software solo puede acceder al directorio de archivos, la memoria y los recursos de red para los que está permitido. Esta limitación, aplicada a nivel del sistema operativo, evita que el programa dañe el sistema host o a otros usuarios. Crea una línea de defensa crítica al probar código que no es de confianza o aislar el riesgo de malware.

***Analogía:** Es como dejar que un huésped de la casa se siente solo en la habitación de invitados y cerrar todas las demás puertas, en lugar de permitirle visitar todas las habitaciones.*

## Cómo funciona

El kernel del sistema operativo limita la raíz del proceso y sus llamadas al sistema a restricciones especiales. Aunque el proceso cree que está en el sistema principal, en realidad sólo puede ver un subdirectorio virtual. Si un programa en esta área aislada falla o es atacado, el daño permanece solo en esa área restringida.

## Dónde se usa

Se utiliza ampliamente para separar las acciones del usuario en servidores web, en aplicaciones que ejecutan complementos y en plataformas de ejecución de código en línea.

## Suele confundirse con

Está muy cerca del concepto de sandbox; sin embargo, jail es un término más tradicional que generalmente se centra en el aislamiento del sistema de archivos en sistemas Unix/Linux (como chroot o FreeBSD jail).

## Preguntas frecuentes

**¿Puede un programa encarcelado acceder al sistema principal?**

En circunstancias normales, no. Sin embargo, estos límites pueden excederse si se encuentra una vulnerabilidad a nivel de kernel (vulnerabilidad de jailbreak).

**¿Las tecnologías de contenedores son también cárceles?**

Las estructuras de contenedores modernas (como Docker) son una evolución mucho más avanzada y destacada de la lógica carcelaria tradicional.

## Términos relacionados

- [Sandbox](https://trescout.com/es/dictionary/sandbox/)
- [Containers](https://trescout.com/es/dictionary/containers/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Security Scanner](https://trescout.com/es/dictionary/security-scanner/)

## Herramientas relacionadas

- [Madeira](https://trescout.com/es/discover/madeira/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/jailed/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/jailed/
