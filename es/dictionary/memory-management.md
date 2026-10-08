# ¿Qué es Memory Management?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

La gestión de memoria (memory management) es el proceso de asignar, proteger y devolver al sistema la memoria de acceso aleatorio (RAM) física y virtual de la computadora entre los programas en ejecución una vez que se termina de utilizar.

## 1. Anatomía de la memoria: distinción entre Stack (Pila) y Heap (Montículo)

Cuando se ejecuta un programa, el sistema operativo asigna un espacio de memoria virtual específico para ese proceso. Los dos componentes más críticos de este espacio son el Stack y el Heap:

```
+------------------------------------+ Yüksek Bellek Adresleri (0xFFFFFFFF)
|           İşletim Sistemi / Kernel |
+------------------------------------+
|  STACK (Aşağıya doğru büyür ↓)     | <-- Yerel değişkenler, fonksiyon çerçeveleri
|                 ↓                  |
|                                    |
|                 ↑                  |
|  HEAP (Yukarıya doğru büyür ↑)     | <-- Dinamik nesneler (malloc, new)
+------------------------------------+
|  BSS (İlklendirilmemiş Global)     |
+------------------------------------+
|  DATA (İlklendirilmiş Statik Veri) |
+------------------------------------+
|  TEXT (Makine Kodu / Talimatlar)   |
+------------------------------------+ Düşük Bellek Adresleri (0x00000000)
```

- Stack (Pila): Es gestionada automáticamente por la arquitectura de la CPU (LIFO). Es extremadamente rápida (solo se desplaza el registro del puntero de pila). Sin embargo, su tamaño es fijo (1MB - 8MB) y provoca un Stack Overflow en caso de recursión infinita.
- Heap (Montículo): Gestionado por el desarrollador o el entorno de ejecución (Runtime) del lenguaje. Se reserva para objetos dinámicos; puede crecer hasta el límite de la memoria RAM física y el espacio de intercambio (swap). Si no se limpia, provoca fugas de memoria (Memory Leak) y fragmentación.

***Analogía:** La pila (Stack) es la torre de documentos en su escritorio; coloca los documentos entrantes en la parte superior y, cuando termina, toma el de arriba al instante; el tiempo de colocación es cero. El montón (Heap) es como un gran almacén; va con el encargado, pide un estante vacío para una caja, el encargado busca un lugar adecuado, le da la llave y, si olvida devolver el estante al encargado cuando termina, el almacén se vuelve inutilizable en poco tiempo.*

## 2. Tres paradigmas fundamentales de gestión de memoria

- Gestión manual de memoria (C, C++): El desarrollador gestiona la memoria personalmente mediante malloc() y free(). Ofrece la máxima velocidad y latencia cero; sin embargo, conlleva los riesgos de fugas, punteros colgantes (dangling pointers) y Use-After-Free, que son la causa de más del 70% de las vulnerabilidades de seguridad en el mundo del software.
- Recolección de basura (Garbage Collection - Java, Go, Python, JS): El programador no realiza la eliminación; el motor de GC que se ejecuta en segundo plano limpia los objetos huérfanos inalcanzables desde las referencias raíz mediante algoritmos de Mark-and-Sweep o Reference Counting. Sin embargo, los escaneos periódicos pueden provocar micro pausas (Stop-The-World).
- Modelo de Propiedad y Préstamo (Ownership & Borrowing - Rust): El compilador de Rust verifica en tiempo de compilación que cada bloque de memoria tenga un único propietario. Sin ejecutar un recolector de basura, garantiza un 100% de seguridad de memoria (Memory Safety) a la velocidad de C.

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

- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [State Management](https://trescout.com/es/dictionary/state-management/)
- [Serialization](https://trescout.com/es/dictionary/serialization/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Assembly](https://trescout.com/es/dictionary/assembly/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/memory-management/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/memory-management/
