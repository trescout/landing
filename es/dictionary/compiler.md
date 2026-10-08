# ¿Qué es Compiler?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Un compilador (derleyici en turco) es un programa que traduce el código que escribes al lenguaje máquina que el ordenador puede ejecutar.

## Definición y origen de la palabra

"Compile" significa compilar, recopilar. Los ordenadores solo entienden secuencias de 0 y 1. Los desarrolladores, en cambio, escriben en un lenguaje legible. El compilador actúa como traductor entre estos dos mundos: analiza el código y, si no hay errores, lo convierte en un archivo ejecutable.

***Analogía:** Es como convertir una receta escrita en inglés en instrucciones escritas para un chef que no habla nada de inglés, en un idioma que pueda entender.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Instalación de aplicaciones:** La versión compilada del programa que descargaste se ejecuta.
**Mensajes de error:** El compilador te advierte cuando olvidas un punto y coma.
**Motores de juegos:** Una salida de compilación separada para cada plataforma.

## Profundidad técnica y arquitectura

La compilación pasa por cuatro etapas:

**Análisis léxico y sintáctico:** El código se divide en fragmentos y se extrae la estructura de las oraciones.
**Control semántico:** Se buscan variables no definidas e incompatibilidades de tipos.
**Optimización:** Se genera código equivalente pero más rápido.
**Generación de código:** Se escribe código máquina específico para el procesador.

La compilación en el lenguaje C es la siguiente:

```
gcc merhaba.c -o merhaba
./merhaba
```

La primera línea compila, la segunda ejecuta. El intérprete (interpreter), por su parte, se ejecuta línea por línea y no produce un archivo de salida independiente.

## Uso en diferentes disciplinas

**Interpretación:** La distinción entre traducción simultánea (intérprete) y traducción escrita (compilador).
**Imprenta:** La conversión del borrador en una placa de impresión.
**Cocina:** La transformación de la receta en un plato preparado.

## Preguntas frecuentes

**¿Es diferente el compilador de cada idioma?**

Sí. Cada lenguaje requiere un compilador o intérprete de acuerdo con sus propias reglas. Algunos lenguajes utilizan ambos juntos.

**¿Cuál es la diferencia con un intérprete?**

El compilador traduce el código de antemano y genera un archivo, por lo que el programa se ejecuta rápidamente después. El intérprete traduce y ejecuta línea por línea, es flexible pero generalmente lento.

**¿Qué es JIT?**

La compilación Just-in-time traduce las secciones de uso frecuente a código de máquina mientras se ejecuta. Es un término medio entre ambos, utilizado por Java y JavaScript.

**¿Quién compiló el primer compilador?**

Es la pregunta del huevo y la gallina. Los primeros compiladores se escribieron a mano en código de máquina, y los siguientes se compilaron con el compilador anterior (bootstrapping).

## Términos relacionados

- [Rust](https://trescout.com/es/dictionary/rust/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Compile-time](https://trescout.com/es/dictionary/compile-time/)

## Herramientas relacionadas

- [Llvm Project](https://trescout.com/es/discover/llvm-project/)
- [SWC](https://trescout.com/es/discover/swc/)
- [FMT](https://trescout.com/es/discover/fmt/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/compiler/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/compiler/
