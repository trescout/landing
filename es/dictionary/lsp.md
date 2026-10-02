# ¿Qué es LSP?

> Language Server Protocol

LSP (Language Server Protocol) es un protocolo abierto basado en JSON-RPC que proporciona una comunicación estándar entre los editores de código modernos y los motores de análisis de lenguajes de programación.

## 1. Definición y el problema matemático que resuelve: complejidad M × N
Language Server Protocol (LSP) es un protocolo universal desarrollado en 2016 bajo el liderazgo de Microsoft (equipo de VS Code), Red Hat y Codenvy, que hoy en día se ha convertido en la piedra angular de las herramientas de desarrollo.

## 2. ¿Cómo funciona LSP? Arquitectura del protocolo y JSON-RPC 2.0
LSP es un protocolo de mensajería JSON-RPC 2.0 que funciona entre un editor (cliente) y un motor de análisis de lenguaje (servidor), generalmente a través de entrada/salida estándar local (stdin/stdout) o sockets locales (IPC).

## 3. Los Language Servers más utilizados en el ecosistema

## 4. LSP vs DAP vs LSIF / SCIP

## Preguntas frecuentes
**¿Qué significa LSP y cuál es su abreviatura?**
Significa Language Server Protocol (Protocolo de Servidor de Lenguaje). Es un protocolo abierto que estandariza la comunicación entre editores de código y los motores de sintaxis, verificación de tipos y autocompletado de los lenguajes de programación.

**¿Por qué LSP resuelve el problema M × N?**
En el modelo antiguo, para M lenguajes y N editores, era necesario escribir M × N complementos específicos para cada editor. Con LSP, cada lenguaje escribe un solo servidor y cada editor un solo cliente, logrando la fórmula de integración M + N.

**¿Cómo evita LSP que el editor se ralentice?**
El análisis pesado del árbol de sintaxis abstracta (AST) del lenguaje y las resoluciones de tipos se ejecutan en procesos en segundo plano aislados del proceso principal del editor (a través de JSON-RPC); de esta manera, la interfaz nunca se bloquea.

**¿Cuál es la diferencia entre DAP y LSP?**
Mientras que LSP analiza la escritura de código, el autocompletado y los errores de sintaxis, DAP (Debug Adapter Protocol) permite depurar el código paso a paso estableciendo puntos de interrupción (breakpoints) durante el tiempo de ejecución.


## Términos relacionados
- [Agentic Coding Tool](/es/dictionary/agentic-coding-tool/)
- [CLI](/es/dictionary/cli/)
- [Keybindings](/es/dictionary/keybindings/)
- [Code Snippets](/es/dictionary/code-snippets/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Oh My Pi](/es/discover/oh-my-pi/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/lsp/
