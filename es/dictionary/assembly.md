# Assembly Definición, registros y arquitectura de sistemas

Assembly representa dos conceptos fundamentales en ciencias de la computación: el lenguaje simbólico de más bajo nivel que controla directamente el procesador (CPU), y los paquetes compilados de despliegue (.NET assemblies).

## 1. Lenguaje de Bajo Nivel (Assembly Language)
La CPU procesa exclusivamente código máquina binario (opcodes). El lenguaje assembly convierte estas instrucciones binarias en nemónicos comprensibles por desarrolladores:

## 2. Registros de CPU y Arquitectura x86-64
En los procesadores modernos de 64 bits x86-64 encontramos registros dedicados y de propósito general:

## 3. CISC vs RISC: Comparativa entre x86-64 y ARM64
La arquitectura x86-64 implementa la filosofía CISC (conjunto complejo de instrucciones) con instrucciones de longitud variable. En cambio, ARM64 (Apple Silicon, chips móviles) adopta RISC (conjunto reducido de instrucciones) con comandos fijos de 32 bits y arquitectura Load-Store, destacando en eficiencia energética.

## 4. Llamadas al Sistema (Syscalls) y Ejemplo Linux x86-64

## 5. .NET Assembly y WebAssembly (WASM)

## Preguntas frecuentes
**¿Qué significa Assembly y para qué se utiliza?**
Es el lenguaje de programación más cercano al hardware físico, asignando nemónicos directamente a instrucciones de procesador para sistemas operativos y drivers.

**¿Cuál es la diferencia entre un ensamblador y un compilador?**
Un compilador traduce estructuras complejas de alto nivel a código máquina; un ensamblador solo mapea nemónicos simbólicos directamente a secuencias binarias fijas.

**¿Dónde se sigue usando Assembly en la actualidad?**
En cargadores de arranque (bootloaders), microcontroladores embebidos, ingeniería inversa de seguridad y módulos de alto rendimiento.


## Términos relacionados
- [Memory Management](/es/dictionary/memory-management/)
- [Runtime](/es/dictionary/runtime/)
- [Compilation](/es/dictionary/compilation/)
- [Apple Silicon](/es/dictionary/apple-silicon/)
- [Emulator](/es/dictionary/emulator/)

## Herramientas relacionadas
- [Apollo-11](/es/discover/apollo-11/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/assembly/
