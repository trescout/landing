# ¿Qué es Multi-process?

Es el método mediante el cual un programa de ordenador ejecuta sus tareas simultáneamente dividiéndolas en múltiples subprocesos que son completamente independientes entre sí y poseen su propio espacio de memoria privado.

## Definición
En la programación tradicional, una aplicación suele ejecutarse secuencialmente a través de un único hilo. En el enfoque de múltiples procesos (multi-process), el sistema operativo crea un espacio de trabajo separado para cada tarea. Gracias a este método, con el que te encontrarás a menudo en el glosario de TreScout, si uno de los procesos experimenta un error y se bloquea, los demás procesos continúan funcionando sin verse afectados por esta situación.

## Cómo funciona
A nivel del sistema operativo, se asigna una dirección de memoria independiente para cada proceso. El programa genera nuevos subprocesos a partir de un proceso principal, y estos procesos se comunican entre sí a través de canales de comunicación privados para compartir tareas.

## Dónde se usa
Se utiliza con frecuencia, especialmente en navegadores web donde cada pestaña se ejecuta como un proceso separado, en sistemas de procesamiento de grandes datos y en aplicaciones de servidor que realizan cálculos pesados en segundo plano.

## Suele confundirse con
Se confunde a menudo con el concepto de multihilo (multi-threading). Mientras que en el método de multihilo las tareas se realizan mediante hilos ligeros que comparten el mismo espacio de memoria, en el método de múltiples procesos cada tarea tiene su propio espacio de memoria completamente aislado.

## Preguntas frecuentes
**¿El uso de múltiples procesos fatiga al ordenador?**
Sí, dado que se asignan memoria y recursos separados para cada proceso, puede consumir más recursos del ordenador en comparación con otros métodos.

**¿En qué situaciones se debe preferir el multi-process?**
Debe preferirse en tareas pesadas donde la seguridad y la estabilidad son prioritarias, y en las que no deseas que se vean afectadas por el fallo de las demás.


## Términos relacionados
- [Concurrency](/es/dictionary/concurrency/)
- [Runtime](/es/dictionary/runtime/)
- [Thread-safety](/es/dictionary/thread-safety/)
- [Distributed](/es/dictionary/distributed/)

## Herramientas relacionadas
- [Raddebugger](/es/discover/raddebugger/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/multi-process/
