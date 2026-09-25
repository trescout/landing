# ¿Qué es el Contexto (Context)? IA y Sistemas

> Inglés: Context · Etimología: latín contexere (tejer juntos, entrelazar)

**Categoría:** AI  
**Última actualización:** 2026-09-19

El contexto (context) es un principio informático transversal que abarca desde la ventana de memoria activa que utilizan los modelos de lenguaje hasta el estado de registros y memoria que conserva un sistema operativo al alternar procesos.

## Por analogía
Si te cruzas con un colega y solo le dices 'Sí, al final aceptó', no sabrá a qué te refieres; si añades 'Respecto a la propuesta que enviamos ayer', le aportas el contexto necesario para entablar el diálogo.

## 1. El Contexto en la Inteligencia Artificial y LLMs
Los modelos de lenguaje no poseen una conciencia persistente entre llamadas de inferencia. Para resolver dudas y entender matices, dependen por completo de su **ventana de contexto**: la secuencia de tokens suministrada en cada petición (instrucciones del sistema, historial y fragmentos documentales RAG). Cuanto más amplia sea esta ventana, mayor cantidad de datos puede analizar el algoritmo en una sola pasada.

## 2. El Contexto en Sistemas Operativos y Programación
En la ingeniería de sistemas, el contexto define la fotografía instantánea de la ejecución de un hilo: registros de CPU, contador de programa (PC) y referencias a páginas de memoria física. Cuando el sistema operativo suspende una tarea para ejecutar otra, realiza un **cambio de contexto (context switch)**, guardando los valores antiguos y cargando los nuevos en el procesador.

## Comparativa entre diferentes disciplinas
Manifestaciones prácticas del contexto :
- **Modelos de Lenguaje:** Ventana de tokens y matriz KV Cache que sirven de memoria de trabajo efímera.- **Sistemas Operativos:** Bloque de Control de Procesos (PCB) que salva el estado del procesador en el kernel.- **Entornos de Desarrollo:** Objetos de contexto (como en React o Go) que trasladan credenciales y señales de cancelación a lo largo de las funciones.

## Preguntas frecuentes

**¿Qué es el problema 'lost in the middle' en prompts de IA?**  
La dificultad de los modelos neuronales para recordar con igual nitidez los datos situados en el tercio central de textos muy largos frente al principio y el final.

**¿Por qué el cambio de contexto en CPUs reduce la velocidad?**  
Porque guardar y restaurar registros de hardware interrumpe el flujo de cálculo y vacía cachés rápidas como la memoria TLB.

**¿Qué utilidad tiene el Context API en librerías de interfaz?**  
Permite propagar variables compartidas a cualquier componente de la jerarquía sin necesidad de pasarlas de padres a hijos manualmente.

**¿Cómo evalúan los modelos Transformer el contexto?**  
Multiplicando matrices de atención que puntúan la afinidad semántica entre todas las palabras presentes en la entrada.

## Términos relacionados
- [Context Window](/es/dictionary/context-window/)
- [Working Memory](/es/dictionary/working-memory/)
- [Attention Mechanism](/es/dictionary/attention-mechanism/)

## Herramientas relacionadas
- [Goose](/es/discover/goose/)
- [Chrome Devtools MCP](/es/discover/chrome-devtools-mcp/)
- [Openclaude](/es/discover/openclaude/)
- [Code Review Graph](/es/discover/code-review-graph/)
- [Fastmcp](/es/discover/fastmcp/)
- [Context Mode](/es/discover/context-mode/)
- [Unity MCP](/es/discover/unity-mcp/)
- [DesktopCommanderMCP](/es/discover/desktopcommandermcp/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/context/
