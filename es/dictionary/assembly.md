# ¿Qué es Assembly?

El ensamblaje se refiere a dos conceptos básicos en informática: primero, el lenguaje de programación simbólico de nivel más bajo (lenguaje ensamblador) que gobierna directamente el procesador de hardware (CPU); El segundo es convertir los módulos de software compilados (ensamblaje .NET) en un único paquete distribuible.

## 1. Lenguaje de programación de bajo nivel (lenguaje ensamblador)
El procesador de la computadora solo entiende las señales binarias 0 y 1 (código de máquina/códigos de operación). El lenguaje ensamblador consta de abreviaturas simbólicas (mnemotécnicas) legibles por humanos correspondientes a estos códigos de máquina sin procesar:

## 2. Registros del procesador y arquitectura x86-64
Los registros más críticos en un procesador x86-64 moderno de 64 bits son:

## 3. CISC vs RISC: diferencia entre x86-64 y ARM64
La arquitectura x86-64 funciona con la filosofía CISC (Conjunto de instrucciones complejas); Tiene tamaños de instrucción variables e instrucciones ricas que pueden operar directamente en la memoria. ARM64 (Apple Silicon, Mobile) se basa en RISC (conjunto de instrucciones reducido); Proporciona una gran superioridad en eficiencia energética con su longitud de comando fija de 32 bits y su arquitectura Load-Store.

## 4. Llamadas al sistema (Syscall) y ejemplo de Linux x86-64

## 5. Ensamblaje .NET y ensamblaje web (WASM)

## Preguntas frecuentes
**¿Qué significa asamblea y para qué sirve?**
El ensamblador es el lenguaje de programación simbólico de nivel más bajo que corresponde 1 a 1 al conjunto de instrucciones de hardware del procesador de la computadora. Se utiliza para controlar directamente los registros y la memoria de la CPU.

**¿Cuál es la diferencia entre ensamblador y compilador?**
El compilador (C, C++, Rust) analiza, optimiza y traduce lógica humana compleja y bucles en código de máquina. Assembler, por otro lado, convierte las instrucciones ensambladoras, que ya son versiones simbólicas del código de máquina, directamente en código de bytes binario.

**¿Dónde se sigue utilizando el lenguaje ensamblador hoy en día?**
Se utiliza activamente en núcleos de sistemas operativos (cargador de arranque), controladores de dispositivos de hardware, ingeniería inversa, análisis de malware, detección de vulnerabilidades cibernéticas y sistemas integrados (IoT/microcontrolador).

**¿Cuál es la diferencia entre CISC y RISC?**
CISC (x86-64) tiene un rico conjunto de instrucciones que puede realizar múltiples subprocesos y accesos a memoria en una sola instrucción; RISC (ARM), por otro lado, es una arquitectura simplificada y energéticamente eficiente que ejecuta cada comando en un único ciclo de reloj.


## Términos relacionados
- [Memory Management](/es/dictionary/memory-management/)
- [Runtime](/es/dictionary/runtime/)
- [Compilation](/es/dictionary/compilation/)
- [Apple Silicon](/es/dictionary/apple-silicon/)
- [Emulator](/es/dictionary/emulator/)

## Herramientas relacionadas
- [Ghidra](/es/discover/ghidra/)
- [Apollo-11](/es/discover/apollo-11/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/assembly/
