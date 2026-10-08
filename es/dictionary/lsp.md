# ¿Qué es LSP?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

> Language Server Protocol

LSP (Language Server Protocol) es un protocolo abierto basado en JSON-RPC que proporciona una comunicación estándar entre los editores de código modernos y los motores de análisis de lenguajes de programación.

## 1. Definición y el problema matemático que resuelve: complejidad M × N

Language Server Protocol (LSP) es un protocolo universal desarrollado en 2016 bajo el liderazgo de Microsoft (equipo de VS Code), Red Hat y Codenvy, que hoy en día se ha convertido en la piedra angular de las herramientas de desarrollo.

La mayor revolución que aporta LSP es reducir la crisis de complejidad M × N, que el mundo del software ha sufrido durante años, al nivel de M + N:

- Antes de LSP (M × N): Si en el mercado hay 5 editores de código populares (VS Code, Neovim, Sublime Text, Emacs, Eclipse) y 10 lenguajes de programación populares (Python, Rust, Go, TypeScript, C++, etc.), para proporcionar autocompletado y verificación de sintaxis en cada lenguaje, era necesario escribir y actualizar por separado 5 × 10 = 50 complementos diferentes.
- Post-LSP (M + N): Cada comunidad lingüística escribe un único "Language Server" (Servidor de lenguaje); cada desarrollador de editores integra solo un "LSP Client" (Cliente). Resultado: 5 + 10 = 15 componentes. Un lenguaje de programación recién lanzado, al escribir un único servidor LSP, funciona a la perfección desde el primer día en todos los editores del mercado.

***Analogía:** LSP es el intérprete simultáneo entre expertos locales que hablan todos los idiomas del mundo con las reglas de su propio país y una asamblea diplomática internacional que escucha a estos expertos; sin importar quién sea el editor en la asamblea, el mensaje se transmite perfectamente.*

## 2. ¿Cómo funciona LSP? Arquitectura del protocolo y JSON-RPC 2.0

LSP es un protocolo de mensajería JSON-RPC 2.0 que funciona entre un editor (cliente) y un motor de análisis de lenguaje (servidor), generalmente a través de entrada/salida estándar local (stdin/stdout) o sockets locales (IPC).

Las operaciones pesadas de análisis semántico y resolución de tipos se ejecutan en un proceso del sistema operativo separado del hilo principal del editor (hilo de UI); de esta manera, su editor nunca se congela ni se bloquea, incluso en proyectos de 100 mil líneas.

```
   Editör (LSP Client)                   Dil Sunucusu (Language Server)
          │                                            │
          │─────── textDocument/didOpen ──────────────>│ (Dosya açıldı, AST kurulur)
          │─────── textDocument/didChange ───────────>│ (Kullanıcı harf yazdı, artımlı senk.)
          │<────── textDocument/publishDiagnostics ────│ (Kırmızı dalgalı alt çizgi / Hatalar)
          │                                            │
          │─────── textDocument/completion ───────────>│ (Ctrl+Space: Öneriler istendi)
          │<────── CompletionItem[] ───────────────────│ (Metot ve değişken listesi döner)
          │                                            │
          │─────── textDocument/definition ───────────>│ (F12: Tanıma git / Go to definition)
          │<────── Location (Dosya, Satır, Sütun) ────│ (İlgili kaynak kod konumu açılır)
```

1. Inicialización (initialize): Cuando se inicia el editor, este notifica al servidor sus capacidades (client capabilities); a su vez, el servidor confirma qué características admite (server capabilities).
2. Sincronización de documentos (didChange): A medida que el usuario escribe código, solo se transfieren al servidor las líneas y los rangos de caracteres modificados (sincronización incremental de documentos) en lugar del archivo completo.
3. Diagnóstico (publishDiagnostics): El servidor de lenguaje actualiza el Árbol de Sintaxis Abstracta (AST) y la tabla de tipos en segundo plano sin compilar el código. Si hay errores, envía líneas de error rojas al editor como una notificación asíncrona.
4. Solicitudes enriquecidas (hover, autocompletado, renombrado): cuando el usuario coloca el cursor sobre una función o realiza un renombrado, el servidor calcula todas las referencias en el proyecto y devuelve una respuesta.

## 3. Los Language Servers más utilizados en el ecosistema

- Rust: rust-analyzer (Inferencia de tipos, expansiones de macros y advertencias del borrow checker extraordinariamente rápidas)
- Python: pyright / basedpyright / ruff (Verificación de tipos estáticos y linting a velocidad de microsegundos con Ruff)
- Go: gopls (desarrollado por el equipo oficial de Go, un servidor con reconocimiento de módulos y paquetes)
- TypeScript / JS: vtsls / typescript-language-server (IntelliSense y refactorización)
- C / C++: clangd (basado en LLVM, precisión superior en proyectos grandes con compile_commands.json)
- Lua: lua-language-server (anotaciones de tipo personalizadas para desarrolladores de complementos de Neovim)

## 4. LSP vs DAP vs LSIF / SCIP

- LSP (Language Server Protocol): Gestiona las funciones inteligentes dinámicas durante la escritura de código (autocompletado, detección de errores, formato).
- DAP (Debug Adapter Protocol): Gestiona las operaciones de depuración en tiempo de ejecución. Los puntos de interrupción (breakpoints), el seguimiento de variables y la ejecución paso a paso se comunican a través de DAP.
- SCIP / LSIF: Son formatos de indexación estática que permiten preindexar bases de código extensas en tiempo de compilación, facilitando la navegación por el código en interfaces web sin necesidad de ejecutar un servidor.

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

- [Agentic Coding Tool](https://trescout.com/es/dictionary/agentic-coding-tool/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Keybindings](https://trescout.com/es/dictionary/keybindings/)
- [Code Snippets](https://trescout.com/es/dictionary/code-snippets/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)

## Herramientas relacionadas

- [Oh My Pi](https://trescout.com/es/discover/oh-my-pi/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/lsp/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/lsp/
