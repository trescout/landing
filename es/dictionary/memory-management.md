# Memory Management Stack, Heap, recolector de basura y memoria del SO


**Categoría:** Dev  

**Última actualización:** 2026-09-19


La gestión de memoria (memory management) es la disciplina informática y del sistema operativo que coordina cómo se asigna, rastrea y recicla la memoria RAM a lo largo de la ejecución de un programa.


## 1. Anatomía de la Memoria: Separación entre Stack y Heap
Todo software en ejecución distribuye su espacio de trabajo en memoria en dos áreas diferenciadas :
- **Memoria de Pila (Stack):** Estructura secuencial de tipo LIFO (último en entrar, primero en salir) gestionada de forma directa por el procesador. Guarda las variables locales y marcos de función. La asignación consiste en desplazar el puntero RSP, resultando instantánea y liberándose automáticamente al terminar la función.- **Memoria de Montículo (Heap):** Área extensa de asignación dinámica pensada para objetos de tamaño variable que deben persistir fuera del ámbito local. Requiere llamadas al asignador del sistema, lo que conlleva mayor flexibilidad pero menor velocidad.

## 2. Tres Paradigmas Fundamentales de Gestión de Memoria
Los lenguajes de programación se dividen en tres grandes modelos de control :
- **Gestión Manual (C, C++):** El desarrollador reserva bloques mediante <code>malloc()</code> y debe liberarlos obligatoriamente con <code>free()</code>. Ofrece la máxima velocidad, pero conlleva peligros de fugas de memoria o fallos graves de seguridad por desbordamiento.- **Recolección Automática de Basura (Java, Go, JavaScript, Python):** Un recolector (Garbage Collector) escanea la memoria en segundo plano para liberar los objetos que ya no tienen referencias activas, a cambio de pequeñas pausas de CPU.- **Propiedad y Préstamo en Tiempo de Compilación (Rust):** Garantiza la seguridad de memoria sin recolector mediante reglas de Ownership que verifican el ciclo de vida de los datos antes de compilar y liberan la memoria de forma determinista.

## 3. Nivel de Sistema Operativo: Memoria Virtual y OOM Killer
Por debajo del software de usuario, el núcleo del sistema operativo administra los módulos de RAM mediante la MMU :
- **Memoria Virtual y Paginación:** Cada programa interactúa con un espacio lógico de memoria dividido en páginas de 4 KB que la MMU traduce a posiciones físicas reales.- **Fallos de Página (Page Faults) y Swap:** Cuando el sistema requiere datos que fueron derivados temporalmente al disco duro, se produce un fallo de página para volver a cargarlos en RAM.- **OOM Killer (Out Of Memory):** Cuando la memoria física se agota por completo, el núcleo Linux invoca el OOM Killer para abortar los procesos que más memoria consumen y evitar el colapso del equipo.

## Por analogía
La memoria de pila es como un montón de platos donde se apilan y recogen piezas ágilmente desde arriba; la memoria de montículo es como un almacén de paquetería donde se guardan cajas de cualquier tamaño llevando un registro para no olvidarlas.

## Preguntas frecuentes

**¿Qué diferencia hay entre la memoria Stack y la memoria Heap?**  
La Stack es automática, instantánea y limitada al ámbito de una función; la Heap es flexible, amplia y exige control manual o recolección de basura.

**¿Qué consecuencias tiene una fuga de memoria (memory leak)?**  
Consume recursos de RAM progresivamente sin liberarlos, degradando el rendimiento general hasta que la aplicación colapsa.

**¿Cómo gestiona Rust la memoria sin usar recolector de basura?**  
Mediante su sistema de reglas de propiedad (Ownership) validadas por el compilador, que programa la liberación exacta de la memoria de forma determinista.

**¿Cuál es la función del OOM Killer en Linux?**  
Cerrar procesos consumidores cuando la memoria RAM se agota por completo para salvar la estabilidad del sistema operativo.

## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [State Management](/es/dictionary/state-management/)
- [Serialization](/es/dictionary/serialization/)
- [Network Stack](/es/dictionary/network-stack/)
- [Assembly](/es/dictionary/assembly/)

---
Fuente: Glosario técnico TreScout · https://trescout.com/es/dictionary/memory-management/
