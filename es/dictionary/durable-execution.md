# ¿Qué es Durable Execution?

Es un sistema que permite que un proceso continúe de forma segura donde se quedó, incluso si hay un error o una interrupción.

## Definición
Normalmente, si un programa de computadora se queda sin energía o falla mientras se está ejecutando, todo se borra y hay que empezar de nuevo. La ejecución duradera registra cada paso del programa, recordando dónde quedó en el momento de la interrupción. De esta forma, las transacciones que tardan horas se pueden completar de forma segura.

## Cómo funciona
El sistema realiza constantemente una copia de seguridad del estado del programa en una base de datos. Cuando ocurre un error, el sistema reinicia el proceso desde el último punto respaldado.

## Dónde se usa
Se utiliza para transferencias bancarias, largos procesos de procesamiento de datos y flujos de trabajo complejos de inteligencia artificial.

## Suele confundirse con
Puede confundirse con el guardado automático, pero preserva toda la lógica operativa del programa, no sólo el archivo.

## Preguntas frecuentes
**¿Todos los programas deberían ser duraderos?**
No es necesario para transacciones cortas, pero es esencial para transacciones críticas que duran horas.

**¿Por qué es tan importante?**
En caso de error, empezar todo el proceso desde cero es una pérdida de tiempo y dinero.


## Términos relacionados
- [State Management](/es/dictionary/state-management/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Pg Durable](/es/discover/pg-durable/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/durable-execution/
