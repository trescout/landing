# ¿Qué es Stacked Pull Requests?

Es un método para introducir cambios importantes de software en el sistema de forma secuencial en piezas pequeñas y manejables que están interconectadas.

## Definición
Al desarrollar software, en lugar de enviar un gran cambio de una sola vez, se divide este cambio en partes lógicas y se envían una tras otra. Cada pieza se basa en la anterior. De esta manera, las personas que revisan su código pueden aprobar pasos pequeños y específicos más rápidamente, en lugar de intentar comprender una estructura compleja de una vez.

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
- [Code Review](/es/dictionary/code-review/)
- [Git Push](/es/dictionary/git-push/)
- [Checkout](/es/dictionary/checkout/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/stacked-pull-requests/
