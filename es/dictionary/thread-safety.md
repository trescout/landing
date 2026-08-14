# ¿Qué es Thread-safety?

Una característica de seguridad de un programa que evita que los datos se dañen al realizar múltiples operaciones al mismo tiempo.

## Definición
Las computadoras hacen muchas cosas a la vez. Si dos procesos diferentes intentan cambiar los mismos datos al mismo tiempo, se producirá el caos. Esta característica permite que los procesos se esperen unos a otros o se ejecuten secuencialmente.

## Cómo funciona
Las reglas de acceso a los datos se determinan mientras se escribe el programa. Mientras que un proceso utiliza los datos, los demás parecen tener un estado "bloqueado".

## Dónde se usa
Es obligatorio para aplicaciones bancarias, servidores web y todo el software multitarea.

## Suele confundirse con
No se trata sólo de seguridad (piratería), sino de coherencia de los datos.

## Preguntas frecuentes
**¿Qué sucede si no es seguro para subprocesos?**
Sus datos se estropean, las aplicaciones fallan o se producen errores de cálculo.


## Términos relacionados
- [Concurrency](/es/dictionary/concurrency/)
- [System Programming Language](/es/dictionary/system-programming-language/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/thread-safety/
