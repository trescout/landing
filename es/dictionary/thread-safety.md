# ¿Qué es Thread-safety?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

La seguridad de los hilos (Thread safety), en su equivalente en turco iş parçacığı güvenliği, es la garantía de que un fragmento de código no corrompe los datos cuando es ejecutado simultáneamente por múltiples hilos.

## Definición y origen de la palabra

"Thread" significa hilo y "safety", seguridad. La seguridad aquí no es contra los piratas informáticos, sino para garantizar que los datos se mantengan coherentes: si dos procesos actualizan la misma cuenta al mismo tiempo, el resultado puede ser incorrecto. El código seguro para hilos (thread-safe) regula esta competencia. Las aplicaciones bancarias, los servidores web y todo el software multiproceso necesitan esto.

***Analogía:** Es como ponerle pestillo a la puerta en una casa con un solo baño; cuando alguien está dentro, el otro tiene que esperar.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Bancario:** Dos solicitudes de retiro de la misma cuenta no reducen el saldo a negativo.
**Venta de entradas:** El último asiento no debe venderse a dos personas a la vez.
**Contadores:** El contador de visitantes aumenta en un incremento completo con cada solicitud.

## Profundidad técnica y arquitectura

Las herramientas típicas son:

**Bloquear (Mutex/Bloquear):** Un hilo ingresa a la región crítica a la vez, el otro espera.
**Operación atómica:** Lectura y escritura indivisible en un solo paso.
**Datos inmutables:** Los datos que no se pueden cambiar no entran en carrera, se copian.
**Mensajería:** Comunicación a través de cola en lugar de datos compartidos (por ejemplo, canales Go).

Un pequeño ejemplo en Python:

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

Mientras se ejecutan las líneas bloqueadas, ningún otro hilo puede intervenir. Si se olvida un bloqueo o se adquiere en el orden incorrecto, el programa puede bloquearse (interbloqueo o deadlock). Por esta razón, la sección crítica se mantiene corta.

## Cosas frecuentemente mezcladas

No está relacionado con la ciberseguridad. El tema no son los piratas informáticos, sino la consistencia de los datos: evitar que dos operaciones que acceden a los mismos datos al mismo tiempo se sobrescriban mutuamente.

## Uso en diferentes disciplinas

**Tráfico:** Semáforos que determinan el orden de paso en un puente de un solo carril.
**Cocina:** Cineros que utilizan un solo cuchillo por turnos.
**Biblioteca:** El intercambio de un único ejemplar de un libro mediante el registro de préstamos.

## Preguntas frecuentes

**¿Qué sucede si no es seguro para subprocesos?**

Los datos se mezclan, los cálculos salen mal o la aplicación se bloquea. Es difícil de depurar porque el error no se repite en cada ejecución.

**¿Se debe añadir un bloqueo a cada código?**

No. En el código de un solo hilo, los bloqueos introducen una sobrecarga innecesaria. Solo se protegen las secciones concurrentes que tocan datos compartidos.

**¿Qué es el interbloqueo (deadlock) y cómo se previene?**

Es cuando dos procesos se quedan atascados esperando el bloqueo del otro. Tomar siempre los bloqueos en el mismo orden y mantener la sección crítica corta reduce el riesgo.

**¿Se detecta con una prueba?**

Es difícil de detectar, ya que el error depende del momento de ejecución. Se utilizan pruebas de carga y detectores de carreras especiales (race detector).

## Términos relacionados

- [Concurrency](https://trescout.com/es/dictionary/concurrency/)
- [System Programming Language](https://trescout.com/es/dictionary/system-programming-language/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/thread-safety/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/thread-safety/
