# ¿Qué es Emitter?

Emitter (emisor) es un término crítico en la ingeniería de software que aparece en dos áreas fundamentales: el mecanismo que anuncia cambios de estado a los oyentes en arquitecturas orientadas a eventos (Event-Driven Architecture) (Event Emitter) y el módulo de generación de código que convierte el código analizado en lenguaje de máquina objetivo o bytecode en la tecnología de compiladores (Compiler) (Code Emitter).

## Origen conceptual: De la física a la arquitectura de software
La palabra "emitter" deriva del verbo latino emittere, que significa "lanzar hacia afuera, dejar salir". En electrónica, se denomina emitter a los cátodos que emiten electrones, o en telecomunicaciones, a los transmisores de radio que emiten señales. El mundo del software ha tomado prestado este término con el significado de "una fuente que transfiere al mundo exterior un estado que se produce en ella o un resultado que genera".

## 1. Arquitectura orientada a eventos y Event Emitter
En la programación basada en eventos, el Emitter es el corazón de los patrones de diseño Observer (Observador) y Publish-Subscribe (Publicar-Suscribir). Permite que los componentes del sistema se comuniquen a través de eventos (acoplamiento débil) en lugar de conocerse directamente entre sí (acoplamiento fuerte).

## 2. Code Emitter (Generador de código) en la arquitectura del compilador
La etapa final y más crucial de un compilador o transpilador es la capa del Emitter (generador de código). La cadena de compilación funciona en el siguiente orden: Código fuente → Lexer (tokens) → Parser (árbol de sintaxis abstracta - AST) → Análisis semántico → Optimización → Emitter → Código destino

## Preguntas frecuentes
**¿Qué significa Emitter y cuál es su equivalente en turco?**
Emitter significa "emisor" o "transmisor" en inglés. En software, generalmente se utiliza como "emisor de eventos" (event emitter) o en compiladores como "generador/emisor de código" (code emitter).

**¿Cuál es la mayor ventaja de usar un Event Emitter?**
Reduce el acoplamiento (coupling) entre componentes a cero. Un módulo lanza un evento; no le importa quién, cuándo ni cómo procesa el evento. Esto aumenta la modularidad y la capacidad de prueba.

**¿Qué función cumple el Emitter en los compiladores?**
Es el componente final que toma la estructura de árbol optimizada (AST) tras analizar el código fuente y genera la salida de destino (ensamblador, código máquina, código de bytes o código fuente transformado).

**¿Cuál es la diferencia entre un Observable de RxJS y un Event Emitter?**
Un Event Emitter generalmente realiza una difusión múltiple (multicast) y se utiliza para notificaciones de eventos instantáneos. Por otro lado, un Observable de RxJS ofrece el poder de transformar flujos de datos enriquecidos a lo largo del tiempo (streams) mediante operadores funcionales como filtrado, mapeo y retraso.


## Términos relacionados
- [Parser](/es/dictionary/parser/)
- [Compiler](/es/dictionary/compiler/)
- [Runtime](/es/dictionary/runtime/)
- [Assembly](/es/dictionary/assembly/)
- [API](/es/dictionary/api/)
- [Bundler](/es/dictionary/bundler/)

## Herramientas relacionadas
- [YAML Cpp](/es/discover/yaml-cpp/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/emitter/
