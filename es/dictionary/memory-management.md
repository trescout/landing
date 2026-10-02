# ¿Qué es Memory Management?

La gestión de memoria (memory management) es el proceso de asignar, proteger y devolver al sistema la memoria de acceso aleatorio (RAM) física y virtual de la computadora entre los programas en ejecución una vez que se termina de utilizar.

## 1. Anatomía de la memoria: distinción entre Stack (Pila) y Heap (Montículo)
Cuando se ejecuta un programa, el sistema operativo asigna un espacio de memoria virtual específico para ese proceso. Los dos componentes más críticos de este espacio son el Stack y el Heap:

## 2. Tres paradigmas fundamentales de gestión de memoria

## 3. Memoria a nivel de sistema operativo: Memoria virtual y OOM Killer
Los sistemas operativos modernos utilizan una arquitectura de memoria virtual y paginación para evitar que los programas lean la memoria de los demás. La Unidad de Gestión de Memoria (MMU) de la CPU traduce las direcciones virtuales a direcciones físicas en el hardware con la ayuda de la caché TLB. Cuando la memoria RAM física y el espacio de intercambio (swap) se agotan por completo, el mecanismo OOM Killer (Out of Memory Killer) del kernel de Linux termina el proceso más agresivo con una señal SIGKILL para salvar el sistema.

## Preguntas frecuentes
**¿Qué significa 'Memory management' y cuál es su equivalente en español?**
Memory Management significa "gestión de memoria" en español. Es el conjunto de procesos de asignación, seguimiento y liberación de recursos de RAM durante la ejecución de un programa informático.

**¿Cuál es la diferencia fundamental entre Stack y Heap?**
La pila (Stack) gestiona las variables locales conocidas en tiempo de compilación de forma extremadamente rápida con lógica LIFO; el montón (Heap) es un grupo de memoria flexible, reservado para objetos que crecen dinámicamente en tiempo de ejecución, cuya gestión es más compleja.

**¿Cómo funciona el Garbage Collection (Recolector de basura)?**
En lenguajes donde el programador no realiza la eliminación manual (Java, Go, JS, etc.), un motor que se ejecuta en segundo plano detecta los objetos huérfanos a los que no se puede acceder desde las variables raíz y limpia la RAM.

**¿Cómo se evita una fuga de memoria (Memory Leak)?**
En lenguajes manuales, escribiendo un 'free' por cada 'malloc' o estableciendo patrones RAII; en lenguajes con recolector de basura, limpiando las referencias globales a arreglos y los escuchadores de eventos (event listeners) que no se cierran.


## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [State Management](/es/dictionary/state-management/)
- [Serialization](/es/dictionary/serialization/)
- [Network Stack](/es/dictionary/network-stack/)
- [Assembly](/es/dictionary/assembly/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/memory-management/
