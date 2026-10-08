# ¿Qué es Skill?

*Glosario · AI · Última actualización: 22 de septiembre de 2026*

Una habilidad (Skill en su equivalente en turco) es una unidad definida que permite a un asistente de inteligencia artificial realizar tareas utilizando una herramienta externa.

## Definición y origen de la palabra

La conversación general del asistente no es suficiente; a veces necesita leer archivos o realizar búsquedas. Cada una de estas funciones específicas se define como una habilidad (skill). El concepto ha evolucionado desde la era de los asistentes de voz hasta la era de los agentes: desde las habilidades de Alexa hasta las capacidades de los agentes actuales.

***Analogía:** Es como tener diferentes herramientas en la mano del chef; el chef es uno solo y elige la herramienta adecuada para cada tarea.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Archivo:** Lectura y resumen de documentos.
**Calendario:** Programación de reuniones.
**Búsqueda:** Recuperación de información actualizada.

## Profundidad técnica y arquitectura

Una habilidad se compone de tres partes:

**Nombre:** El nombre corto que llamará el modelo.
**Descripción:** La descripción de cuándo se utilizará. El modelo hace la selección basándose en esto.
**Esquema de parámetros:** Formato de entrada.

Definición de ejemplo:

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Flujo: El usuario hace una solicitud, el modelo selecciona la capacidad adecuada, completa el parámetro, la herramienta se ejecuta y el resultado regresa al modelo. Se solicita la aprobación del usuario para las capacidades que tienen permisos de escritura.

## Cosas frecuentemente mezcladas

Se suele pensar que es una capacidad general del modelo. Sin embargo, aquí nos referimos a la habilidad del asistente para utilizar una herramienta externa. El modelo entiende el idioma, la habilidad hace el trabajo.

## Uso en diferentes disciplinas

**Cocina:** El cuchillo y las técnicas de salsa en manos del chef.
**Taladro:** Función que cambia según la broca.
**Teléfono:** Cada aplicación instalada.

## Preguntas frecuentes

**¿Tiene cada modelo una capacidad?**

No. Los modelos básicos generan texto, la capacidad se adquiere cuando se añade una herramienta externa al asistente.

**¿Cómo desarrollar habilidades?**

Se define mediante una conexión API o un bloque de código. La descripción se escribe con claridad y el modelo la selecciona correctamente.

**¿Es seguro?**

Las capacidades de lectura son de bajo riesgo. En operaciones como escritura y pagos, la aprobación y el límite de alcance son obligatorios.

**¿Quiénes escriben las capacidades?**

Los desarrolladores las escriben y las plataformas las distribuyen en la tienda. Escribir una buena descripción es la mitad del trabajo.

## Términos relacionados

- [AI Agent](https://trescout.com/es/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/es/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/es/dictionary/agent-skills/)
- [Tools](https://trescout.com/es/dictionary/tools/)
- [AI Capabilities](https://trescout.com/es/dictionary/ai-capabilities/)

## Herramientas relacionadas

- [Anthropic Skills](https://trescout.com/es/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/es/discover/taste-skill/)
- [Archify](https://trescout.com/es/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/es/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/es/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/es/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/es/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/es/discover/book-to-skill/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/skill/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/skill/
