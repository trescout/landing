# ¿Qué es Append-only?

Es un método de grabación en el que los datos sólo se pueden agregar, no se pueden cambiar ni eliminar.

## Definición
Al agregar información a una base de datos o archivo, el principio es agregar cada nueva información al final de la lista en lugar de reemplazar datos antiguos. Este método es fundamental para preservar el historial y la seguridad de los datos. Como no se elimina ningún dato, es posible rastrear todos los movimientos en el sistema.

## Cómo funciona
El sistema sólo acepta un comando 'agregar' en lugar de un comando que actualice los datos. De esta forma, siempre se conserva el historial de los datos.

## Dónde se usa
Se utiliza en tecnologías blockchain, sistemas de mantenimiento de registros y bases de datos auditables.

## Suele confundirse con
Puede confundirse con las bases de datos tradicionales; los tradicionales pueden actualizar los datos, este método nunca lo permite.

## Preguntas frecuentes
**¿Qué pasa si cometo un error?**
En lugar de eliminar los datos erróneos, agrega un nuevo registro que corrige el error.

**¿Por qué es tan seguro?**
Como los datos no se pueden cambiar, es casi imposible manipular el pasado.


## Términos relacionados
- [Database](/es/dictionary/database/)
- [Logs](/es/dictionary/logs/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/append-only/
