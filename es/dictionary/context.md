# ¿Qué es Context?

*Inteligencia artificial · Última actualización: 19 de septiembre de 2026*

El contexto es el conjunto de información ambiental y semántica que un dato, comando o proceso necesita para ser interpretado y ejecutado correctamente.

## 1. Contexto en Inteligencia Artificial y LLM

Los modelos de lenguaje grandes (LLM) no tienen una memoria permanente o una memoria de experiencias como los humanos; en cada consulta, solo "recuerdan" los datos incluidos en ese momento en la ventana de contexto (context window).

### Transformer y mecanismo de atención (Self-Attention)

En la arquitectura Transformer, el contexto se establece ponderando la relación entre una palabra al principio de la oración y una al final (vectores de Consulta/Query, Clave/Key, Valor/Value). El modelo resuelve si la palabra "banco" se refiere a una institución financiera o a la orilla de un río solo observando el contexto de la oración en la que aparece.

### Ventana de contexto (Context Window) y sus límites

- Capacidad de tokens: Es la longitud máxima que un modelo puede leer y procesar para generar una respuesta de una sola vez (p. ej., 8K, 32K, 128K o más de 1M de tokens).
- Costo de memoria (KV Cache): A medida que el contexto se alarga, el requisito de memoria de la matriz de atención aumenta de forma cuadrática. Para aliviar esta carga, se utilizan optimizaciones de FlashAttention y KV-Cache.
- El problema del centro perdido (Lost in the Middle): Las investigaciones demuestran que los LLM se centran mejor en la información situada al principio y al final de los textos largos en comparación con la información situada en el medio.
- RAG (Generación Aumentada por Recuperación): En lugar de intentar ajustar millones de páginas de datos corporativos dentro de una ventana de contexto, se filtran solo los párrafos más relevantes para la consulta mediante un motor de búsqueda o una base de datos vectorial y se transfieren al modelo como contexto.

***Analogía:** Si hablas con un amigo y solo dices "Sí, él también dijo eso", no te entenderá; pero si dices "Me refiero a esa película de la que hablamos ayer", habrás proporcionado el contexto necesario.*

## 2. Contexto en sistemas operativos y programación

En la programación de sistemas, el "contexto" se refiere a todos los valores de variables y registros que reflejan completamente el estado actual de un programa durante su ejecución.

### Cambio de contexto (Context Switching)

Un sistema operativo que ejecuta multitarea (multitasking) distribuye el núcleo de la CPU entre diferentes procesos e hilos (threads):

1. Los registros de la CPU del proceso en ejecución (RAX, RSP, RIP, etc.), el puntero de pila y las páginas de memoria se guardan en el Bloque de Control de Procesos (PCB - Process Control Block).
2. Los registros del siguiente proceso se restauran en la CPU.
3. Costo: El cambio de contexto es muy costoso a nivel de hardware, ya que provoca la invalidación (contaminación de caché) de las memorias caché L1/L2 de la CPU y de los mapas de direcciones TLB (Translation Lookaside Buffer).

### Gestión de contexto en lenguajes

- Go (context.Context): Se utiliza para transmitir señales de cancelación, plazos (deadlines) y metadatos de ámbito de solicitud entre peticiones de red o goroutines asíncronas.
- Python (bloques with): Los gestores de contexto (Context Managers) hacen que las operaciones de limpieza de recursos, como la lectura de archivos o la apertura y cierre de conexiones a bases de datos, sean seguras.
- React (Context API): Es un método para transmitir el estado global a través del árbol de componentes sin necesidad de pasar props manualmente a cada nivel intermedio (evitando el prop drilling).

## Comparación: El concepto de contexto en diferentes disciplinas

| Campo | Valor representado por el contexto | Componentes típicos | Problemas encontrados |
|---|---|---|---|
| Inteligencia Artificial (LLM) | Prompt de entrada + Historial de chat + Documentos | Tokens, máscaras de atención, caché KV | Límite de tokens, alucinaciones, consumo de memoria |
| Sistemas operativos | Estado instantáneo del hardware de un proceso | Registros, contador de programa, tablas de páginas | Latencia de CPU, fallos de caché (cache misses), vaciado de TLB (TLB flush) |
| Desarrollo de software | Ciclo de vida de la solicitud y datos del entorno | Señal de tiempo de espera (timeout), token de autorización | Fuga de memoria, llamadas asíncronas no canceladas |

## Preguntas frecuentes

**¿Qué significa 'Context' y cuál es su equivalente en español?**

Su equivalente en español es "contexto". Se refiere al conjunto de condiciones, antecedentes y situaciones complementarias relacionadas en las que se encuentra cualquier expresión, dato o proceso.

**¿Cuál es la diferencia entre Prompt y Context?**

El Prompt es la entrada, pregunta o instrucción de acción dada directamente a la inteligencia artificial ("Explica este código"). El Contexto, por otro lado, es la información adicional, el código completo, las variables de entorno o las conversaciones previas proporcionadas para que el modelo ejecute esa instrucción correctamente.

**¿Por qué la ventana de contexto (Context Window) es limitada?**

En la arquitectura Transformer, cada token se relaciona de forma cruzada con todos los demás tokens. Dado que este cálculo matemático y la memoria almacenada (KV-Cache) aumentan en proporción directa al cuadrado de la longitud del contexto, la memoria de la GPU establece un límite de hardware.

**¿Por qué el "cambio de contexto" (Context Switch) en el sistema operativo provoca una pérdida de rendimiento?**

Al cambiar de un proceso a otro, la CPU debe guardar sus registros, cargar el espacio de memoria del nuevo proceso y limpiar y volver a llenar las cachés del procesador (L1/L2/L3 y TLB). Esta situación provoca una pérdida directa de procesamiento del orden de los microsegundos.

**¿Por qué en el lenguaje Go el paquete context se pasa como primer parámetro a cada función?**

En Go, el parámetro ctx context.Context evita el consumo innecesario de recursos del servidor al garantizar que, cuando se cancela una solicitud HTTP o se agota su tiempo de espera, las consultas a la base de datos y los trabajos en segundo plano asociados también se detengan.

## Términos relacionados

- [Context Window](https://trescout.com/es/dictionary/context-window/)
- [Prompt](https://trescout.com/es/dictionary/prompt/)
- [RAG](https://trescout.com/es/dictionary/rag/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)

## Herramientas relacionadas

- [REA](https://trescout.com/es/discover/rea/)
- [Servers](https://trescout.com/es/discover/servers/)
- [OmniRoute](https://trescout.com/es/discover/omniroute/)
- [Goose](https://trescout.com/es/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/es/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/es/discover/openclaude/)
- [Code Review Graph](https://trescout.com/es/discover/code-review-graph/)
- [Context Mode](https://trescout.com/es/discover/context-mode/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/context/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/context/
