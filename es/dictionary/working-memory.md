# ¿Qué es Working Memory?

*Inteligencia artificial · Última actualización: 22 de septiembre de 2026*

La memoria de trabajo (working memory) es la información temporal que el modelo retiene para la tarea en curso.

## Definición y origen de la palabra

Cuando la tarea termina o el contexto cambia, el contenido se borra. El contenedor de la ventana de contexto es la información activa dentro de la memoria de trabajo. El historial del chat y los resultados intermedios se almacenan aquí.

***Analogía:** Es como las notas temporales tomadas al margen al resolver matemáticas; una vez terminado el problema, ya no tienen importancia.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Conversación:** Recordar mensajes anteriores.
**Razonamiento:** Mantener pasos intermedios.
**Vehículo:** Retener los resultados de las llamadas.

## Profundidad técnica y arquitectura

Cálculo de presupuesto:

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

Cuando se desborda, el modelo se despide de lo antiguo: se aplica poda, resumen o desplazamiento. Diferencia con RAG: RAG trae información del exterior, la memoria de trabajo mantiene la información actual. Ambos trabajan juntos.

## Cosas frecuentemente mezcladas

Se confunde con la memoria a largo plazo. Aquella es el perfil permanente, esta es la mesa de trabajo temporal. Cuando la sesión se cierra, esto se vacía.

## Uso en diferentes disciplinas

**Nota al margen:** Borrador desechado al terminar el problema.
**Pararse:** Herramienta recogida al finalizar el trabajo.
**RAM:** Espacio que se borra al cortar la energía.

## Preguntas frecuentes

**¿Qué pasa si se llena?**

La información antigua se olvida, el contexto se desplaza. Se gestiona mediante resumen y poda.

**¿Cómo se amplía?**

Se elige un modelo con ventana grande o se añade información externa mediante RAG.

**¿Cuál es la diferencia con RAG?**

RAG trae información del exterior, la memoria retiene el momento actual. Ambos son complementarios.

**¿Olvida?**

Sí. Es un espacio temporal, no se espera persistencia. La información permanente se escribe fuera.

## Términos relacionados

- [Memory](https://trescout.com/es/dictionary/memory/)
- [Context Window](https://trescout.com/es/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/es/dictionary/long-term-memory/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/working-memory/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/working-memory/
