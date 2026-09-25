# ¿Qué es Thread Safety?

> Inglés: Thread Safety · Etimología: inglés antiguo thraed (hilo) + latín salvus (intacto/seguro)

**Categoría:** Dev  
**Última actualización:** 2026-09-22

Thread safety (seguridad de hilos) es la garantía de que una función, módulo o estructura de datos opera sin errores ni corrupción de memoria cuando es ejecutada concurrentemente por múltiples hilos de procesamiento.

## Definición y etimología
El concepto une thread (hilo de ejecución en el procesador) con safety (coherencia de datos). No tiene que ver con ataques informáticos, sino con la sincronización interna: cuando dos tareas modifican la misma variable a la vez sin coordinación, los datos intermedios se corrompen.

## Contexto cotidiano e uso práctico
Campos habituales de aplicación :
- **Sistemas Financieros:** Evitar que dos pagos simultáneos dejen una cuenta bancaria con saldo negativo incoherente.- **Plataformas de Entradas:** Asegurar que una butaca de teatro no pueda asignarse a dos compradores a la vez.- **Servidores de Backend:** Servir cientos de peticiones por segundo compartiendo variables globales en memoria.

## Profundidad técnica y arquitectura
Técnicas principales para lograr thread safety :
- **Cerrojos (Mutex / Locks):** Permiten que únicamente un hilo acceda a la sección crítica en cada instante.- **Operaciones Atómicas:** Instrucciones de hardware directas que impiden interrupciones a mitad de una modificación.- **Estructuras Inmutables:** Datos de solo lectura accesibles por múltiples hilos de forma paralela sin bloqueos.- **Modelo de Propiedad de Rust:** El compilador analiza las referencias en memoria e impide condiciones de carrera antes de la ejecución.

## Suele confundirse con
Se confunde a menudo con la ciberseguridad. Thread safety no protege contra malware o intrusiones de red; previene fallos lógicos debidos a accesos concurrentes no sincronizados en la memoria.

## Perspectivas interdisciplinares
Situaciones paralelas en la vida real :
- **Circulación:** Un puente estrecho de un solo carril regulado por semáforos temporizados.- **Taller:** Dos mecánicos que se turnan ordenadamente para usar la única herramienta disponible.- **Mostrador:** Un único empleado que atiende a los clientes uno por uno mediante turno asignado.

## Por analogía
Es como poner un cerrojo en el cuarto de baño compartido de una vivienda: mientras una persona está dentro, las demás esperan en el pasillo hasta que termine.

## Preguntas frecuentes

**¿Qué ocurre si un sistema carece de thread safety?**  
Se producen condiciones de carrera que corrompen variables en memoria de forma aleatoria e impredecible.

**¿El uso intensivo de cerrojos siempre es la mejor solución?**  
No, porque los cerrojos excesivos reducen el rendimiento e introducen riesgos de bloqueo mutuo (deadlock).

**¿Cómo ayuda Rust a escribir código seguro entre hilos?**  
A través de su sistema de ownership y borrowing, que garantiza en tiempo de compilación que no existan mutaciones compartidas.

**¿Por qué las estructuras inmutables son thread-safe por naturaleza?**  
Porque al no poder modificarse una vez creadas, múltiples hilos pueden leer sus datos simultáneamente sin interferirse.

## Términos relacionados
- [Concurrency](/es/dictionary/concurrency/)
- [System Programming Language](/es/dictionary/system-programming-language/)
- [Mutex](/es/dictionary/mutex/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/thread-safety/
