# Assembly: Definición, registros y arquitectura de sistemas

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

Assembly representa dos conceptos fundamentales en ciencias de la computación: el lenguaje simbólico de más bajo nivel que controla directamente el procesador (CPU), y los paquetes compilados de despliegue (.NET assemblies).

## 1. Lenguaje de Bajo Nivel (Assembly Language)

La CPU procesa exclusivamente código máquina binario (opcodes). El lenguaje assembly convierte estas instrucciones binarias en nemónicos comprensibles por desarrolladores:

- `MOV`: Transfiere información entre registros o posiciones de memoria.
- `ADD` / `SUB`: Ejecuta operaciones de suma y resta aritmética.
- `PUSH` / `POP`: Inserta y extrae datos de la pila de llamadas (call stack).
- `JMP` / `JE` / `JNE`: Altera el flujo de ejecución evaluando banderas de estado.

El código fuente se compila a código de máquina mediante ensambladores directos (nasm, gas) sin necesidad de entornos virtuales intermedios.

## 2. Registros de CPU y Arquitectura x86-64

En los procesadores modernos de 64 bits x86-64 encontramos registros dedicados y de propósito general:

- **Registros de Propósito General:** `RAX` (acumulador y valor de retorno), `RBX` (registro base), `RCX` (contador de bucles), `RDX` (datos de E/S), `RDI` y `RSI` (índices destino y origen).
- **Registros Especializados:** `RSP` (puntero de pila), `RBP` (puntero base del marco), `RIP` (puntero a la siguiente instrucción) y `RFLAGS` (banderas de desbordamiento, signo y cero).

## 3. CISC vs RISC: Comparativa entre x86-64 y ARM64

La arquitectura x86-64 implementa la filosofía **CISC** (conjunto complejo de instrucciones) con instrucciones de longitud variable. En cambio, ARM64 (Apple Silicon, chips móviles) adopta **RISC** (conjunto reducido de instrucciones) con comandos fijos de 32 bits y arquitectura Load-Store, destacando en eficiencia energética.

## 4. Llamadas al Sistema (Syscalls) y Ejemplo Linux x86-64

```
section .text
global _start

_start:
    ; 1. Escribir en salida estándar (sys_write = syscall 1)
    mov rax, 1          ; número syscall: 1 (sys_write)
    mov rdi, 1          ; descriptor: 1 (stdout)
    mov rsi, msg        ; puntero a memoria del mensaje
    mov rdx, 14         ; tamaño en bytes
    syscall             ; salto al kernel

    ; 2. Finalizar programa (sys_exit = syscall 60)
    mov rax, 60         ; número syscall: 60 (sys_exit)
    xor rdi, rdi        ; código de salida 0
    syscall

section .data
    msg db "¡Hola, mundo!", 10
```

## 5. .NET Assembly y WebAssembly (WASM)

- **.NET Assembly:** Conjunto empaquetado de código binario intermedio CIL y metadatos distribuido como archivos `.dll` o `.exe`.
- **WebAssembly (WASM):** Formato binario portable ejecutado en el navegador web con aislamiento de memoria y velocidad cercana al código nativo.

*El lenguaje ensamblador es similar a colocar cada diminuto engranaje y espiral de un reloj mecánico con pinzas bajo lupa: entrega control y velocidad absolutos, pero exige extrema meticulosidad.*

## Preguntas frecuentes

**¿Qué significa Assembly y para qué se utiliza?**

Es el lenguaje de programación más cercano al hardware físico, asignando nemónicos directamente a instrucciones de procesador para sistemas operativos y drivers.

**¿Cuál es la diferencia entre un ensamblador y un compilador?**

Un compilador traduce estructuras complejas de alto nivel a código máquina; un ensamblador solo mapea nemónicos simbólicos directamente a secuencias binarias fijas.

**¿Dónde se sigue usando Assembly en la actualidad?**

En cargadores de arranque (bootloaders), microcontroladores embebidos, ingeniería inversa de seguridad y módulos de alto rendimiento.

## Términos relacionados

- [Memory Management](https://trescout.com/es/dictionary/memory-management/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Compilation](https://trescout.com/es/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/es/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/es/dictionary/emulator/)

## Herramientas relacionadas

- [Apollo-11](https://trescout.com/es/discover/apollo-11/)

Esta explicación se redactó en lenguaje llano para TreScout y se **tradujo automáticamente** a partir del original en turco · la versión en turco es la que prevalece. Si detecta algún error o carencia, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/assembly/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/assembly/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/assembly/
