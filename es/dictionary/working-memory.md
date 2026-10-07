# ¿Qué es la Working Memory en IA?

> Inglés: Working Memory · Etimología: inglés antiguo weorc (trabajo) + latín memoria (recuerdo)

La working memory (memoria de trabajo) en inteligencia artificial es la información activa y transitoria que un modelo mantiene dentro de su ventana de contexto para resolver el razonamiento o la petición en curso.

## Definición y etimología
Funciona como la mesa de operaciones del sistema: una vez concluida la inferencia o reiniciada la sesión, esos datos de borrador se descartan. La ventana de contexto representa el espacio disponible, y los tokens alojados en ella componen la memoria operativa en uso.

## Contexto cotidiano e uso práctico
Funciones clave en la interacción con IA :

## Profundidad técnica y arquitectura
Gestión del presupuesto de tokens :

## Suele confundirse con
A menudo se confunde con la memoria a largo plazo. La memoria a largo plazo almacena datos permanentes en bases vectoriales; la memoria de trabajo es el búfer efímero que se vacía al terminar la tarea.

## Perspectivas interdisciplinares
Paralelos en la vida práctica :

## Preguntas frecuentes
**¿Qué ocurre si se satura la memoria de trabajo?**
El sistema se ve forzado a recortar mensajes antiguos o resumir el contenido para no rebasar el límite del modelo.

**¿En qué se diferencia de los pesos del modelo?**
Los pesos son el conocimiento fijo fijado durante el entrenamiento; la memoria de trabajo es el contexto temporal que se pasa en el prompt.

**¿Por qué no ampliar la ventana de contexto de forma ilimitada?**
Porque incrementa exponencialmente el consumo de cómputo y puede perjudicar la capacidad de recuperar datos situados en el medio.

**¿Qué ventaja aporta la caché KV?**
Permite generar cada nueva palabra sin necesidad de procesar desde cero todas las anteriores, multiplicando la velocidad de respuesta.


## Términos relacionados
- [Memory](/es/dictionary/memory/)
- [Context Window](/es/dictionary/context-window/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/working-memory/
