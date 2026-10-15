# ¿Qué es Borrow Checker?

*Dev · Última actualización: 13 de octubre de 2026*

Mecanismo que evita que los programas escritos en Rust cometan errores de memoria y controla cómo se utilizan los datos.

## Definición

El borrow checker es una de las partes más importantes del compilador de Rust y garantiza el uso seguro de la memoria. Examina meticulosamente si más de un lugar interfiere con los mismos datos al mismo tiempo en el código que escribes y si la vida útil de los datos es suficiente. Cuando encuentra una situación que no cumple con la regla de seguridad, no permite que el programa se ejecute y te advierte.

***Analogía:** Es un registro de seguimiento estricto en un laboratorio sensible que garantiza que solo un investigador a la vez pueda tomar prestado un equipo especial y devolverlo cuando termine su trabajo.*

## Cómo funciona

Se activa en segundo plano cuando intentas compilar tu código. Observa las reglas de propiedad de las variables y los tiempos de préstamo. Si detecta un uso compartido de datos que infringe las reglas, detiene la compilación y muestra dónde está el error.

## Dónde se usa

En la programación de sistemas, opera activamente durante la fase de compilación en proyectos de Rust que desean prevenir fugas de memoria y bloqueos desde el principio.

## Suele confundirse con

Es diferente de los depuradores normales; no se ejecuta mientras el programa está en marcha, sino mientras el código se escribe y se compila.

## Preguntas frecuentes

**¿Por qué es tan estricto?**

Toma medidas en una etapa temprana para eliminar por completo los fallos de memoria en tiempo de ejecución.

**¿Hace que funcione lento?**

No, solo funciona en la fase de compilación y no genera un costo adicional en tiempo de ejecución.

## Términos relacionados

- [Rust](https://trescout.com/es/dictionary/rust/)
- [Compiler](https://trescout.com/es/dictionary/compiler/)
- [Thread-safety](https://trescout.com/es/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/es/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/es/dictionary/memory-management/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/borrow-checker/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/borrow-checker/
