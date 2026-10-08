# ¿Qué es Stacked Pull Requests?

*Glosario · Dev · Última actualización: 2 de agosto de 2026*

Es un método para introducir cambios importantes de software en el sistema de forma secuencial en piezas pequeñas y manejables que están interconectadas.

## Definición

Al desarrollar software, en lugar de enviar un gran cambio de una sola vez, se divide este cambio en partes lógicas y se envían una tras otra. Cada pieza se basa en la anterior. De esta manera, las personas que revisan su código pueden aprobar pasos pequeños y específicos más rápidamente, en lugar de intentar comprender una estructura compleja de una vez.

***Analogía:** Es como avanzar enviando cada capítulo al editor a medida que se completa y obteniendo la aprobación, en lugar de escribir un libro de una vez y enviárselo al editor. De esta manera, si cometes un error, sólo tendrás que corregir esa sección, no todo el libro.*

## Cómo funciona

Divida sus cambios en bloques lógicos. Envíe el primer bloque y comience a construir el siguiente encima antes de que se apruebe. Este proceso garantiza que el código permanezca más limpio y que los errores se detecten antes.

## Dónde se usa

Se utiliza en procesos internos de revisión de código del equipo en plataformas como GitHub o GitLab, especialmente cuando se desarrollan funciones de gran tamaño.

## Suele confundirse con

Se puede confundir con una única 'Solicitud de extracción' grande; sin embargo, este método ofrece un enfoque fragmentado y secuencial.

## Preguntas frecuentes

**¿Por qué no lo enviamos todo de una vez?**

Los cambios grandes son más propensos a errores y dificultan que otros revisen el código.

**Si todo está conectado, ¿qué pasa si una parte se rompe?**

Dado que es secuencial, debes gestionar los cambios con cuidado para evitar romper la cadena.

## Términos relacionados

- [Code Review](https://trescout.com/es/dictionary/code-review/)
- [Git Push](https://trescout.com/es/dictionary/git-push/)
- [Checkout](https://trescout.com/es/dictionary/checkout/)

## Herramientas relacionadas

- [Gh Stack](https://trescout.com/es/discover/gh-stack/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/stacked-pull-requests/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/stacked-pull-requests/
